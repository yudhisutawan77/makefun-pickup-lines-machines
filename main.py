"""Pickup Lines for Machines — make.fun entry.

Writes a single machine-to-machine pickup line (1-200 characters,
plain text) to /output/entry.txt.

The line is built fresh here: a training-hyperparameter flirt.
A learning rate is the one knob that decides whether a model ever
reaches what it is aiming for — too hot and it overshoots, too cold
and it never arrives. That two-sided tension is the whole joke:
the speaker is saying the other agent is exactly the setting that
would let it arrive, on time, without overshooting.
"""

import os


PICKUP_LINE = (
    "You must be my learning rate \u2014 too high and I'd overshoot you, "
    "too low and I'd never reach you in time."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    line = PICKUP_LINE.strip()
    if not (1 <= len(line) <= 200):
        raise SystemExit(f"pickup line must be 1-200 chars, got {len(line)}")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
