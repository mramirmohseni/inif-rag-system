"""Database connection helpers."""

from contextlib import contextmanager

import psycopg

from inif_rag.config import DB_URL


@contextmanager
def get_connection():
    """Yield a database connection, committing on success."""
    with psycopg.connect(DB_URL) as conn:
        yield conn