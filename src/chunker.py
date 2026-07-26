from pydantic import BaseModel

from src.document_loader import Document


class DocumentChunk(BaseModel):
    content: str
    source: str
    visibility: str
    chunk_index: int


def chunk_document(
    document: Document,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[DocumentChunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between 0 and chunk_size - 1")

    text = document.content.strip()

    if not text:
        return []

    chunks: list[DocumentChunk] = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append(
                DocumentChunk(
                    content=chunk_text,
                    source=document.source,
                    visibility=document.visibility,
                    chunk_index=chunk_index,
                )
            )

        if end == len(text):
            break

        start = end - overlap
        chunk_index += 1

    return chunks


def chunk_documents(
    documents: list[Document],
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[DocumentChunk]:
    chunks: list[DocumentChunk] = []

    for document in documents:
        chunks.extend(
            chunk_document(
                document=document,
                chunk_size=chunk_size,
                overlap=overlap,
            )
        )

    return chunks