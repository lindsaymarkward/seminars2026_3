"""
Write a program to read a file and print ONLY the lines
that start with a #
The user should enter the filename.
"""

# filename = "seminar02.py"
filename = input("filename: ")
try:
    in_file = open(filename, "r")
    for line in in_file:
        # print(repr(line))
        line = line.strip()
        # if line.startswith("#"):
        try:
            if line[0] == "#":
                print(line)
        except IndexError:
            continue
    in_file.close()
except FileNotFoundError:
    print("File not found :(")
