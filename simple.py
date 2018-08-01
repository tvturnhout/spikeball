import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

accel_x = []
accel_y = []
accel_z = []

while True:
    accel_x.append(np.random.random())
    accel_y.append(np.random.random())
    accel_z.append(np.random.random())
    if len(accel_x) > 100:
        accel_x.pop(0)
        accel_y.pop(0)
        accel_z.pop(0)
    plt.plot(accel_x,c='red',label='accel_x')
    plt.plot(accel_y,c='blue',label='accel_y')
    plt.plot(accel_z,c='green',label='accel_z')
    plt.pause(0.05)
    plt.gcf().clear()

plt.show()