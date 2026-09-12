"""indexing's output / generation's input domain: a chunk ranked by relevance."""

from __future__ import annotations

from docquery_core.base import CoreModel
from docquery_core.chunks import Chunk


class RetrievedChunk(CoreModel):
    chunk: Chunk
    score: float
