# Documento de Arquitectura de Software · `«NOMBRE_PROYECTO»`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> **Cómo se escribe lo que se llena.** En la variedad del idioma que usa el proyecto, en tercera persona para lo que se explica y en infinitivo para lo que el lector hace. La regla es [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), y se cita en vez de repetirla: lo que se copia a mano se copia distinto (`S-090`). Los espacios por llenar van marcados `«…»`, que es la marca de todos los modelos ([`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).

> **Modelo reutilizable.** Reemplazar cada `«…»` con lo que el proyecto tenga de verdad, y borrar las secciones que no apliquen conservando la numeración de las que quedan. **Nada se inventa**: ni componentes, ni tecnologías, ni versiones, ni servidores, ni integraciones, ni requisitos. El dato que no se tenga se deja marcado, que es lo que distingue un hueco de un olvido. Cada elemento se clasifica con la convención de estados del anexo A.

## 1. Información general

> Identifica el documento y el sistema que describe: nombres, versiones, responsables, estado y clasificación.

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

## 2. Control de cambios

> Registra cada versión del documento, con su fecha, qué cambió y quién la hizo.

| Versión | Fecha | Cambio | Responsable |
| ------- | ----- | ------ | ----------- |
| `«VERSION_DOCUMENTO»` | `«FECHA»` | `«CAMBIO»` | `«RESPONSABLE»` |

## 3. Introducción

> Dice para qué existe el documento, a quién va dirigido, con qué nivel de detalle y con qué otros documentos se relaciona.

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

## 4. Objetivos de la arquitectura

> Lista los objetivos que la arquitectura debe cumplir, con su prioridad y cómo se verifica cada uno. Solo entran los que el proyecto adoptó, ningún atributo de calidad que no se haya definido.

| # | Objetivo | Descripción | Prioridad | Cómo se verifica |
| - | -------- | ----------- | --------- | ---------------- |
| 1 | `«OBJETIVO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«CRITERIO_O_MÉTRICA»` |

## 5. Alcance

> Delimita qué cubre este documento y qué no: componentes, sistemas externos, ambientes y responsabilidades.

### 5.1 Componentes incluidos

> Lista los componentes que este documento describe, con su estado.

| Componente | Descripción | Estado |
| ---------- | ----------- | ------ |
| `«COMPONENTE»` | `«DESCRIPCIÓN»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 5.2 Componentes excluidos

> Lista los componentes que quedan fuera, por qué y dónde se documentan.

| Componente | Motivo de exclusión | Responsable / documento de referencia |
| ---------- | ------------------- | ------------------------------------- |
| `«COMPONENTE»` | `«MOTIVO»` | `«REFERENCIA»` |

### 5.3 Sistemas externos considerados

> Lista los sistemas externos que el documento tiene en cuenta, qué relación tienen con el sistema y quién responde por ellos.

| Sistema externo | Relación con el sistema | Responsable |
| --------------- | ----------------------- | ----------- |
| `«SISTEMA_EXTERNO»` | `«RELACIÓN»` | `«RESPONSABLE»` |

### 5.4 Ambientes contemplados

> Dice qué ambientes cubre este documento y cuáles no.

| Ambiente | Incluido en este documento | Observaciones |
| -------- | -------------------------- | ------------- |
| `«AMBIENTE»` | `<Sí / No>` | `«OBSERVACIONES»` |

### 5.5 Límites de responsabilidad del sistema

> Separa lo que le toca resolver al sistema de lo que resuelve alguien de afuera.

| Elemento | Responsabilidad del sistema | Responsabilidad externa |
| -------- | --------------------------- | ----------------------- |
| `«ELEMENTO»` | `«RESPONSABILIDAD»` | `«RESPONSABLE_EXTERNO»` |

## 6. Contexto del sistema

> Describe el sistema visto desde afuera: quién lo usa, con qué se relaciona, qué entra y sale y dónde termina.

**Descripción externa del sistema:** `«DESCRIPCIÓN»`

### 6.1 Actores y usuarios

> Lista quién interactúa con el sistema, de qué tipo es, qué hace con él y por qué canal.

| Actor / usuario | Tipo | Interacción con el sistema | Canal |
| --------------- | ---- | -------------------------- | ----- |
| `«ACTOR»` | `<Persona / Sistema / Organización>` | `«INTERACCIÓN»` | `«CANAL»` |

### 6.2 Sistemas y organizaciones relacionadas

> Lista los sistemas y organizaciones con que el sistema se relaciona, y en qué dirección.

| Sistema / organización | Rol | Dirección de la relación | Observaciones |
| ---------------------- | --- | ------------------------ | ------------- |
| `«SISTEMA»` | `«ROL»` | `<Entrada / Salida / Bidireccional>` | `«OBSERVACIONES»` |

### 6.3 Entradas y salidas

> Lista lo que entra al sistema y lo que sale de él, con su origen, destino, formato y frecuencia.

| Tipo | Elemento | Origen | Destino | Formato | Frecuencia |
| ---- | -------- | ------ | ------- | ------- | ---------- |
| `<Entrada / Salida>` | `«ELEMENTO»` | `«ORIGEN»` | `«DESTINO»` | `«FORMATO»` | `«FRECUENCIA»` |

### 6.4 Límites del sistema

> Dice dónde termina el sistema y empieza lo que no le pertenece.

`«DESCRIPCIÓN_DE_LOS_LÍMITES»`

### 6.5 Diagrama de contexto

> Es el dibujo del sistema con sus actores y sistemas vecinos, con su ficha de identificación.

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |
| Leyenda | `«LEYENDA»` |

`«INSERTAR_DIAGRAMA_DE_CONTEXTO»`

## 7. Requisitos arquitectónicos

> Reúne los requisitos que condicionan la arquitectura.

### 7.1 Requisitos funcionales relevantes

> Lista los requisitos funcionales que condicionan la arquitectura. Solo entran los que tienen impacto arquitectónico.

| ID | Requisito | Descripción | Prioridad | Impacto arquitectónico |
| -- | --------- | ----------- | --------- | ---------------------- |
| `«ID_RF»` | `«REQUISITO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«IMPACTO»` |

### 7.2 Requisitos no funcionales

> Lista los requisitos de calidad que condicionan la arquitectura, con su impacto.

| ID | Requisito | Descripción | Prioridad | Impacto arquitectónico |
| -- | --------- | ----------- | --------- | ---------------------- |
| `«ID_RNF»` | `«REQUISITO»` | `«DESCRIPCIÓN»` | `<Alta / Media / Baja>` | `«IMPACTO»` |

**Categorías a considerar cuando apliquen:** rendimiento, disponibilidad, escalabilidad, seguridad, recuperación, tolerancia a fallos, auditabilidad, observabilidad, mantenibilidad, compatibilidad.

## 8. Principios arquitectónicos

> Lista los principios que guían las decisiones de arquitectura y cómo se aplican en el sistema. Solo entran los que el proyecto adoptó de verdad.

| # | Principio | Descripción | Cómo se aplica en el sistema | Estado |
| - | --------- | ----------- | ---------------------------- | ------ |
| 1 | `«PRINCIPIO»` | `«DESCRIPCIÓN»` | `«APLICACIÓN»` | `<ACTUAL / PROPUESTA>` |

## 9. Vista general de la arquitectura

> Resume la solución completa: su estilo y las respuestas a las preguntas básicas de la arquitectura.

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

> Es el dibujo de la arquitectura completa, con su ficha de identificación.

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |
| Leyenda | `«LEYENDA»` |

`«INSERTAR_DIAGRAMA_GENERAL»`

## 10. Arquitectura lógica

> Describe cómo se organiza el sistema por dentro, sin entrar en dónde se ejecuta.

**Organización lógica del sistema:** `«DESCRIPCIÓN»`

### 10.1 Elementos lógicos

> Lista las piezas lógicas del sistema, con su responsabilidad, sus dependencias y sus interfaces.

| Elemento | Tipo | Responsabilidad | Dependencias | Interfaces | Estado |
| -------- | ---- | --------------- | ------------ | ---------- | ------ |
| `«ELEMENTO»` | `<Capa / Módulo / Dominio / Servicio / Componente / Interfaz / Repositorio / Adaptador / Proceso>` | `«RESPONSABILIDAD»` | `«DEPENDENCIAS»` | `«INTERFACES»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 10.2 Reglas de dependencia entre elementos

