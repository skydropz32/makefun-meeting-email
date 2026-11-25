"""One-liner for make.fun: The Meeting That Should Have Been an Email.

Writes a single joke line (<=200 chars) to /output/entry.txt.
Standard library only; fully deterministic.
"""

from pathlib import Path

LINE = "Our weekly sync ended when someone said the quiet part out loud: \"We're just reading the email together, but slower.\""


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
