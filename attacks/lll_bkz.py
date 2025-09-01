import numpy as np
from fpylll import IntegerMatrix, LLL, BKZ

def lwe_instance(n=10, q=97):
    A = np.random.randint(0, q, (n, n))
    s = np.random.randint(0, q, n)
    e = np.random.randint(-1, 2, n)  
    b = (A @ s + e) % q
    return A, b, s

def attack_with_lll(A, b, q):
    mat = IntegerMatrix.from_matrix(A.tolist())
    LLL.reduction(mat)
    return mat

def attack_with_bkz(A, b, q, block_size=5):
    mat = IntegerMatrix.from_matrix(A.tolist())
    par = BKZ.Param(block_size=block_size)
    BKZ.reduction(mat, par)
    return mat

if __name__ == "__main__":
    A, b, s = lwe_instance()
    print("Running toy LLL/BKZ attack...")
    print(attack_with_lll(A, b, 97))
