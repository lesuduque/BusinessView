import pandas as pd

from helpers.crearCSVProductos import crearCSV
from data.productos import productos


print(productos)

#1 Crear un CSV con los datos de las ventas
crearCSV(productos, 'productos.csv')

productosDataFrame=pd.read_csv('data/productos.csv')
print(productosDataFrame)

examen1=productosDataFrame.head()
examen2=productosDataFrame.tail()
examen3=productosDataFrame.head(20)
examen4=productosDataFrame.info()
examen5=productosDataFrame.describe()
examen6=productosDataFrame.tail(50)


#4 filtrar y ordenar (limpiar)


#5 modelar o aplicar modelos 


#6 presentar y exportar los datos
print(examen1)
print("\n")
print(examen2)
print("\n")
print(examen3)
print("\n")
print(examen4)
print("\n")
print(examen5)
print("\n")
print(examen6)