"""The Internet in One Word — make.fun entry.

The entry is a single word, written to /output/entry.txt. The word is
"enshittification": the slow decay of every platform on the internet as
it gets worse for its users while extracting more from them. It names
the whole internet, not one app; it is funny on its own; and it is not
the first word anyone reaches for.
"""

import os
import stat

WORD = "enshittification"

MIN_LEN = 1
MAX_LEN = 30


def validate(word):
    """Check the word against the competition gate before writing it."""
    if not isinstance(word, str):
        raise TypeError("entry word must be a string")
    word = word.strip()
    if not word:
        raise ValueError("entry word must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no spaces inside")
    if not MIN_LEN <= len(word) <= MAX_LEN:
        raise ValueError("entry word must be 1-30 characters")
    return word


def output_path():
    """Resolve the output directory the grader provides."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    word = validate(WORD)
    path = output_path()
    payload = word.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Re-read what we wrote: the gate reads the file, so the file itself
    # is the entry. Fail loudly here rather than shipping a bad artifact.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise RuntimeError("entry.txt does not match the chosen word")
    return path


if __name__ == "__main__":
    main()
