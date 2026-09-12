"""Shared pydantic configuration for every type in this package."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CoreModel(BaseModel):
    """Base for every DocQuery-core type: immutable, rejects unknown fields.

    Frozen because every pipeline stage produces a *new* object rather than
    mutating what it received. `extra="forbid"` catches a misspelled field
    name at construction instead of silently ignoring it.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")
