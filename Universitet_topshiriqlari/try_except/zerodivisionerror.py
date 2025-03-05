# Example of an exception
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError

except ZeroDivisionError:
    print("Can't be divided by zero!")