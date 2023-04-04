
from scipy import signal
import matplotlib.pyplot as plot
import numpy as np


t = np.linspace(0, 15, 1000, endpoint=True)

# Plot the square wave signal
v1 = .5 * (signal.sawtooth(2 * np.pi * t / 10, .5) - 1)
v2 = .5 * (signal.square(2 * np.pi * (t - .5) / 2) + 1)
v3 = 5
vO = -(2.14*v1 + v2 + .47*v3)

plot.plot(t, vO)

# title
plot.title("Voltage VO")

# x axis label
plot.xlabel("Time (ms)")

# y axis label
plot.ylabel("Voltage (V)")

plot.grid(True, which="both")

# Provide x axis and line color
plot.axhline(y=0, color="k")

# Set the max and min values for y axis
plot.ylim(-4, 0)

# Display
plot.show()
