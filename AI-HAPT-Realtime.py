import sys
import time
import math
import IMU
from pathlib import Path
#import datetime
import os
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
#import os.path
from os import path
import piDataWrangler
from fastai.tabular.all import *
from fastai.vision.widgets import *




IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass

path=Path()

if path.ls(file_exts='.pkl'):
    learn_inf = load_learner(path/'Wrangled_no_ID.pkl')
    id_to_name = {1:'walking', 2: 'walking_upstairs', 3: 'walking_downstairs', 4:'sitting', 5:'standing', 6:'laying',7:'stand_to_sit', 8:'sit_to_stand', 9:'sit_to_lie', 10:'lie_to_sit', 11:'stand_to_lie', 12:'lie_to_stand'} 
else:    
    print('No .PKL file found in path directory ' + path)
    print('Aborting execution")
    sys.exit()
          
          
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
#df = pd.DataFrame(0, index=np.arange(128), columns=Old_Feature_list)
a = np.zeros(shape=(window_size,6))

while True:
    tic=time.perf_counter()
    tic3=time.perf_counter()
    
    #df=pd.DataFrame(columns=Old_Feature_list)
   
    for x in range(0,window_size):
        toc3=time.perf_counter()
        while toc3-tic3<.02:
            toc3=time.perf_counter()
        tic3=time.perf_counter()   
        ACCx = IMU.readACCx()*2*0.061/1000
        ACCy = IMU.readACCy()*2*0.061/1000
        ACCz = IMU.readACCz()*2*0.061/1000
        GYRx = IMU.readGYRx()*0.07
        GYRy = IMU.readGYRy()*0.07
        GYRz = IMU.readGYRz()*0.07
            
        a[x]=[ACCx,ACCy,ACCz,GYRx, GYRy,GYRz]

      
       
        
    df=pd.DataFrame(a, columns = Old_Feature_list)
    toc=time.perf_counter()
    tic2=time.perf_counter()
    wf=piDataWrangler.Create_Features(df,file_name)
    row, clas, probs = learn_inf.predict(wf.iloc[0])
    rowList = list(probs)
    Confidence = max(rowList)
    Guess_ID=rowList.index(Confidence)+1
    
    toc2=time.perf_counter()
    print('Physiological State:',id_to_name.pop(Guess_ID), f" Confidence: {Confidence*100:0.2f} %",  f" Sensor time: {toc - tic:0.4f} seconds", f"Data Wrangling time: {toc2 - tic2:0.4f} seconds" )
    
    
    
    
   
    

    
