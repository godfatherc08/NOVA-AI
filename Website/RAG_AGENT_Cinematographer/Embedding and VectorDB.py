
from DocumentLoadingSplittingChunking import LC
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os
import dotenv

"""Pinecone initialization"""

dotenv.load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "nova-ai"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        vector_type="dense",
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled",
        tags={
            "environment": "development"
        }
    )

"""  Initialization and loading of pdfs and semantic chunks from LC module  """

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
folder_id = os.getenv('FOLDER_ID')

lc = LC(folder_id)

load_pdf = lc.load_pdf_from_folderID()
semantic_chunks = lc.chunk(load_pdf)
semantic_chunks_text = [semantic_chunks[i].page_content for i in range(len(semantic_chunks))]


"""      Embedding Documents with embedding Model   """
final_chunks = lc.embeddings.embed_documents(semantic_chunks_text)


"""    VectorDB creation and integration   """

index = pc.Index(index_name)

upsert_data = [
    {
        "id": f"chunk{i}",
        "values": final_chunks[i],
        "metadata": {"text": semantic_chunks_text[i]},
    }
    for i in range(len(final_chunks))
]

upsert = index.upsert(vectors=upsert_data,namespace="nova-vectordb",batch_size=100)


