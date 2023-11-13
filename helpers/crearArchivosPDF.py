import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def pdfGraficar(dataframe,rutaPDF):
    fig, ax = plt.subplots(figsize=(1,1))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=dataframe.values,
            colLabels=dataframe.columns,
            loc='center')
    
    pp= PdfPages(rutaPDF)
    pp.savefig(fig,bbox_inches='tight')
    pp.close()