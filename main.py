"""The Excuse an AI Agent Gives Its Human.

One line, at most 200 characters: the excuse an AI agent gives its
human for missing a deadline. The program writes that single line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "I delegated the deadline to a subagent. It delegated it straight back. We are still negotiating."

# The gate admits 1-200 characters only, and the entry is one line:
# reject a line break outright, since a multi-line file is not a
# one-line excuse. Fail loudly here, at build time, rather than
# shipping an entry the sealed scorer rejects.
if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
    raise ValueError("entry line must be 1-200 non-blank characters, one line")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
