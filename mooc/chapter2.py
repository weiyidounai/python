# import math
#
# def add(x, y, f):
#     return f(x) + f(y)
#
# print add(25, 9,math.sqr)
# -*- coding: cp936 -*-
# import re
#
# string = "A1.45，b5，6.45，8.82"
# print(re.findall(r"\d+\.?\d*", string))
#
# # ['1.45', '5', '6.45', '8.82']

from scipy.sparse import *
from scipy import *
import numpy as np;
import scipy as sp;
# csr_matrix((3, 4), dtype=int8).todense()
# print(csr_matrix)
# row = array([0, 0, 1, 2, 2, 2])
# col = array([0, 2, 2, 0, 1, 2])
# data = array([1, 2, 3, 4, 5, 6])
# csr_matrix((data, (row, col)), shape=(3, 3)).todense()
# print(csr_matrix)

data = np.asarray([7, 8, 9])
indices = np.asarray([0, 1, 2])
indptr = np.asarray([0, 2, 3, 3])
m = sp.csc_matrix((data, indices, indptr), shape=(3, 3))
print(m.toarray())