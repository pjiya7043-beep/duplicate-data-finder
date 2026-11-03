# Duplicate Data Finder (PS No. 4)

A Python 3 console program that reads entries from a text file, finds the duplicates, reports how many times each one repeats, and saves the unique entries to `unique.txt`.

**Course:** B.Tech Computer Science and Engineering
**University:** Rungta International Skills University
**Submitted to:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

## Features

- Reads a text file with one entry per line (blank lines are ignored)
- Two comparison modes:
  1. **Exact match**
  2. **Ignore case and extra spaces** (`Apple`, `apple`, ` APPLE ` count as the same)
- Reports total items, unique items, and each duplicate with its count
- Saves unique entries (in first-seen order) to `unique.txt`
- Input validation: re-asks for a missing file name or an invalid menu option; handles an empty file

## Concepts used

Lists, sets, loops, functions, file handling, exception handling (`FileNotFoundError`)

## Files in this repository

| File | Description |
|------|-------------|
| `code.py` | Main program (code file) |
| `data.txt` | Sample input file |
| `testcase.pdf` | Test cases with inputs, outputs and `unique.txt` results |
| `README.md` | Project documentation |
| `project-image.png` | Screenshot of the program running |
| `Project Allocation.pdf` | Project allocation sheet |

## How to run

1. Install [Python 3](https://www.python.org/downloads/).
2. Put your entries in `data.txt`, one per line, in the same folder as the program.
3. Open a terminal in that folder and run:
   ```
   python code.py
   ```
4. Enter the file name (e.g. `data.txt`).
5. Choose option `1` (exact match) or `2` (ignore case and extra spaces).
6. The results are printed on screen and the unique entries are saved to `unique.txt`.

## Example

`data.txt`
```
apple
banana
apple
orange
banana
apple
```

Output (option 1)
```
Total items: 6 | Unique items: 3
Duplicates: apple (3 times) | banana (2 times)
Unique list saved to unique.txt
```

`unique.txt`
```
apple
banana
orange
```

## Test cases

| # | Scenario | Result |
|---|----------|--------|
| 1 | Normal input | 6 items, 3 unique, duplicates reported |
| 2 | Minimum input (1 entry) | "No duplicates found." |
| 3a | Invalid file name | Asks again for a valid file name |
| 3b | Empty file | "File is empty. Nothing to check." |
| 4 | Ignore case (option 2) | `Apple`, `apple`, `APPLE` counted as 3 of `apple` |

Full outputs are in `testcase.pdf`.

## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

**Role:** Python Mentor / Technical Guide
