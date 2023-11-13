import pandas as pd

from helpers.crearCSVempleados import crearCSV
from data.empleados import empleados

crearCSV(empleados, 'empleados.csv')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
print(empleadosDataFrame)