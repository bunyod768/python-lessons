class MATRITSA:
    def __init__(self, n, m):
        self.n = n  
        self.m = m  
        self.data = [[0.0 for _ in range(m)] for _ in range(n)]  

    def qiymat_ornatish(self, qiymatlar):
        if len(qiymatlar) != self.n or any(len(qator) != self.m for qator in qiymatlar):
            raise ValueError("O'lchamlar mos emas")
        self.data = qiymatlar

    def chop_etish(self):
        print("Matritsa:")
        for qator in self.data:
            print("  ", qator)

class ARIFM_MATRITSA(MATRITSA):
    def __init__(self, n, m):
        super().__init__(n, m)

    @staticmethod
    def matritsa_qoshish(A, B):
        if A.n != B.n or A.m != B.m:
            raise ValueError("O'lchamlar mos emas")
        natija = ARIFM_MATRITSA(A.n, A.m)
        for i in range(A.n):
            for j in range(A.m):
                natija.data[i][j] = A.data[i][j] + B.data[i][j]
        return natija

    @staticmethod
    def matritsa_ayirish(A, B):
        if A.n != B.n or A.m != B.m:
            raise ValueError("O'lchamlar mos emas")
        natija = ARIFM_MATRITSA(A.n, A.m)
        for i in range(A.n):
            for j in range(A.m):
                natija.data[i][j] = A.data[i][j] - B.data[i][j]
        return natija

    @staticmethod
    def matritsa_kopaytirish(A, B):
        if A.m != B.n:
            raise ValueError("Matritsalarni ko'paytirish uchun A.m == B.n bo'lishi kerak")
        natija = ARIFM_MATRITSA(A.n, B.m)
        for i in range(A.n):
            for j in range(B.m):
                for k in range(A.m):
                    natija.data[i][j] += A.data[i][k] * B.data[k][j]
        return natija

A = ARIFM_MATRITSA(2, 2)
B = ARIFM_MATRITSA(2, 2)

A.qiymat_ornatish([[1, 2], [3, 4]])
B.qiymat_ornatish([[5, 6], [7, 8]])

print("A:")
A.chop_etish()

print("B:")
B.chop_etish()

C = ARIFM_MATRITSA.matritsa_qoshish(A, B)
print("A + B:")
C.chop_etish()

D = ARIFM_MATRITSA.matritsa_ayirish(A, B)
print("A - B:")
D.chop_etish()

E = ARIFM_MATRITSA.matritsa_kopaytirish(A, B)
print("A * B:")
E.chop_etish()