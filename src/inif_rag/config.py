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

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPENROUTER_API_BASE = os.environ["OPENROUTER_API_BASE"]

EMBEDDING_MODEL = "baai/bge-m3"   # was "BAAI/bge-m3" — OpenRouter uses lowercase/slash
EMBEDDING_DIM = 1024

FAQ_CSV = PROJECT_ROOT / "data" / "faq_qa_pairs.csv"