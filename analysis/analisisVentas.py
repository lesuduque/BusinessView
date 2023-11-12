import pandas as pd
import matplotlib.pyplot as plt

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.ventas import ventas

crearCSV(ventas, 'ventas.csv')

ventasDataFrame=pd.read_csv('data/ventas.csv')

ventasMayores=ventasDataFrame.query('Costo >= 600000')
filtroVentas=ventasMayores[['NumeroOrden','Costo']]
crearTabla(filtroVentas,'ventas600')

#Graficando un DATAFRAME co MATLOTLIB
filtroVentas["NumeroOrden"]=filtroVentas["NumeroOrden"].astype(str)
colores=['#e36dec', '#f364dc','#ff5ccb','#ff55ba','#ff51a8','#ff4f96','#ff5185','#ff5573']
plt.figure(figsize=(10,10))
plt.bar(filtroVentas["Costo"],filtroVentas["NumeroOrden"], color=colores)

#Personalizando la grafica
plt.xlabel("Costo")
plt.ylabel("NumeroOrden")
plt.title("Ventas mayores a 600mil")
plt.xticks(rotation=35)

rutaPDF="assets/img/ventas600.pdf"
rutaGrafica="assets/img/ventas600.png"
plt.savefig(rutaGrafica)
plt.savefig(rutaPDF)
