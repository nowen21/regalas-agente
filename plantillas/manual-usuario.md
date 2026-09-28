# Manual de Usuario · `«NOMBRE_SISTEMA»`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> **Cómo se escribe lo que se llena.** En la variedad del idioma que usa el proyecto, en tercera persona para lo que se explica y en infinitivo para lo que el lector hace. La regla es [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), y se cita en vez de repetirla: lo que se copia a mano se copia distinto (`S-090`). Los espacios por llenar van marcados `«…»`, que es la marca de todos los modelos ([`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).

> **Modelo reutilizable.** Reemplazar cada `«…»` con lo que el sistema hace de verdad, y borrar las secciones que no apliquen conservando la numeración de las que quedan. Las notas como esta se borran al llenarlo. Acá no va código, ni instalación, ni configuración: eso vive en el [modelo de manual de instalación](manual-instalacion.md).

## 1. Información general del documento

> Identifica el documento y el sistema que describe: versiones, fechas, responsable, estado y a quién va dirigido.

| Campo | Valor |
| ----- | ----- |
| Nombre del sistema | `«NOMBRE_SISTEMA»` |
| Código o identificador | `«CODIGO_SISTEMA»` |
| Versión del sistema | `«VERSION_SISTEMA»` |
| Versión del manual | `«VERSION_MANUAL»` |
| Fecha de elaboración | `«FECHA_ELABORACION»` |
| Fecha de actualización | `«FECHA_ACTUALIZACION»` |
| Responsable | `«RESPONSABLE»` |
| Estado del documento | `<BORRADOR / EN REVISIÓN / APROBADO / OBSOLETO>` |
| Dirigido a | `«PERFILES_DESTINATARIOS»` |

## 2. Introducción

> Presenta el sistema a quien lo abre por primera vez, antes de entrar en pantallas y pasos.

**¿Qué es el sistema?**
`«DESCRIPCIÓN_FUNCIONAL_DEL_SISTEMA»`

**¿Para qué sirve?**
`«UTILIDAD_PRINCIPAL»`

**¿Qué necesidad o proceso resuelve?**
`«NECESIDAD_O_PROCESO»`

**¿Quiénes lo utilizan?**
`«USUARIOS_PRINCIPALES»`

**¿Qué procesos pueden realizarse en el sistema?**

- `«PROCESO_1»`
- `«PROCESO_2»`
- `«PROCESO_N»`

## 3. Objetivo del manual

> Dice para qué se escribió el manual, medido en lo que el lector sabe hacer al terminarlo.

**Objetivo:** `«OBJETIVO_DEL_MANUAL»`

**Al finalizar la lectura, el usuario podrá:**

- `«CAPACIDAD_1»`
- `«CAPACIDAD_2»`
- `«CAPACIDAD_N»`

## 4. Alcance

> Delimita qué cubre el manual y qué no, para que el lector sepa dónde buscar lo que falta.

### 4.1 Incluido en este manual

> Los módulos y las funcionalidades que el manual explica, uno por fila.

| Elemento | Descripción |
| -------- | ----------- |
| `«MÓDULO_O_FUNCIONALIDAD»` | `«DESCRIPCIÓN»` |

### 4.2 Tipos de usuario contemplados

> Los perfiles de usuario para los que está escrito el manual.

| Tipo de usuario | Descripción |
| --------------- | ----------- |
| `«TIPO_USUARIO»` | `«DESCRIPCIÓN»` |

### 4.3 Fuera del alcance

> Lo que el manual no explica, con el motivo y el documento donde sí está. Si no queda nada fuera, se escribe «Ninguno».

| Elemento | Motivo | Documento de referencia |
| -------- | ------ | ----------------------- |
| `«ELEMENTO_EXCLUIDO»` | `«MOTIVO»` | `«DOCUMENTO»` |

## 5. Conceptos básicos

> Explica las palabras que el lector necesita entender antes de usar el sistema.

### 5.1 Conceptos del negocio

> Los términos propios del negocio que aparecen en pantallas y reportes.

| Concepto | Explicación | Dónde se utiliza en el sistema |
| -------- | ----------- | ------------------------------ |
| `«CONCEPTO»` | `«EXPLICACIÓN»` | `«MÓDULO_O_PANTALLA»` |

