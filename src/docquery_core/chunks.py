"""chunking's output domain: header-aware, retrieval-sized fragments of a document."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from docquery_core.base import CoreModel

type ChunkType = Literal["text", "table", "image", "list", "code"]


class Chunk(CoreModel):
    """A chunk of a document, ready to embed and index.

    `chunk_id` is a content hash (doc_id, chunk_type, page, content,
    asset_ref) — stable across re-runs, which is what makes re-ingestion
    idempotent.
    """

    chunk_id: str = Field(min_length=1)
    doc_id: str = Field(min_length=1)
    page_number: int = Field(ge=1)
    chunk_type: ChunkType
    section_path: tuple[str, ...] = Field(default_factory=tuple)
    content: str
    # Reference to a raw, non-text asset this chunk represents (e.g. an
    # extracted image file path) -- set only for chunk_type="image"; None
    # otherwise. Lets a vision-capable generator ground its answer in the
    # real image instead of just its markdown description in `content`.
    asset_ref: str | None = None
    parent_chunk_id: str | None = None
