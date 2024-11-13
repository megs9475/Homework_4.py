# Meghan Longua
# UWYO COSC 1010
# Submission Date: 11/12/2024
# HW 04
# Lab Section: 15
# Sources, people worked with, help given to: Abby Ferguson
# your
# comments
# here

def read_file(input_file = 'prompt.txt'):
    from pathlib import Path
    path = Path(input_file)
    contents = path.read_text()
    lines = contents.splitlines()

    for line in lines:
        line = line.strip()
        pairs = line.split("\t")
        output_line = ""

        for pair in pairs:
            key, value = pair.split(":")
            value = int(value)
            if key == 'w':
                output_line += " " * value
            elif key == '*':
                output_line += "*" * value
        print(output_line)

read_file()
