import pandas as pd

from helpers.crearCSVempleados import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.empleados import empleados
from helpers.crearGraficas import imgGraficar
from helpers.crearArchivosPDF import pdfGraficar

crearCSV(empleados, 'empleados.csv')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
crearTabla(empleadosDataFrame,'tablaempleados')
pdfGraficar(empleadosDataFrame, "data/empleadosTabla.pdf")

asalariadosTop = empleadosDataFrame.nlargest(10, 'SalarioMensual')
imgGraficar(asalariadosTop, "assets/img/graficas/asalariadosTop.png","Id","SalarioMensual","Identificación","Salario mensual","10 Empleados más asalariados mensualmente")

empleadosJovenes = empleadosDataFrame.query("(Edad < 24)")
filtroUnoEmpleado = empleadosJovenes[['Nombre','Apellidos','Cargo']]
crearTabla(filtroUnoEmpleado, 'empleados_jovenes')

desarrolladores = empleadosDataFrame.query("(Cargo == 'Desarrollador Junior')")
filtroTresEmpleado = desarrolladores[['Nombre','Apellidos','Cargo']]
crearTabla(filtroTresEmpleado, 'desarrolladores')

empleadosAsalariados = empleadosDataFrame.query("(SalarioMensual > 2500000)")
filtroCuatroEmpleado = empleadosAsalariados[['Nombre','Apellidos','Cargo']]
crearTabla(filtroCuatroEmpleado, 'empleados_asalariados')