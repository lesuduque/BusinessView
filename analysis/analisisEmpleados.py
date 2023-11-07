import pandas as pd

from helpers.crearCSVempleados import crearCSV
from data.empleados import empleados


print(empleados)

#1 Crear un CSV con los datos de las ventas
crearCSV(empleados, 'empleados.csv')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
print(empleadosDataFrame)

examen1=empleadosDataFrame.head()
examen2=empleadosDataFrame.tail()
examen3=empleadosDataFrame.head(20)
examen4=empleadosDataFrame.info()
examen5=empleadosDataFrame.describe()
examen6=empleadosDataFrame.tail(50)


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
