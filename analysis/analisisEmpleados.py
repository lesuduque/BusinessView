import pandas as pd

from helpers.crearCSVempleados import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.empleados import empleados

crearCSV(empleados, 'empleados.csv')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
crearTabla(empleadosDataFrame,'tablaempleados')