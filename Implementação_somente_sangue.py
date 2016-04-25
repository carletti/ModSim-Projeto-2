# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equações
def EquacoesDiferenciais(q, t):
    a = 0.95
    b = 0.35
    m = 0.65
    dsdt = (a*q[0]) - (b*q[1]) - (m*q[1])
    return dsdt
# Definindo valores iniciais
p0 = 10
s0 = 0   
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,100,0.0001)
# Definindo odeint
q = odeint(EquacoesDiferenciais, q0, T)
# Gráfico THCs X Tempo
plt.plot(T, q)
plt.ylabel('s(t)')
plt.xlabel('t')
plt.title(r'Quantidade de THC no sangue')
plt.grid(True)
plt.show()