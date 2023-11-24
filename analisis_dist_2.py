import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('datos.csv')

# Obtener las cantidades de anémicos, diabéticos, fumadores y muertos
cantidad_anemicos = datos['anemico'].sum()
cantidad_diabeticos = datos['diabetico'].sum()
cantidad_fumadores = datos['fumador'].sum()
cantidad_muertos = datos['muerto'].sum()

# Crear una figura con subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Grafica de torta para la cantidad de anémicos
axs[0, 0].pie([len(datos) - cantidad_anemicos, cantidad_anemicos], labels=['No Anémicos', 'Anémicos'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
axs[0, 0].set_title('Cantidad de Anémicos')

# Grafica de torta para la cantidad de diabéticos
axs[0, 1].pie([len(datos) - cantidad_diabeticos, cantidad_diabeticos], labels=['No Diabéticos', 'Diabéticos'], autopct='%1.1f%%', colors=['lightgreen', 'coral'])
axs[0, 1].set_title('Cantidad de Diabéticos')

# Grafica de torta para la cantidad de fumadores
axs[1, 0].pie([len(datos) - cantidad_fumadores, cantidad_fumadores], labels=['No Fumadores', 'Fumadores'], autopct='%1.1f%%', colors=['lightyellow', 'lightpink'])
axs[1, 0].set_title('Cantidad de Fumadores')

# Grafica de torta para la cantidad de muertos
axs[1, 1].pie([len(datos) - cantidad_muertos, cantidad_muertos], labels=['No Muertos', 'Muertos'], autopct='%1.1f%%', colors=['lightgrey', 'darksalmon'])
axs[1, 1].set_title('Cantidad de Muertos')

plt.tight_layout()
plt.show()
