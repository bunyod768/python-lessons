a = [10, 20, 30]

try:
    # Valid negative index
    print(a[-1])

    # Invalid negative index
    print(a[-4])
except IndexError:
    print("Negative index is out of range.")
