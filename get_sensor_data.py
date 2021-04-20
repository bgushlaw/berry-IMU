import sys
import time
import math
import IMU
import datetime
import os
 
  
while True:
    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    GYRx = IMU.readGYRx()
    GYRy = IMU.readGYRy()
    GYRz = IMU.readGYRz()
    print('ACCx:',ACCx,'ACCy',ACCy,'ACCz:',ACCz,'GYRx:',GYRx,'GYRy:',GYRy,'GYRz:',GYRz)
