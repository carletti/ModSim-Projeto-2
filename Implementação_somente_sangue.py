# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equaçâo
def EquacoesDiferenciais(s, t):
    kmvmax = 0.10 # Concentrção por segundo 
    kevmax = 0.65
    dsdt = - (kmvmax*s) 
    return dsdt
# Definindo valores iniciais
p0 = 10
s0 = p0*(95/100)
# Definindo intervalo de tempo
T = np.arange(0,100,0.0001)
# Definindo odeint
s = odeint(EquacoesDiferenciais, s0, T)
# Gráfico THCs X Tempo
plt.plot(T, s)
plt.ylabel('[THC]')
plt.xlabel('t')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show()