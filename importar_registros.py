import sqlite3

# Ruta a tu archivo GeoPackage
geopackage_path = "consolidado.gpkg"

def migrate_data():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect(geopackage_path)
        cursor = conn.cursor()
        
        # Verificar si las tablas existen
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='predio';")
        if not cursor.fetchone():
            print("La tabla 'predio' no existe en el GeoPackage.")
            return
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cca_predio';")
        if not cursor.fetchone():
            print("La tabla 'cca_predio' no existe en el GeoPackage.")
            return

        # Migrar datos
        insert_query = """
        INSERT INTO cca_predio (
            T_Id, id_operacion, departamento_municipio, clase_suelo_registro, categoria_suelo, 
            validacion_datos_localizacion, nupre, numero_predial, numero_predial_anterior, 
            validacion_datos_catastrales, tiene_fmi, codigo_orip, matricula_inmobiliaria, estado_folio, 
            tiene_area_registral, area_registral_m2, validacion_datos_registrales, condicion_predio, 
            total_unidades_privadas, numero_torres, area_total_terreno, area_total_terreno_privada, 
            area_total_terreno_comun, area_total_construida, area_total_construida_privada, 
            area_total_construida_comun, predio_matriz, coeficiente_copropiedad, 
            validacion_condicion_predio, destinacion_economica, validacion_destinacion_economica, 
            predio_tipo, validacion_tipo_predio, validacion_derechos, resultado_visita, 
            otro_cual_resultado_visita, suscribe_acta_colindancia, valor_referencia, fecha_visita_predial, 
            tipo_documento_quien_atendio, numero_documento_quien_atendio, nombres_apellidos_quien_atendio, 
            celular, correo_electronico, observaciones, despojo_abandono, estrato, otro_cual_estrato, usuario
        )
        SELECT 
            T_Id, id_operacion, departamento_municipio, clase_suelo_registro, categoria_suelo, 
            validacion_datos_localizacion, nupre, numero_predial, numero_predial_anterior, 
            validacion_datos_catastrales, tiene_fmi, codigo_orip, matricula_inmobiliaria, estado_folio, 
            tiene_area_registral, area_registral_m2, validacion_datos_registrales, condicion_predio, 
            total_unidades_privadas, numero_torres, area_total_terreno, area_total_terreno_privada, 
            area_total_terreno_comun, area_total_construida, area_total_construida_privada, 
            area_total_construida_comun, predio_matriz, coeficiente_copropiedad, 
            validacion_condicion_predio, destinacion_economica, validacion_destinacion_economica, 
            predio_tipo, validacion_tipo_predio, validacion_derechos, resultado_visita, 
            otro_cual_resultado_visita, suscribe_acta_colindancia, valor_referencia, fecha_visita_predial, 
            tipo_documento_quien_atendio, numero_documento_quien_atendio, nombres_apellidos_quien_atendio, 
            celular, correo_electronico, observaciones, despojo_abandono, estrato, otro_cual_estrato, usuario
        FROM predio;
        """
        
        cursor.execute(insert_query)
        conn.commit()
        print("Migración completada con éxito.")
    
    except sqlite3.Error as e:
        print(f"Error en la migración: {e}")
    finally:
        if conn:
            conn.close()

# Ejecutar la función
migrate_data()
