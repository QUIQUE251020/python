import glob

directorio_raiz = r"C:\Users\tecnologia\Documents\Productos\Fotos"
extensiones_excluidas = ['.png', '.jpg']

# Obtener la lista de archivos en el directorio raíz y subdirectorios
archivos = glob.glob(directorio_raiz + '/**/*', recursive=True)

# Recorrer los archivos y verificar la extensión
for archivo in archivos:
    # Comprobar si el archivo no tiene una extensión excluida
    if not any(archivo.endswith(ext) for ext in extensiones_excluidas):
        print('Se encontró un archivo distinto de PNG o JPG:', archivo)
