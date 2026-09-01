# Documento de Arquitectura de Software — `«NOMBRE_PROYECTO»`

> **Cómo se escribe lo que se llena.** En la variedad del idioma que usa el proyecto, en tercera persona para lo que se explica y en infinitivo para lo que el lector hace. La regla es [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), y se cita en vez de repetirla: lo que se copia a mano se copia distinto (`S-090`). Los espacios por llenar van marcados `«…»`, que es la marca de todos los modelos ([`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).

> **Modelo reutilizable.** Reemplazar cada `«…»` con lo que el proyecto tenga de verdad, y borrar las secciones que no apliquen conservando la numeración de las que quedan. **Nada se inventa**: ni componentes, ni tecnologías, ni versiones, ni servidores, ni integraciones, ni requisitos. El dato que no se tenga se deja marcado, que es lo que distingue un hueco de un olvido. Cada elemento se clasifica con la convención de estados del anexo A.

---

## 1. Información general

| Campo | Valor |
| ----- | ----- |
| Nombre del proyecto | `«NOMBRE_PROYECTO»` |
| Código o identificador | `«CODIGO_PROYECTO»` |
| Sistema | `«NOMBRE_SISTEMA»` |
| Versión del sistema | `«VERSION_SISTEMA»` |
| Versión del documento | `«VERSION_DOCUMENTO»` |
| Fecha | `«FECHA»` |
| Responsable | `«RESPONSABLE»` |
| Arquitecto | `«ARQUITECTO»` |
| Estado del documento | `<BORRADOR / EN REVISIÓN / APROBADO / OBSOLETO>` |
| Clasificación | `<PÚBLICO / INTERNO / CONFIDENCIAL / RESERVADO>` |
| Área o dependencia | `«AREA»` |

---

## 2. Control de cambios

| Versión | Fecha | Cambio | Responsable |
| ------- | ----- | ------ | ----------- |
| `«VERSION_DOCUMENTO»` | `«FECHA»` | `«CAMBIO»` | `«RESPONSABLE»` |

---

## 3. Introducción

**Propósito del documento:** `«PROPÓSITO»`

**Contexto general del sistema:** `«CONTEXTO_GENERAL»`

**Público objetivo**

| Perfil | Uso que dará al documento |
| ------ | ------------------------- |
| `«PERFIL»` | `«USO»` |

**Nivel de detalle de la arquitectura:** `«NIVEL_DE_DETALLE»`

**Relación con otros documentos**

| Documento | Versión | Relación | Ubicación |
| --------- | ------- | -------- | --------- |
| `«DOCUMENTO»` | `«VERSION»` | `«RELACIÓN»` | `«UBICACIÓN»` |

---

## 4. Objetivos de la arquitectura

| # | Objetivo | Descripción | Prioridad | Cómo se verifica |
| - | -------- | ----------- | --------- | ---------------- |
| 1 | `«OBJETIVO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«CRITERIO_O_MÉTRICA»` |

> Se documentan solo los objetivos que el proyecto adoptó. No entran atributos de calidad que no hayan sido definidos.

---

## 5. Alcance

### 5.1 Componentes incluidos

| Componente | Descripción | Estado |
| ---------- | ----------- | ------ |
| `«COMPONENTE»` | `«DESCRIPCIÓN»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 5.2 Componentes excluidos

| Componente | Motivo de exclusión | Responsable / documento de referencia |
| ---------- | ------------------- | ------------------------------------- |
| `«COMPONENTE»` | `«MOTIVO»` | `«REFERENCIA»` |

### 5.3 Sistemas externos considerados

| Sistema externo | Relación con el sistema | Responsable |
| --------------- | ----------------------- | ----------- |
| `«SISTEMA_EXTERNO»` | `«RELACIÓN»` | `«RESPONSABLE»` |

### 5.4 Ambientes contemplados

| Ambiente | Incluido en este documento | Observaciones |
| -------- | -------------------------- | ------------- |
| `«AMBIENTE»` | `<Sí / No>` | `«OBSERVACIONES»` |

### 5.5 Límites de responsabilidad del sistema

| Elemento | Responsabilidad del sistema | Responsabilidad externa |
| -------- | --------------------------- | ----------------------- |
| `«ELEMENTO»` | `«RESPONSABILIDAD»` | `«RESPONSABLE_EXTERNO»` |

---

## 6. Contexto del sistema

**Descripción externa del sistema:** `«DESCRIPCIÓN»`

### 6.1 Actores y usuarios

| Actor / usuario | Tipo | Interacción con el sistema | Canal |
| --------------- | ---- | -------------------------- | ----- |
| `«ACTOR»` | `<Persona / Sistema / Organización>` | `«INTERACCIÓN»` | `«CANAL»` |

### 6.2 Sistemas y organizaciones relacionadas

| Sistema / organización | Rol | Dirección de la relación | Observaciones |
| ---------------------- | --- | ------------------------ | ------------- |
| `«SISTEMA»` | `«ROL»` | `<Entrada / Salida / Bidireccional>` | `«OBSERVACIONES»` |

### 6.3 Entradas y salidas

| Tipo | Elemento | Origen | Destino | Formato | Frecuencia |
| ---- | -------- | ------ | ------- | ------- | ---------- |
| `<Entrada / Salida>` | `«ELEMENTO»` | `«ORIGEN»` | `«DESTINO»` | `«FORMATO»` | `«FRECUENCIA»` |

### 6.4 Límites del sistema

`«DESCRIPCIÓN_DE_LOS_LÍMITES»`

### 6.5 Diagrama de contexto

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |
| Leyenda | `«LEYENDA»` |

`«INSERTAR_DIAGRAMA_DE_CONTEXTO»`

---

## 7. Requisitos arquitectónicos

### 7.1 Requisitos funcionales relevantes

> Incluir únicamente los requisitos con impacto arquitectónico.

| ID | Requisito | Descripción | Prioridad | Impacto arquitectónico |
| -- | --------- | ----------- | --------- | ---------------------- |
| `«ID_RF»` | `«REQUISITO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«IMPACTO»` |

### 7.2 Requisitos no funcionales

| ID | Requisito | Descripción | Prioridad | Impacto arquitectónico |
| -- | --------- | ----------- | --------- | ---------------------- |
| `«ID_RNF»` | `«REQUISITO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«IMPACTO»` |

**Categorías a considerar cuando apliquen:** rendimiento, disponibilidad, escalabilidad, seguridad, recuperación, tolerancia a fallos, auditabilidad, observabilidad, mantenibilidad, compatibilidad.

---

## 8. Principios arquitectónicos

| # | Principio | Descripción | Cómo se aplica en el sistema | Estado |
| - | --------- | ----------- | ---------------------------- | ------ |
| 1 | `«PRINCIPIO»` | `«DESCRIPCIÓN»` | `«APLICACIÓN»` | `<ACTUAL / PROPUESTA>` |

> Se documentan solo los principios que el proyecto adoptó de verdad.

---

## 9. Vista general de la arquitectura

**Descripción general de la solución:** `«DESCRIPCIÓN_GENERAL»`

**Estilo o patrón arquitectónico:** `«ESTILO_ARQUITECTÓNICO»`

| Pregunta | Respuesta |
| -------- | --------- |
| ¿Cuáles son los componentes principales? | `«COMPONENTES»` |
| ¿Cómo se comunican? | `«MECANISMOS_DE_COMUNICACIÓN»` |
| ¿Dónde se ejecutan? | `«UBICACIÓN_DE_EJECUCIÓN»` |
| ¿Dónde se almacenan los datos? | `«ALMACENES_DE_DATOS»` |
| ¿Qué sistemas externos intervienen? | `«SISTEMAS_EXTERNOS»` |

### 9.1 Diagrama general de arquitectura

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |
| Leyenda | `«LEYENDA»` |

`«INSERTAR_DIAGRAMA_GENERAL»`

---

## 10. Arquitectura lógica

**Organización lógica del sistema:** `«DESCRIPCIÓN»`

### 10.1 Elementos lógicos

| Elemento | Tipo | Responsabilidad | Dependencias | Interfaces | Estado |
| -------- | ---- | --------------- | ------------ | ---------- | ------ |
| `«ELEMENTO»` | `<Capa / Módulo / Dominio / Servicio / Componente / Interfaz / Repositorio / Adaptador / Proceso>` | `«RESPONSABILIDAD»` | `«DEPENDENCIAS»` | `«INTERFACES»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 10.2 Reglas de dependencia entre elementos

| Desde | Hacia | Permitida | Regla / justificación |
| ----- | ----- | --------- | --------------------- |
| `«ELEMENTO_ORIGEN»` | `«ELEMENTO_DESTINO»` | `<Sí / No>` | `«REGLA»` |

### 10.3 Diagrama de arquitectura lógica

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |

`«INSERTAR_DIAGRAMA_LÓGICO»`

---

## 11. Arquitectura de componentes

> Duplicar la ficha por cada componente principal del sistema.

### 11.1 Inventario de componentes

| # | Componente | Tipo | Estado | Responsable |
| - | ---------- | ---- | ------ | ----------- |
| 1 | `«NOMBRE_COMPONENTE»` | `«TIPO»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN / OBSOLETA>` | `«RESPONSABLE»` |

### 11.2 `«NOMBRE_COMPONENTE»`

**Responsabilidad:** `«RESPONSABILIDAD»`

**Entradas:** `«ENTRADAS»`

**Salidas:** `«SALIDAS»`

**Dependencias:** `«DEPENDENCIAS»`

**Interfaces:** `«INTERFACES»`

**Tecnología:** `«TECNOLOGIA»` — versión `«VERSION»`

**Ubicación:** `«UBICACION»`

**Estado:** `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN / OBSOLETA / PENDIENTE>`

**Observaciones:** `«OBSERVACIONES»`

### 11.3 `«NOMBRE_COMPONENTE»`

`«REPETIR_FICHA»`

### 11.4 Diagrama de componentes

`«INSERTAR_DIAGRAMA_DE_COMPONENTES»`

---

## 12. Arquitectura de datos

**Descripción general de la gestión de datos:** `«DESCRIPCIÓN»`

### 12.1 Fuentes de información

| Fuente | Tipo | Origen | Uso en el sistema | Responsable |
| ------ | ---- | ------ | ----------------- | ----------- |
| `«FUENTE»` | `<Interna / Externa>` | `«ORIGEN»` | `«USO»` | `«RESPONSABLE»` |

### 12.2 Almacenes de información

| Almacén | Tipo | Motor / servicio | Versión | Contenido | Componentes que lo usan | Estado |
| ------- | ---- | ---------------- | ------- | --------- | ----------------------- | ------ |
| `«ALMACÉN»` | `<Base de datos / Archivos / Caché / Cola / Otro>` | `«MOTOR_O_SERVICIO»` | `«VERSION»` | `«CONTENIDO»` | `«COMPONENTES»` | `<ACTUAL / PROPUESTA>` |

### 12.3 Esquemas y organización

| Esquema / espacio | Almacén | Propósito | Observaciones |
| ----------------- | ------- | --------- | ------------- |
| `«ESQUEMA»` | `«ALMACÉN»` | `«PROPÓSITO»` | `«OBSERVACIONES»` |

### 12.4 Almacenamiento de archivos

| Tipo de archivo | Ubicación | Tamaño estimado | Acceso | Retención |
| --------------- | --------- | --------------- | ------ | --------- |
| `«TIPO»` | `«UBICACIÓN»` | `«TAMAÑO»` | `«ACCESO»` | `«RETENCIÓN»` |

### 12.5 Caché y colas

| Elemento | Tipo | Propósito | Componentes involucrados | Política |
| -------- | ---- | --------- | ------------------------ | -------- |
| `«ELEMENTO»` | `<Caché / Cola / Tópico>` | `«PROPÓSITO»` | `«COMPONENTES»` | `«POLÍTICA»` |

### 12.6 Flujos de datos entre componentes y almacenes

| Origen | Destino | Datos | Dirección | Mecanismo | Frecuencia |
| ------ | ------- | ----- | --------- | --------- | ---------- |
| `«ORIGEN»` | `«DESTINO»` | `«DATOS»` | `<Lectura / Escritura / Ambas>` | `«MECANISMO»` | `«FRECUENCIA»` |

### 12.7 Retención e integridad

| Conjunto de datos | Política de retención | Mecanismo de integridad | Responsable |
| ----------------- | --------------------- | ----------------------- | ----------- |
| `«CONJUNTO»` | `«RETENCIÓN»` | `«MECANISMO»` | `«RESPONSABLE»` |

### 12.8 Diagrama de datos

`«INSERTAR_DIAGRAMA_DE_DATOS»`

---

## 13. Modelo de datos

> Incluir cuando el sistema requiera persistencia estructurada.

### 13.1 Entidades principales

| Entidad | Descripción | Almacén / esquema | Volumen estimado | Estado |
| ------- | ----------- | ----------------- | ---------------- | ------ |
| `«ENTIDAD»` | `«DESCRIPCIÓN»` | `«ESQUEMA»` | `«VOLUMEN»` | `<ACTUAL / PROPUESTA>` |

### 13.2 Relaciones

| Entidad origen | Entidad destino | Tipo de relación | Cardinalidad | Regla |
| -------------- | --------------- | ---------------- | ------------ | ----- |
| `«ENTIDAD»` | `«ENTIDAD»` | `«TIPO»` | `«CARDINALIDAD»` | `«REGLA»` |

### 13.3 Claves y restricciones relevantes

| Entidad | Clave / restricción | Tipo | Descripción |
| ------- | ------------------- | ---- | ----------- |
| `«ENTIDAD»` | `«CLAVE_O_RESTRICCIÓN»` | `<Primaria / Foránea / Única / Verificación>` | `«DESCRIPCIÓN»` |

### 13.4 Catálogos

| Catálogo | Contenido | Origen | Mantenimiento |
| -------- | --------- | ------ | ------------- |
| `«CATÁLOGO»` | `«CONTENIDO»` | `«ORIGEN»` | `«RESPONSABLE_Y_PERIODICIDAD»` |

### 13.5 Auditoría e históricos

| Entidad | Mecanismo de auditoría | Datos registrados | Retención |
| ------- | ---------------------- | ----------------- | --------- |
| `«ENTIDAD»` | `«MECANISMO»` | `«DATOS»` | `«RETENCIÓN»` |

### 13.6 Modelo entidad-relación

`«INSERTAR_MODELO_ENTIDAD_RELACIÓN_O_DIAGRAMA_EQUIVALENTE»`

---

## 14. Flujos de información

> Duplicar la ficha por cada flujo principal.

### 14.1 `«NOMBRE_DEL_FLUJO»`

| Campo | Valor |
| ----- | ----- |
| Objetivo | `«OBJETIVO»` |
| Origen | `«ORIGEN»` |
| Punto de entrada | `«PUNTO_DE_ENTRADA»` |
| Componentes involucrados | `«COMPONENTES»` |
| Tipo | `<Síncrono / Asíncrono>` |
| Frecuencia | `«FRECUENCIA»` |
| Estado | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

**Secuencia**

| Paso | Componente | Acción | Datos | Resultado |
| ---- | ---------- | ------ | ----- | --------- |
| 1 | `«COMPONENTE»` | `«ACCIÓN»` | `«DATOS»` | `«RESULTADO»` |

**Validaciones aplicadas:** `«VALIDACIONES»`

**Persistencia:** `«QUÉ_SE_ALMACENA_Y_DÓNDE»`

**Integraciones involucradas:** `«INTEGRACIONES»`

**Resultado del flujo:** `«RESULTADO»`

**Manejo de errores del flujo:** `«MANEJO_DE_ERRORES»`

**Diagrama:** `«INSERTAR_DIAGRAMA_DE_FLUJO_O_SECUENCIA»`

### 14.2 `«NOMBRE_DEL_FLUJO»`

`«REPETIR_FICHA»`

---

## 15. Integraciones

### 15.1 Inventario de integraciones

| Sistema | Tipo | Protocolo | Dirección | Propósito | Autenticación |
| ------- | ---- | --------- | --------- | --------- | ------------- |
| `«SISTEMA»` | `«TIPO»` | `«PROTOCOLO»` | `<Entrante / Saliente / Bidireccional>` | `«PROPÓSITO»` | `<MECANISMO — sin credenciales reales>` |

### 15.2 `«NOMBRE_DE_LA_INTEGRACIÓN»`

| Campo | Valor |
| ----- | ----- |
| Sistema origen | `«SISTEMA_ORIGEN»` |
| Sistema destino | `«SISTEMA_DESTINO»` |
| Propósito | `«PROPÓSITO»` |
| Tipo de integración | `«TIPO»` |
| Protocolo | `«PROTOCOLO»` |
| Formato de datos | `«FORMATO»` |
| Autenticación | `«MECANISMO»` |
| Frecuencia | `«FRECUENCIA»` |
| Volumen estimado | `«VOLUMEN»` |
| Manejo de errores | `«MANEJO_DE_ERRORES»` |
| Reintentos / timeouts | `«POLÍTICA»` |
| Dependencias | `«DEPENDENCIAS»` |
| Responsable del sistema externo | `«RESPONSABLE»` |
| Estado | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN / OBSOLETA>` |

### 15.3 Diagrama de integración

`«INSERTAR_DIAGRAMA_DE_INTEGRACIÓN»`

> No incluir credenciales, tokens ni claves reales en esta sección.

---

## 16. APIs e interfaces

> Incluir cuando el sistema exponga o consuma APIs. Si existe documentación técnica específica, referénciela en lugar de duplicarla.

### 16.1 Inventario de APIs

| API | Tipo | Propósito | Consumidores | Versionamiento | Estado |
| --- | ---- | --------- | ------------ | -------------- | ------ |
| `«API»` | `<Expuesta / Consumida>` | `«PROPÓSITO»` | `«CONSUMIDORES»` | `«ESTRATEGIA»` | `<ACTUAL / PROPUESTA>` |

### 16.2 `«NOMBRE_API»`

| Campo | Valor |
| ----- | ----- |
| Propósito | `«PROPÓSITO»` |
| Punto de acceso base | `«URL_BASE»` |
| Autenticación | `«MECANISMO»` |
| Autorización | `«MECANISMO_Y_ROLES»` |
| Formato de entrada | `«FORMATO»` |
| Formato de salida | `«FORMATO»` |
| Manejo de errores | `«ESTRATEGIA»` |
| Versionamiento | `«ESTRATEGIA»` |
| Documentación técnica detallada | `«REFERENCIA_AL_DOCUMENTO»` |

**Endpoints principales**

| Endpoint | Método | Propósito | Entrada | Salida | Autorización |
| -------- | ------ | --------- | ------- | ------ | ------------ |
| `«ENDPOINT»` | `«MÉTODO»` | `«PROPÓSITO»` | `«ENTRADA»` | `«SALIDA»` | `«ROL_O_PERMISO»` |

**Códigos de error relevantes**

| Código | Significado | Acción esperada del consumidor |
| ------ | ----------- | ------------------------------ |
| `«CÓDIGO»` | `«SIGNIFICADO»` | `«ACCIÓN»` |

---

## 17. Arquitectura de seguridad

> No incluir contraseñas, tokens, claves privadas ni ningún otro secreto real.

### 17.1 Autenticación

| Campo | Valor |
| ----- | ----- |
| Mecanismo | `«MECANISMO»` |
| Proveedor de identidad | `«PROVEEDOR»` |
| Componentes involucrados | `«COMPONENTES»` |
| Estado | `<ACTUAL / PROPUESTA>` |

### 17.2 Autorización, roles y permisos

| Rol | Ámbito | Permisos | Dónde se aplica | Mecanismo de control |
| --- | ------ | -------- | --------------- | -------------------- |
| `«ROL»` | `«ÁMBITO»` | `«PERMISOS»` | `«COMPONENTE»` | `«MECANISMO»` |

### 17.3 Gestión de sesiones

| Aspecto | Definición |
| ------- | ---------- |
| Mecanismo de sesión | `«MECANISMO»` |
| Duración / expiración | `«VALOR»` |
| Renovación | `«MECANISMO»` |
| Cierre de sesión | `«MECANISMO»` |

### 17.4 Protección de APIs y comunicaciones

| Elemento | Mecanismo de protección | Alcance | Estado |
| -------- | ----------------------- | ------- | ------ |
| `«ELEMENTO»` | `«MECANISMO»` | `«ALCANCE»` | `<ACTUAL / PROPUESTA>` |

### 17.5 Cifrado y gestión de secretos

| Elemento | Estado del dato | Mecanismo de cifrado | Gestión de claves / secretos | Responsable |
| -------- | --------------- | -------------------- | ---------------------------- | ----------- |
| `«ELEMENTO»` | `<En tránsito / En reposo>` | `«MECANISMO»` | `«GESTOR_O_MEDIO»` | `«RESPONSABLE»` |

### 17.6 Seguridad de datos

| Dato sensible | Clasificación | Protección aplicada | Normativa aplicable |
| ------------- | ------------- | ------------------- | ------------------- |
| `«DATO»` | `«CLASIFICACIÓN»` | `«PROTECCIÓN»` | `«NORMATIVA»` |

### 17.7 Auditoría, trazabilidad y gestión de accesos

| Evento auditado | Componente | Información registrada | Retención | Consulta |
| --------------- | ---------- | ---------------------- | --------- | -------- |
| `«EVENTO»` | `«COMPONENTE»` | `«INFORMACIÓN»` | `«RETENCIÓN»` | `«MECANISMO»` |

---

## 18. Arquitectura de despliegue

**Descripción general del despliegue:** `«DESCRIPCIÓN»`

### 18.1 Nodos de despliegue

| Nodo | Tipo | Componentes desplegados | Ubicación | Recursos asignados | Estado |
| ---- | ---- | ----------------------- | --------- | ------------------ | ------ |
| `«NODO»` | `<Servidor físico / Máquina virtual / Contenedor / Servicio gestionado / Función>` | `«COMPONENTES»` | `«UBICACIÓN»` | `«RECURSOS»` | `<ACTUAL / PROPUESTA>` |

### 18.2 Red, balanceadores y proxies

| Elemento | Tipo | Propósito | Componentes que atiende | Configuración relevante |
| -------- | ---- | --------- | ----------------------- | ----------------------- |
| `«ELEMENTO»` | `<Red / Balanceador / Proxy / Firewall>` | `«PROPÓSITO»` | `«COMPONENTES»` | `«CONFIGURACIÓN»` |

### 18.3 Almacenamiento y bases de datos en despliegue

| Recurso | Tipo | Ubicación | Alta disponibilidad | Respaldo |
| ------- | ---- | --------- | ------------------- | -------- |
| `«RECURSO»` | `«TIPO»` | `«UBICACIÓN»` | `<Sí / No — MECANISMO>` | `«MECANISMO»` |

### 18.4 Proceso de despliegue

| Aspecto | Definición |
| ------- | ---------- |
| Estrategia de despliegue | `«ESTRATEGIA»` |
| Automatización | `«MECANISMO»` |
| Artefactos desplegados | `«ARTEFACTOS»` |
| Reversión | `«MECANISMO»` |
| Referencia al manual de instalación | `«DOCUMENTO»` |

### 18.5 Diagrama de despliegue

`«INSERTAR_DIAGRAMA_DE_DESPLIEGUE»`

---

## 19. Ambientes

| Ambiente | Componentes | Infraestructura | URL / Acceso | Observaciones |
| -------- | ----------- | --------------- | ------------ | ------------- |
| `«AMBIENTE»` | `«COMPONENTES»` | `«INFRAESTRUCTURA»` | `«URL_O_ACCESO»` | `«OBSERVACIONES»` |

### 19.1 Diferencias arquitectónicas entre ambientes

| Aspecto | `«AMBIENTE_1»` | `«AMBIENTE_2»` | Motivo de la diferencia |
| ------- | -------------- | -------------- | ----------------------- |
| `«ASPECTO»` | `«VALOR»` | `«VALOR»` | `«MOTIVO»` |

---

## 20. Infraestructura

### 20.1 Recursos por nodo

| Nodo | CPU | Memoria | Disco | Red | Sistema operativo | Observaciones |
| ---- | --- | ------- | ----- | --- | ----------------- | ------------- |
| `«NODO»` | `«CPU»` | `«MEMORIA»` | `«DISCO»` | `«RED»` | `«SISTEMA_OPERATIVO»` | `«OBSERVACIONES»` |

### 20.2 Servicios de infraestructura

| Servicio | Propósito | Proveedor / origen | Componentes que lo usan | Estado |
| -------- | --------- | ------------------ | ----------------------- | ------ |
| `«SERVICIO»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `«COMPONENTES»` | `<ACTUAL / PROPUESTA>` |

### 20.3 Puertos

| Puerto | Protocolo | Componente | Exposición | Origen permitido | Propósito |
| ------ | --------- | ---------- | ---------- | ---------------- | --------- |
| `«PUERTO»` | `«PROTOCOLO»` | `«COMPONENTE»` | `<Interna / Externa>` | `«ORIGEN»` | `«PROPÓSITO»` |

### 20.4 Dependencias externas de infraestructura

| Dependencia | Propósito | Proveedor | Criticidad | Responsable |
| ----------- | --------- | --------- | ---------- | ----------- |
| `«DEPENDENCIA»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `<Alta / Media / Baja>` | `«RESPONSABLE»` |

---

## 21. Comunicación entre componentes

| Origen | Destino | Tipo | Protocolo | Puerto | Formato | Canal / mecanismo | Observaciones |
| ------ | ------- | ---- | --------- | ------ | ------- | ----------------- | ------------- |
| `«COMPONENTE»` | `«COMPONENTE»` | `<Síncrona / Asíncrona>` | `«PROTOCOLO»` | `«PUERTO»` | `«FORMATO»` | `«MECANISMO»` | `«OBSERVACIONES»` |

### 21.1 Mensajería y eventos

> Incluir cuando el sistema utilice comunicación asíncrona.

| Evento / mensaje | Productor | Consumidores | Canal / tópico | Garantía de entrega | Manejo de fallos |
| ---------------- | --------- | ------------ | -------------- | ------------------- | ---------------- |
| `«EVENTO»` | `«COMPONENTE»` | `«COMPONENTES»` | `«CANAL»` | `«GARANTÍA»` | `«MANEJO»` |

### 21.2 Diagrama de comunicación

`«INSERTAR_DIAGRAMA_DE_COMUNICACIÓN»`

---

## 22. Disponibilidad y tolerancia a fallos

| Mecanismo | Componente | Descripción | Estado |
| --------- | ---------- | ----------- | ------ |
| `<Redundancia / Replicación / Balanceo / Reintentos / Timeouts / Circuit breaker / Failover / Backup / Otro>` | `«COMPONENTE»` | `«DESCRIPCIÓN»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 22.1 Puntos únicos de falla identificados

| Componente | Impacto si falla | Mitigación existente | Mitigación propuesta |
| ---------- | ---------------- | -------------------- | -------------------- |
| `«COMPONENTE»` | `«IMPACTO»` | `«MITIGACIÓN_ACTUAL»` | `«MITIGACIÓN_PROPUESTA»` |

### 22.2 Objetivos de disponibilidad

| Indicador | Valor definido | Ambiente | Cómo se mide |
| --------- | -------------- | -------- | ------------ |
| `«INDICADOR»` | `«VALOR»` | `«AMBIENTE»` | `«MEDICIÓN»` |

---

## 23. Escalabilidad y rendimiento

### 23.1 Estrategias de escalabilidad

| Componente | Tipo de escalabilidad | Mecanismo | Límite conocido | Estado |
| ---------- | --------------------- | --------- | --------------- | ------ |
| `«COMPONENTE»` | `<Vertical / Horizontal / No escalable>` | `«MECANISMO»` | `«LÍMITE»` | `<ACTUAL / PROPUESTA>` |

### 23.2 Carga esperada

| Indicador | Valor | Origen del dato | Ambiente |
| --------- | ----- | --------------- | -------- |
| `«INDICADOR»` | `«VALOR»` | `«ORIGEN»` | `«AMBIENTE»` |

> No inventar métricas. Cuando el valor no esté definido, dejar el placeholder.

### 23.3 Procesamiento intensivo, caché y colas

| Elemento | Propósito | Componente | Efecto en el rendimiento | Estado |
| -------- | --------- | ---------- | ------------------------ | ------ |
| `«ELEMENTO»` | `«PROPÓSITO»` | `«COMPONENTE»` | `«EFECTO»` | `<ACTUAL / PROPUESTA>` |

### 23.4 Estrategias de crecimiento

`«DESCRIPCIÓN_DE_LA_ESTRATEGIA»`

---

## 24. Observabilidad y monitoreo

| Mecanismo | Propósito | Componente | Retención | Responsable |
| --------- | --------- | ---------- | --------- | ----------- |
| `<Logs / Métricas / Trazas / Alertas / Monitoreo / Auditoría / Health check>` | `«PROPÓSITO»` | `«COMPONENTE»` | `«RETENCIÓN»` | `«RESPONSABLE»` |

### 24.1 Alertas definidas

| Alerta | Condición | Severidad | Destinatario | Acción esperada |
| ------ | --------- | --------- | ------------ | --------------- |
| `«ALERTA»` | `«CONDICIÓN»` | `«SEVERIDAD»` | `«DESTINATARIO»` | `«ACCIÓN»` |

### 24.2 Health checks

| Componente | Punto de verificación | Frecuencia | Respuesta esperada |
| ---------- | --------------------- | ---------- | ------------------ |
| `«COMPONENTE»` | `«ENDPOINT_O_MECANISMO»` | `«FRECUENCIA»` | `«RESPUESTA»` |

---

## 25. Gestión de errores

| Tipo de error | Dónde se origina | Detección | Tratamiento | Registro | Notificación |
| ------------- | ---------------- | --------- | ----------- | -------- | ------------ |
| `<Validación / Excepción / Integración / Persistencia / Infraestructura>` | `«COMPONENTE»` | `«MECANISMO»` | `«TRATAMIENTO»` | `«DÓNDE_SE_REGISTRA»` | `«MECANISMO»` |

### 25.1 Políticas de reintento y recuperación

| Operación | Política de reintento | Timeout | Acción tras agotar reintentos | Recuperación |
| --------- | --------------------- | ------- | ----------------------------- | ------------ |
| `«OPERACIÓN»` | `«POLÍTICA»` | `«TIMEOUT»` | `«ACCIÓN»` | `«MECANISMO»` |

---

## 26. Respaldo y recuperación

| Elemento | Tipo de respaldo | Frecuencia | Retención | Ubicación | Responsable |
| -------- | ---------------- | ---------- | --------- | --------- | ----------- |
| `«ELEMENTO»` | `<Completo / Incremental / Diferencial>` | `«FRECUENCIA»` | `«RETENCIÓN»` | `«UBICACIÓN»` | `«RESPONSABLE»` |

### 26.1 Procedimiento de recuperación

| Escenario | Procedimiento | Tiempo estimado | Responsable | Documento de referencia |
| --------- | ------------- | --------------- | ----------- | ----------------------- |
| `«ESCENARIO»` | `«PROCEDIMIENTO»` | `«TIEMPO»` | `«RESPONSABLE»` | `«DOCUMENTO»` |

### 26.2 Objetivos de recuperación

| Indicador | Valor definido | Alcance | Observaciones |
| --------- | -------------- | ------- | ------------- |
| RPO | `«VALOR»` | `«ALCANCE»` | `«OBSERVACIONES»` |
| RTO | `«VALOR»` | `«ALCANCE»` | `«OBSERVACIONES»` |

### 26.3 Pruebas de restauración

| Prueba | Frecuencia | Última ejecución | Resultado | Responsable |
| ------ | ---------- | ---------------- | --------- | ----------- |
| `«PRUEBA»` | `«FRECUENCIA»` | `«FECHA»` | `«RESULTADO»` | `«RESPONSABLE»` |

---

## 27. Tecnologías utilizadas

| Componente | Tecnología | Versión | Propósito |
| ---------- | ---------- | ------- | --------- |
| `«COMPONENTE»` | `«TECNOLOGIA»` | `«VERSION»` | `«PROPÓSITO»` |

> No inventar versiones. Cuando la versión no esté disponible, mantener `«VERSION»`.

---

## 28. Dependencias

### 28.1 Dependencias de software

| Dependencia | Versión | Componente que la usa | Criticidad | Licencia | Observaciones |
| ----------- | ------- | --------------------- | ---------- | -------- | ------------- |
| `«DEPENDENCIA»` | `«VERSION»` | `«COMPONENTE»` | `<Alta / Media / Baja>` | `«LICENCIA»` | `«OBSERVACIONES»` |

### 28.2 Dependencias de infraestructura

| Dependencia | Propósito | Componente afectado | Criticidad | Responsable |
| ----------- | --------- | ------------------- | ---------- | ----------- |
| `«DEPENDENCIA»` | `«PROPÓSITO»` | `«COMPONENTE»` | `<Alta / Media / Baja>` | `«RESPONSABLE»` |

### 28.3 Dependencias de servicios externos

| Servicio | Propósito | Proveedor | Disponibilidad comprometida | Plan de contingencia |
| -------- | --------- | --------- | --------------------------- | -------------------- |
| `«SERVICIO»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `«COMPROMISO»` | `«CONTINGENCIA»` |

### 28.4 Dependencias de terceros

| Tercero | Elemento del que depende el sistema | Impacto si no está disponible | Responsable del relacionamiento |
| ------- | ----------------------------------- | ----------------------------- | ------------------------------- |
| `«TERCERO»` | `«ELEMENTO»` | `«IMPACTO»` | `«RESPONSABLE»` |

---

## 29. Decisiones arquitectónicas

### 29.1 Índice de decisiones

| ID | Título | Fecha | Estado | Componentes afectados |
| -- | ------ | ----- | ------ | --------------------- |
| ADR-`«XXX»` | `«TÍTULO»` | `«FECHA»` | `<PROPUESTA / ACEPTADA / RECHAZADA / OBSOLETA>` | `«COMPONENTES»` |

### 29.2 ADR-`«XXX»` — `«TÍTULO»`

**Contexto:** `«CONTEXTO»`

**Problema:** `«PROBLEMA»`

**Opciones consideradas:**

| Opción | Ventajas | Desventajas |
| ------ | -------- | ----------- |
| `«OPCIÓN»` | `«VENTAJAS»` | `«DESVENTAJAS»` |

**Decisión:** `«DECISION»`

**Justificación:** `«JUSTIFICACION»`

**Consecuencias:** `«CONSECUENCIAS»`

**Requisitos relacionados:** `«REQUISITOS»`

**Estado:** `<PROPUESTA | ACEPTADA | RECHAZADA | OBSOLETA>`

**Fecha:** `«FECHA»` — **Responsable:** `«RESPONSABLE»`

### 29.3 ADR-`«XXX»` — `«TÍTULO»`

`«REPETIR_FICHA»`

---

## 30. Restricciones arquitectónicas

| # | Restricción | Tipo | Origen | Impacto en la arquitectura | Negociable |
| - | ----------- | ---- | ------ | -------------------------- | ---------- |
| 1 | `«RESTRICCIÓN»` | `<Tecnológica / Legada / Institucional / Infraestructura / Presupuestal / Compatibilidad / Regulatoria / Externa>` | `«ORIGEN»` | `«IMPACTO»` | `<Sí / No>` |

---

## 31. Riesgos arquitectónicos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
| -- | ------ | ------------ | ------- | ---------- | ------ |
| `«ID»` | `«RIESGO»` | `<Alta / Media / Baja>` | `<Alto / Medio / Bajo>` | `«MITIGACIÓN»` | `<Identificado / En mitigación / Mitigado / Aceptado>` |

---

## 32. Deuda técnica

| ID | Descripción | Impacto | Prioridad | Acción propuesta |
| -- | ----------- | ------- | --------- | ---------------- |
| `«ID»` | `«DESCRIPCIÓN»` | `«IMPACTO»` | `<Alta / Media / Baja>` | `«ACCIÓN»` |

---

## 33. Estado actual y arquitectura objetivo

### 33.1 Arquitectura actual

`«DESCRIPCIÓN_DE_LO_QUE_EXISTE_HOY»`

| Componente | Estado | Observaciones |
| ---------- | ------ | ------------- |
| `«COMPONENTE»` | `<ACTUAL / OBSOLETA>` | `«OBSERVACIONES»` |

### 33.2 Arquitectura objetivo

`«DESCRIPCIÓN_DEL_ESTADO_DESEADO»`

| Componente | Estado | Justificación |
| ---------- | ------ | ------------- |
| `«COMPONENTE»` | `<PROPUESTA / EN CONSTRUCCIÓN / PENDIENTE>` | `«JUSTIFICACIÓN»` |

### 33.3 Brechas

| # | Brecha | Situación actual | Situación objetivo | Acción requerida | Prioridad |
| - | ------ | ---------------- | ------------------ | ---------------- | --------- |
| 1 | `«BRECHA»` | `«ACTUAL»` | `«OBJETIVO»` | `«ACCIÓN»` | `<Alta / Media / Baja>` |

> No presentar componentes futuros como si ya existieran.

---

## 34. Matriz de trazabilidad arquitectónica

| Requisito | Componente | Solución | Evidencia |
| --------- | ---------- | -------- | --------- |
| `«ID_REQUISITO»` | `«COMPONENTE»` | `«SOLUCIÓN_ARQUITECTÓNICA»` | `«EVIDENCIA_O_REFERENCIA»` |

### 34.1 Trazabilidad requisito → decisión

| Requisito | Decisión relacionada | Componente afectado | Infraestructura |
| --------- | -------------------- | ------------------- | --------------- |
| `«ID_REQUISITO»` | ADR-`«XXX»` | `«COMPONENTE»` | `«INFRAESTRUCTURA»` |

---

## 35. Diagramas

> Incluir únicamente los diagramas que aporten valor. Cada diagrama debe registrarse en este inventario.

| # | Diagrama | Objetivo | Notación | Versión / fecha | Ubicación |
| - | -------- | -------- | -------- | --------------- | --------- |
| 1 | Diagrama de contexto | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 2 | Diagrama de arquitectura general | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 3 | Diagrama de componentes | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 4 | Diagrama de despliegue | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 5 | Diagrama de flujo de información | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 6 | Diagrama de secuencia | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 7 | Diagrama de datos | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |
| 8 | Diagrama de integración | `«OBJETIVO»` | `«NOTACIÓN»` | `«VERSION_O_FECHA»` | `«SECCIÓN_O_ARCHIVO»` |

**Ficha estándar de diagrama**

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Notación / herramienta | `«NOTACIÓN»` |
| Leyenda | `«LEYENDA»` |
| Versión / fecha | `«VERSION_O_FECHA»` |
| Autor | `«AUTOR»` |

---

## 36. Recomendaciones y evolución futura

### 36.1 Mejoras recomendadas

| # | Mejora | Justificación | Impacto esperado | Prioridad | Estado |
| - | ------ | ------------- | ---------------- | --------- | ------ |
| 1 | `«MEJORA»` | `«JUSTIFICACIÓN»` | `«IMPACTO»` | `<Alta / Media / Baja>` | `«PROPUESTA»` |

### 36.2 Evoluciones futuras

| # | Evolución | Descripción | Precondiciones | Horizonte | Estado |
| - | --------- | ----------- | -------------- | --------- | ------ |
| 1 | `«EVOLUCIÓN»` | `«DESCRIPCIÓN»` | `«PRECONDICIONES»` | `«HORIZONTE»` | `<PROPUESTA / PENDIENTE>` |

### 36.3 Componentes potenciales

| Componente | Propósito | Condición para incorporarlo | Estado |
| ---------- | --------- | --------------------------- | ------ |
| `«COMPONENTE»` | `«PROPÓSITO»` | `«CONDICIÓN»` | `<PROPUESTA / PENDIENTE>` |

### 36.4 Riesgos pendientes

| Riesgo | Estado | Acción pendiente | Responsable |
| ------ | ------ | ---------------- | ----------- |
| `«RIESGO»` | `«PENDIENTE»` | `«ACCIÓN»` | `«RESPONSABLE»` |

> Ninguna recomendación de esta sección debe presentarse como funcionalidad existente.

---

## 37. Checklist de arquitectura

- [ ] Contexto documentado.
- [ ] Componentes identificados.
- [ ] Responsabilidades definidas.
- [ ] Arquitectura lógica documentada.
- [ ] Arquitectura física documentada.
- [ ] Arquitectura de despliegue documentada.
- [ ] Flujos principales documentados.
- [ ] Integraciones documentadas.
- [ ] Datos documentados.
- [ ] Seguridad documentada.
- [ ] Tecnologías identificadas.
- [ ] Dependencias identificadas.
- [ ] Decisiones arquitectónicas documentadas.
- [ ] Riesgos identificados.
- [ ] Deuda técnica documentada.
- [ ] Diagramas actualizados.
- [ ] Arquitectura actual diferenciada de la objetivo.

| Campo | Valor |
| ----- | ----- |
| Fecha de verificación | `«FECHA»` |
| Verificado por | `«RESPONSABLE»` |
| Aprobado por | `«RESPONSABLE»` |
| Observaciones | `«OBSERVACIONES»` |

---

## Anexo A. Convenciones de documentación

### A.1 Estados de la información

| Estado | Significado |
| ------ | ----------- |
| **Actual** | Existe y está implementada. |
| **Propuesta** | Se plantea como solución futura. |
| **En construcción** | Está siendo implementada. |
| **Obsoleta** | Existió pero ya no forma parte de la solución. |
| **Pendiente** | Requiere definición. |

No mezclar estados dentro de una misma descripción: cada componente, integración, mecanismo o decisión debe llevar su estado explícito.

### A.2 Reglas de calidad

- No inventar componentes, tecnologías, versiones, servidores, integraciones ni requisitos.
- No asumir patrones arquitectónicos.
- No presentar propuestas como funcionalidades existentes.
- No incluir credenciales ni secretos.
- Mantener trazabilidad entre requisitos y decisiones arquitectónicas.
- Utilizar diagramas solamente cuando aporten valor.
- Evitar duplicar información; usar referencias cruzadas entre secciones.
- Mantener consistencia entre diagramas y descripción textual.
- Cuando un dato no esté disponible, utilizar un placeholder.
- Cada componente debe tener una responsabilidad claramente definida.
- Las dependencias entre componentes deben quedar explícitas.
- Las decisiones importantes deben registrar su justificación.

### A.3 Preguntas que debe responder el documento completo

**¿Qué sistema tenemos? → ¿Qué componentes lo conforman? → ¿Qué responsabilidad tiene cada uno? → ¿Cómo se comunican? → ¿Dónde se ejecutan? → ¿Dónde están los datos? → ¿Cómo se protege? → ¿Cómo se despliega? → ¿Qué decisiones arquitectónicas se tomaron y por qué? → ¿Cómo puede evolucionar?**

---

## Anexo B. Instrucciones de uso de la plantilla

1. Llenar la sección 1 antes que cualquier otra.
2. Borrar las secciones y subsecciones que no apliquen, sin renumerar las que quedan.
3. Duplicar las fichas repetibles (componentes, flujos, integraciones, interfaces, decisiones) según lo que el proyecto tenga.
4. Asignar un estado del anexo A a todo componente, integración, mecanismo y decisión.
5. Anotar cada diagrama en el inventario de la sección 35, con su nombre, su objetivo, su notación y su versión.
6. Numerar las decisiones de arquitectura de corrido, sin reutilizar un identificador aunque la decisión cambie.
7. Mantener la sección 33 al día cuando la arquitectura cambie.
8. **Antes de aprobar, no queda ningún `«…»` sin llenar.** El que no se pueda llenar todavía se deja diciendo que está pendiente, con quién lo decide: un hueco callado se lee como un olvido.

### Placeholders estándar

| Placeholder | Significado |
| ----------- | ----------- |
| `«NOMBRE_PROYECTO»` | Nombre del proyecto |
| `«CODIGO_PROYECTO»` | Código o identificador |
| `«NOMBRE_SISTEMA»` | Nombre del sistema |
| `«VERSION_SISTEMA»` | Versión del sistema |
| `«VERSION_DOCUMENTO»` | Versión de este documento |
| `«RESPONSABLE»` | Persona o rol responsable |
| `«ARQUITECTO»` | Arquitecto responsable del diseño |
| `«NOMBRE_COMPONENTE»` | Componente de la arquitectura |
| `«TECNOLOGIA»` | Tecnología utilizada |
| `«VERSION»` | Versión no definida o no disponible |
| `«AMBIENTE»` | Ambiente de ejecución |
| `«NODO»` | Nodo de despliegue |
| `«SISTEMA_EXTERNO»` | Sistema externo integrado |
| `«API»` | Interfaz de programación |
| `«ID_REQUISITO»` | Identificador de requisito |
| ADR-`«XXX»` | Identificador de decisión arquitectónica |
| `<INSERTAR_DIAGRAMA_...>` | Espacio destinado a un diagrama |
| `«FECHA»` | Fecha en formato `AAAA-MM-DD` |
