import pandas as pd

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablaHTML import crearTabla

from data.ventas import ventas

#1 Crear un CSV con los datos de las ventas
crearCSV(ventas, 'ventas.csv')

#2 cargo la fuente de datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')

ventasMayores=ventasDataFrame.query('Costo >= 600000')
filtroVentas=ventasMayores[['NumeroOrden','Costo']]

crearTabla(filtroVentas,'ventas600')