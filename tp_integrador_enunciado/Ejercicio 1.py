import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def norm(vector):
    l0 = la.norm(vector, ord=0, axis=1)
    l1 = la.norm(vector, ord=1, axis=1)
    l2 = la.norm(vector, ord=2, axis=1)
    linf = la.norm(vector, ord=np.inf, axis=1)
    return l0, l1, l2, linf

a = np.array([[-2, -4, 2],[-2, 1, 2],[4, 2, 5]])

print (norm(a))

