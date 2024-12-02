import os

def listar_archivos_y_guardar(ruta_carpeta, ruta_txt):
    try:
        with open(ruta_txt, 'w', encoding='utf-8') as archivo_txt:
            for raiz, _, archivos in os.walk(ruta_carpeta):
                for nombre_archivo in archivos:
                    ruta_completa = os.path.join(raiz, nombre_archivo)
                    ruta_relativa = os.path.relpath(ruta_completa, ruta_carpeta)
                    archivo_txt.write(ruta_relativa + '\n')
        print(f"Se ha creado el archivo: {ruta_txt}")
    except Exception as e:
        print(f"Error al listar archivos: {e}")

ruta_carpeta = r"C:\Users\Paula Aragonés\OneDrive\Escritorio\ACC\Cuentas de cobro\Diciembre\incremento_T_id\gpkg"
ruta_txt = "rutas_geopackages.txt"

listar_archivos_y_guardar(ruta_carpeta, ruta_txt)