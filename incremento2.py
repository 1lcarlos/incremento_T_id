import sqlite3

def actualizar_ids_geopackage(geopackage_path, incremento):
    # Definir relaciones
    relaciones = [
        {
            "tabla_principal": "cca_usuario",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_predio", "clave_foranea": "usuario"},                
            ],
        },
        {
            "tabla_principal": "cca_predio",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_derecho", "clave_foranea": "predio"},
                {"tabla_relacionada": "cca_terreno", "clave_foranea": "predio"},
                {"tabla_relacionada": "cca_construccion", "clave_foranea": "predio"},
                {"tabla_relacionada": "cca_predio_informalidad", "clave_foranea": "cca_predio_formal"},
                {"tabla_relacionada": "cca_predio_informalidad", "clave_foranea": "cca_predio_informal"},
                {"tabla_relacionada": "cca_predio_copropiedad", "clave_foranea": "unidad_predial"},
                {"tabla_relacionada": "cca_predio_copropiedad", "clave_foranea": "matriz"},
                {"tabla_relacionada": "cca_estructuranovedadfmi", "clave_foranea": "cca_predio_novedad_fmi"},
                {"tabla_relacionada": "cca_estructuranovedadnumeropredial", "clave_foranea": "cca_predio_novedad_numeros_prediales"},
                {"tabla_relacionada": "extdireccion", "clave_foranea": "cca_predio_direccion"},
                {"tabla_relacionada": "cca_adjunto", "clave_foranea": "cca_predio_adjunto"},
                {"tabla_relacionada": "cca_ofertasmercadoinmobiliario", "clave_foranea": "predio"},
                
            ],
        },
        
        {
          "tabla_principal": "cca_construccion",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_unidadconstruccion", "clave_foranea": "construccion"}, 
                {"tabla_relacionada": "cca_adjunto", "clave_foranea": "cca_construccion_adjunto"}, 
            ],  
        },
        {
            "tabla_principal": "cca_interesado",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_derecho", "clave_foranea": "interesado"},
                {"tabla_relacionada": "cca_miembros", "clave_foranea": "interesado"},
                {"tabla_relacionada": "cca_adjunto", "clave_foranea": "cca_interesado_adjunto"},
            ],
        },
        {
            "tabla_principal": "cca_agrupacioninteresados",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_derecho", "clave_foranea": "agrupacion_interesados"},
                {"tabla_relacionada": "cca_miembros", "clave_foranea": "agrupacion"},
            ],
        },{
            "tabla_principal": "cca_fuenteadministrativa",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_fuenteadministrativa_derecho", "clave_foranea": "fuente_administrativa"},               
                {"tabla_relacionada": "cca_adjunto", "clave_foranea": "cca_fuenteadminstrtiva_adjunto"},               
            ],
        },
        {
            "tabla_principal": "cca_derecho",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_fuenteadministrativa_derecho", "clave_foranea": "derecho"},               
            ],
        },
        {
            "tabla_principal": "cca_caracteristicasunidadconstruccion",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_unidadconstruccion", "clave_foranea": "caracteristicasunidadconstruccion"},               
            ],
        },
        {
            "tabla_principal": "cca_calificacionconvencional",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_caracteristicasunidadconstruccion", "clave_foranea": "calificacion_convencional"},               
            ],
        },        
        {
            "tabla_principal": "cca_unidadconstruccion",
            "clave_primaria": "T_Id",
            "relaciones": [
                {"tabla_relacionada": "cca_adjunto", "clave_foranea": "cca_unidadconstruccion_adjunto"},               
            ],
        },        
    ]
    
    try:
        # Conectar al GeoPackage
        conn = sqlite3.connect(geopackage_path)
        cursor = conn.cursor()

        # Desactivar claves foráneas
        cursor.execute("PRAGMA foreign_keys = OFF;")

        # Iterar sobre cada relación definida
        for relacion in relaciones:
            tabla_principal = relacion["tabla_principal"]
            clave_primaria = relacion["clave_primaria"]
            relaciones_foraneas = relacion["relaciones"]

            # Obtener los IDs actuales de la tabla principal
            cursor.execute(f"SELECT {clave_primaria} FROM {tabla_principal};")
            ids_principales = cursor.fetchall()

            # Actualizar los IDs en la tabla principal y las tablas relacionadas
            for (id_actual,) in ids_principales:
                nuevo_id = id_actual + incremento

                # Actualizar clave primaria en la tabla principal
                cursor.execute(
                    f"UPDATE {tabla_principal} SET {clave_primaria} = ? WHERE {clave_primaria} = ?;",
                    (nuevo_id, id_actual),
                )

                # Actualizar claves foráneas en las tablas relacionadas
                for relacion_foranea in relaciones_foraneas:
                    tabla_relacionada = relacion_foranea["tabla_relacionada"]
                    clave_foranea = relacion_foranea["clave_foranea"]

                    cursor.execute(
                        f"UPDATE {tabla_relacionada} SET {clave_foranea} = ? WHERE {clave_foranea} = ?;",
                        (nuevo_id, id_actual),
                    )

        # Reactivar claves foráneas
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Confirmar cambios
        conn.commit()
        print("Actualización completada exitosamente.")
    
    except sqlite3.Error as e:
        print(f"Error durante la actualización: {e}")
        conn.rollback()
    
    finally:
        # Cerrar conexión
        conn.close()

# Ejemplo de uso
ruta_geopackage = "manzana_8.gpkg"
incremento = 1000  # Valor a sumar a los IDs
actualizar_ids_geopackage(ruta_geopackage, incremento)
