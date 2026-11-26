#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (stdlib only, no network).

Writes one funny line to /output/entry.txt, byte-for-byte, no trailing
newline. Sealed gate: UTF-8 text of 1 to 140 characters, single line.
"""

import os

LINE = "My plants died, so I bought plastic ones. They died too. I have now been banned from the garden centre."

assert 1 <= len(LINE) <= 140, f"line length {len(LINE)} outside gate 1-140"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "  " not in LINE, "no double spaces"
assert LINE.isascii(), "line must be pure ASCII (no multi-byte surprises)"
LINE.encode("utf-8")  # strict UTF-8 check

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
path = os.path.join(OUT_DIR, "entry.txt")

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read-back verification: byte-for-byte match, no trailing newline.
with open(path, "rb") as f:
    data = f.read()
assert not data.startswith(b"\xef\xbb\xbf"), "BOM present in output"
text = data.decode("utf-8", errors="strict")  # strict UTF-8 decode
assert text == LINE, "read-back mismatch"
assert 1 <= len(text) <= 140, "read-back length outside gate 1-140"
assert "\n" not in text and "\r" not in text, "read-back is not a single line"
assert not data.endswith(b"\n"), "trailing newline present"
print(f"Wrote {len(data)} bytes to {path}")
