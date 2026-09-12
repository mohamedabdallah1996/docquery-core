"""DocQuery shared data contracts -- pure types, no logic, no I/O.

Every submodule (ingestion, chunking, embedding, indexing, generation) and
the orchestrator depend on these types to pass data between pipeline
stages. See each type's owning module for which stage produces it.
"""

from __future__ import annotations

from docquery_core.chunks import Chunk, ChunkType
from docquery_core.documents import ParsedDocument, ParsedPage, ParseStatus
from docquery_core.embeddings import EmbeddedChunk
from docquery_core.exceptions import DocQueryError
from docquery_core.generation import GenerationResult, TokenUsage
from docquery_core.retrieval import RetrievedChunk

__all__ = [
    "Chunk",
    "ChunkType",
    "DocQueryError",
    "EmbeddedChunk",
    "GenerationResult",
    "ParseStatus",
    "ParsedDocument",
    "ParsedPage",
    "RetrievedChunk",
    "TokenUsage",
]
