import random

empleados=[]

for _ in range(2000):
    
    ide=random.randint(0,500000)
    nombre=random.choice(['Andres', 'Ana', 'Isabel', 'Pablo', 'Juan', 'Kelly', 'Mauricio', 'Manuela', 'Veronica', 'Raul'])
    apellidos=random.choice(['Montoya','Perez','Gonzalez', 'Peralta', 'Gomez', 'Urrego', 'Gutierrez' ])
    edad = random.randint(22,60)
    salariomensual=random.randint(2000000, 50000000)
    retencionfuente=0.1
    cargo=random.choice(['Arquitecto', 'Desarrollador Junior', 'Desarrollador Senior'])
    empleado = [ide, nombre, apellidos, edad, salariomensual, retencionfuente, cargo]
    empleados.append(empleado)