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
y_range = [0, 10]  # Range of possible Y values to display
x_vals,ACCx_vals,ACCy_vals,ACCz_vals=[],[],[],[]

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)

# Initialize communication with TMP102
tmp102.init()

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('Sensor Data')
plt.xlabel('Samples')
plt.ylabel('amplitudes')

# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
           
    ACCx = IMU.readACCx()*0.061/1000
    ACCy = IMU.readACCy()*0.061/1000
    ACCz = IMU.readACCz()*0.061/1000
    GYRx = IMU.readGYRx()*0.07
    GYRy = IMU.readGYRy()*0.07
    GYRz = IMU.readGYRz()*0.07
  
    
    print('ACCx:',ACCx,'ACCy:',ACCy,'ACCz:',ACCz,'GYRx:',GYRx,'GYRy:',GYRy,'GYRz:',GYRz)
    
   
    ACCx_vals.append(ACCx)
    ACCy_vals.append(ACCy)
    ACCz_vals.append(ACCz)
    
    # Add y to list
    ys.append(ACCx_vals)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=50,
    blit=True)
plt.show()
