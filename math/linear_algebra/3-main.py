#!/usr/bin/env python3
matrix_transpose = __import__('3-flip_me_over').matrix_transpose
mat1 = [[1, 2], [3, 4]]
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]
print(matrix_transpose(mat2))
