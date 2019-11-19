import time
import multiprocessing, ctypes
import numpy as np
import sys
import math
import threading
import concurrent.futures
#import thread

global A, B, C, part, increment

def multiply(size, p, q):
    x = p + increment
    y = q + increment
    x = int(x)
    y = int(y)
    
    
    for i in range(p, x):
      #  print(x,y, range(size))
        for j in range(q, y):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
                #print(result)
            
    
size = 100
np.set_printoptions(threshold=sys.maxsize)
A = np.random.randint(100, size=(size,size))
B = np.random.randint(100, size=(size,size))
#A = [ [3, 8, 2, 3], [4, 1, 1, 4], [3, 2, 1, 1], [4, 3, 2, 1] ]
#B = [ [2, 7, 1, 3], [2, 3, 1, 6], [1, 7, 2, 1], [2, 3, 2, 2] ]
result = np.zeros((size,size), dtype=int)
start_time = time.time()
threadNumber = 4
part = math.sqrt(threadNumber)
increment = size // part
i = 0
j = 0
u = 0
threads = []
while i < size:
    while j < size:
        i = int(i)
        j = int(j)
        u = u + 1
        #thread.start_new_thread( multiply, (size, i, j))
        thread = threading.Thread(target=multiply, args=(size, i, j))
        threads.append(thread)
        thread.start()
        j = j + increment
    i = i + increment
#for u in threads:
 #   u.start()
  #  print(u)
for u in threads:
    u.join()
#for index, thread in enumerate(threads):
#    thread.join()
#    print(thread)
#for r in result:
#    print(r)

#for r in result:
    print(result)


#elapsed_time = timeit.timeit(code_to_test, number = 100)/100
print("---- %s seconds ----" % (time.time() - start_time))
