# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equações
def EquacoesDiferenciais(s, t):
    b = 0.35
    m = 0.65
    dsdt = -(b*s) - (m*s)
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
plt.ylabel('s(t)')
plt.xlabel('t')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show()