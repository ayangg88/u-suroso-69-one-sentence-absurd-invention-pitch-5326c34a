#!/usr/bin/env python3
"""One-sentence absurd invention pitch: the Comfort Charger.

Writes the pitch to $MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt).
Deterministic: no input, no randomness, no trailing newline.
"""

import os

PITCH = "The Comfort Charger is a phone charger that unplugs itself the moment you finally get comfortable, then plays a tiny violin to mark the occasion."

def main():
    # Gate, same as the bounty scorer: one sentence, 1-220 characters.
    assert 1 <= len(PITCH) <= 220, "pitch outside the 1-220 character gate"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read back what was written: the file must hold exactly the pitch.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == PITCH, "entry.txt does not match the pitch"

if __name__ == "__main__":
    main()