### 5.2 Estados de los registros

> Los estados por los que pasa un registro, qué se puede hacer en cada uno y a cuál pasa después.

| Estado | Significado | Acciones permitidas | Estado siguiente |
| ------ | ----------- | ------------------- | ---------------- |
| `«ESTADO»` | `«SIGNIFICADO»` | `«ACCIONES»` | `«ESTADO_SIGUIENTE»` |

### 5.3 Tipos de documentos o registros

> Las clases de documento o registro que maneja el sistema.

| Tipo | Descripción | Módulo asociado |
| ---- | ----------- | --------------- |
| `«TIPO»` | `«DESCRIPCIÓN»` | `«MÓDULO»` |

### 5.4 Botones y acciones especiales

> Los botones e íconos cuyo sentido no se deduce a simple vista.

| Botón o ícono | Nombre | Qué hace | Dónde aparece |
| ------------- | ------ | -------- | ------------- |
| `«ÍCONO_O_BOTÓN»` | `«NOMBRE»` | `«ACCIÓN»` | `«UBICACIÓN»` |

## 6. Requisitos para utilizar el sistema

> Lo que el lector debe tener antes de entrar al sistema, y a quién se lo pide.

| Requisito | Detalle | Obligatorio | Cómo obtenerlo |
| --------- | ------- | ----------- | -------------- |
| Acceso al sistema | `«DETALLE»` | `<Sí / No>` | `«RESPONSABLE_O_PROCEDIMIENTO»` |
| Usuario y contraseña | `«DETALLE»` | `<Sí / No>` | `«RESPONSABLE_O_PROCEDIMIENTO»` |
| Navegador soportado | `«NAVEGADOR_Y_VERSION»` | `<Sí / No>` | `«PROCEDIMIENTO»` |
| Conexión requerida | `<INTERNET / RED_INSTITUCIONAL / VPN>` | `<Sí / No>` | `«PROCEDIMIENTO»` |
| Permisos o rol asignado | `«PERMISO_O_ROL»` | `<Sí / No>` | `«RESPONSABLE»` |
| `«OTRO_REQUISITO»` | `«DETALLE»` | `<Sí / No>` | `«PROCEDIMIENTO»` |

**Recomendaciones adicionales:** `«RECOMENDACIONES»`

## 7. Acceso al sistema

> Cómo entra y cómo sale el lector del sistema.

### 7.1 Punto de acceso

> Dónde está el sistema y desde qué red se alcanza.

| Campo | Valor |
| ----- | ----- |
| Dirección del sistema | `«URL_SISTEMA»` |
| Ambiente | `«AMBIENTE»` |
| Requiere red específica | `<Sí / No — DETALLE>` |

### 7.2 Inicio de sesión

> El procedimiento de ingreso, con lo que se ve cuando sale bien y cuando falla.

**Objetivo:** ingresar al sistema con las credenciales asignadas.

**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. Ingresar a `«URL_SISTEMA»`.
2. Diligenciar el campo `«CAMPO_USUARIO»`.
3. Diligenciar el campo `«CAMPO_CONTRASEÑA»`.
4. `«PASO_ADICIONAL_SI_APLICA»`
5. Seleccionar la opción `«BOTON_INGRESAR»`.

**Resultado esperado (credenciales correctas):** `«RESULTADO_ESPERADO»`

**Resultado cuando las credenciales son incorrectas:** `«MENSAJE_Y_COMPORTAMIENTO»`

| Situación | Mensaje mostrado | Qué debe hacer el usuario |
| --------- | ---------------- | ------------------------- |
| `«SITUACIÓN»` | `«MENSAJE»` | `«ACCIÓN»` |

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

### 7.3 Recuperación de contraseña

> Los pasos para recuperar una contraseña olvidada. La subsección se incluye solo si el sistema ofrece esa opción.

**Acceso:** `«UBICACIÓN_DE_LA_OPCIÓN»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`
3. `«PASO_N»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Consideraciones:** `«CONSIDERACIONES»`

### 7.4 Cierre de sesión

> Los pasos para salir del sistema sin dejar la sesión abierta.

**Acceso:** `«UBICACIÓN_DE_LA_OPCIÓN»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

