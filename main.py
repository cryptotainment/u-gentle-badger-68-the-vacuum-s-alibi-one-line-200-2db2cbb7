"""The Vacuum's Alibi: one line, 200 characters or fewer.

A robot vacuum explains, in its own deadpan voice, why it missed a spot.
The program writes the line to /output/entry.txt (the gate reads it from
there) and prints it to stdout for inspection.
"""

import os

LINE = (
    "The spot under the sofa was 96% cat hair, so per Section 4 of my "
    "firmware I classified it as the cat's property. Case closed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