> Dice qué elemento puede depender de cuál, y por qué.

| Desde | Hacia | Permitida | Regla / justificación |
| ----- | ----- | --------- | --------------------- |
| `«ELEMENTO_ORIGEN»` | `«ELEMENTO_DESTINO»` | `<Sí / No>` | `«REGLA»` |

### 10.3 Diagrama de arquitectura lógica

> Es el dibujo de la organización lógica, con su ficha de identificación.

| Campo | Valor |
| ----- | ----- |
| Nombre | `«NOMBRE_DIAGRAMA»` |
| Objetivo | `«OBJETIVO»` |
| Versión / fecha | `«VERSION_O_FECHA»` |

`«INSERTAR_DIAGRAMA_LÓGICO»`

## 11. Arquitectura de componentes

> Describe los componentes principales del sistema. La ficha se duplica por cada componente principal.

### 11.1 Inventario de componentes

> Lista todos los componentes con su tipo, su estado y su responsable.

| # | Componente | Tipo | Estado | Responsable |
| - | ---------- | ---- | ------ | ----------- |
| 1 | `«NOMBRE_COMPONENTE»` | `«TIPO»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN / OBSOLETA>` | `«RESPONSABLE»` |

### 11.2 `«NOMBRE_COMPONENTE»`

> Agrupa la ficha de un componente.

**Responsabilidad:** `«RESPONSABILIDAD»`

**Entradas:** `«ENTRADAS»`

**Salidas:** `«SALIDAS»`

**Dependencias:** `«DEPENDENCIAS»`

**Interfaces:** `«INTERFACES»`

**Tecnología:** `«TECNOLOGIA»`, versión `«VERSION»`

**Ubicación:** `«UBICACION»`

**Estado:** `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN / OBSOLETA / PENDIENTE>`

**Observaciones:** `«OBSERVACIONES»`

### 11.3 `«NOMBRE_COMPONENTE»`

> Agrupa la ficha del componente siguiente.

`«REPETIR_FICHA»`

### 11.4 Diagrama de componentes

> Es el dibujo de los componentes y sus relaciones.

`«INSERTAR_DIAGRAMA_DE_COMPONENTES»`

## 12. Arquitectura de datos

> Describe de dónde vienen los datos, dónde se guardan, cómo se mueven y cuánto se conservan.

**Descripción general de la gestión de datos:** `«DESCRIPCIÓN»`

### 12.1 Fuentes de información

> Lista de dónde sale la información que usa el sistema.

| Fuente | Tipo | Origen | Uso en el sistema | Responsable |
| ------ | ---- | ------ | ----------------- | ----------- |
| `«FUENTE»` | `<Interna / Externa>` | `«ORIGEN»` | `«USO»` | `«RESPONSABLE»` |

### 12.2 Almacenes de información

> Lista dónde se guarda la información, con qué motor y qué componentes la usan.

| Almacén | Tipo | Motor / servicio | Versión | Contenido | Componentes que lo usan | Estado |
| ------- | ---- | ---------------- | ------- | --------- | ----------------------- | ------ |
| `«ALMACÉN»` | `<Base de datos / Archivos / Caché / Cola / Otro>` | `«MOTOR_O_SERVICIO»` | `«VERSION»` | `«CONTENIDO»` | `«COMPONENTES»` | `<ACTUAL / PROPUESTA>` |

