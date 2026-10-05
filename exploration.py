"""
1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos

2. Mostrar los primeros 100 registros

3. Mostrar los últimos 20 registros

4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos

5.Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija), 
"""


from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('avocado.csv')

#print(data['region'].unique())

"""



print(data.shape) # tarea 1

print(data.head(100)) # tarea 2

print(data.tail(20)) # tarea 3

print(data['AveragePrice'].min()) # tarea 4
print(data['AveragePrice'].max()) # tarea 4
print(data['AveragePrice'].mean()) # tarea 4

"""

Charlotte = data[data['region'] == 'Charlotte']
HarrisburgScranton = data[data['region'] == 'HarrisburgScranton']
Philadelphia = data[data['region'] == 'Philadelphia']

fig, axes = plt.subplots(1,3)
g_Charlotte = Charlotte.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'red', ax = axes[0], title = 'Charlotte')
g_HarrisburgScranton = HarrisburgScranton.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'blue', ax = axes[1], title = 'HarrisburgScranton')
g_Philadelphia = Philadelphia.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'green', ax = axes[2], title = 'Philadelphia')

plt.show()



"""
data = pd.read_csv('iris.csv')

print(data['species'].value_counts())

print(data.fillna('99'))

setosa = data[data['species'] == 'setosa']
virginica = data[data['species'] == 'virginica']
virsicolor = data[data['species'] == 'versicolor']

print(virsicolor, setosa, virginica )


x1 = plt.subplot()
g_setosa = setosa.plot(x = 'petal_length', y = 'petal_width', kind = 'scatter', color = 'red', ax = x1)
g_virginica = virginica.plot(x = 'petal_length', y = 'petal_width', kind = 'scatter', color = 'blue', ax = x1)
g_virsicolor = virsicolor.plot(x = 'petal_length', y = 'petal_width', kind = 'scatter', color = 'green', ax = x1)

plt.show()
"""


"""
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

ganado = [1, 17.5,40, 48, 52, 69, 88]
perdido = [2, 8, 78, 1.5, 25, 12, 28]
index = ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D', 'Equipo E', 'Equipo F', 'Equipo G']

df = pd.DataFrame({'ganado': ganado, 'perdido': perdido}, index=index)

ax = df.plot.bar(rot = 0, subplots = True)

plt.show()

"""