import matplotlib.pyplot as plt

def imgGraficar(dataFrame,rutaGrafica,xColumn, yColumn,xLabel,yLabel,title):
    dataFrame[xColumn] = dataFrame[xColumn].astype(str)
    colores = ['#e74a3b', '#f6c23e','#4e73df','#36b9cc','#1cc88a','#daf7a6','#884EA0','#82E0AA']
    plt.figure(figsize=(10,10))
    plt.bar(dataFrame[xColumn],dataFrame[yColumn], color=colores)
    
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.xticks(rotation = 35)
    plt.savefig(rutaGrafica)