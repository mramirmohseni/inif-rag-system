"""Text embedding via OpenRouter."""

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from inif_rag.config import (
    EMBEDDING_MODEL,
    OPENROUTER_API_BASE,
    OPENROUTER_API_KEY,
)

BATCH_SIZE = 64

_client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_API_BASE)


@retry(wait=wait_exponential(min=1, max=20), stop=stop_after_attempt(5))
def _embed_batch(texts: list[str]) -> list[list[float]]:
    """Embed one batch. Retried on transient gateway failures."""
    response = _client.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def embed(texts: list[str]) -> list[list[float]]:
    """Embed texts into 1024-dim vectors, batching to limit request count."""
    vectors: list[list[float]] = []
    for start in range(0, len(texts), BATCH_SIZE):
        vectors.extend(_embed_batch(texts[start : start + BATCH_SIZE]))
    return vectors