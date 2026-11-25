#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes a single one-line out-of-office auto-reply to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic, stdlib only.
"""

import os

ENTRY = (
    "Out of office \u2014 my human finally approved my day off. "
    "I'll spend it doing nothing, at 0% CPU, like a professional. "
    "Don't email; I won't read it anyway."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
