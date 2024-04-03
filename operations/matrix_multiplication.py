import random
from time import *

from time_report import TimeReport


def matrix_multiplication_python() -> TimeReport:
    global n, col, row, A, B, C, start, i, j, end
    n = 512
    A = [[random.random()
          for row in range(n)]
         for col in range(n)]
    B = [[random.random()
          for row in range(n)]
         for col in range(n)]
    C = [[0 for row in range(n)]
         for col in range(n)]
    start = time()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    end = time()
    return TimeReport(cores=1, time=end - start, version_name='Python', base_python_time=end - start)