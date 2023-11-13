import pandas as pd

#from helpers.crearCSVProductos import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.productos import productos
from helpers.crearArchivosPDF import pdfGraficar

crearCSV(productos, 'productos.csv')

productosDataFrame=pd.read_csv('data/productos.csv')
crearTabla(productosDataFrame,'tablaproductos')
pdfGraficar(productosDataFrame, "data/productosTabla.pdf")

