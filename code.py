"""Duplicate Data Finder (PS No. 4)

Reads a text file (one entry per line), finds duplicate entries, reports how
many times each repeats, and saves the unique entries to unique.txt.
"""


def read_entries(filename):
    """Return list of non-blank lines, or None if the file doesn't exist."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f if line.strip()]
    except FileNotFoundError:
        return None


def normalize(entry, ignore_case):
    """Option 1: exact match. Option 2: ignore case and extra spaces."""
    if ignore_case:
        return " ".join(entry.split()).lower()
    return entry


def main():
    # 1. Get a valid, existing file
    while True:
        filename = input("Enter file name (e.g. data.txt): ").strip()
        entries = read_entries(filename)
        if entries is None:
            print(f"File '{filename}' not found. Please enter a valid file name.")
            continue
        break

    if not entries:
        print("File is empty. Nothing to check.")
        return

    # 2. Menu
    print("\nMenu")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    while True:
        choice = input("Enter option (1/2): ").strip()
        if choice in ("1", "2"):
            break
        print("Invalid option. Please enter 1 or 2.")
    ignore_case = choice == "2"

    # 3. Normalize entries for comparison
    items = [normalize(e, ignore_case) for e in entries]

    # 4. Unique entries (set for membership, list to keep first-seen order)
    seen = set()
    unique_list = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)

    # 5. Count repeats with a loop
    duplicates = []
    for item in unique_list:
        count = items.count(item)
        if count > 1:
            duplicates.append((item, count))

    # 6. Report
    print(f"\nTotal items: {len(items)} | Unique items: {len(unique_list)}")
    if duplicates:
        parts = [f"{name} ({count} times)" for name, count in duplicates]
        print("Duplicates: " + " | ".join(parts))
    else:
        print("No duplicates found.")

    # 7. Save unique entries
    with open("unique.txt", "w", encoding="utf-8") as f:
        for item in unique_list:
            f.write(item + "\n")
    print("Unique list saved to unique.txt")


if __name__ == "__main__":
    main()
