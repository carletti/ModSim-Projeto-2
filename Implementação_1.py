# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# Definindo equações
def EquacoesDiferenciais(q, t):
    ka = 0.95
    ks = 0.05
    vmax = (13.6*(10**(-9))) # mol por minuto
    km = (12.5*(10**(-9)*(314.45))) # Molaridade 
    kevmax = 0.9
    
    dpdt = -(ka*q[0]) - (ks*q[0])
    dsdt = (ka*q[0]) - ((vmax*q[1])/(km + q[1])) - (kevmax*q[1])
    return [dpdt,dsdt]
# Definindo valores iniciais (1g de maconha)
I0 = 0.1 # Gramas
CI0 = I0/(5*1000) # Gramas por ml
p0 = (0.1*CI0) # Grmas por ml
s0 = 0 # Gramas por ml
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,10,0.0001) # Dias
# Definindo odeint
q1 = odeint(EquacoesDiferenciais, q0, T)
# Definindo valores iniciais (2g de maconha)
I0 = 0.2 # Gramas
CI0 = I0/(5*1000) # Gramas por ml
p0 = (0.1*CI0) # Grmas por ml
s0 = 0 # Gramas por ml
q0 = [p0, s0]
# Definindo intervalo de tempo
T = np.arange(0,10,0.0001) # Dias
# Definindo odeint
q2 = odeint(EquacoesDiferenciais, q0, T)
# Quantidade limite no teste 
limite= [] 
for i in range(100000):
    l = 25*(10**(-9))
    limite.append(l)
print(len(T))

# Gráficos

# Gráfico [THC]p X Tempo
plt.plot(T, q1[:, 0])
plt.plot(T, q2[:, 0])
#plt.plot(T, q3[:, 0])
plt.ylabel('[THC]')
plt.xlabel('Tempo (dias)')
plt.title(r'Concentração de THC no pulmão')
plt.grid(True)
plt.show()
# Gráfico [THC]s X Tempo
plt.plot(T, q1[:, 1])
plt.plot(T, q2[:, 1])
#plt.plot(T, q3[:, 1])
plt.plot(T, limite)
plt.ylabel('[THC]')
plt.xlabel('Tempo (dias)')
plt.title(r'Concentração de THC no sangue')
plt.grid(True)
plt.show()