# 3-misol
from xml.sax.handler import property_interning_dict

n = int(input("n:"))
m = int(input("m:"))
s = 0
p = 1
i = 1
j = 5
for i in range(i,n+1):
    for j in range(j,m+1):
        p *= (i+j)
    s += p
    p = 1
print("Yig'ndi:",s)