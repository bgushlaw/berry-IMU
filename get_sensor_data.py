import sys
import time
import math
import IMU
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('fivethirtyeight')

IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass


    
#fig = plt.figure()
#ax = fig.add_subplot(111)
i=0

time.sleep(1) # wait for mpu9250 sensor to settle


# prepping for visualization
berry_imu_str = ['accel-x','accel-y','accel-z','gyro-x','gyro-y','gyro-z']

x_vals,ACCx_vals,ACCy_vals,ACCz_vals=[],[],[],[]

def animate(i,x_vals,ACCx_vals,ACCy_vals,ACCz_vals):

    plt.cla()

    plt.plot(x_vals, ACCx_vals, label='Channel 1')
    plt.plot(x_vals, ACCy_vals, label='Channel 2')
    plt.plot(x_vals, ACCz_vals, label='Channel 3')
    
   
    
    plt.legend(loc='upper left')
    plt.tight_layout()


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
    
    

    ani = FuncAnimation(plt.gcf(), animate(i,x_vals,ACCx_vals,ACCy_vals,ACCz_vals), interval=1000)
    i += 1
    plt.tight_layout()
    plt.show()
    time.sleep(.02)
   
