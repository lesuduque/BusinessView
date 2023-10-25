import random

productos = []

for _ in range(3000):

    ide = random.randint(0, 3000)
    nombre = random.choice(['Smartphone', 'Tablet', 'Laptop', 'Smartwatch', 'Auriculares inalámbricos', 'Cámara digital', 'Videocámara', 'Televisor', 'Consola de videojuegos', 'Reproductor de DVD/Blu-ray', 'Sistema de sonido envolvente', 'Proyector', 'Impresora', 'Router inalámbrico', 'Disco duro externo', 'Monitor de computadora','Teclado mecánico', 'Ratón óptico', 'Altavoces Bluetooth', 'Tableta gráfica', 'Linterna LED', 'Máquina de afeitar eléctrica', 'Plancha de ropa con vapor', 'Robot aspirador', 'Reloj inteligente para deportes', 'Termostato inteligente', 'Cargador inalámbrico', 'Batería externa', 'Kit de realidad virtual (VR)', 'Dron'])
    costounitario = random.randint(500000, 10000000)
    iva = 0.19
    producto = [ide, nombre, costounitario, iva]
    productos.append(producto)
