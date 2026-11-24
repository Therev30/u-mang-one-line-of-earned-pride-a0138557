import os

# Deterministic entry: one fixed line, 135 characters, no trailing newline.
LINE = "She had practised the same scale every morning since she was seven; tonight, her grandmother stopped humming along and simply listened."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
