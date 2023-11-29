import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_directory():
    # Obtener la ruta del directorio actual
    directorio_actual = os.getcwd()
    
    # Nombre del archivo de salida
    archivo_salida = 'pdf_combinado.pdf'

    if os.path.exists(archivo_salida):
        os.remove(archivo_salida)
        print(f'Se ha eliminado el archivo existente "{archivo_salida}".')


    # Inicializar un objeto PdfMerger
    merger = PdfMerger()

    pdf_files = [file for file in os.listdir(directorio_actual) if file.endswith('.pdf')]
    pdf_files.sort()

    # Buscar archivos PDF en el directorio actual
    for filename in pdf_files:
        if filename.endswith('.pdf'):
            # Combinar archivos PDF encontrados
            merger.append(os.path.join(directorio_actual, filename))


    # Guardar el archivo combinado
    with open(archivo_salida, 'wb') as salida:
        merger.write(salida)

    print(f'Se han combinado los archivos PDF en "{archivo_salida}".')

if __name__ == "__main__":
    merge_pdfs_in_directory()
