# import os
# Opening a File

# To work with a file, you must first open it using the built-in open() function.
# Syntax:
# file = open("filename", "mode")

# Reading from a File

# You can read file content in several ways.

# (a) read()

# Reads the entire file as one string.

# file=open("demo.txt", "r")
# print(file.read()) #read whole file
# print(file.read(5)) #read first 5 characters

# readline()
# Reads one line at a time.
# print(file.readline()) #read line by line 
# file.close()

#  Writing to a File

# You can create or overwrite files using 'w'. 
# it also returns the number of characters written to the file.

# file=open("demo.txt", "w")

# print(file.write("Hey bro< it's SD"))


# file.close()

# Appending to a File

# Appending means adding new content without deleting old data.

# f = open("demo.txt", "a")
# f.write("\nAdding another line!")
# f.close()

# "r+" means read and write mode.

# It allows you to:
# Read from a file
# Write (or modify) data in the same file
# But — the file must already exist (else you’ll get an error).

# Syntax:
# file = open("demo.txt", "r+")

# How it works:

# When you open a file with "r+",
# the file pointer starts at the beginning of the file.
# If you write something, it overwrites existing content from the start.

# file = open("demo.txt", "a+")
# print(file.read())
# print(file.write("Subhamoy Datta...."))
# file.close()

# | Mode | Read | Write | File must exist? | Overwrites?               | Pointer starts at |
# | ---- | ---- | ----- | ---------------- | ------------------------- | ----------------- |
# | `r`  | ✅    | ❌     | ✅                | ❌                         | Start             |
# | `w`  | ❌    | ✅     | ❌ (creates new)  | ✅                         | Start             |
# | `a`  | ❌    | ✅     | ❌ (creates new)  | ❌ (adds at end)           | End               |
# | `r+` | ✅    | ✅     | ✅                | ✅ (from pointer position) | Start             |
# | `w+` | ✅    | ✅     | ❌ (creates new)  | ✅                         | Start             |
# | `a+` | ✅    | ✅     | ❌ (creates new)  | ❌ (adds at end)           | End               |

# "r+" means read and write mode.

# It allows you to:
# Read from a file
# Write (or modify) data in the same file
# But — the file must already exist (else you’ll get an error).

# Syntax:
# file = open("demo.txt", "r+")

# How it works:

# When you open a file with "r+",
# the file pointer starts at the beginning of the file.

# If you write something, it overwrites existing content from the start.

# file = open("demo.txt", "r+")
# print(file.read())
# print(file.write("hello....I'm subhamoy"))
# file.close()

# using with syntax:
# The with statement automatically closes the file after use — even if an error occurs.

# with open("demo.txt", "r") as f:
#     print(f.read())

 
# OS module:

# The os module provides functions to interact with the operating system.

# You can do things like:

# Create, delete, or rename files and directories

# Check file existence

# Get the current working directory

# Work with paths

# Run system commands

# Import it first:

# import os

# os.remove("demo.txt")

# os.remove("demo.txt") Deletes the file "demo.txt" from your system.

# Important: only works for files, not folders.

# After this, the file is permanently removed.

# os.path.exists("demo.txt") Checks if a file or folder exists at the given path.

# Returns:

# True → file/folder exists

# False → file/folder does not exist

# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("File deleted successfully")
# else:
#     print("File does not exist")






