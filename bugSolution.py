def improved_function(x, y):
    try:
        result = x / y
        return result
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example Usage
print(improved_function(10, 2)) # Output: 5.0
print(improved_function(10, 0)) # Output: Error: division by zero
print(improved_function(10, "a")) # Output: Error: unsupported operand type(s) for /: 'int' and 'str'
print(improved_function(10, 2/0)) #Output: An unexpected error occurred: float division by zero