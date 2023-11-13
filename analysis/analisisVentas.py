import pandas as pd

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.ventas import ventas
from helpers.crearGraficas import imgGraficar
from helpers.crearArchivosPDF import pdfGraficar

crearCSV(ventas, 'ventas.csv')

ventasDataFrame=pd.read_csv('data/ventas.csv')
pdfGraficar(ventasDataFrame, "data/ventasTabla.pdf")

ventasMayores=ventasDataFrame.query('Costo >= 600000')
filtroUnoVentas=ventasMayores[['NumeroOrden','Costo']]
crearTabla(filtroUnoVentas,'ventas600')
imgGraficar(filtroUnoVentas, "assets/img/graficas/ventas600.png","NumeroOrden","Costo","Numero de orden","Costo","Ventas mayores a 600mil")


