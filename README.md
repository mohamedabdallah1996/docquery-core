# docquery-core

Shared data types and schemas for DocQuery's submodules.

## Overview

DocQuery is split into independently versioned submodules (ingestion, chunking, embedding,
indexing, generation) composed by a main orchestrator repository. Every one of those
submodules needs to agree on the shape of the data passed between them — a `Chunk`, a
`ParsedDocument`, an embedding vector, a retrieval result, a generated answer. `docquery-core`
is that shared vocabulary: a small, dependency-light package of [Pydantic](https://docs.pydantic.dev/)
models with no business logic and no external calls, so every submodule can depend on it
without pulling in anything heavier than `pydantic` itself.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12+ |
| Data validation | Pydantic 2 |
| Package/dependency management | uv |
| Linting & formatting | Ruff |
| Type checking | mypy (`--strict`) |
| Testing | pytest |

## Architecture

Every type here is immutable (`model_config = ConfigDict(frozen=True, extra="forbid")`, set
once on the shared `CoreModel` base) and organized by which pipeline stage produces it:

- **`documents.py`** — ingestion's output: `ParsedDocument`, `ParsedPage`, `ParseStatus`.
- **`chunks.py`** — chunking's output: `Chunk`, `ChunkType`.
- **`embeddings.py`** — embedding's output: `EmbeddedChunk` (a `Chunk` paired with its vector).
- **`retrieval.py`** — indexing's output / generation's input: `RetrievedChunk`.
- **`generation.py`** — generation's output: `GenerationResult`, `TokenUsage`.
- **`exceptions.py`** — `DocQueryError`, the base every submodule's own exceptions inherit
  from, so the orchestrator can catch broadly without this package knowing about any
  submodule's specific failure modes.

All types are re-exported from the package root (`docquery_core/__init__.py`), so consumers
import from `docquery_core` directly without knowing the internal file layout:

```python
from docquery_core import Chunk, ParsedDocument
```

Because every submodule pins a version of this package, changes here are meant to be rare and
additive (new optional fields) rather than breaking (renamed/removed fields) once submodules
depend on a given version.

## Project Structure

```
src/docquery_core/
  base.py          # CoreModel — shared frozen/extra="forbid" config
  documents.py     # ParsedDocument, ParsedPage, ParseStatus
  chunks.py        # Chunk, ChunkType
  embeddings.py    # EmbeddedChunk
  retrieval.py     # RetrievedChunk
  generation.py    # GenerationResult, TokenUsage
  exceptions.py    # DocQueryError
  __init__.py      # Flat re-export of the above
tests/             # One test module per src file
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

### Installation

```bash
git clone https://github.com/mohamedabdallah1996/docquery-core
cd docquery-core
uv sync
```

### Using it from another submodule

This package isn't published to PyPI — it's consumed either as a `uv` workspace member during
local development (a path dependency resolved from source, live-reloaded on every change) or
installed from a built wheel via `build-submodules.sh` in DocQuery main repo, which clones this
repo, builds it, and installs the resulting wheel.

## Testing

```bash
uv run pytest
```

## Development

```bash
uv run ruff check .
uv run ruff format .
uv run mypy src
```