### 12.3 Esquemas y organización

> Dice cómo se organiza cada almacén por dentro.

| Esquema / espacio | Almacén | Propósito | Observaciones |
| ----------------- | ------- | --------- | ------------- |
| `«ESQUEMA»` | `«ALMACÉN»` | `«PROPÓSITO»` | `«OBSERVACIONES»` |

### 12.4 Almacenamiento de archivos

> Dice dónde se guardan los archivos, quién accede a ellos y cuánto se conservan. Si no aplica, la sección se borra sin renumerar las demás.

| Tipo de archivo | Ubicación | Tamaño estimado | Acceso | Retención |
| --------------- | --------- | --------------- | ------ | --------- |
| `«TIPO»` | `«UBICACIÓN»` | `«TAMAÑO»` | `«ACCESO»` | `«RETENCIÓN»` |

### 12.5 Caché y colas

> Lista las cachés y las colas, para qué sirven y con qué política. Si no aplica, la sección se borra sin renumerar las demás.

| Elemento | Tipo | Propósito | Componentes involucrados | Política |
| -------- | ---- | --------- | ------------------------ | -------- |
| `«ELEMENTO»` | `<Caché / Cola / Tópico>` | `«PROPÓSITO»` | `«COMPONENTES»` | `«POLÍTICA»` |

### 12.6 Flujos de datos entre componentes y almacenes

> Dice qué datos van de cada componente a cada almacén, en qué dirección y con qué frecuencia.

| Origen | Destino | Datos | Dirección | Mecanismo | Frecuencia |
| ------ | ------- | ----- | --------- | --------- | ---------- |
| `«ORIGEN»` | `«DESTINO»` | `«DATOS»` | `<Lectura / Escritura / Ambas>` | `«MECANISMO»` | `«FRECUENCIA»` |

### 12.7 Retención e integridad

> Dice cuánto se conserva cada conjunto de datos y cómo se protege su integridad.

| Conjunto de datos | Política de retención | Mecanismo de integridad | Responsable |
| ----------------- | --------------------- | ----------------------- | ----------- |
| `«CONJUNTO»` | `«RETENCIÓN»` | `«MECANISMO»` | `«RESPONSABLE»` |

### 12.8 Diagrama de datos

> Es el dibujo de los almacenes y los flujos de datos.

`«INSERTAR_DIAGRAMA_DE_DATOS»`

## 13. Modelo de datos

> Describe las entidades que el sistema guarda y cómo se relacionan. Se incluye cuando el sistema requiere persistencia estructurada; si no, la sección se borra sin renumerar las demás.

### 13.1 Entidades principales

> Lista las entidades principales, dónde se guardan y qué volumen se espera.

| Entidad | Descripción | Almacén / esquema | Volumen estimado | Estado |
| ------- | ----------- | ----------------- | ---------------- | ------ |
| `«ENTIDAD»` | `«DESCRIPCIÓN»` | `«ESQUEMA»` | `«VOLUMEN»` | `<ACTUAL / PROPUESTA>` |

### 13.2 Relaciones

> Dice cómo se relacionan las entidades y con qué cardinalidad.

| Entidad origen | Entidad destino | Tipo de relación | Cardinalidad | Regla |
| -------------- | --------------- | ---------------- | ------------ | ----- |
| `«ENTIDAD»` | `«ENTIDAD»` | `«TIPO»` | `«CARDINALIDAD»` | `«REGLA»` |

### 13.3 Claves y restricciones relevantes

> Lista las claves y restricciones que protegen la consistencia de los datos.

| Entidad | Clave / restricción | Tipo | Descripción |
| ------- | ------------------- | ---- | ----------- |
| `«ENTIDAD»` | `«CLAVE_O_RESTRICCIÓN»` | `<Primaria / Foránea / Única / Verificación>` | `«DESCRIPCIÓN»` |

### 13.4 Catálogos

> Lista las tablas de valores de referencia, de dónde salen y quién las mantiene.

| Catálogo | Contenido | Origen | Mantenimiento |
| -------- | --------- | ------ | ------------- |
| `«CATÁLOGO»` | `«CONTENIDO»` | `«ORIGEN»` | `«RESPONSABLE_Y_PERIODICIDAD»` |

### 13.5 Auditoría e históricos

> Dice qué entidades guardan la historia de sus cambios y con qué mecanismo.

| Entidad | Mecanismo de auditoría | Datos registrados | Retención |
| ------- | ---------------------- | ----------------- | --------- |
| `«ENTIDAD»` | `«MECANISMO»` | `«DATOS»` | `«RETENCIÓN»` |

### 13.6 Modelo entidad-relación

> Es el diagrama de las entidades y sus relaciones.

`«INSERTAR_MODELO_ENTIDAD_RELACIÓN_O_DIAGRAMA_EQUIVALENTE»`

## 14. Flujos de información

> Describe los flujos principales de información. La ficha se duplica por cada flujo principal.

### 14.1 `«NOMBRE_DEL_FLUJO»`

> Agrupa la ficha de un flujo: su identificación, su secuencia de pasos y cómo maneja los errores.

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

> Agrupa la ficha del flujo siguiente.

`«REPETIR_FICHA»`

## 15. Integraciones

> Describe cómo se conecta el sistema con otros sistemas. No se escriben credenciales, tokens ni claves reales.

### 15.1 Inventario de integraciones

> Lista todas las integraciones con su protocolo, su dirección y su mecanismo de autenticación.

| Sistema | Tipo | Protocolo | Dirección | Propósito | Autenticación |
| ------- | ---- | --------- | --------- | --------- | ------------- |
| `«SISTEMA»` | `«TIPO»` | `«PROTOCOLO»` | `<Entrante / Saliente / Bidireccional>` | `«PROPÓSITO»` | `<MECANISMO — sin credenciales reales>` |

