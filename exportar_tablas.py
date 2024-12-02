import sqlite3
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

ruta_txt = "rutas_geopackages.txt"  # Rutas de los GeoPackages de entrada
geopackage2 = "modelo_captura_20241029_vacio.gpkg"  # GeoPackage de salida

tablas = ["cca_usuario", "cca_predio", "cca_interesado", "cca_agrupacioninteresados", 
          "cca_miembros", "cca_fuenteadministrativa", "cca_derecho", "cca_fuenteadministrativa_derecho", 
          "cca_estructuranovedadfmi", "cca_estructuranovedadnumeropredial", "cca_predio_informalidad", 
          "cca_predio_copropiedad", "cca_ofertasmercadoinmobiliario", "cca_calificacionconvencional", 
          "cca_caracteristicasunidadconstruccion", "cca_adjunto"]

def quitar_prefijo(nombre):
    return nombre.replace("cca_", "", 1)

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

def eliminar_tabla_si_existe(geopackage, tabla):
    try:
        with sqlite3.connect(geopackage) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {tabla};")
            conn.commit()
    except Exception as e:
        logging.error(f"Error al intentar eliminar la tabla '{tabla}' en el GeoPackage destino: {e}")

def procesar_geopackage(ruta_txt, geopackage2, tablas):
    try:
        rutas = leer_rutas(ruta_txt)
        
        for ruta in rutas:
            logging.info(f"Procesando GeoPackage: {ruta}")
            
            tablas_disponibles = listar_tablas(ruta)

            for tabla in tablas:
                if tabla not in tablas_disponibles:
                    logging.warning(f"La tabla '{tabla}' no existe en el GeoPackage '{ruta}'. Saltando...")
                    continue

                try:
                    with sqlite3.connect(ruta) as conn1:
                        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn1)

                    nuevo_nombre = quitar_prefijo(tabla)

                    eliminar_tabla_si_existe(geopackage2, nuevo_nombre)

                    with sqlite3.connect(geopackage2) as conn2:
                        df.to_sql(nuevo_nombre, conn2, if_exists="replace", index=False)

                    logging.info(f"Tabla '{tabla}' exportada como '{nuevo_nombre}' en el GeoPackage 2.")
                except Exception as e:
                    logging.error(f"Error al procesar la tabla '{tabla}' desde '{ruta}': {e}")

    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")

def leer_rutas(archivo):
    try:
        with open(archivo, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        logging.error(f"Error al leer el archivo '{archivo}': {e}")
        return []

procesar_geopackage(ruta_txt, geopackage2, tablas)