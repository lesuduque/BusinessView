import random

empleados=[]

for _ in range(2000):
    
    ide=random.randint(0,500000)
    nombre=random.choice(['Andres', 'Ana', 'Isabel', 'Pablo', 'Juan', 'Kelly', 'Mauricio', 'Manuela', 'Veronica', 'Raul'])
    apellidos=random.choice(['Montoya','Perez','Gonzalez', 'Peralta', 'Gomez', 'Urrego', 'Gutierrez' ])
    salariomensual=random.randint(1000000, 5000000)
    deudas=True
    retencionfuente=0.1
    correo=random.choice(['aaaa@hotmail.com', 'bbbb@hotmail.com', 'cccc@hotmail.com', 'dddd@hotmail.com'])
    telefono=random.randint(4598760,5082345)
    cargo=random.choice(['arquitecto', 'desarrollador junior', 'desarrollador senior'])
    empleado = [ide, nombre, apellidos, salariomensual, deudas, retencionfuente, correo, telefono, cargo]
    empleados.append(empleado)