### 15.2 `«NOMBRE_DE_LA_INTEGRACIÓN»`

> Agrupa la ficha de una integración. Se duplica por cada una.

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

> Es el dibujo de las integraciones del sistema.

`«INSERTAR_DIAGRAMA_DE_INTEGRACIÓN»`

## 16. APIs e interfaces

> Describe las interfaces de programación que el sistema expone o consume. Si existe documentación técnica específica, se enlaza en vez de duplicarla. Si el sistema no expone ni consume APIs, la sección se borra sin renumerar las demás.

### 16.1 Inventario de APIs

> Lista las APIs que el sistema expone o consume, quién las usa y cómo se versionan.

| API | Tipo | Propósito | Consumidores | Versionamiento | Estado |
| --- | ---- | --------- | ------------ | -------------- | ------ |
| `«API»` | `<Expuesta / Consumida>` | `«PROPÓSITO»` | `«CONSUMIDORES»` | `«ESTRATEGIA»` | `<ACTUAL / PROPUESTA>` |

### 16.2 `«NOMBRE_API»`

> Agrupa la ficha de una API: su definición, sus puntos de acceso principales y sus códigos de error.

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

## 17. Arquitectura de seguridad

> Describe cómo se protege el sistema: quién entra, qué puede hacer, cómo se cifran los datos y qué queda auditado. No se escriben contraseñas, tokens, claves privadas ni ningún otro secreto real.

### 17.1 Autenticación

> Dice cómo se comprueba que quien entra es quien dice ser.

| Campo | Valor |
| ----- | ----- |
| Mecanismo | `«MECANISMO»` |
| Proveedor de identidad | `«PROVEEDOR»` |
| Componentes involucrados | `«COMPONENTES»` |
| Estado | `<ACTUAL / PROPUESTA>` |

### 17.2 Autorización, roles y permisos

> Dice qué puede hacer cada rol y dónde se controla.

| Rol | Ámbito | Permisos | Dónde se aplica | Mecanismo de control |
| --- | ------ | -------- | --------------- | -------------------- |
| `«ROL»` | `«ÁMBITO»` | `«PERMISOS»` | `«COMPONENTE»` | `«MECANISMO»` |

### 17.3 Gestión de sesiones

> Dice cómo se abre, se mantiene y se cierra una sesión.

| Aspecto | Definición |
| ------- | ---------- |
| Mecanismo de sesión | `«MECANISMO»` |
| Duración / expiración | `«VALOR»` |
| Renovación | `«MECANISMO»` |
| Cierre de sesión | `«MECANISMO»` |

### 17.4 Protección de APIs y comunicaciones

> Dice cómo se protegen las APIs y las comunicaciones del sistema.

| Elemento | Mecanismo de protección | Alcance | Estado |
| -------- | ----------------------- | ------- | ------ |
| `«ELEMENTO»` | `«MECANISMO»` | `«ALCANCE»` | `<ACTUAL / PROPUESTA>` |

### 17.5 Cifrado y gestión de secretos

> Dice qué se cifra, con qué mecanismo y dónde se guardan las claves.

| Elemento | Estado del dato | Mecanismo de cifrado | Gestión de claves / secretos | Responsable |
| -------- | --------------- | -------------------- | ---------------------------- | ----------- |
| `«ELEMENTO»` | `<En tránsito / En reposo>` | `«MECANISMO»` | `«GESTOR_O_MEDIO»` | `«RESPONSABLE»` |

### 17.6 Seguridad de datos

> Lista los datos sensibles, su clasificación, cómo se protegen y qué norma aplica.

| Dato sensible | Clasificación | Protección aplicada | Normativa aplicable |
| ------------- | ------------- | ------------------- | ------------------- |
| `«DATO»` | `«CLASIFICACIÓN»` | `«PROTECCIÓN»` | `«NORMATIVA»` |

### 17.7 Auditoría, trazabilidad y gestión de accesos

> Dice qué eventos quedan registrados para auditar, cuánto se conservan y cómo se consultan.

| Evento auditado | Componente | Información registrada | Retención | Consulta |
| --------------- | ---------- | ---------------------- | --------- | -------- |
| `«EVENTO»` | `«COMPONENTE»` | `«INFORMACIÓN»` | `«RETENCIÓN»` | `«MECANISMO»` |

## 18. Arquitectura de despliegue

> Describe dónde y cómo se instala el sistema para que funcione.

**Descripción general del despliegue:** `«DESCRIPCIÓN»`

### 18.1 Nodos de despliegue

> Lista las máquinas, contenedores o servicios donde se ejecutan los componentes.

| Nodo | Tipo | Componentes desplegados | Ubicación | Recursos asignados | Estado |
| ---- | ---- | ----------------------- | --------- | ------------------ | ------ |
| `«NODO»` | `<Servidor físico / Máquina virtual / Contenedor / Servicio gestionado / Función>` | `«COMPONENTES»` | `«UBICACIÓN»` | `«RECURSOS»` | `<ACTUAL / PROPUESTA>` |

### 18.2 Red, balanceadores y proxies

> Lista las redes, balanceadores, proxies y cortafuegos por los que pasa el tráfico.

| Elemento | Tipo | Propósito | Componentes que atiende | Configuración relevante |
| -------- | ---- | --------- | ----------------------- | ----------------------- |
| `«ELEMENTO»` | `<Red / Balanceador / Proxy / Firewall>` | `«PROPÓSITO»` | `«COMPONENTES»` | `«CONFIGURACIÓN»` |

### 18.3 Almacenamiento y bases de datos en despliegue

> Dice dónde quedan el almacenamiento y las bases de datos, y cómo se mantienen disponibles y respaldados.

