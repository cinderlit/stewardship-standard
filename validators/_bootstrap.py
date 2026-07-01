"""Resolve cinderlit_governance from install or sibling monorepo src."""

from __future__ import annotations

import sys
from pathlib import Path


def ensure_package() -> None:
    try:
        import cinderlit_governance  # noqa: F401
        return
    except ModuleNotFoundError:
        pass

    here = Path(__file__).resolve()
    for ancestor in here.parents:
        for rel in (
            "packages/governance-validators/src",
            "mind-over-meta-parent/packages/governance-validators/src",
        ):
            src = ancestor / rel
            if (src / "cinderlit_governance").is_dir():
                sys.path.insert(0, str(src.resolve()))
                return

    raise ModuleNotFoundError(
        "cinderlit_governance not found. Run: pip install -r requirements-dev.txt"
    )
