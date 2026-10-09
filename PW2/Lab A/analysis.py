"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py

!!!In class Notes :

in python easiest way to calc der:
numpy.gradient(values, times)(np.gradient())  we put in it array of anything and we get array of derivatives
To find integral in python we use:
cumulative_trapizoid() from scipy.     , but also we should add v(t0) from formula for correct answer 

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv",  delimiter=",",skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
v = np.gradient(y, t)
#and acceleration a = derivative of v w.r.t. t    (np.gradient again)
a = np.gradient(v, t)

#Print the mean acceleration. Is it close to -9.81? Is it noisy?
mean_a = np.mean(a)
std_a = np.std(a)
print(f"Mean acceleration: {np.max(mean_a)} m/s^2")
print(f"Acceleration standard deviation: {np.max(std_a)} m/s^2")


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a,t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec,t,initial=0)+ y[0]
max_diff = np.abs(y_rec - y)
print(f"Maximum position difference: {np.max(max_diff)} m")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
# Pos
axes[0].plot(t,y,label="Measured position")
axes[0].plot(t,y_rec,"--",label = "Recovered position")
axes[0].set_ylabel("Position(m)")
axes[0].set_title("Position vs Time")
axes[0].legend()
axes[0].grid(True)
#vel
axes[1].plot(t, v, color="orange")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].set_title("Velocity vs Time")
axes[1].grid(True)
#ac
axes[2].plot(t, a, color="green", label="Measured acceleration")
axes[2].axhline(-9.81,color="red",linestyle="--",label="Theoretical acceleration (-9.81 m/s²)")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")
axes[2].set_title("Acceleration vs Time")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
#Save it as motion.png
plt.savefig("motion.png")
plt.show()


