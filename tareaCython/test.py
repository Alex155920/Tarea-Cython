from functionE import rbf_network
from Cy_functionE import c_rbf_network
#import Cy_functionE 
import numpy as np
import time
#import matplotib.pyplot as plt
from matplotlib import pyplot as plt

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10


inicio = time.time()
start = time.time()
rbf_network(X, beta, theta)

total_time = time.time()-start

start = time.time()

c_rbf_network(X, beta, theta)

cy_total_time = time.time() - start

#start = time.time()

#c_array_f_multi(X)

#cy_multi_total_time = time.time() - start


speedUP = round(total_time/cy_total_time, 3)
#speedUp_multi = round(total_time/cy_multi_total_time,3)

print("Tiempo Python: {} \n".format(total_time))
print("Tiempo Cython: {} \n".format(cy_total_time))
#print("Cython_multi time: {} \n".format(cy_multi_total_time))
print("SpeedUP: {} \n".format(speedUP))
#print("SpeedUP: {} \n".format(speedUp_multi))

fig, ax = plt.subplots()
img = ["tiempo Python","Tiempo Cython"]
var = [total_time , cy_total_time]
ax.set_ylabel("tiempo")
plt.bar(img , var, width = 0.4 , color=["cyan","darkviolet"])
plt.savefig("comparativa.png")
plt.grid()
plt.show()










