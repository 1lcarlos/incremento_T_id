import sqlite3
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

ruta_txt = "rutas_geopackages.txt"
geopackage2 = "modelo_captura_20241029_vacio.gpkg"

tablas = ["cca_usuario", "cca_predio", "cca_interesado", "cca_agrupacioninteresados", "cca_miembros", "cca_fuenteadministrativa",
          "cca_derecho", "cca_fuenteadministrativa_derecho", "cca_estructuranovedadfmi", "cca_estructuranovedadnumeropredial",
          "cca_predio_informalidad", "cca_predio_copropiedad", "cca_ofertasmercadoinmobiliario", 
          "cca_calificacionconvencional", "cca_caracteristicasunidadconstruccion", "cca_adjunto"]

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
            logging.info(f"Tabla '{tabla}' eliminada en el GeoPackage destino si existía.")
    except Exception as e:
        logging.error(f"Error al intentar eliminar la tabla '{tabla}' en el GeoPackage destino: {e}")

def leer_rutas_desde_txt(ruta_txt):
    try:
        with open(ruta_txt, 'r', encoding='utf-8') as archivo:
            rutas = [linea.strip() for linea in archivo.readlines()]
        return rutas
    except Exception as e:
        logging.error(f"Error al leer el archivo '{ruta_txt}': {e}")
        return []

def procesar_geopackage(rutas_geopackages, geopackage2, tablas):
    try:
        for i, geopackage1 in enumerate(rutas_geopackages):
            logging.info(f"Conectando al GeoPackage: {geopackage1}")
            tablas_disponibles = listar_tablas(geopackage1)
            if i == 0:
                for tabla in tablas:
                    eliminar_tabla_si_existe(geopackage2, quitar_prefijo(tabla))
            
            for tabla in tablas:
                if tabla not in tablas_disponibles:
                    logging.warning(f"La tabla '{tabla}' no existe en el GeoPackage '{geopackage1}'. Saltando...")
                    continue

                logging.info(f"Procesando la tabla '{tabla}'...")
                try:
                    with sqlite3.connect(geopackage1) as conn1:
                        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn1)

                    nuevo_nombre = quitar_prefijo(tabla)

                    with sqlite3.connect(geopackage2) as conn2:
                        df.to_sql(nuevo_nombre, conn2, if_exists="append", index=False)

                    logging.info(f"Tabla '{tabla}' exportada como '{nuevo_nombre}' en el GeoPackage 2.")
                except Exception as e:
                    logging.error(f"Error al procesar la tabla '{tabla}' desde '{geopackage1}': {e}")

    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")

rutas_geopackages = leer_rutas_desde_txt(ruta_txt)
procesar_geopackage(rutas_geopackages, geopackage2, tablas)