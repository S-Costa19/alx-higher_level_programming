#!/usr/bin/python3

def read_file(filename=""):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')  # Print each line without adding extra newline

    except FileNotFoundError:
        pass  # File not found, do nothing

# Example usage:
if __name__ == "__main__":
    read_file("example.txt")  # Replace with your file name

