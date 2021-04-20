import sys
import time
import math
import IMU
import datetime
import os
import matplotlib
matplotlib.use('Agg')
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
  
    
       
    ACCx = IMU.readACCx()*0.061/1000
    ACCy = IMU.readACCy()*0.061/1000
    ACCz = IMU.readACCz()*0.061/1000
    GYRx = IMU.readGYRx()*0.07
    GYRy = IMU.readGYRy()*0.07
    GYRz = IMU.readGYRz()*0.07
    
    print('ACCx:',ACCx,'ACCy:',ACCy,'ACCz:',ACCz,'GYRx:',GYRx,'GYRy:',GYRy,'GYRz:',GYRz)
    
    x_vals.append(i)
    ACCx_vals.append(ACCx)
    ACCy_vals.append(ACCy)
    ACCz_vals.append(ACCz)
    
    
    ax.plot(x_vals,ACCx_vals,color='b')
    ax.plot(x_vals,ACCy_vals,color='r')
    ax.plot(x_vals,ACCz_vals,color='g')
    ax.set_xlim(left=max(0, i-50), right=i+50)
    fig.show()
    time.sleep(.02)
    i += 1
   
   
