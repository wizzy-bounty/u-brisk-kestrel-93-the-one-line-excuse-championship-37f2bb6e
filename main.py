import os
from pathlib import Path

ENTRY = "I sent the apology to the printer because the error log listed it as the affected user."


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


def main() -> None:
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError("entry must contain 1 to 140 non-whitespace characters")

    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
