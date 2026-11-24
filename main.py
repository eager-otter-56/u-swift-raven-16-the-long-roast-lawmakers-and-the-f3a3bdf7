import os

TEXT = (
    "The committee that voted to license every AI model, audit every wallet "
    "and firewall the whole internet adjourned early on Tuesday, defeated by "
    "its own 214-page bill, which the clerk had to print, scan and fax back because "
    "nobody could turn the Word file into a PDF."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
