

from typing import NoReturn

import matplotlib.pyplot as plt
import numpy as np


P1 = 186158
T1 = 22.4 + 273.15
# PV = nRT
# P = nRT/V
# P/T = nR/V
nR_V = 186158 / T1

def internal_pressure(temp):
    return nR_V * (temp + 273.15)

def mean(*args):
    return sum(args) / len(args)

data = np.asarray([
    # Temp height
    [internal_pressure(22.4), mean(.54, .54, .55, .54)],    # room temp
    [internal_pressure(50.0), mean(.63, .64)],    # hot
    [internal_pressure(63.0), mean(.63, .63)],      # really hot
    [internal_pressure(60.0), mean(.62)],      # really hotish
    [internal_pressure(10.5), mean(.42, .38, .35, .36, .35)],    # cold
])



# Logarithmic regression
# 0.0685 + 0.1394 * ln(x)

T2 = 0
P2 = internal_pressure(T2)
#print(P2)

"""
plt.title("Lab Data") 
plt.xlabel("Internal Pressure (Pa)")
plt.ylabel("Height (m)") 

plt.plot(data[:, 0], data[:, 1], "o")
plt.show()
"""



#Logarithmic regression
def log_regression(data):
    x = np.log(data[:, 0])
    y = np.log(data[:, 1])
    m, b = np.polyfit(x, y, 1)
    return m, b


data = np.asarray([
    [2, 1],
    [4, 2],
    [8, 3],
    [16, 4],
    [32, 5],
    [64, 6],
    [128, 7],
])

print(log_regression(data))