| Recurso | Tipo | Ubicación | Alta disponibilidad | Respaldo |
| ------- | ---- | --------- | ------------------- | -------- |
| `«RECURSO»` | `«TIPO»` | `«UBICACIÓN»` | `<Sí / No — MECANISMO>` | `«MECANISMO»` |

### 18.4 Proceso de despliegue

> Dice cómo se lleva una versión a producción y cómo se revierte.

| Aspecto | Definición |
| ------- | ---------- |
| Estrategia de despliegue | `«ESTRATEGIA»` |
| Automatización | `«MECANISMO»` |
| Artefactos desplegados | `«ARTEFACTOS»` |
| Reversión | `«MECANISMO»` |
| Referencia al manual de instalación | `«DOCUMENTO»` |

### 18.5 Diagrama de despliegue

> Es el dibujo del despliegue.

`«INSERTAR_DIAGRAMA_DE_DESPLIEGUE»`

## 19. Ambientes

> Lista los ambientes donde corre el sistema, con sus componentes, su infraestructura y su acceso.

| Ambiente | Componentes | Infraestructura | URL / Acceso | Observaciones |
| -------- | ----------- | --------------- | ------------ | ------------- |
| `«AMBIENTE»` | `«COMPONENTES»` | `«INFRAESTRUCTURA»` | `«URL_O_ACCESO»` | `«OBSERVACIONES»` |

### 19.1 Diferencias arquitectónicas entre ambientes

> Dice en qué se diferencia la arquitectura de un ambiente a otro, y por qué.

| Aspecto | `«AMBIENTE_1»` | `«AMBIENTE_2»` | Motivo de la diferencia |
| ------- | -------------- | -------------- | ----------------------- |
| `«ASPECTO»` | `«VALOR»` | `«VALOR»` | `«MOTIVO»` |

## 20. Infraestructura

> Describe los recursos físicos y los servicios de base sobre los que corre el sistema.

### 20.1 Recursos por nodo

> Dice con qué recursos cuenta cada nodo.

| Nodo | CPU | Memoria | Disco | Red | Sistema operativo | Observaciones |
| ---- | --- | ------- | ----- | --- | ----------------- | ------------- |
| `«NODO»` | `«CPU»` | `«MEMORIA»` | `«DISCO»` | `«RED»` | `«SISTEMA_OPERATIVO»` | `«OBSERVACIONES»` |

### 20.2 Servicios de infraestructura

> Lista los servicios de infraestructura que usa el sistema y quién los provee.

| Servicio | Propósito | Proveedor / origen | Componentes que lo usan | Estado |
| -------- | --------- | ------------------ | ----------------------- | ------ |
| `«SERVICIO»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `«COMPONENTES»` | `<ACTUAL / PROPUESTA>` |

### 20.3 Puertos

> Lista los puertos abiertos, qué componente los usa y desde dónde se permite el acceso.

| Puerto | Protocolo | Componente | Exposición | Origen permitido | Propósito |
| ------ | --------- | ---------- | ---------- | ---------------- | --------- |
| `«PUERTO»` | `«PROTOCOLO»` | `«COMPONENTE»` | `<Interna / Externa>` | `«ORIGEN»` | `«PROPÓSITO»` |

### 20.4 Dependencias externas de infraestructura

> Lista la infraestructura externa de la que depende el sistema y qué tan crítica es.

| Dependencia | Propósito | Proveedor | Criticidad | Responsable |
| ----------- | --------- | --------- | ---------- | ----------- |
| `«DEPENDENCIA»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `<Alta / Media / Baja>` | `«RESPONSABLE»` |

## 21. Comunicación entre componentes

> Dice cómo se habla cada componente con los demás: tipo, protocolo, puerto y formato.

| Origen | Destino | Tipo | Protocolo | Puerto | Formato | Canal / mecanismo | Observaciones |
| ------ | ------- | ---- | --------- | ------ | ------- | ----------------- | ------------- |
| `«COMPONENTE»` | `«COMPONENTE»` | `<Síncrona / Asíncrona>` | `«PROTOCOLO»` | `«PUERTO»` | `«FORMATO»` | `«MECANISMO»` | `«OBSERVACIONES»` |

### 21.1 Mensajería y eventos

> Lista los eventos y mensajes que se intercambian de forma asíncrona, quién los produce y quién los consume. Si el sistema no usa comunicación asíncrona, la sección se borra sin renumerar las demás.

| Evento / mensaje | Productor | Consumidores | Canal / tópico | Garantía de entrega | Manejo de fallos |
| ---------------- | --------- | ------------ | -------------- | ------------------- | ---------------- |
| `«EVENTO»` | `«COMPONENTE»` | `«COMPONENTES»` | `«CANAL»` | `«GARANTÍA»` | `«MANEJO»` |

### 21.2 Diagrama de comunicación

> Es el dibujo de la comunicación entre componentes.

`«INSERTAR_DIAGRAMA_DE_COMUNICACIÓN»`

## 22. Disponibilidad y tolerancia a fallos

> Dice qué mecanismos mantienen el sistema funcionando cuando algo falla.

| Mecanismo | Componente | Descripción | Estado |
| --------- | ---------- | ----------- | ------ |
| `<Redundancia / Replicación / Balanceo / Reintentos / Timeouts / Circuit breaker / Failover / Backup / Otro>` | `«COMPONENTE»` | `«DESCRIPCIÓN»` | `<ACTUAL / PROPUESTA / EN CONSTRUCCIÓN>` |

### 22.1 Puntos únicos de falla identificados

> Lista los componentes cuya falla detiene el sistema, con su mitigación actual y la propuesta.

| Componente | Impacto si falla | Mitigación existente | Mitigación propuesta |
| ---------- | ---------------- | -------------------- | -------------------- |
| `«COMPONENTE»` | `«IMPACTO»` | `«MITIGACIÓN_ACTUAL»` | `«MITIGACIÓN_PROPUESTA»` |

