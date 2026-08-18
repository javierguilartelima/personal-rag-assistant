# Personal RAG Assistant

A privacy-aware Retrieval-Augmented Generation (RAG) system built in Python for retrieving relevant information from selected documents while maintaining clear boundaries between public and private data.

## Why I Built This

Personal knowledge is often scattered across notes, documents, and different systems. This project explores how a personal AI assistant can retrieve useful information from that knowledge while keeping sensitive information separated from content that can safely be shared.

The long-term goal is to build a modular personal assistant that can support learning, projects, planning, and automation without training a foundation model from scratch.

## Current Capabilities

The current implementation includes:

- Privacy-aware document loading and access filtering
- Public/private source classification
- Metadata-preserving document chunking
- Keyword-based chunk retrieval
- Semantic retrieval
- Combined keyword and semantic retrieval modes
- Knowledge retrieval pipeline
- Source-aware results
- Automated tests for public/private data boundaries

## How It Works

The system follows a simple RAG pipeline:

1. Load approved documents.
2. Apply visibility metadata (`public` or `private`).
3. Split documents into searchable chunks while preserving metadata.
4. Retrieve relevant chunks using keyword or semantic search.
5. Filter retrieved information according to the active privacy boundary.
6. Provide relevant source context for grounded downstream answers.

## Privacy Design

Privacy is treated as part of the architecture rather than an afterthought.

Private personal data is excluded from the repository through `.gitignore`, while the project keeps separate public and private data locations.

The retrieval layer also includes tests designed to ensure that private content cannot be returned when operating under a public visibility boundary.

## Project Structure

```text
data/
├── public/      # Shareable example knowledge
└── private/     # Local private data excluded from GitHub

src/             # Application and retrieval code
docs/            # Architecture and design decisions
tests/           # Automated tests
## Tech Stack

- Python
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Keyword retrieval
- Vector-based retrieval
- Automated testing
- Git / GitHub

## Setup

Clone the repository:

```bash
git clone https://github.com/javierguilartelima/personal-rag-assistant.git
cd personal-rag-assistant
```

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure any required local environment variables.

Private data and environment secrets should never be committed to the repository.

## Status

Active prototype.

The retrieval and privacy foundations are implemented. Future development may add a user-facing interface, broader document ingestion, additional retrieval strategies, tool integrations, and automation.

## What This Project Demonstrates

This project demonstrates practical experience with:

- Python application development
- AI/RAG system architecture
- Information retrieval
- Privacy-aware system design
- Modular software development
- Automated testing
- Git-based development workflows

## Roadmap

- Expand supported document formats
- Improve retrieval evaluation
- Add additional retrieval strategies
- Build a user-facing query interface
- Integrate selected tools and automations
- Continue strengthening privacy and access controls
