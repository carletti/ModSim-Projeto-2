# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equações
def EquacoesDiferenciais(q, t):
    ka = 0.95
    ks = 0.05
    vmax = 0.1
    km = 1 
    kevmax = 0.9
    
    dpdt = -(ka*q[0]) - (ks*q[0])
    dsdt = (ka*q[0]) - ((vmax*q[1])/(km + q[1])) - (kevmax*q[1])
    return [dpdt,dsdt]
# Definindo valores iniciais (1g de maconha)
I0 = 1
p0 = (0.1*I0)
s0 = 0   
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,10,0.0001)
# Definindo odeint
q1 = odeint(EquacoesDiferenciais, q0, T)
# Definindo valores iniciais (2g de maconha)
I0 = 2
p0 = 0.1*I0
s0 = 0   
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,10,0.0001)
# Definindo odeint
q2 = odeint(EquacoesDiferenciais, q0, T)

# Gráfico THCp X Tempo
plt.plot(T, q1[:, 0])
plt.ylabel('[THC]')
plt.xlabel('Tempo (dias)')
plt.title(r'Concentração de THC no pulmão')
plt.grid(True)
plt.show()
# Gráfico THCs X Tempo
plt.plot(T, q1[:, 1])
plt.ylabel('[THC]')
plt.xlabel('Tempo (dias)')
plt.title(r'Concentração de THC no sangue')
plt.grid(True)
plt.show()