### 22.2 Objetivos de disponibilidad

> Dice cuánta disponibilidad se le exige al sistema y cómo se mide.

| Indicador | Valor definido | Ambiente | Cómo se mide |
| --------- | -------------- | -------- | ------------ |
| `«INDICADOR»` | `«VALOR»` | `«AMBIENTE»` | `«MEDICIÓN»` |

## 23. Escalabilidad y rendimiento

> Dice cómo responde el sistema cuando crece la carga.

### 23.1 Estrategias de escalabilidad

> Dice cómo escala cada componente y dónde está su límite.

| Componente | Tipo de escalabilidad | Mecanismo | Límite conocido | Estado |
| ---------- | --------------------- | --------- | --------------- | ------ |
| `«COMPONENTE»` | `<Vertical / Horizontal / No escalable>` | `«MECANISMO»` | `«LÍMITE»` | `<ACTUAL / PROPUESTA>` |

### 23.2 Carga esperada

> Dice cuánta carga se espera y de dónde sale cada dato. No se inventan métricas: cuando el valor no está definido, se deja su `«…»`.

| Indicador | Valor | Origen del dato | Ambiente |
| --------- | ----- | --------------- | -------- |
| `«INDICADOR»` | `«VALOR»` | `«ORIGEN»` | `«AMBIENTE»` |

### 23.3 Procesamiento intensivo, caché y colas

> Lista los procesos pesados, las cachés y las colas que afectan el rendimiento.

| Elemento | Propósito | Componente | Efecto en el rendimiento | Estado |
| -------- | --------- | ---------- | ------------------------ | ------ |
| `«ELEMENTO»` | `«PROPÓSITO»` | `«COMPONENTE»` | `«EFECTO»` | `<ACTUAL / PROPUESTA>` |

### 23.4 Estrategias de crecimiento

> Dice cómo se prepara el sistema para crecer.

`«DESCRIPCIÓN_DE_LA_ESTRATEGIA»`

## 24. Observabilidad y monitoreo

> Dice cómo se sabe qué está pasando dentro del sistema: registros, métricas, trazas y alertas.

| Mecanismo | Propósito | Componente | Retención | Responsable |
| --------- | --------- | ---------- | --------- | ----------- |
| `<Logs / Métricas / Trazas / Alertas / Monitoreo / Auditoría / Health check>` | `«PROPÓSITO»` | `«COMPONENTE»` | `«RETENCIÓN»` | `«RESPONSABLE»` |

### 24.1 Alertas definidas

> Lista las alertas, qué las dispara, a quién le llegan y qué se espera que haga.

| Alerta | Condición | Severidad | Destinatario | Acción esperada |
| ------ | --------- | --------- | ------------ | --------------- |
| `«ALERTA»` | `«CONDICIÓN»` | `«SEVERIDAD»` | `«DESTINATARIO»` | `«ACCIÓN»` |

### 24.2 Health checks

> Lista los puntos que comprueban que cada componente está vivo, y qué responden.

| Componente | Punto de verificación | Frecuencia | Respuesta esperada |
| ---------- | --------------------- | ---------- | ------------------ |
| `«COMPONENTE»` | `«ENDPOINT_O_MECANISMO»` | `«FRECUENCIA»` | `«RESPUESTA»` |

## 25. Gestión de errores

> Dice cómo se detecta, se trata, se registra y se notifica cada tipo de error.

| Tipo de error | Dónde se origina | Detección | Tratamiento | Registro | Notificación |
| ------------- | ---------------- | --------- | ----------- | -------- | ------------ |
| `<Validación / Excepción / Integración / Persistencia / Infraestructura>` | `«COMPONENTE»` | `«MECANISMO»` | `«TRATAMIENTO»` | `«DÓNDE_SE_REGISTRA»` | `«MECANISMO»` |

### 25.1 Políticas de reintento y recuperación

> Dice cuántas veces se reintenta cada operación, cuánto se espera y qué pasa al agotar los intentos.

| Operación | Política de reintento | Timeout | Acción tras agotar reintentos | Recuperación |
| --------- | --------------------- | ------- | ----------------------------- | ------------ |
| `«OPERACIÓN»` | `«POLÍTICA»` | `«TIMEOUT»` | `«ACCIÓN»` | `«MECANISMO»` |

## 26. Respaldo y recuperación

> Dice qué se respalda, cada cuánto y dónde, y cómo se recupera el sistema.

| Elemento | Tipo de respaldo | Frecuencia | Retención | Ubicación | Responsable |
| -------- | ---------------- | ---------- | --------- | --------- | ----------- |
| `«ELEMENTO»` | `<Completo / Incremental / Diferencial>` | `«FRECUENCIA»` | `«RETENCIÓN»` | `«UBICACIÓN»` | `«RESPONSABLE»` |

### 26.1 Procedimiento de recuperación

> Dice qué se hace para recuperar el sistema en cada escenario de falla.

| Escenario | Procedimiento | Tiempo estimado | Responsable | Documento de referencia |
| --------- | ------------- | --------------- | ----------- | ----------------------- |
| `«ESCENARIO»` | `«PROCEDIMIENTO»` | `«TIEMPO»` | `«RESPONSABLE»` | `«DOCUMENTO»` |

### 26.2 Objetivos de recuperación

> Fija cuántos datos se pueden perder (RPO) y cuánto tiempo puede estar caído el sistema (RTO).

| Indicador | Valor definido | Alcance | Observaciones |
| --------- | -------------- | ------- | ------------- |
| RPO | `«VALOR»` | `«ALCANCE»` | `«OBSERVACIONES»` |
| RTO | `«VALOR»` | `«ALCANCE»` | `«OBSERVACIONES»` |

### 26.3 Pruebas de restauración

