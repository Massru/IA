import numpy as np

puzle_final = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
puzle_inicial = np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])

print((puzle_final != puzle_inicial).sum())

