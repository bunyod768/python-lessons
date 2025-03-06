#Python number guessing game 
import random

quyi = 1
yuqori = 100
tanlanma = random.randint(quyi,yuqori)
urinish_soni = 0
davomiylik = True

print("Welcome to the number guessing game")

while davomiylik:
    sorov = input(f"select a number betwen {quyi} and {yuqori}:")
    if not sorov.isdigit():
        print(f" Please select a number betwen {quyi} and {yuqori}:")
    else:
        sorov = int(sorov)
        if sorov < quyi or sorov > yuqori:
            print(f" Please select a number betwen {quyi} and {yuqori}:")
        else:
            urinish_soni += 1
            if sorov < tanlanma:
             print("Too low.Try again!")
            elif sorov > tanlanma:
                 print("Too high.Try again!")
            else:
                print("CORRECT!")
                print(f"Number of guesses {urinish_soni}")
                print("GaMe OvEr!")
                davomiylik = False




