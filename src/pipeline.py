from typing import Literal

from src.chunker import DocumentChunk, chunk_documents
from src.document_loader import (
    filter_documents_by_mode,
    load_markdown_documents,
)
from src.retriever import retrieve_relevant_chunks


AccessMode = Literal["public", "private"]


def retrieve_knowledge(
    query: str,
    mode: AccessMode = "private",
    top_k: int = 3,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[DocumentChunk]:
    documents = load_markdown_documents()
    accessible_documents = filter_documents_by_mode(
        documents=documents,
        mode=mode,
    )

    chunks = chunk_documents(
        documents=accessible_documents,
        chunk_size=chunk_size,
        overlap=overlap,
    )

    return retrieve_relevant_chunks(
        query=query,
        chunks=chunks,
        top_k=top_k,
    )