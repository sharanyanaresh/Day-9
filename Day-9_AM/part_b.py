# Matrix Addition
def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# Matrix Transpose
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]


# Matrix Multiplication
def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        return "Matrix multiplication not possible"

    return [[sum(a*b for a, b in zip(row_a, col_b))
            for col_b in zip(*B)]
            for row_a in A]


# Testing
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

print(matrix_add(a,b))
print(matrix_transpose(a))
print(matrix_multiply(a,b))