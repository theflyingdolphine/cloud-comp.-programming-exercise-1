#D=(A*B)*C, A=10^6*10^3, B=10^3*10^6, C=10^6*1

import numpy as np
import matplotlib.pyplot as plt
import psutil as ps
import time

def main():
   start = time.time()


   #initialize 2D matrices of set, all vaues are assigned a random number in the range (0, 1)
   arrayA = np.random.randint(2, size=(pow(10,3), pow(10,1)))  
   arrayB = np.random.randint(2, size=(pow(10,1), pow(10, 3)))  
   arrayC = np.random.randint(2, size=(pow(10,3), 1))
   print("arrays initialized")

   #print(np.array(arrayA), "\n", np.array(arrayB), "\n", np.array(arrayC), "\n")

   #calculate the dot product of matrix A and matrix B
   calculated_AB = np.dot(arrayA, arrayB)
   print("calculate 1 done")

   #calculate the dot product of matrix AB and matrix C
   calculated_D = np.dot(calculated_AB, arrayC)
   print("calculate 2 done")

   #CPU and memory usage
   print("CPU percentage", ps.cpu_percent())
   print("Virtual memory", ps.virtual_memory())

   #displays time taken for system to run
   end = time.time()
   print(end - start)

   #plot CDF
   calculated_CDF = np.cumsum(np.argsort(calculated_D))
   initiate1, initiate2 = np.histogram(calculated_CDF)
   plt.xlabel("Data")
   plt.ylabel("Percent")
   plt.title("CDF")

   cdf = np.cumsum((initiate1 / sum(initiate1)))
   plt.plot(initiate2[1:], cdf, color="pink", marker="o")
   plt.show()
   

if __name__=="__main__":
   main()


#multiplication of two matrices - method not used
#array_base = np.random.randint(1, size=(pow(10,3),pow(10,3))) 
#for i in range(len(array1)):
   # for j in range(len(array2[0])):
  #      for k in range(len(array2)):
 #         array_base[i, j] += (array1[i, k] * array2[k, j])

#print(array_base)
