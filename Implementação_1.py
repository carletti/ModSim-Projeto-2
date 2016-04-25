# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def EquacoesDiferenciais(p, s, a, g, b, m):
    dpdt = i- (a*p) - (g*p)
    dsdt = (a*p) - (b*s) - (m*s)
    return dsdt

p0 = 
s0 = 
t = np.arange(0,100,0.0001)
a = (95/100)
g = (5/100)
b = 
m =

s = odeint(EquacoesDiferenciais, p0, s0, t, args=(a,g,b,m))

plt.plot(t,  s)
plt.ylabel('s(t)')
plt.xlabel('t')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show