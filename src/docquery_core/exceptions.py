"""Shared error base for every DocQuery submodule.

Each submodule defines its own specific subclasses of `DocQueryError` — this
package only holds the common root, so the orchestrator can catch broadly
(`except DocQueryError`) without core needing to know about any submodule's
specific failure modes.
"""

from __future__ import annotations


class DocQueryError(Exception):
    """Base for every error raised across DocQuery's submodules."""
