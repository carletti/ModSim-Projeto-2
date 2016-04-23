# -*- coding: utf-8 -*-
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
