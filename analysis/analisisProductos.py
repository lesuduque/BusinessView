import pandas as pd

#from helpers.crearCSVProductos import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.productos import productos
from helpers.crearGraficas import imgGraficar
from helpers.crearArchivosPDF import pdfGraficar

#crearCSV(productos, 'productos.csv')

productosDataFrame=pd.read_csv('data/productos.csv')
crearTabla(productosDataFrame,'tablaproductos')
pdfGraficar(productosDataFrame, "data/productosTabla.pdf")

productosBaratos = productosDataFrame.nsmallest(8, 'CostoUnitario')
imgGraficar(productosBaratos, "assets/img/graficas/productosBaratos.png","Id","CostoUnitario","Código del Producto","Precio","Productos mas baratos en el ultimo año")

productosMayores = productosDataFrame.query("(CostoUnitario > 500000)")
filtroUnoProducto = productosMayores[['Id','Nombre','CostoUnitario']]


