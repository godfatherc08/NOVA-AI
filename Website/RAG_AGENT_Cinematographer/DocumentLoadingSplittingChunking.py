
from GoogleDrivePDFlloader import GoogleDrivePDFLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import os
from cleanFunction import clean_text
from transformers import logging

logging.set_verbosity_info()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

"""       Loading and Chunking = LC        """

class LC:
    def __init__(self, folderID, **kwargs):
        """Initialize the Character splitter."""
        self.text_raw = RecursiveCharacterTextSplitter(
            separators=["\\n\\n", "\\n", " "],
            chunk_size=900,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
            strip_whitespace=True
        )

        # Set up Google Drive PDF loader
        self.loader = GoogleDrivePDFLoader(
            folder_id=folderID,
            file_loader_cls=OnlinePDFLoader,
            file_types=['pdf'],
            token_path="./token.json",  #token json and credentials json must be in the same file directory
            scopes=["https://www.googleapis.com/auth/drive.readonly"],
            credentials_path="./credentials.json",
            recursive=True,
        )

        # Set up embedding model
        self.embeddings = HuggingFaceEmbeddings(
            model_name="nomic-ai/nomic-embed-text-v1",
            model_kwargs={"trust_remote_code": True}
        )

        # Set up semantic chunker
        self.semantic_splitter = SemanticChunker(
            self.embeddings,
            breakpoint_threshold_type="standard_deviation",
            breakpoint_threshold_amount=1
        )

    def load_pdf_from_folderID(self):
        load_pdfs = self.loader.load()
        return load_pdfs

    def chunk(self, load_pdfs):
        txt_pdf_cleaned = [clean_text(doc.page_content) for doc in load_pdfs]
        full_text = "\n\n".join(txt_pdf_cleaned)

        """  split_raw_text = self.text_raw.create_documents(txt_pdfs)

        recursive_text = [split_raw_text[i].page_content for i in range(len(split_raw_text))]"""
        docs = self.semantic_splitter.create_documents([full_text])
        return docs
