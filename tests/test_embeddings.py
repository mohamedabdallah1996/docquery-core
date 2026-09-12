import pytest
from pydantic import ValidationError

from docquery_core import Chunk, EmbeddedChunk


def _chunk() -> Chunk:
    return Chunk(chunk_id="c1", doc_id="d1", page_number=1, chunk_type="text", content="hello")


def test_rejects_an_empty_vector() -> None:
    with pytest.raises(ValidationError):
        EmbeddedChunk(chunk=_chunk(), vector=())


def test_holds_the_chunk_and_its_vector() -> None:
    embedded = EmbeddedChunk(chunk=_chunk(), vector=(0.1, 0.2, 0.3))
    assert embedded.chunk.chunk_id == "c1"
    assert embedded.vector == (0.1, 0.2, 0.3)
