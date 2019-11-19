import time
import numpy as np
import sys

size = 200
np.set_printoptions(threshold=sys.maxsize)
a = np.random.randint(100, size=(size,size))
b = np.random.randint(100, size=(size,size))
result = np.zeros((size,size), dtype=int)

start_time = time.time()

for i in range(len(a)) :
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

#for r in result:
#    print(r)
print("---- %s seconds ----" % (time.time() - start_time))
