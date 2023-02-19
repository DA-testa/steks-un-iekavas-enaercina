#ena daniela ercina
import os
import sys
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    mismatches = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))
        elif next_char in ")]}":
            if not opening_brackets_stack:
                mismatches.append(Bracket(next_char, i))
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next_char):
                    mismatches.append(Bracket(next_char, i))
    while opening_brackets_stack:
        top = opening_brackets_stack.pop()
        mismatches.append(Bracket(top.char, top.position))
    if not mismatches:
        return "Success"
    return mismatches

def main():
    input_type = input("Enter input type (I for input, F for file): ")
    if input_type == "F":
        while True:
            test_name = input("Enter the test name: ")
            filename = f"test/{test_name}"
            if os.path.isfile(filename):
                with open(filename, 'r') as file:
                    text = file.readline().strip()
                    break
            else:
                print(f"File '{filename}' not found. Please enter a valid test name.")
    else:
        print("Enter the text:")
        if sys.stdin.isatty():
            text = input()
        else:
            text = sys.stdin.read(100000)
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch[0].position + 1)

if __name__ == "__main__":
    main()
