# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def EquacoesDiferenciais(q, t):
    a = (95/100)
    g = (5/100)
    b = (35/100)
    m = (65/100)
    dpdt = -(a*q[0]) - (g*q[0])
    dsdt = (a*q[0]) - (b*q[1]) - (m*q[1])
    return [dpdt,dsdt]

p0 = 10
s0 = 10   
q0 = [p0, s0]
T = np.arange(0,100,0.0001)

s = odeint(EquacoesDiferenciais, q0, T)

plt.plot(T, s[:, 1])
plt.ylabel('s(t)')
plt.xlabel('T')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show()