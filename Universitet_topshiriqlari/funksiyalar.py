# Ihtiyariy n ta sonning maxsimumini  hisoblash funktsiasi tuzilsin.

def Max(*son):
    big = son[0]
    for i in son:
        if i > big:
            big = i
    return big

result = Max(1,2,3,4,5,6,100,200,10,300)
print(result)