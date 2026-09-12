import pytest

from docquery_core import DocQueryError


def test_is_a_regular_exception() -> None:
    assert issubclass(DocQueryError, Exception)
    with pytest.raises(DocQueryError):
        raise DocQueryError("something failed")
