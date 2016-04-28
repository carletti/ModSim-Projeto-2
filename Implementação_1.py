# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equações
def EquacoesDiferenciais(q, t):
    ka = (95/100)
    ks = (5/100)
    kmvmax = (10/100) # Concentrção por segundo 
    kevmax = 0.9
    
    dpdt = -(ka*q[0]) - (ks*q[0])
    dsdt = (ka*q[0]) - (kmvmax*q[1]) - (kevmax*q[1])
    return [dpdt,dsdt]
# Definindo valores iniciais
p0 = 20
s0 = 0   
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,10,0.0001)
# Definindo odeint
q = odeint(EquacoesDiferenciais, q0, T)
# Gráfico THCp X Tempo
plt.plot(T, q[:, 0])
plt.ylabel('[THC]')
plt.xlabel('t')
plt.title(r'Quantidade de THC no pulmão')
plt.grid(True)
plt.show()
# Gráfico THCs X Tempo
plt.plot(T, q[:, 1])
plt.xlim(0.1)
plt.ylim(0.1)
plt.ylabel('[THC]')
plt.xlabel('t')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show()