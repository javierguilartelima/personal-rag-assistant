import re

from src.chunker import DocumentChunk


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"\b\w+\b", text.lower()))


def score_chunk(query: str, chunk: DocumentChunk) -> int:
    query_terms = tokenize(query)
    chunk_terms = tokenize(chunk.content)

    return len(query_terms.intersection(chunk_terms))


def retrieve_relevant_chunks(
    query: str,
    chunks: list[DocumentChunk],
    top_k: int = 3,
) -> list[DocumentChunk]:
    if not query.strip():
        return []

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    scored_chunks = [
        (score_chunk(query, chunk), chunk)
        for chunk in chunks
    ]

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        chunk
        for score, chunk in scored_chunks
        if score > 0
    ][:top_k]