import matplotlib.pyplot as plt
import numpy as np

# Vamos começar com uma bela função de onda, função senoidal, sin (x), em que x varia de 0 a 10.
# Precisamos gerar a sequência ao longo do eixo x, uma matriz uniformemente espaçada, via linspace () .

x = np.linspace(0,10,1000) # x is a 1000 evenly spaced numbers from 0 to 10
y = np.sin(x)

fig = plt.figure()
ax = plt.axes()

ax.plot(x, y)
plt.show()