## 8. Interfaz principal

> Describe la pantalla que se ve al entrar, elemento por elemento, y quién ve cada uno.

**Captura general de la interfaz:** `«INSERTAR_CAPTURA»`

| # | Elemento | Ubicación en pantalla | Descripción | Disponible para |
| - | -------- | --------------------- | ----------- | --------------- |
| 1 | Encabezado | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 2 | Menú principal | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 3 | Menú lateral | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 4 | Área de trabajo | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 5 | Panel de usuario | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 6 | Notificaciones | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 7 | Botones principales | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 8 | Indicadores | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 9 | Buscador | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 10 | Filtros | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |
| 11 | Acciones rápidas | `«UBICACIÓN»` | `«DESCRIPCIÓN»` | `«ROL»` |

### 8.1 Navegación general

> Cómo se mueve el lector entre pantallas y módulos.

| Acción | Cómo se realiza | Resultado |
| ------ | --------------- | --------- |
| `«ACCIÓN»` | `«PROCEDIMIENTO»` | `«RESULTADO»` |

## 9. Roles y permisos

> Los roles que existen en el sistema y qué puede hacer cada uno.

| Rol | Descripción | Módulos disponibles | Principales acciones |
| --- | ----------- | ------------------- | -------------------- |
| `«ROL_ADMINISTRADOR»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |
| `«ROL_USUARIO»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |
| `«ROL_CONSULTA»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |

### 9.1 Matriz de permisos por funcionalidad

> Cruza cada funcionalidad con cada rol para ver quién la tiene. Cuando una funcionalidad se comporta distinto según el rol, la diferencia se explica en la sección de su módulo.

| Funcionalidad | `«ROL_1»` | `«ROL_2»` | `«ROL_3»` |
| ------------- | --------- | --------- | --------- |
| `«FUNCIONALIDAD»` | `<Sí / No>` | `<Sí / No>` | `<Sí / No>` |

## 10. Módulos del sistema

> Documenta cada módulo del sistema en una subsección `10.X` con la misma estructura. Se duplica por cada módulo, y se borran las subsecciones que no apliquen sin renumerar las demás.

### 10.1 `«NOMBRE_DEL_MÓDULO»`

> Agrupa todo lo que el lector hace dentro de un módulo.

#### 10.1.1 Objetivo del módulo

`«PARA_QUÉ_SIRVE_EL_MÓDULO»`

**Roles con acceso:** `«ROLES»`

#### 10.1.2 Acceso al módulo

**Ruta de navegación:** `«MENÚ» → «OPCIÓN» → «SUBOPCIÓN»`

**Precondiciones:** `«PRECONDICIONES»`

#### 10.1.3 Pantalla principal

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

| # | Elemento | Descripción | Acción que permite |
| - | -------- | ----------- | ------------------ |
| 1 | `<Tabla / Formulario / Botón / Filtro / Buscador / Paginación / Indicador>` | `«DESCRIPCIÓN»` | `«ACCIÓN»` |

**Columnas de la tabla (si aplica)**

| Columna | Descripción | Observaciones |
| ------- | ----------- | ------------- |
| `«COLUMNA»` | `«DESCRIPCIÓN»` | `«OBSERVACIONES»` |

#### 10.1.4 Consultar información

**Objetivo:** `«OBJETIVO»`

**Acceso:** `«UBICACIÓN»`

**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`
3. `«PASO_N»`

**Filtros disponibles**

| Filtro | Descripción | Valores posibles | Obligatorio |
| ------ | ----------- | ---------------- | ----------- |
| `«FILTRO»` | `«DESCRIPCIÓN»` | `«VALORES»` | `<Sí / No>` |

