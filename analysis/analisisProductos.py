import pandas as pd

from helpers.crearCSVProductos import crearCSV
from data.productos import productos

crearCSV(productos, 'productos.csv')

productosDataFrame=pd.read_csv('data/productos.csv')
print(productosDataFrame)
