from DelimitedDataReader import DelimitedDataReader

class DelimitedDataReaderSet:
    """
    Provides a collection class for working with multiple DelimitedDataReader instances
    Usage:
      dds = DelimitedDataReaderSet()
      for ddr in dds.items:
        # Work with ddr instance
    """
    def __init__(self):
        """
        Initializes a new instance of the DelimitedDataReaderSet class.
        """
        self.reader_collection = []

    def clear(self):
        """
        Clears the reader collection.
        """
        self.reader_collection.clear()

    def add_reader(self, file_name, delimiter=','):
        """
        Adds a new DelimitedDataReader to the collection.
        Args:
            file_name (str): The file for the new DelimitedDataReader to read.
            delimiter (str, optional): The character used to separate values in the file. Defaults to ','.
        """
        ddr = DelimitedDataReader(file_name, delimiter)
        self.reader_collection.append(ddr)

    @property
    def items(self):
        """
        Returns the collection of DelimitedDataReaders.
        Returns:
            list: The collection of DelimitedDataReaders.
        """
        return self.reader_collection

    @property
    def count(self):
        """
        Returns the number of DelimitedDataReaders in the collection.
        Returns:
            int: The number of DelimitedDataReaders in the collection.
        """
        return len(self.reader_collection)

    def __getitem__(self, index):
        """
        Gets the DelimitedDataReader at the given index.
        Args:
            index (int): The index of the DelimitedDataReader to get.
        Returns:
            DelimitedDataReader: The DelimitedDataReader at the given index.
        """
        return self.reader_collection[index]

    def __del__(self):
        self.clear()
