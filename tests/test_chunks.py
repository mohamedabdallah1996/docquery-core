import pytest
from pydantic import ValidationError

from docquery_core import Chunk


def _chunk(**overrides: object) -> Chunk:
    defaults: dict[str, object] = {
        "chunk_id": "c1",
        "doc_id": "d1",
        "page_number": 1,
        "chunk_type": "text",
        "content": "hello",
    }
    return Chunk(**{**defaults, **overrides})  # type: ignore[arg-type]


def test_section_path_defaults_to_empty_tuple() -> None:
    assert _chunk().section_path == ()


def test_asset_ref_and_parent_chunk_id_default_to_none() -> None:
    chunk = _chunk()
    assert chunk.asset_ref is None
    assert chunk.parent_chunk_id is None


def test_rejects_invalid_chunk_type() -> None:
    with pytest.raises(ValidationError):
        _chunk(chunk_type="not-a-real-type")


def test_section_path_has_no_mutating_methods() -> None:
    # A tuple, not a list -- there is no in-place mutation to guard against,
    # which is a stronger guarantee than "frozen model + mutable list field".
    chunk = _chunk(section_path=("A", "B"))
    assert not hasattr(chunk.section_path, "append")


def test_round_trips_through_json() -> None:
    chunk = _chunk(section_path=("Intro",))
    restored = Chunk.model_validate_json(chunk.model_dump_json())
    assert restored == chunk
