import pickle

with open("data",'rb') as file:
    PI = pickle.load(file)
print(PI)    