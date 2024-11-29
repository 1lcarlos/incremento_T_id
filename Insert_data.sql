/*Insercion de usuario*/
INSERT INTO cca_usuario
(T_Id, T_Ili_Tid, id, tipo_documento, numero_documento, 
coordinador, estado, departamento_municipio_codigo, nombre, 
contrasena, rol)
SELECT T_Id, T_Ili_Tid, id, tipo_documento, numero_documento, 
coordinador, estado, municipio_codigo, nombre, 
contrasena, rol
FROM usuario_3;


/*Insercion de predio*/
INSERT INTO cca_predio
(T_Id, T_Ili_Tid, id_operacion, departamento_municipio, 
clase_suelo_registro, categoria_suelo, 
validacion_datos_localizacion, nupre, numero_predial, 
numero_predial_anterior, validacion_datos_catastrales, 
tiene_fmi, codigo_orip, matricula_inmobiliaria, estado_folio, 
tiene_area_registral, area_registral_m2, 
validacion_datos_registrales, condicion_predio, 
total_unidades_privadas, numero_torres, area_total_terreno, 
area_total_terreno_privada, area_total_terreno_comun, 
area_total_construida, area_total_construida_privada, 
area_total_construida_comun, predio_matriz, 
coeficiente_copropiedad, validacion_condicion_predio, 
destinacion_economica, validacion_destinacion_economica, 
predio_tipo, validacion_tipo_predio, validacion_derechos, 
resultado_visita, otro_cual_resultado_visita, 
suscribe_acta_colindancia, valor_referencia, 
fecha_visita_predial, tipo_documento_quien_atendio, 
numero_documento_quien_atendio, nombres_apellidos_quien_atendio, 
celular, correo_electronico, observaciones, despojo_abandono, 
estrato, otro_cual_estrato, usuario)
SELECT T_Id, T_Ili_Tid, id_operacion, departamento_municipio, 
clase_suelo_registro, categoria_suelo, 
validacion_datos_localizacion, nupre, numero_predial, 
numero_predial_anterior, validacion_datos_catastrales, 
tiene_fmi, codigo_orip, matricula_inmobiliaria, estado_folio, 
tiene_area_registral, area_registral_m2, 
validacion_datos_registrales, condicion_predio, 
total_unidades_privadas, numero_torres, area_total_terreno, 
area_total_terreno_privada, area_total_terreno_comun, 
area_total_construida, area_total_construida_privada, 
area_total_construida_comun, predio_matriz, 
coeficiente_copropiedad, validacion_condicion_predio, 
destinacion_economica, validacion_destinacion_economica, 
predio_tipo, validacion_tipo_predio, validacion_derechos, 
resultado_visita, otro_cual_resultado_visita, 
suscribe_acta_colindancia, valor_referencia, fecha_visita_predial, 
tipo_documento_quien_atendio, numero_documento_quien_atendio, 
nombres_apellidos_quien_atendio, celular, correo_electronico, 
observaciones, despojo_abandono, estrato, otro_cual_estrato, 
usuario
FROM predio_3;


INSERT INTO cca_interesado
(T_Id, T_Ili_Tid, tipo, tipo_documento, documento_identidad, 
primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, 
sexo, grupo_etnico, razon_social, departamento, municipio, 
direccion_residencia, telefono, correo_electronico, 
autoriza_notificacion_correo, estado_civil)
SELECT T_Id, T_Ili_Tid, tipo, tipo_documento, documento_identidad, 
primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, 
sexo, grupo_etnico, razon_social, departamento, municipio, 
direccion_residencia, telefono, correo_electronico,
autoriza_notificacion_correo, estado_civil
FROM interesado_3;


/*insercion agrupacion interesados*/
INSERT INTO cca_agrupacioninteresados
(T_Id, T_Ili_Tid, tipo, nombre)
SELECT T_Id, T_Ili_Tid, tipo, nombre
FROM agrupacioninteresados_3;


/*insercion tabla cca_miembros*/
INSERT INTO cca_miembros
(T_Id, T_Ili_Tid, interesado, agrupacion, participacion)
SELECT T_Id, T_Ili_Tid, interesado, agrupacion, participacion
FROM miembros_3;


/*Insercion Fuentes Administrativas*/
INSERT INTO cca_fuenteadministrativa
(T_Id, T_Ili_Tid, tipo, numero_fuente, fecha_documento_fuente, 
ente_emisor, observacion)
SELECT T_Id, T_Ili_Tid, tipo, numero_fuente, fecha_documento_fuente, 
ente_emisor, observacion
FROM fuenteadministrativa_3;


