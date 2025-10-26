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

