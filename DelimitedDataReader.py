import csv

class DelimitedDataReader:
    """
    Creates a mechanism for reading delimited data files (i.e., numeric data)
    Usage:
      ddr = DelimitedDataReader("somefile.csv")
      for v in ddr.read_next():
        # Process v
    """
    def __init__(self, file_name, delimiter=','):
        """
        Initializes the DelimitedDataReader.
        Args:
            file_name (str): The file to read.
            delimiter (str, optional): The character used to separate values in the file. Defaults to ','.
        """
        self.file_name = file_name
        self.delimiter = delimiter
        self.file = open(file_name, 'r')
        self.reader = csv.reader(self.file, delimiter=self.delimiter)
        self.line_number = 0

    def read_next(self):
        """
        Ignores comments and blank lines -- yields None when end of file is reached.
        Returns:
            list: A list of values from the next non-blank, non-comment line in the file.
        """
        while True:
            try:
                row = next(self.reader)
                self.line_number += 1
                # Remove leading and trailing whitespaces
                row = [x.strip() for x in row]
                # Ignore comments and blank lines
                if not row or row[0].startswith(("//", "/*", "'")):
                    continue
                yield row
            except StopIteration:
                yield None
                break

    def clear(self):
        """
        Closes the open file and resets the reader and line number.
        """
        self.file.close()
        self.file = None
        self.reader = None
        self.line_number = 0

    def __del__(self):
        self.clear()


# In Python, the equivalent of the VBA ClassInitialize method is the __init__ method, and the equivalent of ClassTerminate is the __del__ method.

# Note that, unlike VBA, Python doesn't directly support properties the same way. So the fileName and LineNumber properties are accessed directly as attributes of the class instance (i.e., ddr.file_name and ddr.line_number).

# Moreover, the "EndOfFile" and "IsCommentLine" functions aren't necessary in Python, as Python's CSV reader will automatically raise a StopIteration exception when it reaches the end of the file. The Python version simply uses a for loop to iterate through lines in the file and ignores lines that are comments or blank.

# Finally, the error handling is implicit in Python. When an error occurs (like trying to open a non-existent file), Python will automatically raise an exception. You can use a try/except block if you want to catch and handle specific exceptions.