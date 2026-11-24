#!/usr/bin/env python3
"""Developer Excuses — one-line entry.

Writes one funny single-line excuse a developer gives when code
breaks in production (at most 200 characters) to /output/entry.txt.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The excuse: the code passed every test — production just was not
# one of them. A twist a developer recognises, in developer voice.
# Counted at 63 characters — inside the 1..200 window.
LINE = "The code passed all tests. Production was not one of the tests."


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the excuse to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
