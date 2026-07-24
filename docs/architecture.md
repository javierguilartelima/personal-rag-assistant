# Architecture

## Initial Goal

Build a small local RAG system that can ingest selected notes, retrieve relevant fragments, and answer with sources.

## Knowledge Separation

The project begins with two knowledge classes:

- `public`: knowledge that may eventually be shared or included in a public product;

- `private`: personal information that must remain local and must never be committed to GitHub.

## Initial Flow

```text

Selected documents

→ text extraction

→ chunking

→ metadata assignment

→ embeddings

→ vector storage

→ retrieval

→ grounded answer with sources