# import all required libraries
from cmath import pi
# from multiprocessing.spawn import import_main_path
import odrive
import numpy as np
from odrive.enums import *
import time
import statistics
import math
import random
from matplotlib import pyplot as plt

# Define our odrive
drive = odrive.find_any()
time.sleep(5)

# To check closed loop control
print("starting closed loop control...")
drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

#Define all testing points
alpha1 = np.linspace(0,((1/4)*math.pi), 500)
alpha = np.array(alpha1)
value = []

# NumPy arrays have an attribute called shape that returns a tuple 
# with each index having the number of corresponding elements.
z = alpha.shape

# Finding the cosine values of all our testing points  
# and store in a empty list
for j in range(0, z[0]):
    x1 = math.tan(alpha[j])
    value.append(x1)
# To create an array of all listed values
value = np.array(value)
    
# Give the command to the odrive for controlling the position according to the cosine values 
alpha_actual = []
for i in range(0,len(alpha)):
    setpoint = value[i] 
    drive.axis0.controller.input_pos = setpoint
    time.sleep(0.05)
    # Now, estimate the current position using encoders and store its value in empty list
    # And this is our final output to compare the original one
    current_pos = drive.axis0.encoder.pos_estimate
    alpha_actual.append(current_pos)

# Plotting the graph to trace the original curve and our curve
fig = plt.figure()
plt.plot(alpha,value,label='desired curve')
plt.xlabel("time in seconds")
plt.plot(alpha,alpha_actual,label='actual curve')
plt.ylabel("angular displacement in no. of turns")
plt.legend()
plt.show()
quit()