/*Insercion de derechos*/
INSERT INTO cca_derecho
(T_Id, T_Ili_Tid, tipo, cuota_participacion, fraccion_derecho, 
fecha_inicio_tenencia, origen_derecho, observacion, 
agrupacion_interesados, interesado, predio)
SELECT T_Id, T_Ili_Tid, tipo, cuota_participacion, fraccion_derecho,
fecha_inicio_tenencia, origen_derecho, observacion, 
agrupacion_interesados, interesado, predio
FROM derecho_3;

/*Insercion Fuente administrativa derecho*/

INSERT INTO cca_fuenteadministrativa_derecho
(derecho, fuente_administrativa)
SELECT  derecho, fuente_administrativa
FROM fuenteadministrativa_derecho_3;


/*Insercion novedades fmi*/

INSERT INTO cca_estructuranovedadfmi
(T_Id, T_Seq, codigo_orip, numero_fmi, tipo_novedadfmi, 
cca_predio_novedad_fmi)
SELECT T_Id, T_Seq, codigo_orip, numero_fmi, tipo_novedadfmi, 
cca_predio_novedad_fmi
FROM novedadfmi_2;

/*Insercion novedades numero_predial*/
INSERT INTO cca_estructuranovedadnumeropredial
(T_Id, T_Seq, numero_predial, tipo_novedad, 
cca_predio_novedad_numeros_prediales)
SELECT T_Id, T_Seq, numero_predial, tipo_novedad, 
cca_predio_novedad_numeros_prediales
FROM estructuranovedadnumeropredial_2 ;


/*Insercion Informalidades*/
INSERT INTO cca_predio_informalidad
(T_Id, T_Ili_Tid, cca_predio_formal, cca_predio_informal)
SELECT T_Id, T_Ili_Tid, cca_predio_formal, cca_predio_informal
FROM predio_informalidad_3;

/*Insercion predios copropiedad*/
INSERT INTO cca_predio_copropiedad
(T_Id, unidad_predial, matriz, coeficiente)
SELECT T_Id, unidad_predial, matriz, coeficiente
FROM predio_copropiedad;

/*Insercion ofertas mercado inmobiliario*/
INSERT INTO cca_ofertasmercadoinmobiliario
(T_Id, T_Ili_Tid, tipo_oferta, valor_pedido, valor_negociado, 
fecha_captura_oferta, tiempo_oferta_mercado, nombre_oferente, 
numero_contacto_oferente, predio)
SELECT T_Id, T_Ili_Tid, tipo_oferta, valor_pedido, valor_negociado, 
fecha_captura_oferta, tiempo_oferta_mercado, nombre_oferente, 
numero_contacto_oferente, predio
FROM ofertasmercadoinmobiliario;

/*Insercion referencia registral sistema antiguo*/
INSERT INTO extreferenciaregistralsistemaantiguo
(T_Id, T_Seq, tipo_referencia, oficina, libro, tomo, pagina, 
numero, dia, mes, anio, matricula, 
cca_predio_referencia_registral_sistema_antiguo)
SELECT T_Id, T_Seq, tipo_referencia, oficina, libro, tomo, pagina, 
numero, dia, mes, anio, matricula, 
cca_predio_referencia_registral_sistema_antiguo
FROM referenciaregistralsistemaantiguo;

/*Insercion calificacion convencionales*/
INSERT INTO cca_calificacionconvencional
(T_Id, T_Ili_Tid, tipo_calificar, total_calificacion, 
clase_calificacion, armazon, muros, cubierta, 
conservacion_estructura, subtotal_estructura, fachada, 
cubrimiento_muros, piso, conservacion_acabados, 
subtotal_acabados, tamanio_banio, enchape_banio, 
mobiliario_banio, conservacion_banio, subtotal_banio, 
tamanio_cocina, enchape_cocina, mobiliario_cocina, 
conservacion_cocina, subtotal_cocina, cerchas, subtotal_cerchas)
SELECT T_Id, T_Ili_Tid, tipo_calificar, total_calificacion, 
clase_calificacion, armazon, muros, cubierta, 
conservacion_estructura, subtotal_estructura, fachada, 
cubrimiento_muros, piso, conservacion_acabados, 
subtotal_acabados, tamanio_banio, enchape_banio, 
mobiliario_banio, conservacion_banio, subtotal_banio, 
tamanio_cocina, enchape_cocina, mobiliario_cocina, 
conservacion_cocina, subtotal_cocina, cerchas, subtotal_cerchas
FROM calificacionconvencional_3 ;



