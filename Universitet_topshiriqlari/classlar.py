### Berilgan natural n soni uchun n*n o’lchamidagi A va B matritsalar ustida A+B, A*B, AT   amallarini bajaradigan MATRITSA sinfi yaratilsin. ###

class MATRITSA:
    def __init__(self, n, A, B):
        self.n = n
        self.A = A
        self.B = B

    def qoshish(self):
        natija = []
        for i in range(self.n):
            qator = []
            for j in range(self.n):
                qator.append(self.A[i][j] + self.B[i][j])
            natija.append(qator)
        return natija

    def kopaytirish(self):
        natija = []
        for i in range(self.n):
            qator = []
            for j in range(self.n):
                summa = 0
                for k in range(self.n):
                    summa += self.A[i][k] * self.B[k][j]
                qator.append(summa)
            natija.append(qator)
        return natija

    def transpozitsiya(self):
        natija = []
        for j in range(self.n):
            qator = []
            for i in range(self.n):
                qator.append(self.A[i][j])
            natija.append(qator)
        return natija

    def chop_et(self, matritsa):
        for qator in matritsa:
            print(qator)

# ==== MISOL UCHUN ====
n = 2
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]

mat = MATRITSA(n, A, B)

print("A + B:")
mat.chop_et(mat.qoshish())

print("\nA * B:")
mat.chop_et(mat.kopaytirish())

print("\nA Transpozitsiyasi:")
mat.chop_et(mat.transpozitsiya())