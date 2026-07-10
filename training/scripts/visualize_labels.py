from pathlib import Path


LABEL_DIR = Path("dataset/license_plate/labels/train")


def main() -> None:
    label_files = list(LABEL_DIR.glob("*.txt"))
    print(f"Found {len(label_files)} label files")


if __name__ == "__main__":
    main()