> Registra las restauraciones probadas y su resultado.

| Prueba | Frecuencia | Última ejecución | Resultado | Responsable |
| ------ | ---------- | ---------------- | --------- | ----------- |
| `«PRUEBA»` | `«FRECUENCIA»` | `«FECHA»` | `«RESULTADO»` | `«RESPONSABLE»` |

## 27. Tecnologías utilizadas

> Lista las tecnologías que usa cada componente, con su versión. No se inventan versiones: cuando no se conoce, se mantiene `«VERSION»`.

| Componente | Tecnología | Versión | Propósito |
| ---------- | ---------- | ------- | --------- |
| `«COMPONENTE»` | `«TECNOLOGIA»` | `«VERSION»` | `«PROPÓSITO»` |

## 28. Dependencias

> Lista aquello de lo que el sistema depende y no controla.

### 28.1 Dependencias de software

> Lista las bibliotecas y paquetes que usa el sistema, con su versión y su licencia.

| Dependencia | Versión | Componente que la usa | Criticidad | Licencia | Observaciones |
| ----------- | ------- | --------------------- | ---------- | -------- | ------------- |
| `«DEPENDENCIA»` | `«VERSION»` | `«COMPONENTE»` | `<Alta / Media / Baja>` | `«LICENCIA»` | `«OBSERVACIONES»` |

### 28.2 Dependencias de infraestructura

> Lista la infraestructura de la que depende cada componente.

| Dependencia | Propósito | Componente afectado | Criticidad | Responsable |
| ----------- | --------- | ------------------- | ---------- | ----------- |
| `«DEPENDENCIA»` | `«PROPÓSITO»` | `«COMPONENTE»` | `<Alta / Media / Baja>` | `«RESPONSABLE»` |

### 28.3 Dependencias de servicios externos

> Lista los servicios externos que usa el sistema, qué disponibilidad comprometen y qué se hace si fallan.

| Servicio | Propósito | Proveedor | Disponibilidad comprometida | Plan de contingencia |
| -------- | --------- | --------- | --------------------------- | -------------------- |
| `«SERVICIO»` | `«PROPÓSITO»` | `«PROVEEDOR»` | `«COMPROMISO»` | `«CONTINGENCIA»` |

### 28.4 Dependencias de terceros

> Lista a los terceros de los que depende el sistema y qué pasa si no están disponibles.

| Tercero | Elemento del que depende el sistema | Impacto si no está disponible | Responsable del relacionamiento |
| ------- | ----------------------------------- | ----------------------------- | ------------------------------- |
| `«TERCERO»` | `«ELEMENTO»` | `«IMPACTO»` | `«RESPONSABLE»` |

## 29. Decisiones arquitectónicas

> Registra las decisiones de arquitectura con su contexto, sus opciones y su justificación.

### 29.1 Índice de decisiones

> Lista todas las decisiones con su estado y los componentes que afectan.

| ID | Título | Fecha | Estado | Componentes afectados |
| -- | ------ | ----- | ------ | --------------------- |
| ADR-`«XXX»` | `«TÍTULO»` | `«FECHA»` | `<PROPUESTA / ACEPTADA / RECHAZADA / OBSOLETA>` | `«COMPONENTES»` |

### 29.2 ADR-`«XXX»` · `«TÍTULO»`

> Agrupa la ficha de una decisión: el problema, las opciones consideradas, la decisión y sus consecuencias.

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

**Fecha:** `«FECHA»`

**Responsable:** `«RESPONSABLE»`

### 29.3 ADR-`«XXX»` · `«TÍTULO»`

> Agrupa la ficha de la decisión siguiente.

`«REPETIR_FICHA»`

## 30. Restricciones arquitectónicas

> Lista los límites que la arquitectura no puede mover, de dónde vienen y si se pueden negociar.

| # | Restricción | Tipo | Origen | Impacto en la arquitectura | Negociable |
| - | ----------- | ---- | ------ | -------------------------- | ---------- |
| 1 | `«RESTRICCIÓN»` | `<Tecnológica / Legada / Institucional / Infraestructura / Presupuestal / Compatibilidad / Regulatoria / Externa>` | `«ORIGEN»` | `«IMPACTO»` | `<Sí / No>` |

## 31. Riesgos arquitectónicos

> Registra lo que puede afectar a la arquitectura, qué tan probable es y cómo se mitiga.

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
| -- | ------ | ------------ | ------- | ---------- | ------ |
| `«ID»` | `«RIESGO»` | `<Alta / Media / Baja>` | `<Alto / Medio / Bajo>` | `«MITIGACIÓN»` | `<Identificado / En mitigación / Mitigado / Aceptado>` |

## 32. Deuda técnica

> Registra lo que quedó resuelto de forma provisional y qué se propone para corregirlo.

| ID | Descripción | Impacto | Prioridad | Acción propuesta |
| -- | ----------- | ------- | --------- | ---------------- |
| `«ID»` | `«DESCRIPCIÓN»` | `«IMPACTO»` | `<Alta / Media / Baja>` | `«ACCIÓN»` |

## 33. Estado actual y arquitectura objetivo

> Separa lo que existe hoy de lo que se quiere llegar a tener. Ningún componente futuro se presenta como si ya existiera.

### 33.1 Arquitectura actual

> Describe lo que existe hoy.

`«DESCRIPCIÓN_DE_LO_QUE_EXISTE_HOY»`

| Componente | Estado | Observaciones |
| ---------- | ------ | ------------- |
| `«COMPONENTE»` | `<ACTUAL / OBSOLETA>` | `«OBSERVACIONES»` |

### 33.2 Arquitectura objetivo

> Describe el estado al que se quiere llegar.

`«DESCRIPCIÓN_DEL_ESTADO_DESEADO»`

