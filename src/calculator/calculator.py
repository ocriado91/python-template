class Calculator:
    """ A Calculator class to compute basic operations."""

    def sum(a: float, b: float) -> float:
        """ Compute the sum between two float variables."""
        return a + b

    def substract(a: float, b: float) -> float:
        """ Compute the substraction between two float variables."""
        return a - b

    def multiplication(a: float, b: float) -> float:
        """ Computhe the multiplication between two float variables."""
        return a * b

    def division(a: float, b: float) -> float:
        """ Compute the division between two float variables."""
        try:
            return a / b
        except ZeroDivisionError:
            raise ZeroDivisionError("ERROR: Divisor must be different from 0.")
