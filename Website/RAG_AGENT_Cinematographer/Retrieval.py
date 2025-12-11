
from pinecone.grpc import PineconeGRPC as Pinecone, PineconeGRPC
import os
import dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from sentence_transformers import SentenceTransformer
import nltk
from nltk.tokenize import word_tokenize
from sentence_transformers import CrossEncoder
from rank_bm25 import BM25Okapi

dotenv.load_dotenv()

class Retrieval:
    def __init__(self):
        self.k_vector = 35
        self.final_k = 5

        pinecone_key = os.getenv('PINECONE_API_KEY')
        pc = Pinecone(api_key=pinecone_key)

        index = pc.Index("nova-ai")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="nomic-ai/nomic-embed-text-v1",
            model_kwargs={"trust_remote_code": True}
        )

        self.vector_store = PineconeVectorStore(index=index, embedding=self.embeddings)

        self.reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

        nltk.download("punkt_tab")

    def devectorizeBM25(self, query):
        results = self.vector_store.similarity_search_with_score(
            query=query,
            k=self.k_vector,
            namespace="nova-vectordb",
        )

        texts = [doc for doc, score in results]
        t_text = [doc.page_content for doc, score in results]
        vector_scores = [score for doc, score in results]

        """  BM25  """
        """bm25 = BM25Retriever.from_documents(texts, k=self.final_k, preprocess_func=word_tokenize)

        bm25 = BM25Okapi(word_tokenize)
        bm25_scores = bm25.get_scores(query.split())"""

        tokenized_corpus = [word_tokenize(t) for t in t_text]
        query_tokens = word_tokenize(query)

        bm25 = BM25Okapi(tokenized_corpus)
        bm25_scores = bm25.get_scores(query_tokens)

        α, β = 1.0, 0.8  # tune these
        fused_scores = [
            α * vector_scores[i] + β * bm25_scores[i]
            for i in range(len(texts))
        ]

        # Step 4: Sort by fused score
        ordered_indices = sorted(
            range(len(fused_scores)),
            key=lambda i: fused_scores[i],
            reverse=True
        )

        top_candidates = [
            results[i][0]
            for i in ordered_indices
        ]

        pairs = [
            [query, doc.page_content]
            for doc in top_candidates
        ]

        rerank_scores = self.reranker.predict(pairs)

        ranked = sorted(
            zip(top_candidates, rerank_scores),
            key=lambda x: x[1],
            reverse=True
        )

        final_docs = [doc for doc, s in ranked[:self.final_k]]
        return final_docs





