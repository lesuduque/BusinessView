import pandas as pd

#from helpers.crearVentasCSV import crearCSV
#from helpers.crearTablaHTML import crearTabla
from data.ventas import ventas
#from helpers.crearGraficas import imgGraficar
#from helpers.crearArchivosPDF import pdfGraficar

crearCSV(ventas, 'ventas.csv')

ventasDataFrame=pd.read_csv('data/ventas.csv')
crearTabla(ventasDataFrame,'tablaventas')
pdfGraficar(ventasDataFrame, "data/ventasTabla.pdf")

ventasAltas = ventasDataFrame.nlargest(8, "Costo")
imgGraficar(ventasAltas, "assets/img/graficas/ventasAltas.png","NumeroOrden","Costo","Numero de orden","Costo","Ventas mas altas en el ultimo año")

ventasMayores=ventasDataFrame.query('Costo >= 600000')
filtroUnoVentas=ventasMayores[['NumeroOrden','Costo']]
crearTabla(filtroUnoVentas,'ventas600')

ventasIntermedio = ventasDataFrame.query("(Costo>200000) and (Costo<600000)")
filtroDosVentas = ventasIntermedio[['NumeroOrden', 'Costo']]
crearTabla(filtroDosVentas,'ventasintermedio')

