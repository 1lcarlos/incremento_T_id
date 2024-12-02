import os

rutas_directorios = [
    r"C:\Users\Paula Aragonés\OneDrive\Documentos\Prueba",
    r"C:\Users\Paula Aragonés\OneDrive\Documentos\Documentos pasantías",
    r"C:\Users\Paula Aragonés\OneDrive\Documentos\Pijamas Consentidas"
]

def generar_lista_rutas_geopackages(directorios):
    archivo_contador = 1

    for directorio in directorios:
        if os.path.exists(directorio):
            if archivo_contador == 1:
                archivo_salida = os.path.join(directorio, "rutas_geopackages.txt")
            else:
                archivo_salida = os.path.join(directorio, f"geopackage{archivo_contador}_list.txt")

            with open(archivo_salida, "w", encoding="utf-8") as archivo:
                for root, dirs, files in os.walk(directorio):
                    for file in files:
                        if file.lower().endswith(".gpkg"):
                            archivo.write(os.path.join(root, file) + "\n")
            print(f"Archivo con las rutas generado: {archivo_salida}")
            
            archivo_contador += 1

        else:
            print(f"El directorio no existe: {directorio}")

generar_lista_rutas_geopackages(rutas_directorios)