**Cómo interpretar los resultados:** `«EXPLICACIÓN»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

#### 10.1.5 Crear un registro

**Objetivo:** `«OBJETIVO»`

**Acceso:** `«UBICACIÓN_DE_LA_OPCIÓN»`

**Precondiciones:** `«PRECONDICIONES»`

**Campos del formulario**

| Campo | Descripción | Obligatorio | Formato | Ejemplo | Validaciones |
| ----- | ----------- | ----------- | ------- | ------- | ------------ |
| `«CAMPO»` | `«DESCRIPCIÓN»` | `<Sí / No>` | `«FORMATO»` | `«EJEMPLO»` | `«VALIDACIÓN»` |

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`
3. Seleccionar `«BOTON_GUARDAR»`.

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Errores frecuentes y solución**

| Situación | Causa probable | Qué debe hacer el usuario |
| --------- | -------------- | ------------------------- |
| `«SITUACIÓN»` | `«CAUSA»` | `«ACCIÓN»` |

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

#### 10.1.6 Consultar un registro

**Objetivo:** `«OBJETIVO»`

**Acceso:** `«UBICACIÓN»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_N»`

**Información visible**

| Sección / campo | Descripción |
| --------------- | ----------- |
| `«SECCIÓN_O_CAMPO»` | `«DESCRIPCIÓN»` |

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

#### 10.1.7 Editar un registro

**Objetivo:** `«OBJETIVO»`

**Acceso:** `«UBICACIÓN»`

**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. Seleccionar el registro: `«PROCEDIMIENTO_DE_SELECCIÓN»`
2. `«PASO_2»`
3. Seleccionar `«BOTON_GUARDAR»`.

**Campos modificables**

| Campo | Modificable | Condición | Observaciones |
| ----- | ----------- | --------- | ------------- |
| `«CAMPO»` | `<Sí / No>` | `«CONDICIÓN»` | `«OBSERVACIONES»` |

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Cómo verificar la actualización:** `«VERIFICACIÓN»`

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

#### 10.1.8 Eliminar o desactivar un registro

> Incluir únicamente si la funcionalidad existe en el sistema.

**Objetivo:** `«OBJETIVO»`

**Acceso:** `«UBICACIÓN»`

**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. `«PASO_1»`
2. Confirmar la acción en `«MENSAJE_O_VENTANA_DE_CONFIRMACIÓN»`.

**Consecuencias de la acción:** `«CONSECUENCIAS»`

**¿Es reversible?** `<Sí / No — DETALLE>`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

#### 10.1.9 Otras funcionalidades del módulo

> Acá van las funcionalidades propias del módulo, con la convención del anexo A.

##### `«NOMBRE_DE_LA_FUNCIONALIDAD»`

**Objetivo:** `«OBJETIVO»`
**Acceso:** `«ACCESO»`
**Precondiciones:** `«PRECONDICIONES»`
**Pasos:** `«PASOS»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`
**Validaciones:** `«VALIDACIONES»`
**Errores frecuentes:** `«ERRORES»`
**Solución:** `«SOLUCIÓN»`
**Captura de pantalla:** `«INSERTAR_CAPTURA»`

### 10.2 `«NOMBRE_DEL_MÓDULO»`

> El siguiente módulo, con la misma estructura de la 10.1.

`<REPETIR_ESTRUCTURA_10.X>`

## 11. Formularios

> Documenta los formularios que se usan desde varios módulos o con mucha frecuencia. Los propios de un módulo pueden ir en su sección.

### 11.1 `«NOMBRE_DEL_FORMULARIO»`

> Agrupa los campos y los botones de un formulario.

**Objetivo:** `«OBJETIVO»`
**Acceso:** `«UBICACIÓN»`
**Roles con acceso:** `«ROLES»`

| Campo | Descripción | Obligatorio | Formato | Ejemplo | Validaciones |
| ----- | ----------- | ----------- | ------- | ------- | ------------ |
| `«CAMPO»` | `«DESCRIPCIÓN»` | `<Sí / No>` | `«FORMATO»` | `«EJEMPLO»` | `«VALIDACIÓN»` |

**Botones y acciones disponibles**

| Botón | Acción | Resultado |
| ----- | ------ | --------- |
| `«BOTÓN»` | `«ACCIÓN»` | `«RESULTADO»` |

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

## 12. Búsquedas y filtros

> Explica cómo encontrar información en el sistema: buscar, filtrar, ordenar y pasar de página.

### 12.1 Búsqueda simple

> La búsqueda rápida por texto o por un solo criterio.

