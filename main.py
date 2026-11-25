"""One-line roast entry for u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes a single original line (1-200 characters) roasting a gadget used
every day to /output/entry.txt. Python standard library only.
"""

import os
import stat

ENTRY = (
    "My laptop fan spins up like a jet engine every time I open a "
    "spreadsheet, as if the numbers might escape."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the bounty brief's constraints."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")  # must be valid UTF-8 text
    return True


def write_entry(text, out_dir):
    """Write one validated line to entry.txt, world-readable for the grader.

    Returns the path written. Plain open() + explicit chmod 644: the
    grader runs as a different user, so the file must be world-readable
    (never tempfile.mkstemp, which forces mode 0600).
    """
    validate(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return path


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    path = write_entry(ENTRY, out_dir)
    print(f"wrote {len(ENTRY)}-character entry to {path}")


if __name__ == "__main__":
    main()
