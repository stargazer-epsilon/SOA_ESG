class DelimitedString:
    """A helper class for working with delimited strings."""

    def __init__(self):
        # Default delimiter is ", " -- override using set_delimiter() method
        self.delimiter = ", "

    def get_delimiter(self):
        """Get the current delimiter."""
        return self.delimiter

    def set_delimiter(self, delimiter):
        """Set a new delimiter."""
        self.delimiter = delimiter

    def create_delimited_string(self, *args):
        """Create a string from the input arguments, separated by the delimiter."""
        return self.delimiter.join(map(str, args))

    def split_data(self, expression, delimiter=","):
        """
        Split a delimited string into a list of floating point numbers.

        If the delimiter is not specified, use the current delimiter.

        Return an empty list if the expression is empty or if there are no numbers.
        """

        if not expression:
            # Return an empty list if the expression is empty
            return []

        try:
            # Attempt to split the expression by the delimiter and convert each item to a float
            return [float(item) for item in expression.split(delimiter)]
        except ValueError:
            # If the conversion fails, return an empty list
            return []