**Ubicación:** `«UBICACIÓN»`
**Qué permite buscar:** `«CAMPOS_O_CRITERIOS»`
**Pasos:** `«PASOS»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.2 Búsqueda avanzada

> La búsqueda que combina varios criterios a la vez. Se incluye solo si el sistema la ofrece.

**Ubicación:** `«UBICACIÓN»`
**Pasos:** `«PASOS»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.3 Filtros disponibles

> Todos los filtros del sistema en una tabla, con sus valores y con qué otros se combinan.

| Filtro | Módulo | Descripción | Valores posibles | Se combina con |
| ------ | ------ | ----------- | ---------------- | -------------- |
| `«FILTRO»` | `«MÓDULO»` | `«DESCRIPCIÓN»` | `«VALORES»` | `«OTROS_FILTROS»` |

### 12.4 Combinación de filtros

> Qué resultado da aplicar varios filtros juntos.

`«EXPLICACIÓN_DEL_COMPORTAMIENTO»`

### 12.5 Limpieza de filtros

> Cómo se quitan los filtros aplicados para volver a la lista completa.

**Cómo se realiza:** `«PROCEDIMIENTO»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.6 Ordenamiento

> Por qué columnas o criterios se pueden ordenar los resultados.

| Columna / criterio | Permite ordenar | Cómo se realiza |
| ------------------ | --------------- | --------------- |
| `«COLUMNA»` | `<Sí / No>` | `«PROCEDIMIENTO»` |

### 12.7 Paginación

> Cómo se reparten los resultados en páginas y cómo se pasa de una a otra.

**Cómo funciona:** `«EXPLICACIÓN»`
**Opciones disponibles:** `«OPCIONES»`

## 13. Reportes

> Documenta los reportes que genera el sistema.

### 13.1 Reportes disponibles

> La lista de todos los reportes, con quién puede generarlos y en qué formato salen.

| Reporte | Objetivo | Módulo | Roles con acceso | Formato de salida |
| ------- | -------- | ------ | ---------------- | ----------------- |
| `«NOMBRE_REPORTE»` | `«OBJETIVO»` | `«MÓDULO»` | `«ROLES»` | `«FORMATO»` |

### 13.2 `«NOMBRE_REPORTE»`

> Agrupa cómo se genera un reporte y cómo se lee. Se repite por cada reporte de la tabla 13.1.

**Objetivo:** `«OBJETIVO»`
**Acceso:** `«RUTA_DE_NAVEGACIÓN»`
**Precondiciones:** `«PRECONDICIONES»`

**Filtros disponibles**

| Filtro | Descripción | Obligatorio | Valores posibles |
| ------ | ----------- | ----------- | ---------------- |
| `«FILTRO»` | `«DESCRIPCIÓN»` | `<Sí / No>` | `«VALORES»` |

**Pasos para generarlo:**

1. `«PASO_1»`
2. `«PASO_N»`

**Cómo interpretar el reporte**

| Columna / indicador | Significado |
| ------------------- | ----------- |
| `«COLUMNA»` | `«SIGNIFICADO»` |

**Formato de salida:** `«FORMATO»`
**Opciones de descarga:** `«OPCIONES»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`
**Captura de pantalla:** `«INSERTAR_CAPTURA»`

## 14. Exportación de información

> Qué información se puede sacar del sistema en un archivo, en qué formatos y cómo. La sección se incluye solo si el sistema permite exportar.

| Información exportable | Módulo | Formatos disponibles | Filtros que se aplican | Roles con acceso |
| ---------------------- | ------ | -------------------- | ---------------------- | ---------------- |
| `«INFORMACIÓN»` | `«MÓDULO»` | `«FORMATOS»` | `«FILTROS»` | `«ROLES»` |

**Procedimiento de exportación**

1. `«PASO_1»`
2. `«PASO_2»`
3. `«PASO_N»`

**Dónde se obtiene el archivo:** `«UBICACIÓN_DEL_ARCHIVO»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`
**Consideraciones:** `«CONSIDERACIONES»`

## 15. Notificaciones y mensajes del sistema

> Explica los avisos que muestra el sistema y qué hacer con cada uno.

### 15.1 Tipos de mensaje

> Cómo se distingue a la vista cada clase de mensaje.

| Tipo | Cómo se identifica | Significado general |
| ---- | ------------------ | ------------------- |
| Éxito | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Advertencia | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Error | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Información | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Confirmación | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |

### 15.2 Mensajes del sistema

> Los mensajes concretos que el lector puede ver, con lo que significan y qué hacer.

| Mensaje | Significado | Acción recomendada |
| ------- | ----------- | ------------------ |
| `«MENSAJE»` | `«SIGNIFICADO»` | `«ACCIÓN»` |

### 15.3 Notificaciones

> Los avisos que el sistema genera por su cuenta, cuándo aparecen y dónde se consultan.

| Notificación | Cuándo se genera | Dónde se consulta | Acción del usuario |
| ------------ | ---------------- | ----------------- | ------------------ |
| `«NOTIFICACIÓN»` | `«CONDICIÓN»` | `«UBICACIÓN»` | `«ACCIÓN»` |

## 16. Validaciones y errores frecuentes

> Los problemas que más se repiten al usar el sistema, con su causa y su solución.

| Situación | Causa probable | Qué debe hacer el usuario |
| --------- | -------------- | ------------------------- |
| `«SITUACIÓN»` | `«CAUSA»` | `«ACCIÓN»` |

### 16.1 Validaciones generales del sistema

> Las reglas que el sistema comprueba en todos los formularios, con el mensaje que muestra cuando no se cumplen.

| Validación | Dónde aplica | Qué exige | Mensaje asociado |
| ---------- | ------------ | --------- | ---------------- |
| `«VALIDACIÓN»` | `«MÓDULO_O_FORMULARIO»` | `«REGLA»` | `«MENSAJE»` |

## 17. Flujos completos de operación

> Documenta, de principio a fin, los procesos que pasan por varias funcionalidades o módulos.

### 17.1 `«NOMBRE_DEL_PROCESO»`

> Agrupa los pasos de un proceso, con el rol que hace cada uno.

**Objetivo:** `«OBJETIVO»`
**Roles participantes:** `«ROLES»`
**Precondiciones:** `«PRECONDICIONES»`

| Paso | Responsable / rol | Módulo | Acción | Resultado |
| ---- | ----------------- | ------ | ------ | --------- |
| 1 | `«ROL»` | `«MÓDULO»` | `«ACCIÓN»` | `«RESULTADO»` |
| 2 | `«ROL»` | `«MÓDULO»` | `«ACCIÓN»` | `«RESULTADO»` |
| 3 | `«ROL»` | `«MÓDULO»` | `«ACCIÓN»` | `«RESULTADO»` |
| N | `«ROL»` | `«MÓDULO»` | `«ACCIÓN»` | `«RESULTADO»` |

**Resultado esperado del proceso:** `«RESULTADO_ESPERADO»`

**Diagrama del flujo:** `«INSERTAR_DIAGRAMA»`

**Consideraciones:** `«CONSIDERACIONES»`

### 17.2 `«NOMBRE_DEL_PROCESO»`

> El siguiente proceso, con la misma estructura de la 17.1.

`«REPETIR_ESTRUCTURA»`

## 18. Casos de uso frecuentes

> Las tareas más comunes del día a día, con la sección del manual que las explica.

| # | Caso de uso | Rol | Módulo | Sección de referencia |
| - | ----------- | --- | ------ | --------------------- |
| 1 | `«CASO_DE_USO»` | `«ROL»` | `«MÓDULO»` | `«SECCIÓN»` |

### 18.1 `«NOMBRE_DEL_CASO_DE_USO»`

> Agrupa la situación del usuario y los pasos para resolverla.

**Situación:** `«SITUACIÓN_DEL_USUARIO»`
**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_N»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`
**Si algo falla:** `«QUÉ_HACER»`

