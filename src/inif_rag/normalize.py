"""Persian text normalization for consistent storage and retrieval."""

from hazm import Normalizer

# One shared normalizer instance — configured once, reused for every call.
_normalizer = Normalizer(
    correct_spacing=True,       # fix spacing around ZWNJ / نیم‌فاصله
    remove_diacritics=True,     # strip harakat (e.g. کِتاب -> کتاب)
    persian_numbers=True,       # unify digits to Persian forms
)


def normalize_text(text: str) -> str:
    """Return a canonical Persian form of `text`.

    Applied to every FAQ field before storage AND to every user query
    before retrieval, so both sides match on identical text.
    """
    if not text:
        return ""
    return _normalizer.normalize(text).strip()