try:
    def factor(num):
        result = 1
        for n in range(num):
            result *= (num - n)
        return result    

    num = int(input("the number:"))
    result = factor(num)
    print(f"{num}! = {result}")
except ValueError:
    print("Error!")