## 19. Preguntas frecuentes (FAQ)

> Las dudas que más se repiten, cada una como subtítulo con su respuesta debajo.

### ¿`«PREGUNTA»`?

> Agrupa una pregunta con su respuesta.

**Respuesta:** `«RESPUESTA»`

### ¿`«PREGUNTA»`?

> La siguiente pregunta, con la misma forma.

**Respuesta:** `«RESPUESTA»`

## 20. Buenas prácticas de uso

> Las recomendaciones de uso, una por ámbito.

| Ámbito | Recomendación |
| ------ | ------------- |
| Manejo de información | `«RECOMENDACIÓN»` |
| Validación de datos antes de guardar | `«RECOMENDACIÓN»` |
| Uso de filtros y búsquedas | `«RECOMENDACIÓN»` |
| Protección de credenciales | `«RECOMENDACIÓN»` |
| Cierre de sesión | `«RECOMENDACIÓN»` |
| Manejo de archivos | `«RECOMENDACIÓN»` |
| Uso de las funcionalidades | `«RECOMENDACIÓN»` |
| `«OTRO_ÁMBITO»` | `«RECOMENDACIÓN»` |

## 21. Soporte y atención de incidentes

> Dice a quién acudir cuando algo falla y qué entregarle.

### 21.1 Canales de soporte

