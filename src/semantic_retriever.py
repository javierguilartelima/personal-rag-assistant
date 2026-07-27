from functools import lru_cache

from sentence_transformers import SentenceTransformer

from src.chunker import DocumentChunk


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)


def retrieve_semantic_chunks(
    query: str,
    chunks: list[DocumentChunk],
    top_k: int = 3,
) -> list[DocumentChunk]:
    if not query.strip():
        return []

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    if not chunks:
        return []

    model = get_embedding_model()

    query_embedding = model.encode_query(
        query,
        normalize_embeddings=True,
    )

    document_embeddings = model.encode_document(
        [chunk.content for chunk in chunks],
        normalize_embeddings=True,
    )

    scores = document_embeddings @ query_embedding

    ranked_indexes = scores.argsort()[::-1][:top_k]

    return [
        chunks[int(index)]
        for index in ranked_indexes
    ]