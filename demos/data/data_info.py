
tables =  [
        {
            "table_name": "fcs_computadores",
            "query_name": "dbo_v2.fcs_computadores",
            "columns": ["Id", "IP", "Puerto", "Puerto_Secundario", "Id_Modbus", "Id_Modbus_Secundario", "Tag", "Compatibilidad_Modicon", "Id_Computador_Redundante", "Estado", "Master", "Usuario", "Contraseña", "Leer_Tiempo_Real", "Leer_Configuracion", "Leer_Alarmas", "Leer_Eventos", "Leer_Historicos", "Grupo_Destino", "Unidad_Destino", "Grupo_Fuente", "Unidad_Fuente", "Orden_Archivos", "Numero_Maximo_Horarios", "Numero_Maximo_Diarios", "Numero_Maximo_Proves", "Numero_Maximo_Batch", "Tipo_Protocolo", "Tiempo_Proceso_Historico", "Tiempo_Proceso_TiempoReal", "IdFirmware_fk", "IdEquipo_fk", "Servidor_OPC"],
            "description": "Table with information about computers"
        },
        {
            "table_name": "fcs_computador_medidor",
            "query_name": "dbo_v2.fcs_computador_medidor",
            "columns": ["Id", "Codigo_Medidor", "Estado", "Id_Sisema_Medicion", "Id_Sistema_Medicion_Redundante", "IdComputador_fk"],
            "description": "Table connector between dbo_v2.fcs_computadores table and dbo_v2.med_sistema_medicion table. Has information about meters in the computers like meter codes, status of the meter and the id of measurement system that the computer is connected"
        },
        {
            "table_name": "med_sistema_medicion",
            "query_name": "dbo_v2.med_sistema_medicion",
            "columns": ["Id", "IdPlataforma_fk", "Nombre", "Tag", "Estado", "FechaInicialMuestreo", "IdCliente", "IdTipoFluido_fk", "SubTipoFluido", "IdAplicabilidad_fk", "VarCromatografia", "Prover", "IsDisponible", "IdMeteringStation_fk", "IdClase_fk", "SamplingPointTag", "LimiteEstadisticoInicial", "PROFACCODE", "SOURCE", "RefPid", "NumeroLineaProceso", "Localizacion", "NominalLineSize", "IdSchedule_fk", "IdRating_fk", "ClasificacionArea", "Servicio", "LimiteEstadistico_Default", "LimiteEstadistico_Manual", "IdSamplingPoint_fk", "IsVisible", "Uso", "IdArea_fk", "NombreSanqGas", "IdDeBaseOperacional_fk", "EsProvador", "Tramo", "IdDelSistemaAsociado_fk"],
            "description": "Table with information about measurement systems"
        },
        {
            "table_name": "var_tipo_variable",
            "query_name": "dbo_v2.var_tipo_variable",
            "columns": ["Id", "Nombre", "Reporte_Manual", "IdRepManual", "Id_Field", "Cromatografia", "Estado"],
            "description": "Table with information about the name of medition variables for example: pressure, temperature, density, volume, average flow, etc, and their respective ids"
        },
        {
            "table_name": "var_variable_datos",
            "query_name": "dbo_v2.var_variable_datos",
            "columns": ["Fecha", "idVariable_fk", "idSistemaMedicion_fk", "Valor", "Valor_String"],
            "description": "Table connector between variables in table dbo_v2.var_tipo_variable and measurement systems in table dbo_v2.med_sistema_medicion. Has information about the values of the variables in table dbo_v2.var_variable_datos with their respective measurement system ids"
        }
    ]