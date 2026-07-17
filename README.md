# inif-rag-system

A Persian-language RAG system over the Iran National Innovation Fund's FAQ, using Postgres + pgvector for retrieval and generation. Built as a step-by-step pipeline from baseline search through to full answer generation.

## Stack

- **Python 3.13** managed with [uv](https://docs.astral.sh/uv/)
- **PostgreSQL 17 + pgvector** for storage and vector search
- **sentence-transformers** for multilingual embeddings
- **hazm** for Persian text normalization

## Prerequisites

- Docker Desktop
- uv

## Setup

Clone and install dependencies:

```bash
git clone git@github.com:mramirmohseni/inif-rag-system.git
cd inif-rag-system
uv sync
```

Create your env file from the template:

```bash
cp .env.example .env
```

Open `.env` and set a real `POSTGRES_PASSWORD` before starting the database — the template ships with a placeholder.

Start the database:

```bash
docker compose up -d
```

Verify pgvector is ready (should print a version number):

```bash
docker compose exec db psql -U rag -d ragdb -c "SELECT extversion FROM pg_extension WHERE extname='vector';"
```

> **Note:** the password is read on the database's first boot. If you change it later, run `docker compose down -v` (this wipes the data volume) and `docker compose up -d` again.

## Project layout

```
inif-rag-system/
├── compose.yaml          # Postgres + pgvector
├── db/init/              # SQL run on first DB boot (enables pgvector)
├── data/                 # FAQ dataset
├── src/                  # application code
├── .env.example          # config template
└── pyproject.toml
```

## Status

Work in progress. Data foundation and retrieval first, generation later.