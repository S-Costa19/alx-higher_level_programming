#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')

    except FileNotFoundError:
        pass  # File not found, do nothing

if __name__ == "__main__":


    read_file("my_file_0.txt")

# Add two blank lines here to satisfy the formatting requirement
