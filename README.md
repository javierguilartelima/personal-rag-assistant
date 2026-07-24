# Personal RAG Assistant

A privacy-aware personal AI assistant that retrieves relevant knowledge from selected documents and answers with grounded sources.

## Long-Term Vision

Build a useful personal AI system that can gradually help with:

- retrieving knowledge from personal notes and systems;

- reducing repeated decisions;

- supporting study, projects, planning, and daily organization;

- separating private personal context from public/shareable knowledge;

- eventually integrating tools and automations;

- evolving into a broader personal assistant without training a foundation model from scratch.

## Current Milestone

The first version should:

1. ingest a small set of selected notes;

2. classify each source as `public` or `private`;

3. retrieve the most relevant text fragments;

4. answer questions using those fragments;

5. show the sources used;

6. prevent public mode from accessing private content.

## Initial Structure

```text

data/public/   Shareable knowledge

data/private/  Personal information excluded from GitHub

src/           Application code

docs/          Architecture and project decisions

tests/         Tests