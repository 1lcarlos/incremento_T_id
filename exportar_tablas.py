import sqlite3
import pandas as pd
import logging

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# Archivos de texto con rutas a los GeoPackages
geopackage1_txt = "geopackage1_list.txt"
geopackage2_txt = "geopackage2_list.txt"

# Listado de tablas a copiar y procesar
tablas = ["cca_usuario", "cca_predio", "cca_interesado", "cca_agrupacioninteresados", "cca_miembros", "cca_fuenteadministrativa",
          "cca_derecho", "cca_fuenteadministrativa_derecho", "cca_estructuranovedadfmi", "cca_estructuranovedadnumeropredial",
          "cca_predio_informalidad", "cca_predio_copropiedad", "cca_ofertasmercadoinmobiliario",
          "cca_calificacionconvencional", "cca_caracteristicasunidadconstruccion", "cca_adjunto"]

# Función para eliminar la sigla "cca_" del nombre de la tabla
def quitar_prefijo(nombre):
    return nombre.replace("cca_", "", 1)

# Función para listar las tablas presentes en un GeoPackage
def listar_tablas(geopackage):
    try:
        with sqlite3.connect(geopackage) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tablas_encontradas = [row[0] for row in cursor.fetchall()]
            return tablas_encontradas
    except Exception as e:
        logging.error(f"Error al listar tablas del GeoPackage '{geopackage}': {e}")
        return []

# Función para eliminar tablas existentes en el GeoPackage destino
def eliminar_tabla_si_existe(geopackage, tabla):
    try:
        with sqlite3.connect(geopackage) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {tabla};")
            conn.commit()
            logging.info(f"Tabla '{tabla}' eliminada en el GeoPackage destino si existía.")
    except Exception as e:
        logging.error(f"Error al intentar eliminar la tabla '{tabla}' en el GeoPackage destino: {e}")

# Procesamiento de las tablas
def procesar_geopackage(geopackage1, geopackage2, tablas):
    try:
        # Listar tablas del GeoPackage 1
        logging.info(f"Conectando al GeoPackage: {geopackage1}")
        tablas_disponibles = listar_tablas(geopackage1)

        # Iterar sobre las tablas seleccionadas
        for tabla in tablas:
            if tabla not in tablas_disponibles:
                logging.warning(f"La tabla '{tabla}' no existe en el GeoPackage 1. Saltando...")
                continue

            logging.info(f"Procesando la tabla '{tabla}'...")

            # Leer la tabla como DataFrame
            try:
                with sqlite3.connect(geopackage1) as conn1:
                    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn1)

                # Generar el nuevo nombre de la tabla
                nuevo_nombre = quitar_prefijo(tabla)

                # Eliminar la tabla en el GeoPackage 2 si ya existe
                eliminar_tabla_si_existe(geopackage2, nuevo_nombre)

                # Guardar la tabla en el GeoPackage 2
                with sqlite3.connect(geopackage2) as conn2:
                    df.to_sql(nuevo_nombre, conn2, if_exists="replace", index=False)

                logging.info(f"Tabla '{tabla}' exportada como '{nuevo_nombre}' en el GeoPackage 2.")

            except Exception as e:
                logging.error(f"Error al procesar la tabla '{tabla}': {e}")

    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")

# Leer las rutas desde los archivos .txt
def leer_rutas(archivo):
    try:
        with open(archivo, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        logging.error(f"Error al leer el archivo '{archivo}': {e}")
        return []

# Ejecutar el procesamiento para todas las rutas
def procesar_rutas_multiples(geopackage1_txt, geopackage2_txt, tablas):
    rutas1 = leer_rutas(geopackage1_txt)
    rutas2 = leer_rutas(geopackage2_txt)

    if len(rutas1) != len(rutas2):
        logging.error("La cantidad de rutas en los archivos no coincide.")
        return

    for geopackage1, geopackage2 in zip(rutas1, rutas2):
        logging.info(f"Iniciando procesamiento entre '{geopackage1}' y '{geopackage2}'...")
        procesar_geopackage(geopackage1, geopackage2, tablas)

procesar_rutas_multiples(geopackage1_txt, geopackage2_txt, tablas)