| Componente | Estado | Justificación |
| ---------- | ------ | ------------- |
| `«COMPONENTE»` | `<PROPUESTA / EN CONSTRUCCIÓN / PENDIENTE>` | `«JUSTIFICACIÓN»` |

### 33.3 Brechas

> Lista lo que falta para pasar de la arquitectura actual a la objetivo.

| # | Brecha | Situación actual | Situación objetivo | Acción requerida | Prioridad |
| - | ------ | ---------------- | ------------------ | ---------------- | --------- |
| 1 | `«BRECHA»` | `«ACTUAL»` | `«OBJETIVO»` | `«ACCIÓN»` | `<Alta / Media / Baja>` |

## 34. Matriz de trazabilidad arquitectónica

> Une cada requisito con el componente y la solución que lo cumplen, y con su evidencia.

| Requisito | Componente | Solución | Evidencia |
| --------- | ---------- | -------- | --------- |
| `«ID_REQUISITO»` | `«COMPONENTE»` | `«SOLUCIÓN_ARQUITECTÓNICA»` | `«EVIDENCIA_O_REFERENCIA»` |

### 34.1 Trazabilidad requisito → decisión

> Une cada requisito con la decisión de arquitectura que lo atiende.

| Requisito | Decisión relacionada | Componente afectado | Infraestructura |
| --------- | -------------------- | ------------------- | --------------- |
| `«ID_REQUISITO»` | ADR-`«XXX»` | `«COMPONENTE»` | `«INFRAESTRUCTURA»` |

## 35. Diagramas

> Es el inventario de los diagramas del documento, con la ficha que lleva cada uno. Solo se incluyen los que aportan valor, y cada uno queda registrado acá.

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

## 36. Recomendaciones y evolución futura

> Recoge lo que se recomienda hacer después. Nada de esta sección se presenta como funcionalidad existente.

### 36.1 Mejoras recomendadas

> Lista las mejoras recomendadas, por qué y con qué prioridad.

| # | Mejora | Justificación | Impacto esperado | Prioridad | Estado |
| - | ------ | ------------- | ---------------- | --------- | ------ |
| 1 | `«MEJORA»` | `«JUSTIFICACIÓN»` | `«IMPACTO»` | `<Alta / Media / Baja>` | `«PROPUESTA»` |

### 36.2 Evoluciones futuras

> Lista cómo puede evolucionar el sistema y qué tendría que pasar antes.

| # | Evolución | Descripción | Precondiciones | Horizonte | Estado |
| - | --------- | ----------- | -------------- | --------- | ------ |
| 1 | `«EVOLUCIÓN»` | `«DESCRIPCIÓN»` | `«PRECONDICIONES»` | `«HORIZONTE»` | `<PROPUESTA / PENDIENTE>` |

### 36.3 Componentes potenciales

> Lista los componentes que podrían sumarse y bajo qué condición.

| Componente | Propósito | Condición para incorporarlo | Estado |
| ---------- | --------- | --------------------------- | ------ |
| `«COMPONENTE»` | `«PROPÓSITO»` | `«CONDICIÓN»` | `<PROPUESTA / PENDIENTE>` |

### 36.4 Riesgos pendientes

> Lista los riesgos que siguen abiertos y quién los atiende.

| Riesgo | Estado | Acción pendiente | Responsable |
| ------ | ------ | ---------------- | ----------- |
| `«RIESGO»` | `«PENDIENTE»` | `«ACCIÓN»` | `«RESPONSABLE»` |

## 37. Checklist de arquitectura

> Es la lista de lo que el documento debe cubrir antes de aprobarse, con quién lo verificó.

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

## Anexo A. Convenciones de documentación

> Fija las convenciones con que se escribe todo el documento.

### A.1 Estados de la información

> Define los estados con que se clasifica cada elemento.

| Estado | Significado |
| ------ | ----------- |
| **Actual** | Existe y está implementada. |
| **Propuesta** | Se plantea como solución futura. |
| **En construcción** | Está siendo implementada. |
| **Obsoleta** | Existió pero ya no forma parte de la solución. |
| **Pendiente** | Requiere definición. |

No mezclar estados dentro de una misma descripción: cada componente, integración, mecanismo o decisión debe llevar su estado explícito.

### A.2 Reglas de calidad

> Lista las reglas que cumple todo el contenido del documento.

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

> Son las preguntas que el documento completo responde, en orden.

1. ¿Qué sistema tenemos?
2. ¿Qué componentes lo conforman?
3. ¿Qué responsabilidad tiene cada uno?
4. ¿Cómo se comunican?
5. ¿Dónde se ejecutan?
6. ¿Dónde están los datos?
7. ¿Cómo se protege?
8. ¿Cómo se despliega?
9. ¿Qué decisiones arquitectónicas se tomaron y por qué?
10. ¿Cómo puede evolucionar?

## Anexo B. Instrucciones de uso de la plantilla

> Dice cómo se llena esta plantilla.

1. Llenar la sección 1 antes que cualquier otra.
2. Borrar las secciones y subsecciones que no apliquen, sin renumerar las que quedan.
3. Duplicar las fichas repetibles (componentes, flujos, integraciones, interfaces, decisiones) según lo que el proyecto tenga.
4. Asignar un estado del anexo A a todo componente, integración, mecanismo y decisión.
5. Anotar cada diagrama en el inventario de la sección 35, con su nombre, su objetivo, su notación y su versión.
6. Numerar las decisiones de arquitectura de corrido, sin reutilizar un identificador aunque la decisión cambie.
7. Mantener la sección 33 al día cuando la arquitectura cambie.
8. Antes de aprobar, no queda ningún `«…»` sin llenar. El que no se pueda llenar todavía se deja diciendo que está pendiente, con quién lo decide: un hueco callado se lee como un olvido.

### Placeholders estándar

> Dice qué significa cada marcador que usa la plantilla.

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
