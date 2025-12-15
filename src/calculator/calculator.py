"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""



    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        # Validate inputs
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        # Validate inputs
        self._validate_input(a, b)
        
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        # Validate inputs
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        # Validate inputs
        self._validate_input(a, b)
        return a / b
    
    def _validate_input(self, *value):
        """Validate that the input value is within the acceptable range.

        Args:
            value: The input value to validate 
        Raises:
            InvalidInputException: If value is outside the range -1,000,000 to 1,000,000
        """
        for v in value:
            if v < -1000000 or v > 1000000:
                raise InvalidInputException(f"Input value {v} is outside the valid range (-1,000,000 to 1,000,000)")    
            





