import sqlite3
import geopandas as gpd
import pandas as pd
import logging

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# Ruta a los GeoPackages
geopackage1 = "manzana_14_2.gpkg"
geopackage2 = "consolidado.gpkg"

# Listado de tablas a copiar y procesar
tablas = ["cca_usuario","cca_predio", "cca_interesado", "cca_agrupacioninteresados", "cca_miembros", "cca_fuenteadministrativa",
          "cca_derecho", "cca_fuenteadministrativa_derecho", "cca_estructuranovedadfmi", "cca_estructuranovedadnumeropredial",
          "cca_predio_informalidad", "cca_predio_copropiedad", "cca_ofertasmercadoinmobiliario", "extreferenciaregistralsistemaantiguo",
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

# Procesamiento de las tablas
def procesar_geopackage(geopackage1, geopackage2, tablas):
    try:
        # Listar tablas del GeoPackage 1
        logging.info(f"Conectando al GeoPackage: {geopackage1}")
        tablas_disponibles = listar_tablas(geopackage1)
        """ logging.info(f"Tablas disponibles en '{geopackage1}': {tablas_disponibles}") """

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

                # Guardar la tabla en el GeoPackage 2
                with sqlite3.connect(geopackage2) as conn2:
                    df.to_sql(nuevo_nombre, conn2, if_exists="replace", index=False)
                
                logging.info(f"Tabla '{tabla}' exportada como '{nuevo_nombre}' en el GeoPackage 2.")

            except Exception as e:
                logging.error(f"Error al procesar la tabla '{tabla}': {e}")

    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")

# Ejecutar el script
procesar_geopackage(geopackage1, geopackage2, tablas)
