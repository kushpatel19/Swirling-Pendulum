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
time.sleep(5)

# To check closed loop control
print("starting closed loop control...")
drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# Inputs
alpha = 0.05
alpha1 = math.pi * 0.5
t=np.linspace(0,10, 100)
t1 = np.array(t)


# Set the Troque control mode
drive.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
# Approximately 8.23 / Kv where Kv is in the units [rpm / V]
drive.axis0.motor.config.torque_constant = 8.23 / 150

# Define required variables
err = 0
Kp = 0.02
er = []
tol = 0.00001
alpha_actual = []
# alpha_actual.append(alpha1)
t0 =[]

for i in t1:
    if alpha >=0.1:
        alpha = 0.1
    elif alpha <= (-0.1):
        alpha = (-0.1)
    else:
        alpha
    # print(alpha)
    setpoint = alpha
    drive.axis0.controller.input_torque = setpoint
    time.sleep(0.05)
    # Now, estimate the current position using encoders and store its value in empty list
    # And this is our final output to compare the original one
    current_pos = drive.axis0.encoder.pos_estimate
    err = alpha1 - current_pos
    if err <= tol:
        break
    else:
        t0.append(i)
    er.append(err)
    prop = Kp * err
    # print(current_pos)
    alpha_actual.append(current_pos)
    alpha = prop
   
alpha2 = [alpha1] * len(t0)
# t1 = list(t1)
# alpha2 = list(alpha2)
# alpha_actual = list(alpha_actual)
# er = list(er)
# print(len(t1))
# print(t1)
# print(len(alpha2))
# print(alpha2)
# print(len(alpha_actual))
# print(alpha_actual)
# print(len(er))
# print(er)


# Plotting the graph to trace the original curve and our curve
fig = plt.figure()
plt.plot(t0,alpha2,label='desired curve')
plt.plot(t0,alpha_actual,label='actual curve')
plt.plot(t0,er,label='error')
plt.xlabel("time in seconds")
plt.ylabel("angular displacement in no. of turns")
plt.legend()
plt.show()
quit()