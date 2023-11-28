import os

file_name = "my_first_file.txt"
try:
    os.remove(file_name)
except FileNotFoundError:
    print("File already deleted!")
