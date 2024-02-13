"""A Python script to clean and convert the data to a csv file."""

import re
import os

# Define the pattern for the title and data
PATTERN_TITLE = r"^([A-Za-z-]+\s+){19}[A-Z+a-z+-]+\n$"
PATTERN_DATA = r"^(\d{4})\s+(-?\d+\s+){12}(((-?\d+)|\*+)\s+){6}(\d{4})\n$"


def celcius_to_fahrenheit(celcius: str) -> str:
    """Convert degree celcius to fahrenheit"""
    return f"{float(celcius) / 100 * 9 / 5:.1f}"


def munge_data(raw_data: str, output_file: str) -> None:
    """Clean the data and write to a csv file"""
    clean_data = []
    raw_data = os.path.join("data", "GLB.Ts+dSST.txt")
    with open(raw_data, "r", encoding="utf-8") as file:
        is_title = True
        # Read the file line by line
        for line in file:
            if re.match(re.compile(PATTERN_DATA), line):
                raw_line = line.strip().split()[:-1]
                for i, x in enumerate(raw_line):
                    if i == 0:
                        pass
                    elif re.match(re.compile(r"-?\d+"), x):
                        raw_line[i] = celcius_to_fahrenheit(x)
                    else:
                        raw_line[i] = "0.0"
                clean_data.append(raw_line)
            if re.match(re.compile(PATTERN_TITLE), line) and is_title:
                is_title = False
                clean_data.append(line.strip().split()[:-1])

    # Write the data to a csv file
    with open(output_file, "w", encoding="utf-8") as file:
        for line in clean_data:
            file.write(",".join(line) + "\n")

if __name__ == "__main__":
    munge_data("data/GLB.Ts+dSST.txt", "data/clean_data.csv")
