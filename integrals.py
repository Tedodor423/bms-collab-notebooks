# -*- coding: utf-8 -*-

import numpy as np
dt = 0.1
blood = 0

for t in np.arange(dt/2,60,dt):
  blood = blood + (np.sin(t)+1)*dt

print(blood)
print(60-(np.cos(60)-np.cos(0)))

"""#Space rocket"""

dt = 0.001
d = 0

for t in np.arange(dt/2,5,dt):
  d = d + (2*np.exp(t)-0.5*t**2)*dt

print(d)
print(2*np.exp(5)-0.5*5**3/3-2*np.exp(0))

dt = 0.001
d = 0

for t in np.arange(1+dt/2,5,dt):
  d = d + (2*np.exp(t)-0.5*t**2)*dt

print(d)

"""# Space rocket - influence of dt"""

dt_values = np.linspace(0.001,1,1000)
integral_values = np.zeros(len(dt_values))

def computeIntegral(dt):
  d = 0
  for t in np.arange(dt/2,5,dt):
    d = d + (2*np.exp(t)-0.5*t**2)*dt
  return d

for i,dt in enumerate(dt_values):
  integral_values[i] = computeIntegral(dt)

import matplotlib.pyplot as plt

plt.plot(dt_values, integral_values, marker='o', label='Calculated Integral')
plt.xlabel('Step Size (dt)', fontsize=12)
plt.ylabel('Integral Value', fontsize=12)
plt.show()

"""# Other methods"""

# using sum
t = np.arange(dt/2,5,dt)
v_values = 2 * np.exp(t) - 0.5 * t**2

dt = 0.001

integral = np.sum(v_values)*dt
print(integral)


# using built-in integral computation
from scipy.integrate import quad

def v(t):
    return 2 * np.exp(t) - 0.5 * t**2

result, error = quad(v, 0, 5)
print(result)
print(error)

"""# Appendix

"""

import matplotlib.pyplot as plt

dt_fine = 0.001
t_fine = np.arange(0,5+dt_fine,dt_fine)
v_fine = 2*np.exp(t_fine)-0.5*t_fine**2

plt.plot(t_fine,v_fine, 'r', label='v')
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')

dt_coarse = 0.1
t_coarse = np.arange(dt_coarse/2,5,dt_coarse)
v_coarse = 2*np.exp(t_coarse)-0.5*t_coarse**2

plt.bar(t_coarse, v_coarse, width=dt_coarse, align='center', alpha=0.5, label='Rectangles')
plt.title('Numerical integration of distance travelled')
plt.legend()