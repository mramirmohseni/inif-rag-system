-- FAQ knowledge base for the INIF RAG system.
-- Idempotent: safe to run repeatedly.

CREATE TABLE IF NOT EXISTS faq (
    id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category    text        NOT NULL,
    question    text        NOT NULL,
    answer      text        NOT NULL,
    content     text        NOT NULL,
    embedding   vector(1024),
    created_at  timestamptz NOT NULL DEFAULT now()
);

-- Prevents duplicate rows if the loader is re-run.
CREATE UNIQUE INDEX IF NOT EXISTS faq_question_key ON faq (question);

-- Speeds up metadata filtering by category (Phase 2).
CREATE INDEX IF NOT EXISTS faq_category_idx ON faq (category);

-- Approximate nearest-neighbour index for cosine similarity search.
CREATE INDEX IF NOT EXISTS faq_embedding_idx
    ON faq USING hnsw (embedding vector_cosine_ops);