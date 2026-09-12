import pytest
from pydantic import ValidationError

from docquery_core import Chunk, GenerationResult, RetrievedChunk, TokenUsage


def _citation() -> RetrievedChunk:
    chunk = Chunk(chunk_id="c1", doc_id="d1", page_number=1, chunk_type="text", content="hello")
    return RetrievedChunk(chunk=chunk, score=0.9)


def test_rejects_an_empty_query() -> None:
    with pytest.raises(ValidationError):
        GenerationResult(query="", answer="the answer", citations=(), generator_model="glm-4.6")


def test_confidence_and_token_usage_default_to_none() -> None:
    result = GenerationResult(
        query="what is x?",
        answer="x is y",
        citations=(_citation(),),
        generator_model="glm-4.6",
    )
    assert result.confidence is None
    assert result.token_usage is None


def test_token_usage_requires_both_fields() -> None:
    with pytest.raises(ValidationError):
        TokenUsage(prompt_tokens=10)  # type: ignore[call-arg]
