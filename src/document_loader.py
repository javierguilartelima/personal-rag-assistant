from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from src.config import PROJECT_ROOT


Visibility = Literal["public", "private"]


class Document(BaseModel):
    content: str
    source: str
    visibility: Visibility


def load_markdown_documents() -> list[Document]:
    documents: list[Document] = []

    knowledge_directories: dict[Visibility, Path] = {
        "public": PROJECT_ROOT / "data" / "public",
        "private": PROJECT_ROOT / "data" / "private",
    }

    for visibility, directory in knowledge_directories.items():
        if not directory.exists():
            continue

        for file_path in directory.glob("*.md"):
            content = file_path.read_text(encoding="utf-8").strip()

            if not content:
                continue

            documents.append(
                Document(
                    content=content,
                    source=str(file_path.relative_to(PROJECT_ROOT)),
                    visibility=visibility,
                )
            )

    return documents


def filter_documents_by_mode(
    documents: list[Document],
    mode: Visibility,
) -> list[Document]:
    if mode == "private":
        return documents

    return [
        document
        for document in documents
        if document.visibility == "public"
    ]