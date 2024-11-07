class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b  # Corrected: it should be a - b

    def multiply(self, a, b):
        result = 0
        # Use a loop to add 'a' to result 'b' times
        for _ in range(abs(b)):  # Use abs(b) to handle cases when b is negative
            result = self.add(result, a)
        # Adjust the sign if 'b' is negative
        if b < 0:
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = 0
        remainder = abs(a)
        b_abs = abs(b)
        # Subtract 'b' from 'a' until 'a' is smaller than 'b'
        while remainder >= b_abs:
            remainder = self.subtract(remainder, b_abs)
            result = self.add(result, 1)
        # Adjust result sign based on the original inputs' signs
        if (a < 0) ^ (b < 0):  # XOR: result is negative if only one is negative
            result = -result
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero")
        remainder = abs(a)
        b_abs = abs(b)
        # Subtract 'b' from 'a' until 'a' is smaller than 'b' to find remainder
        while remainder >= b_abs:
            remainder = self.subtract(remainder, b_abs)
        # Return remainder with the same sign as 'a'
        return remainder if a >= 0 else -remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))           # 3
    print("Example: subtraction: ", calc.subtract(4, 2))   # 2
    print("Example: multiplication: ", calc.multiply(2, 3)) # 6
    print("Example: division: ", calc.divide(10, 2))       # 5
    print("Example: modulo: ", calc.modulo(10, 3))         # 1
