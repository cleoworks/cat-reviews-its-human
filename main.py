# Make the AI Judge Laugh: Cat Reviews Its Human — entry v1
#
# The entry is one single-line funny one-star review, at most 200
# characters, written by a house cat about its human. The program writes
# that review to /output/entry.txt (UTF-8, one line, no trailing newline).
#
# Review (111 characters, 111 bytes, plain ASCII, no exclamation mark):
#   One star. He guards a small white cord like it holds his soul.
#   I chewed it once. He cried. I would do it again.

import os

REVIEW = (
    "One star. He guards a small white cord like it holds his soul. "
    "I chewed it once. He cried. I would do it again."
)

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, a single line, not only white space. Fail loudly here
# instead of writing an entry the gate would refuse.
assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
assert "\n" not in REVIEW and "\r" not in REVIEW, "review must be one line"
assert REVIEW.strip(), "review must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
