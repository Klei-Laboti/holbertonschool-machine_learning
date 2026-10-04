#!/usr/bin/env python3
cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
print(cat_matrices2D(mat1, mat2))          # axis=0
print(cat_matrices2D(mat1, mat3, axis=1))  # axis=1
print(cat_matrices2D(mat1, mat2, axis=1))  # s'përputhet -> None
