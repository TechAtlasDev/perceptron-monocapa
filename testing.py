import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Aplicar estilo xkcd
plt.xkcd()

# Crear el gráfico
plt.plot(x, y)

# Añadir títulos y etiquetas
plt.title('Gráfico de ejemplo con estilo xkcd')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()
