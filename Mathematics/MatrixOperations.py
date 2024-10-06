import numpy as np


class MatrixOperations:

    @staticmethod
    def column_count(matrix: np.array) -> int:
        column_count = np.shape(matrix)[1]
        return column_count

    @staticmethod
    def row_count(matrix: np.array) -> int:
        row_count = np.shape(matrix)[0]
        return row_count

    @staticmethod
    def dot_product(matrix1: np.array, matrix2: np.array):
        return np.dot(matrix1, matrix2)

#%%
