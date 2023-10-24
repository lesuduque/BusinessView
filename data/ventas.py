import random

ventas=[]

for _ in range(1000):
    
    numeroOrden=random.randint(0,500000)
    cliente=random.choice(['Andres', 'Ana', 'Isabel', 'Pablo', 'Juan', 'Kelly', 'Mauricio', 'Manuela', 'Veronica', 'Raul'])
    costo = random.randint(150000, 600000)
    orden = [numeroOrden, cliente, costo]
    ventas.append(orden)