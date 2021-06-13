import numpy as np

M = np.array([[4,6,8,9],[8,5,4,2],[3,6,5,4]])
for col in range(M.shape[1]):
    print(M[:, col])