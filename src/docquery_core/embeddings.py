"""embedding's output domain: a chunk paired with its dense vector."""

from __future__ import annotations

from pydantic import Field

from docquery_core.base import CoreModel
from docquery_core.chunks import Chunk


class EmbeddedChunk(CoreModel):
    """A chunk and its embedding vector — embedding's output, indexing's input.

    Carrying the chunk alongside its vector (rather than returning a bare
    list[list[float]] the caller must zip against a list[Chunk] by position)
    avoids a fragile, order-dependent boundary between the two submodules.
    """

    chunk: Chunk
    vector: tuple[float, ...] = Field(min_length=1)
