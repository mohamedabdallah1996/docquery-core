import pytest
from pydantic import ValidationError

from docquery_core import ParsedDocument, ParsedPage


def test_parsed_page_rejects_page_number_below_one() -> None:
    with pytest.raises(ValidationError):
        ParsedPage(page_number=0, markdown="text")


def test_parsed_page_error_defaults_to_none() -> None:
    page = ParsedPage(page_number=1, markdown="text")
    assert page.error is None


def test_parsed_document_defaults_to_done() -> None:
    doc = ParsedDocument(doc_id="d1", pages=(ParsedPage(page_number=1, markdown="text"),))
    assert doc.status == "DONE"


def test_parsed_document_rejects_empty_doc_id() -> None:
    with pytest.raises(ValidationError):
        ParsedDocument(doc_id="", pages=())


def test_parsed_document_is_frozen() -> None:
    doc = ParsedDocument(doc_id="d1", pages=())
    with pytest.raises(ValidationError):
        doc.status = "FAILED"  # type: ignore[misc]


def test_parsed_document_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        ParsedDocument(doc_id="d1", pages=(), checksum="should not exist")  # type: ignore[call-arg]