/*Insercion caracteristicas construccion*/
INSERT INTO cca_caracteristicasunidadconstruccion
(T_Id, T_Ili_Tid, identificador, tipo_dominio, tipo_construccion, 
tipo_unidad_construccion, tipo_planta, total_habitaciones, 
total_banios, total_locales, total_plantas, uso, 
anio_construccion, area_construida, area_privada_construida, 
tipo_anexo, tipo_tipologia, observaciones, calificacion_convencional)
SELECT T_Id, T_Ili_Tid, identificador, tipo_dominio, 
tipo_construccion, tipo_unidad_construccion, tipo_planta, 
total_habitaciones, total_banios, total_locales, total_plantas, 
uso, anio_construccion, area_construida, area_privada_construida, 
tipo_anexo, tipo_tipologia, observaciones, 
calificacion_convencional
FROM caracteristicasunidadconstruccion_3;


/*Insercion terrenos*/

INSERT INTO cca_terreno
(T_Id, T_Ili_Tid, servidumbre_transito, area_terreno, 
etiqueta, geometria, predio)
SELECT t_id, t_ili_tid, servidumbre_transito , area_terreno, 
etiqueta, geom,  predio
FROM "manzana_14_3 — cca_terreno";


INSERT INTO cca_construccion
(T_Id, T_Ili_Tid, identificador, tipo_construccion, tipo_dominio, 
numero_pisos, numero_sotanos, numero_mezanines, 
numero_semisotanos, area_construccion_alfanumerica, 
area_construccion_digital, anio_construccion, 
valor_referencia_construccion, etiqueta, altura, 
observaciones, geometria, predio)
SELECT t_id, t_ili_tid, identificador , tipo_construccion , tipo_dominio , 
numero_pisos , numero_sotanos , numero_mezanines , numero_semisotanos , 
area_construccion_alfanumerica , area_construccion_digital , anio_construccion, 
valor_referencia_construccion , etiqueta, altura, 
observaciones,geom, predio
FROM "manzana_14_3 — cca_construccion";


/*Insercion de unidades construccion*/
INSERT INTO cca_unidadconstruccion
(T_Id, T_Ili_Tid, tipo_planta, planta_ubicacion, 
area_construida, altura, observaciones, geometria, 
caracteristicasunidadconstruccion, construccion)
SELECT t_id, t_ili_tid, tipo_planta , planta_ubicacion , 
area_construida , altura, observaciones , geom,  
caracteristicasunidadconstruccion , construccion 
FROM "manzana_14_3 — cca_unidadconstruccion";


/*Insercion de adjuntos
INSERT INTO cca_adjunto
(T_Id, T_Seq, archivo, observaciones, procedencia, tipo_archivo, 
cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
cca_interesado_adjunto, cca_unidadconstruccion_adjunto, cca_puntocontrol_adjunto, 
cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto)
SELECT T_Id, T_Seq, archivo, observaciones, procedencia, tipo_archivo,  
cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
cca_interesado_adjunto, cca_unidadconstruccion_adjunto, cca_puntocontrol_adjunto, 
cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto
FROM adjunto_3;
*/


INSERT INTO cca_adjunto
(T_Id, T_Seq, archivo, observaciones, procedencia, tipo_archivo, relacion_soporte, 
dependencia_ucons, ruta_modificada, cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
cca_interesado_adjunto, cca_unidadconstruccion_adjunto, cca_predio_adjunto, cca_puntocontrol_adjunto, 
cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto)
SELECT T_Id, T_Seq, archivo, observaciones, procedencia, tipo_archivo, relacion_soporte, 
dependencia_ucons, ruta_modificada, cca_construccion_adjunto, cca_fuenteadminstrtiva_adjunto, 
cca_interesado_adjunto, cca_predio_adjunto, cca_unidadconstruccion_adjunto, cca_puntocontrol_adjunto, 
cca_puntolevantamiento_adjunto, cca_puntolindero_adjunto, cca_puntoreferencia_adjunto
FROM adjunto; 
 
 


/*Insercion de direcciones*/

INSERT INTO extdireccion
(T_Id, T_Seq, tipo_direccion, es_direccion_principal, 
localizacion, codigo_postal, clase_via_principal, 
valor_via_principal, letra_via_principal, sector_ciudad, 
valor_via_generadora, letra_via_generadora, numero_predio, 
sector_predio, complemento, nombre_predio, cca_predio_direccion)
SELECT  t_id, t_seq, tipo_direccion , es_direccion_principal , 
geom,codigo_postal , clase_via_principal , valor_via_principal , letra_via_principal , 
sector_ciudad , valor_via_generadora , letra_via_generadora, numero_predio, sector_predio, 
complemento , nombre_predio, cca_predio_direccion 
FROM "manzana_14_3 — extdireccion" ;


