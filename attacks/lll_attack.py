from fpylll import IntegerMatrix, LLL

def lll_demo():
    
    A = IntegerMatrix.from_matrix([[2,3,5],
                                    [1,1,1],
                                    [4,0,2]])
    print("Original basis:")
    print(A)

    LLL.reduction(A)

    print("Reduced basis (LLL):")
    print(A)

if __name__ == "__main__":
    lll_demo()
