# | Mode   | Meaning      | Description                                                                    |
# | ------ | ------------ | ------------------------------------------------------------------------------ |
# | `'r'`  | Read         | Opens file for reading (default). Error if file doesn’t exist.                 |
# | `'w'`  | Write        | Opens file for writing, **creates** a new file or **overwrites** existing.     |
# | `'a'`  | Append       | Opens file for writing but **adds** content to the end instead of overwriting. |
# | `'x'`  | Create       | Creates new file, **error** if file already exists.                            |
# | `'b'`  | Binary       | Opens file in **binary mode** (useful for images, PDFs).                       |
# | `'t'`  | Text         | Opens file in **text mode** (default).                                         |
# | `'r+'` | Read + Write | Opens file for both reading and writing.                                       |

# Opening a File

# To work with a file, you must first open it using the built-in open() function.
# Syntax:
# file = open("filename", "mode")

# Reading from a File

# You can read file content in several ways.

# (a) read()

# Reads the entire file as one string.

file=open("demo.txt", "r")
# print(file.read()) #read whole file
# print(file.read(5)) #read first 5 characters

# readline()
# Reads one line at a time.
# print(file.readline()) #read line by line 
file.close()

#  Writing to a File

# You can create or overwrite files using 'w'. 
# it also returns the number of characters written to the file.

# file=open("demo.txt", "w")

# print(file.write("Hey bro< it's SD"))


# file.close()

# Appending to a File

# Appending means adding new content without deleting old data.

f = open("demo.txt", "a")
f.write("\nAdding another line!")
f.close()


