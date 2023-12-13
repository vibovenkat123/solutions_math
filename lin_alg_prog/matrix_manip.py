import numpy as np
import scipy
import sympy as sp

a = np.matrix([[1, -1j], [0, 2 - 2j], [0, 1+0j]])
rrefed = sp.Matrix(a).rref()

print(rrefed)
