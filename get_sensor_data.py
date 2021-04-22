import sys
import time
import math
import IMU
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
import os.path
from os import path
import piDataWrangler




IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass


    
window_size=128


# prepping for visualization
berry_imu_str = ['accel-x','accel-y','accel-z','gyro-x','gyro-y','gyro-z']
Old_Feature_list = ['acc-X', 'acc-Y', 'acc-Z','gyro-X', 'gyro-Y', 'gyro-Z']
New_Feature_list = ['Bacc-X', 'Bacc-Y', 'Bacc-Z', 'Gacc-X', 'Gacc-Y', 'Gacc-Z', 'gyro-X', 'gyro-Y', 'gyro-Z']
Final_Feature_list = ['tBodyAcc-mean-X','tBodyAcc-mean-Y','tBodyAcc-mean-Z','tBodyAcc-std-X', 'tBodyAcc-std-Y', 'tBodyAcc-std-Z','tBodyAcc-max-X','tBodyAcc-max-Y','tBodyAcc-max-Z','tBodyAcc-min-X','tBodyAcc-min-Y','tBodyAcc-min-Z','tGravityAcc-mean-X','tGravityAcc-mean-Y','tGravityAcc-mean-Z','tGravityAcc-std-X','tGravityAcc-std-Y','tGravityAcc-std-Z','tGravityAcc-max-X','tGravityAcc-max-Y','tGravityAcc-max-Z','tGravityAcc-min-X','tGravityAcc-min-Y','tGravityAcc-min-Z','tBodyGyro-mean-X','tBodyGyro-mean-Y','tBodyGyro-mean-Z','tBodyGyro-std-X','tBodyGyro-std-Y','tBodyGyro-std-Z','tBodyGyro-max-X','tBodyGyro-max-Y','tBodyGyro-max-Z','tBodyGyro-min-X','tBodyGyro-min-Y','tBodyGyro-min-Z']
#x_vals,ACCx_vals,ACCy_vals,ACCz_vals=[],[],[],[]

new_Path='PiData/'
file_name=new_Path+'TestingIt'
save_data=pd.DataFrame(columns=Final_Feature_list)
save_data.to_csv(file_name+'.csv',index=True)
df=save_data

while True:
  
    
    for x in range(0,window_size)   
        ACCx = IMU.readACCx()*2*0.061/1000
        ACCy = IMU.readACCy()*2*0.061/1000
        ACCz = IMU.readACCz()*2*0.061/1000
        GYRx = IMU.readGYRx()*0.07
        GYRy = IMU.readGYRy()*0.07
        GYRz = IMU.readGYRz()*0.07
        
        df=df.append(df)
        time.sleep(.02)
        
   wf=piDataWrangler.Create_Features(df,file_name,Old_Feature_list,New_Feature_list,Final_Feature_list)
   print(wf)
    
    #print('ACCx:',ACCx,'ACCy:',ACCy,'ACCz:',ACCz,'GYRx:',GYRx,'GYRy:',GYRy,'GYRz:',GYRz)
    

    


   
