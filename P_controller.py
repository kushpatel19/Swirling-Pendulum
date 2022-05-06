# import all required libraries
from cmath import pi
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
# time.sleep(5)

# To check closed loop control
print("starting closed loop control...")
drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

alpha1 = np.linspace(0,2*math.pi, 10)
alpha = np.array(alpha1)
value = []

# NumPy arrays have an attribute called shape that returns a tuple 
# with each index having the number of corresponding elements.
z = alpha.shape
err = 0
K = 1
er = []
alpha_actual = []
# Finding the cosine values of all our testing points  
# and store in a empty list
for j in range(0, z[0]):
    x1 = math.sin(alpha[j])
    value.append(x1)
    setpoint = x1
    drive.axis0.controller.input_pos = setpoint
    time.sleep(0.05)
    # Now, estimate the current position using encoders and store its value in empty list
    # And this is our final output to compare the original one
    current_pos = drive.axis0.encoder.pos_estimate
    err = x1 - current_pos
    er.append(err)
    prop = K * err
    alpha_actual.append(current_pos)

# Plotting the graph to trace the original curve and our curve
fig = plt.figure()
plt.plot(alpha,value,label='desired curve')
plt.xlabel("time in seconds")
plt.plot(alpha,alpha_actual,label='actual curve')
plt.ylabel("angular displacement in no. of turns")
plt.plot(er,value,label='error')
plt.legend()
plt.show()
quit()