> Por dónde se pide ayuda, en qué horario y para qué tipo de solicitud.

| Canal | Dato de contacto | Horario de atención | Tipo de solicitud |
| ----- | ---------------- | ------------------- | ----------------- |
| `«CANAL»` | `«CONTACTO»` | `«HORARIO»` | `«TIPO»` |

### 21.2 Información que debe proporcionar el usuario

> Los datos que el lector entrega al reportar un incidente, para que soporte no tenga que volver a preguntarlos.

- Nombre y usuario: `«DATO»`
- Módulo donde ocurrió: `«DATO»`
- Acción realizada antes del error: `«DATO»`
- Mensaje mostrado por el sistema: `«DATO»`
- Fecha y hora del incidente: `«DATO»`
- `«OTRA_INFORMACIÓN»`

### 21.3 Evidencias recomendadas

> Lo que conviene adjuntar al reporte.

- Captura de pantalla completa del error.
- Captura de la información ingresada (sin credenciales).
- `«OTRA_EVIDENCIA»`

### 21.4 Procedimiento de reporte

> Los pasos para reportar un incidente y el tiempo en que se espera respuesta.

1. `«PASO_1»`
2. `«PASO_N»`

**Tiempo de respuesta estimado:** `«TIEMPO»`

## 22. Glosario

> Los términos técnicos o propios del sistema que aparecen en el manual, cada uno con su definición.

| Término | Definición |
| ------- | ---------- |
| `«TÉRMINO»` | `«DEFINICIÓN»` |

## 23. Historial de cambios del manual

> Una fila por versión del manual, con qué cambió y quién lo hizo.

| Versión | Fecha | Descripción del cambio | Responsable |
| ------- | ----- | ---------------------- | ----------- |
| `«VERSION_MANUAL»` | `«FECHA»` | `«CAMBIO»` | `«RESPONSABLE»` |

## 24. Anexos

> El material de apoyo que no cabe en el cuerpo del manual.

### 24.1 Capturas adicionales

> Las capturas que ayudan pero no acompañan un paso concreto.

`«INSERTAR_CAPTURAS»`

### 24.2 Flujos y diagramas

> Los diagramas completos de los procesos de la sección 17.

`«INSERTAR_DIAGRAMAS»`

### 24.3 Tablas de referencia

> Las tablas que se consultan desde varias secciones.

| Referencia | Descripción | Ubicación |
| ---------- | ----------- | --------- |
| `«REFERENCIA»` | `«DESCRIPCIÓN»` | `«UBICACIÓN»` |

### 24.4 Catálogos

> Las listas de valores fijos que el sistema ofrece para elegir.

| Catálogo | Valores | Dónde se utiliza |
| -------- | ------- | ---------------- |
| `«CATÁLOGO»` | `«VALORES»` | `«MÓDULO»` |

### 24.5 Instructivos complementarios

> Otros documentos que explican tareas relacionadas con el sistema.

| Documento | Propósito | Ubicación |
| --------- | --------- | --------- |
| `«DOCUMENTO»` | `«PROPÓSITO»` | `«UBICACIÓN»` |

### 24.6 Información adicional

> Lo que no encaja en ninguna sección anterior.

