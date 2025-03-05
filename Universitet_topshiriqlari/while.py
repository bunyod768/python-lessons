n = int(input("n:"))
m = int(input("m:"))
i = 3
j  = 2
p = 1
s = 0
while i <= n-1:
    while j <= m-3:
        s += 2 * i + j
        j += 1
    p *= s
    s = 0
    j = 2
    i += 1
print("kopaytma:",p)