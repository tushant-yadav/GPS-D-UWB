import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import random
'''
======================================================================================
LOW PASS FILTER 
======================================================================================'''

#      FILTER FUNCTTION
def lowpass(input,last_output, dt ,timeconstant):
    alpha = dt / ( timeconstant + dt)
    output = (alpha * input) + ((1-alpha) *last_output )
    return (output)

           
plt.xlabel('Iterations')
plt.ylabel('Values X 2')
plt.grid()
plt.legend()


'''
dt= time between readings
tc= Time constant decided from cutoff frequency to be decided from practical data interpretation
'''
dt= 0.033
tc=0.1
last_output=0
data=[]
iter=[]
output=[]

for i in range (100):
    data.append((random.uniform(0,100)* random.choice([1, -1])) )
    iter.append(i)
    last_output=lowpass(data[i],last_output,dt,tc)
    output.append(last_output)  

plt.plot(iter,output,color='b')    
plt.plot(iter,data,color='r')
plt.show()