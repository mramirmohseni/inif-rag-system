"""Application configuration, loaded from environment variables."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_URL = (
    f"postgresql://{os.environ['POSTGRES_USER']}:"
    f"{os.environ['POSTGRES_PASSWORD']}@"
    f"{os.environ.get('POSTGRES_HOST', 'localhost')}:"
    f"{os.environ.get('POSTGRES_PORT', '5432')}/"
    f"{os.environ['POSTGRES_DB']}"
)

EMBEDDING_MODEL = "BAAI/bge-m3"
EMBEDDING_DIM = 1024
FAQ_CSV = PROJECT_ROOT / "data" / "faq_qa_pairs.csv"