import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import IMU


IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass



# Parameters
x_len = 200         # Number of points to display
y_range = [-5, 5]  # Range of possible Y values to display
x_vals,ACCx_vals,ACCy_vals,ACCz_vals=[],[],[],[]

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len
ax.set_ylim(y_range)


# Create a blank line. We will update the line in animate
line1, = ax.plot(xs, ys1)
line2, = ax.plot(xs, ys2)
line3, = ax.plot(xs, ys3)

# Add labels
plt.title('Sensor Data')
plt.xlabel('Samples')
plt.ylabel('amplitudes')

# This function is called periodically from FuncAnimation
def animate(i, ys1,ys2,ys3):

    # Read temperature (Celsius) from TMP102
           
    ACCx = IMU.readACCx()*2*0.061/1000
    ACCy = IMU.readACCy()*2*0.061/1000
    ACCz = IMU.readACCz()*2*0.061/1000
    GYRx = IMU.readGYRx()*0.07
    GYRy = IMU.readGYRy()*0.07
    GYRz = IMU.readGYRz()*0.07
  
    
    #print('ACCx:',ACCx,'ACCy:',ACCy,'ACCz:',ACCz,'GYRx:',GYRx,'GYRy:',GYRy,'GYRz:',GYRz)
    
   
    ACCx_vals.append(ACCx)
    ACCy_vals.append(ACCy)
    ACCz_vals.append(ACCz)
    
    # Add y to list
    ys1.append(ACCx)
    ys2.append(ACCy)
    ys3.append(ACCz)
    
    # Limit y list to set number of items
    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]
    
    # Update line with new Y values
    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)
    line1.set_label('ACCx')
    line2.set_label('ACCy')
    line3.set_label('ACCz')
    ax.legend()
    return line1,line2,line3,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys1,ys2,ys3,),
    interval=20,
    blit=True)
plt.show()
