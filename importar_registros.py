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

        INSERT INTO cca_interesado  (
            T_Id,  tipo, tipo_documento, documento_identidad, 
            primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, 
            sexo, grupo_etnico, razon_social, departamento, municipio, 
            direccion_residencia, telefono, correo_electronico, 
            autoriza_notificacion_correo, estado_civil
        )
        
        SELECT 
            T_Id,  tipo, tipo_documento, documento_identidad, 
            primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, 
            sexo, grupo_etnico, razon_social, departamento, municipio, 
            direccion_residencia, telefono, correo_electronico,
            autoriza_notificacion_correo, estado_civil
        FROM interesado;

        INSERT INTO cca_agrupacioninteresados (
            T_Id,  tipo, nombre
        )
        SELECT 
            T_Id,  tipo, nombre
        FROM agrupacioninteresados;

        INSERT INTO cca_miembros (
            T_Id,  interesado, agrupacion, participacion
        )
        SELECT 
            T_Id,  interesado, agrupacion, participacion
        FROM miembros;

        INSERT INTO cca_fuenteadministrativa (
            T_Id,  tipo, numero_fuente, fecha_documento_fuente, e_emisor, observacion
        )
        SELECT 
            T_Id,  tipo, numero_fuente, fecha_documento_fuente, ente_emisor, observacion
        FROM fuenteadministrativa;

        INSERT INTO cca_derecho (
            T_Id,  tipo, cuota_participacion, fraccion_derecho, 
            fecha_inicio_tenencia, origen_derecho, observacion, 
            agrupacion_interesados, interesado, predio
        )
        SELECT 
            T_Id,  tipo, cuota_participacion, fraccion_derecho,
            fecha_inicio_tenencia, origen_derecho, observacion, 
            agrupacion_interesados, interesado, predio
        FROM derecho;

        INSERT INTO cca_fuenteadministrativa_derecho (
            derecho, fuente_administrativa
        )
        SELECT 
            derecho, fuente_administrativa
        FROM fuenteadministrativa_derecho;

        INSERT INTO cca_estructuranovedadfmi (
            T_Id,  codigo_orip, numero_fmi, tipo_novedadfmi, cca_predio_novedad_fmi
        )
        SELECT
            T_Id,  codigo_orip, numero_fmi, tipo_novedadfmi, cca_predio_novedad_fmi
        FROM estructuranovedadfmi;

        INSERT INTO cca_estructuranovedadnumeropredial (
            T_Id,  numero_predial, tipo_novedad, cca_predio_novedad_numeros_prediales
        )
        SELECT 
            T_Id,  numero_predial, tipo_novedad, cca_predio_novedad_numeros_prediales
        FROM estructuranovedadnumeropredial ;

        INSERT INTO cca_predio_informalidad (
            T_Id,  cca_predio_formal, cca_predio_informal
        )
        SELECT 
            T_Id,  cca_predio_formal, cca_predio_informal
        FROM predio_informalidad;

        INSERT INTO cca_predio_copropiedad (
            T_Id, unidad_predial, matriz, coeficiente
        )
        SELECT 
            T_Id, unidad_predial, matriz, coeficiente
        FROM predio_copropiedad;

        INSERT INTO cca_ofertasmercadoinmobiliario (
            T_Id,  tipo_oferta, valor_pedido, valor_negociado, 
            fecha_captura_oferta, tiempo_oferta_mercado, nombre_oferente, 
            numero_contacto_oferente, predio
        )
        SELECT 
            T_Id,  tipo_oferta, valor_pedido, valor_negociado, 
            fecha_captura_oferta, tiempo_oferta_mercado, nombre_oferente, 
            numero_contacto_oferente, predio
        FROM ofertasmercadoinmobiliario;

        INSERT INTO cca_calificacionconvencional (
            T_Id,  tipo_calificar, total_calificacion, 
            clase_calificacion, armazon, muros, cubierta, 
            conservacion_estructura, subtotal_estructura, fachada, 
            cubrimiento_muros, piso, conservacion_acabados, 
            subtotal_acabados, tamanio_banio, enchape_banio, 
            mobiliario_banio, conservacion_banio, subtotal_banio, 
            tamanio_cocina, enchape_cocina, mobiliario_cocina, 
            conservacion_cocina, subtotal_cocina, cerchas, subtotal_cerchas
        )
        SELECT 
            T_Id,  tipo_calificar, total_calificacion, 
            clase_calificacion, armazon, muros, cubierta, 
            conservacion_estructura, subtotal_estructura, fachada, 
            cubrimiento_muros, piso, conservacion_acabados, 
            subtotal_acabados, tamanio_banio, enchape_banio, 
            mobiliario_banio, conservacion_banio, subtotal_banio, 
            tamanio_cocina, enchape_cocina, mobiliario_cocina, 
            conservacion_cocina, subtotal_cocina, cerchas, subtotal_cerchas
        FROM calificacionconvencional ;

        INSERT INTO cca_caracteristicasunidadconstruccion (
            T_Id,  identificador, tipo_dominio, tipo_construccion, 
            tipo_unidad_construccion, tipo_planta, total_habitaciones, 
            total_banios, total_locales, total_plantas, uso, 
            anio_construccion, area_construida, area_privada_construida, 
            tipo_anexo, tipo_tipologia, observaciones, calificacion_convencional
        )
        SELECT 
            T_Id,  identificador, tipo_dominio, 
            tipo_construccion, tipo_unidad_construccion, tipo_planta, 
            total_habitaciones, total_banios, total_locales, total_plantas, 
            uso, anio_construccion, area_construida, area_privada_construida, 
            tipo_anexo, tipo_tipologia, observaciones, 
            calificacion_convencional
        FROM caracteristicasunidadconstruccion;

        INSERT INTO cca_terreno (
            T_Id, T_Ili_Tid, servidumbre_transito, area_terreno, etiqueta, geometria, predio
        )
        SELECT 
            t_id, t_ili_tid, servidumbre_transito , area_terreno, etiqueta, geom,  predio
        FROM "manzana_13 — cca_terreno" ;

        INSERT INTO cca_construccion (
            T_Id, T_Ili_Tid, identificador, tipo_construccion, tipo_dominio, 
            numero_pisos, numero_sotanos, numero_mezanines, 
            numero_semisotanos, area_construccion_alfanumerica, 
            area_construccion_digital, anio_construccion, 
            valor_referencia_construccion, etiqueta, altura, 
            observaciones, geometria, predio
        )
        SELECT 
            t_id, t_ili_tid, identificador , tipo_construccion , tipo_dominio , 
            numero_pisos , numero_sotanos , numero_mezanines , numero_semisotanos , 
            area_construccion_alfanumerica , area_construccion_digital , anio_construccion, 
            valor_referencia_construccion , etiqueta, altura, 
            observaciones,geom, predio
        FROM "manzana_13 — cca_construccion" ;

        INSERT INTO cca_unidadconstruccion (
            T_Id, T_Ili_Tid, tipo_planta, planta_ubicacion, 
            area_construida, altura, observaciones, geometria, 
            caracteristicasunidadconstruccion, construccion
        )
        SELECT 
            t_id, t_ili_tid, tipo_planta , planta_ubicacion , 
            area_construida , altura, observaciones , geom,  
            caracteristicasunidadconstruccion , construccion 
        FROM "manzana_13 — cca_unidadconstruccion"  ;

        INSERT INTO cca_adjunto (
            T_Id,  archivo, observaciones, procedencia, tipo_archivo, relacion_soporte, 
            dependencia_ucons, ruta_modificada, cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
            cca_interesado_adjunto, cca_unidadconstruccion_adjunto, cca_predio_adjunto, cca_puntocontrol_adjunto, 
            cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto
        )
        SELECT 
            T_Id,  archivo, observaciones, procedencia, tipo_archivo, relacion_soporte, 
            dependencia_ucons, ruta_modificada, cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
            cca_interesado_adjunto, cca_predio_adjunto, cca_unidadconstruccion_adjunto, cca_puntocontrol_adjunto, 
            cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto
        FROM adjunto; 
        
        INSERT INTO extdireccion (
            T_Id, T_Seq, tipo_direccion, es_direccion_principal, 
            localizacion, codigo_postal, clase_via_principal, 
            valor_via_principal, letra_via_principal, sector_ciudad, 
            valor_via_generadora, letra_via_generadora, numero_predio, 
            sector_predio, complemento, nombre_predio, cca_predio_direccion
        )
        SELECT  
            t_id, t_seq, tipo_direccion , es_direccion_principal , 
            geom,codigo_postal , clase_via_principal , valor_via_principal , letra_via_principal , 
            sector_ciudad , valor_via_generadora , letra_via_generadora, numero_predio, sector_predio, 
            complemento , nombre_predio, cca_predio_direccion 
        FROM "modelo_captura_20241029 _diego — extdireccion";


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
