import numpy as np
import scipy
import sympy as sp

a = np.matrix([[1, -2, 2], [0, 2, -2], [1, -3, 4]])
b = np.matrix([[1], [-1], [2]])
x = scipy.linalg.solve(a, b);
print(x)