`«INFORMACIÓN_ADICIONAL»`

## Anexo A. Convención para documentar funcionalidades

> Es el molde que usan las secciones 10 y 11 para documentar cada funcionalidad.

Toda funcionalidad documentada en este manual debe seguir esta estructura:

### `«NOMBRE_DE_LA_FUNCIONALIDAD»`

> Agrupa la ficha de una funcionalidad, con sus campos en este orden.

**Objetivo:** `«QUÉ_PERMITE_REALIZAR»`

**Acceso:** `«DESDE_DÓNDE_SE_ACCEDE»`

**Precondiciones:** `«QUÉ_DEBE_CUMPLIRSE_ANTES»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`
3. `«PASO_3»`
4. `«PASO_N»`

**Resultado esperado:** `«QUÉ_DEBE_OCURRIR»`

**Validaciones:** `«REGLAS_A_TENER_EN_CUENTA»`

**Errores frecuentes:** `«SITUACIONES_QUE_IMPIDEN_COMPLETAR_LA_OPERACIÓN»`

**Solución:** `«QUÉ_PUEDE_HACER_EL_USUARIO»`

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

### Regla fundamental

> Es la prueba con que se revisa si la ficha de una funcionalidad está completa.

Cada funcionalidad debe responder, en este orden:

1. ¿Qué puedo hacer?
2. ¿Dónde lo hago?
3. ¿Qué debo ingresar o seleccionar?
4. ¿Qué debo hacer?
5. ¿Qué debe ocurrir?
6. ¿Qué hago si ocurre un problema?

## Anexo B. Instrucciones de uso de la plantilla

> Cómo se llena esta plantilla, paso a paso.

1. Llenar la sección 1 antes que cualquier otra.
2. Borrar las secciones y subsecciones que no apliquen, sin renumerar las que quedan.
3. Duplicar la estructura `10.X` por cada módulo, manteniendo el mismo orden de subsecciones.
4. Documentar cada funcionalidad con la convención del anexo A.
5. Cuando una funcionalidad se comporte de forma distinta según el rol, indicarlo en la subsección correspondiente y reflejar la diferencia en la matriz de la sección 9.1.
6. Las capturas de pantalla son apoyo: no deben reemplazar las instrucciones escritas.
7. No duplicar información entre módulos; usar referencias cruzadas a la sección correspondiente.
8. Describir las acciones en el mismo orden en que aparecen en el sistema.
9. No registrar credenciales reales, datos personales ni información sensible.
10. Todos los placeholders deben quedar reemplazados o eliminados antes de aprobar el documento.

### Placeholders estándar

> Qué va en cada espacio por llenar que se repite en la plantilla.

| Placeholder | Significado |
| ----------- | ----------- |
| `«NOMBRE_SISTEMA»` | Nombre del sistema |
| `«CODIGO_SISTEMA»` | Código o identificador |
| `«VERSION_SISTEMA»` | Versión del sistema |
| `«VERSION_MANUAL»` | Versión del manual |
| `«URL_SISTEMA»` | Dirección de acceso al sistema |
| `«CAMPO_USUARIO»` | Nombre del campo de usuario en el formulario de ingreso |
| `«CAMPO_CONTRASEÑA»` | Nombre del campo de contraseña |
| `«ROL_ADMINISTRADOR»` | Rol con permisos administrativos |
| `«ROL_USUARIO»` | Rol operativo |
| `«ROL_CONSULTA»` | Rol de solo lectura |
| `«NOMBRE_DEL_MÓDULO»` | Nombre del módulo documentado |
| `«NOMBRE_DE_LA_FUNCIONALIDAD»` | Nombre de la funcionalidad |
| `«CAMPO»` | Campo de un formulario |
| `«FILTRO»` | Filtro de búsqueda |
| `«MENSAJE»` | Mensaje mostrado por el sistema |
| `«INSERTAR_CAPTURA»` | Espacio para una captura de pantalla |
| `«INSERTAR_DIAGRAMA»` | Espacio para un diagrama de flujo |
| `«RESPONSABLE»` | Persona o rol responsable |
| `«FECHA»` | Fecha en formato `AAAA-MM-DD` |
