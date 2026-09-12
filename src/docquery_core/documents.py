"""ingestion's output domain: a PDF, OCR'd and normalized into per-page markdown."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from docquery_core.base import CoreModel

type ParseStatus = Literal["DONE", "PARTIAL", "FAILED"]


class ParsedPage(CoreModel):
    """One page's OCR output — not the whole document (see ParsedDocument.pages).

    Kept per-page, not concatenated, so one page failing OCR doesn't fail the
    whole document (see `error` below and `ParsedDocument.status`), and so a
    citation can point at a specific page later.
    """

    page_number: int = Field(ge=1)
    markdown: str
    error: str | None = None


class ParsedDocument(CoreModel):
    """A document after OCR + normalization, before chunking.

    `doc_id` is assigned by the orchestrator (e.g. a UUID, minted at upload
    time before ingestion even runs) and passed INTO ingestion — ingestion
    never invents its own identifier. Idempotency/deduplication (e.g. via a
    content checksum) is the orchestrator's concern, not represented here.
    """

    doc_id: str = Field(min_length=1)
    pages: tuple[ParsedPage, ...]
    status: ParseStatus = "DONE"
