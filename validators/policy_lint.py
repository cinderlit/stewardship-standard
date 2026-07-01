#!/usr/bin/env python3
"""Thin wrapper — logic lives in cinderlit-governance."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bootstrap import ensure_package

ensure_package()
from cinderlit_governance.policy_lint import main

if __name__ == "__main__":
    sys.exit(main())
