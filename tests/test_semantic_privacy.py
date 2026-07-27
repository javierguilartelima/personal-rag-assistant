from src.chunker import chunk_documents
from src.document_loader import (
    filter_documents_by_mode,
    load_markdown_documents,
)
from src.semantic_retriever import retrieve_semantic_chunks


def test_semantic_public_mode_excludes_private_documents() -> None:
    documents = filter_documents_by_mode(
        load_markdown_documents(),
        mode="public",
    )

    chunks = chunk_documents(
        documents,
        chunk_size=100,
        overlap=20,
    )

    results = retrieve_semantic_chunks(
        "Tell me about the fictional appointment.",
        chunks,
    )

    assert all(result.visibility == "public" for result in results)
    assert all("sample_private.md" not in result.source for result in results)


def test_semantic_private_mode_can_use_private_documents() -> None:
    documents = filter_documents_by_mode(
        load_markdown_documents(),
        mode="private",
    )

    chunks = chunk_documents(
        documents,
        chunk_size=100,
        overlap=20,
    )

    results = retrieve_semantic_chunks(
        "When is the fictional appointment?",
        chunks,
    )

    assert any(result.visibility == "private" for result in results)