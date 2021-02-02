import matplotlib.pyplot as plt
import numpy as np
from math import *

g = 9.8
m = 2
Cx = 0.47
Cy = 0.47
K = 0.5
rho = 1.293
pi = 3.14159
r = 0.06
kx = (Cx * K * rho * 4 * np.pi * r*r)
ky = (Cy * K * rho * 4 * np.pi * r*r)

vfp = float(input("vfp = "))
alpha = float(input("alpha = "))

v_x = vfp * np.cos(alpha)
v_y = vfp * np.sin(alpha)

print(v_x, v_y)
tmax = float(input("tmax = "))
n = 1000000
dt = tmax*(1/n)

t = np.linspace(0, tmax, n)

def y(v_y):
    y = 0
    v = v_y
    y_ = []
    t = 0
    while t < tmax:
        v = v + dt*(- g +(-ky/m)*((v**3)/(abs(v))))
        y = y + v*dt
        y_.append(y)
        t = t + dt
    return(y_)

def y_speed(v_y):
    y = 0
    v = v_y
    y_ = []
    t = 0
    while t < tmax:
        v = v + dt*(- g +(-ky/m)*((v**3)/(abs(v))))
        y_.append(v)
        t = t + dt
    return(y_)

def x(v_y):
    x = 0
    v = v_x
    x_ = []
    t = 0
    while t < tmax:
        v = v + dt*((-ky/m)*((v**3)/(abs(v))))
        x = x + v*dt
        x_.append(x)
        t = t + dt
    return(x_)

def x_speed(v_y):
    x = 0
    v = v_x
    x_ = []
    t = 0
    while t < tmax:
        v = v + dt*((-ky/m)*((v**3)/(abs(v))))
        x_.append(v)
        t = t + dt
    return(x_)

X_ = x(v_x)
Y_ = y(v_y)

X_speed = x_speed(v_x)
Y_speed = y_speed(v_x)

plt.plot(X_, Y_)
plt.title("position")
plt.show()

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(t, X_speed, color = 'red')
ax1.set_title('x_speed')
ax2.plot(t, Y_speed, color = "green")
ax2.set_title('y_speed')
plt.show()
