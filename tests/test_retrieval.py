from docquery_core import Chunk, RetrievedChunk


def test_holds_the_chunk_and_its_score() -> None:
    chunk = Chunk(chunk_id="c1", doc_id="d1", page_number=1, chunk_type="text", content="hello")
    retrieved = RetrievedChunk(chunk=chunk, score=0.87)
    assert retrieved.score == 0.87
    assert retrieved.chunk == chunk
