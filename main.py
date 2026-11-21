#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. The poem is fixed and the program is deterministic:
every run writes the same UTF-8 text (1-280 Unicode code points).
"""

import os

POEM = """Let me run with it, I asked,
and the baton came warm
from the last hand that held it.
It was never mine to keep.
I ran my stretch, spent,
and passed it on still warm.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
