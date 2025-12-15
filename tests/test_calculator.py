"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        # Arrange
        calc = Calculator()
        a = -6
        b = -3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_by_zero_raises(self):
        """Test dividing by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)
    
    def test_divide_negative_numbers(self):
        calc = Calculator()
        assert calc.divide(-6, 3) == -2
        assert calc.divide(6, -3) == -2
        assert calc.divide(-6, -3) == 2

    def test_divide_to_float(self):
        calc = Calculator()
        assert calc.divide(3, 2) == 1.5

class TestInvalid:
    """Tests for invalid inputs."""

    def test_add_too_large_invalid_input(self):
        """Test adding with invalid input."""
        # Arrange
        calc = Calculator()
        a = 150000000
        b = 3

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
    
    def test_second_add_too_large_invalid_input(self):
        """Test adding with invalid input."""
        # Arrange
        calc = Calculator()
        a = 3
        b = 150000000

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
    
    def test_add_too_small_invalid_input(self):
        """Test adding with invalid input."""
        # Arrange
        calc = Calculator()
        a = -150000000
        b = 3

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
    
    def test_second_add_too_small_invalid_input(self):
        """Test adding with invalid input."""
        # Arrange
        calc = Calculator()
        a = 3
        b = -150000000

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
    
    def test_subtract_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1500000, 1)
    
    def test_subtract_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(-1500000, 1)
    
    def test_subtract_second_arg_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1, 1_500_000)

    def test_subtract_second_arg_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1, -1_500_000)
    
    def test_multiply_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1500000, 2)

    def test_multiply_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(-1500000, 2)
    
    def test_multiply_second_arg_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(2, 1500000)
    
    def test_multiply_second_arg_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(2, -1500000)

    def test_divide_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1500000, 2)
    
    def test_divide_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(-1500000, 2)
    
    def test_divide_second_arg_too_large_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(2, 1500000)
    
    def test_divide_second_arg_too_small_invalid_input(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(2, -1500000)


class TestValidateInputBoundary:
    """Boundary tests for input validation."""

    def test_add_at_upper_boundary_is_ok(self):
        calc = Calculator()
        result = calc.add(1000000, 0)
        assert result == 1000000

    def test_add_just_over_upper_boundary_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 0)

    def test_add_at_lower_boundary_is_ok(self):
        calc = Calculator()
        result = calc.add(-1000000, 0)
        assert result == -1000000

    def test_add_just_under_lower_boundary_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 0)
    
