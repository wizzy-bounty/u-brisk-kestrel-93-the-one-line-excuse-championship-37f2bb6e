import os
from pathlib import Path

ENTRY = "I sent the apology to the printer because the error log listed it as the affected user."


def main() -> None:
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError("entry must contain 1 to 140 non-whitespace characters")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
