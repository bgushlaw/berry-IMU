import sys
import time
import math
import IMU
import datetime
import os
import matplotlib.pyplot as plt

IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass


    
fig = plt.figure()
ax = fig.add_subplot(111)
i=0
x_vals,ACCx_vals,ACCy_vals,ACCz_vals=[],[],[],[]


while True:
  
    
       
    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    GYRx = IMU.readGYRx()
    GYRy = IMU.readGYRy()
    GYRz = IMU.readGYRz()
    
    print('ACCx:',ACCx)
    
    x_vals.append(i)
    ACCx_vals.append(ACCx)
    ACCy_vals.append(ACCy)
    ACCz_vals.append(ACCz)
    
    
    ax.plot(x_vals,ACCx_vals,color='b')
    ax.plot(x_vals,ACCy_vals,color='r')
    ax.plot(x_vals,ACCz_vals,color='g')
    ax.set_xlim(left=max(0, i-50), right=i+50)
    fig.canvas.draw()
    fig.show()
    time.sleep(.02)
    i += 1
   
   
