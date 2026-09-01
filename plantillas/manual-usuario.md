# Manual de Usuario — `«NOMBRE_SISTEMA»`

> **Cómo se escribe lo que se llena.** En la variedad del idioma que usa el proyecto, en tercera persona para lo que se explica y en infinitivo para lo que el lector hace. La regla es [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), y se cita en vez de repetirla: lo que se copia a mano se copia distinto (`S-090`). Los espacios por llenar van marcados `«…»`, que es la marca de todos los modelos ([`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).

> **Modelo reutilizable.** Reemplazar cada `«…»` con lo que el sistema hace de verdad, y borrar las secciones que no apliquen conservando la numeración de las que quedan. Acá no va código, ni instalación, ni configuración: eso vive en el [modelo de manual de instalación](manual-instalacion.md).

---

## 1. Información general del documento

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

---

## 2. Introducción

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

---

## 3. Objetivo del manual

**Objetivo:** `«OBJETIVO_DEL_MANUAL»`

**Al finalizar la lectura, el usuario podrá:**

- `«CAPACIDAD_1»`
- `«CAPACIDAD_2»`
- `«CAPACIDAD_N»`

---

## 4. Alcance

### 4.1 Incluido en este manual

| Elemento | Descripción |
| -------- | ----------- |
| `«MÓDULO_O_FUNCIONALIDAD»` | `«DESCRIPCIÓN»` |

### 4.2 Tipos de usuario contemplados

| Tipo de usuario | Descripción |
| --------------- | ----------- |
| `«TIPO_USUARIO»` | `«DESCRIPCIÓN»` |

### 4.3 Fuera del alcance

| Elemento | Motivo | Documento de referencia |
| -------- | ------ | ----------------------- |
| `«ELEMENTO_EXCLUIDO»` | `«MOTIVO»` | `«DOCUMENTO»` |

---

## 5. Conceptos básicos

### 5.1 Conceptos del negocio

| Concepto | Explicación | Dónde se utiliza en el sistema |
| -------- | ----------- | ------------------------------ |
| `«CONCEPTO»` | `«EXPLICACIÓN»` | `«MÓDULO_O_PANTALLA»` |

### 5.2 Estados de los registros

| Estado | Significado | Acciones permitidas | Estado siguiente |
| ------ | ----------- | ------------------- | ---------------- |
| `«ESTADO»` | `«SIGNIFICADO»` | `«ACCIONES»` | `«ESTADO_SIGUIENTE»` |

### 5.3 Tipos de documentos o registros

| Tipo | Descripción | Módulo asociado |
| ---- | ----------- | --------------- |
| `«TIPO»` | `«DESCRIPCIÓN»` | `«MÓDULO»` |

### 5.4 Botones y acciones especiales

| Botón o ícono | Nombre | Qué hace | Dónde aparece |
| ------------- | ------ | -------- | ------------- |
| `«ÍCONO_O_BOTÓN»` | `«NOMBRE»` | `«ACCIÓN»` | `«UBICACIÓN»` |

---

## 6. Requisitos para utilizar el sistema

| Requisito | Detalle | Obligatorio | Cómo obtenerlo |
| --------- | ------- | ----------- | -------------- |
| Acceso al sistema | `«DETALLE»` | `<Sí / No>` | `«RESPONSABLE_O_PROCEDIMIENTO»` |
| Usuario y contraseña | `«DETALLE»` | `<Sí / No>` | `«RESPONSABLE_O_PROCEDIMIENTO»` |
| Navegador soportado | `«NAVEGADOR_Y_VERSION»` | `<Sí / No>` | `«PROCEDIMIENTO»` |
| Conexión requerida | `<INTERNET / RED_INSTITUCIONAL / VPN>` | `<Sí / No>` | `«PROCEDIMIENTO»` |
| Permisos o rol asignado | `«PERMISO_O_ROL»` | `<Sí / No>` | `«RESPONSABLE»` |
| `«OTRO_REQUISITO»` | `«DETALLE»` | `<Sí / No>` | `«PROCEDIMIENTO»` |

**Recomendaciones adicionales:** `«RECOMENDACIONES»`

---

## 7. Acceso al sistema

### 7.1 Punto de acceso

| Campo | Valor |
| ----- | ----- |
| Dirección del sistema | `«URL_SISTEMA»` |
| Ambiente | `«AMBIENTE»` |
| Requiere red específica | `<Sí / No — DETALLE>` |

### 7.2 Inicio de sesión

**Objetivo:** ingresar al sistema con las credenciales asignadas.

**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. Ingrese a `«URL_SISTEMA»`.
2. Diligencie el campo `«CAMPO_USUARIO»`.
3. Diligencie el campo `«CAMPO_CONTRASEÑA»`.
4. `«PASO_ADICIONAL_SI_APLICA»`
5. Seleccione la opción `«BOTON_INGRESAR»`.

**Resultado esperado (credenciales correctas):** `«RESULTADO_ESPERADO»`

**Resultado cuando las credenciales son incorrectas:** `«MENSAJE_Y_COMPORTAMIENTO»`

| Situación | Mensaje mostrado | Qué debe hacer el usuario |
| --------- | ---------------- | ------------------------- |
| `«SITUACIÓN»` | `«MENSAJE»` | `«ACCIÓN»` |

**Captura de pantalla:** `«INSERTAR_CAPTURA»`

### 7.3 Recuperación de contraseña

> Incluir esta subsección únicamente si el sistema ofrece la funcionalidad.

**Acceso:** `«UBICACIÓN_DE_LA_OPCIÓN»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`
3. `«PASO_N»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

**Consideraciones:** `«CONSIDERACIONES»`

### 7.4 Cierre de sesión

**Acceso:** `«UBICACIÓN_DE_LA_OPCIÓN»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_2»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`

---

## 8. Interfaz principal

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

| Acción | Cómo se realiza | Resultado |
| ------ | --------------- | --------- |
| `«ACCIÓN»` | `«PROCEDIMIENTO»` | `«RESULTADO»` |

---

## 9. Roles y permisos

| Rol | Descripción | Módulos disponibles | Principales acciones |
| --- | ----------- | ------------------- | -------------------- |
| `«ROL_ADMINISTRADOR»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |
| `«ROL_USUARIO»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |
| `«ROL_CONSULTA»` | `«DESCRIPCIÓN»` | `«MÓDULOS»` | `«ACCIONES»` |

### 9.1 Matriz de permisos por funcionalidad

| Funcionalidad | `«ROL_1»` | `«ROL_2»` | `«ROL_3»` |
| ------------- | --------- | --------- | --------- |
| `«FUNCIONALIDAD»` | `<Sí / No>` | `<Sí / No>` | `<Sí / No>` |

> Cuando una funcionalidad se comporte de forma distinta según el rol, indíquelo explícitamente en la sección del módulo correspondiente.

---

## 10. Módulos del sistema

> Duplicar la estructura `10.X` por cada módulo del sistema, y borrar las subsecciones que no apliquen sin renumerar las demás.

### 10.1 `«NOMBRE_DEL_MÓDULO»`

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
3. Seleccione `«BOTON_GUARDAR»`.

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

1. Seleccione el registro: `«PROCEDIMIENTO_DE_SELECCIÓN»`
2. `«PASO_2»`
3. Seleccione `«BOTON_GUARDAR»`.

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
2. Confirme la acción en `«MENSAJE_O_VENTANA_DE_CONFIRMACIÓN»`.

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

`<REPETIR_ESTRUCTURA_10.X>`

---

## 11. Formularios

> Acá van los formularios transversales o de uso frecuente. Los formularios propios de un módulo pueden documentarse en su sección correspondiente.

### 11.1 `«NOMBRE_DEL_FORMULARIO»`

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

---

## 12. Búsquedas y filtros

### 12.1 Búsqueda simple

**Ubicación:** `«UBICACIÓN»`
**Qué permite buscar:** `«CAMPOS_O_CRITERIOS»`
**Pasos:** `«PASOS»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.2 Búsqueda avanzada

> Incluir únicamente si el sistema la ofrece.

**Ubicación:** `«UBICACIÓN»`
**Pasos:** `«PASOS»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.3 Filtros disponibles

| Filtro | Módulo | Descripción | Valores posibles | Se combina con |
| ------ | ------ | ----------- | ---------------- | -------------- |
| `«FILTRO»` | `«MÓDULO»` | `«DESCRIPCIÓN»` | `«VALORES»` | `«OTROS_FILTROS»` |

### 12.4 Combinación de filtros

`«EXPLICACIÓN_DEL_COMPORTAMIENTO»`

### 12.5 Limpieza de filtros

**Cómo se realiza:** `«PROCEDIMIENTO»`
**Resultado esperado:** `«RESULTADO_ESPERADO»`

### 12.6 Ordenamiento

| Columna / criterio | Permite ordenar | Cómo se realiza |
| ------------------ | --------------- | --------------- |
| `«COLUMNA»` | `<Sí / No>` | `«PROCEDIMIENTO»` |

### 12.7 Paginación

**Cómo funciona:** `«EXPLICACIÓN»`
**Opciones disponibles:** `«OPCIONES»`

---

## 13. Reportes

### 13.1 Reportes disponibles

| Reporte | Objetivo | Módulo | Roles con acceso | Formato de salida |
| ------- | -------- | ------ | ---------------- | ----------------- |
| `«NOMBRE_REPORTE»` | `«OBJETIVO»` | `«MÓDULO»` | `«ROLES»` | `«FORMATO»` |

### 13.2 `«NOMBRE_REPORTE»`

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

---

## 14. Exportación de información

> Incluir únicamente si el sistema permite exportar.

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

---

## 15. Notificaciones y mensajes del sistema

### 15.1 Tipos de mensaje

| Tipo | Cómo se identifica | Significado general |
| ---- | ------------------ | ------------------- |
| Éxito | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Advertencia | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Error | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Información | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |
| Confirmación | `«IDENTIFICACIÓN_VISUAL»` | `«SIGNIFICADO»` |

### 15.2 Mensajes del sistema

| Mensaje | Significado | Acción recomendada |
| ------- | ----------- | ------------------ |
| `«MENSAJE»` | `«SIGNIFICADO»` | `«ACCIÓN»` |

### 15.3 Notificaciones

| Notificación | Cuándo se genera | Dónde se consulta | Acción del usuario |
| ------------ | ---------------- | ----------------- | ------------------ |
| `«NOTIFICACIÓN»` | `«CONDICIÓN»` | `«UBICACIÓN»` | `«ACCIÓN»` |

---

## 16. Validaciones y errores frecuentes

| Situación | Causa probable | Qué debe hacer el usuario |
| --------- | -------------- | ------------------------- |
| `«SITUACIÓN»` | `«CAUSA»` | `«ACCIÓN»` |

### 16.1 Validaciones generales del sistema

| Validación | Dónde aplica | Qué exige | Mensaje asociado |
| ---------- | ------------ | --------- | ---------------- |
| `«VALIDACIÓN»` | `«MÓDULO_O_FORMULARIO»` | `«REGLA»` | `«MENSAJE»` |

---

## 17. Flujos completos de operación

> Acá van los procesos que involucran varias funcionalidades o módulos.

### 17.1 `«NOMBRE_DEL_PROCESO»`

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

`«REPETIR_ESTRUCTURA»`

---

## 18. Casos de uso frecuentes

| # | Caso de uso | Rol | Módulo | Sección de referencia |
| - | ----------- | --- | ------ | --------------------- |
| 1 | `«CASO_DE_USO»` | `«ROL»` | `«MÓDULO»` | `«SECCIÓN»` |

### 18.1 `«NOMBRE_DEL_CASO_DE_USO»`

**Situación:** `«SITUACIÓN_DEL_USUARIO»`
**Precondiciones:** `«PRECONDICIONES»`

**Pasos:**

1. `«PASO_1»`
2. `«PASO_N»`

**Resultado esperado:** `«RESULTADO_ESPERADO»`
**Si algo falla:** `«QUÉ_HACER»`

---

## 19. Preguntas frecuentes (FAQ)

### ¿`«PREGUNTA»`?

**Respuesta:** `«RESPUESTA»`

### ¿`«PREGUNTA»`?

**Respuesta:** `«RESPUESTA»`

---

## 20. Buenas prácticas de uso

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

---

## 21. Soporte y atención de incidentes

### 21.1 Canales de soporte

| Canal | Dato de contacto | Horario de atención | Tipo de solicitud |
| ----- | ---------------- | ------------------- | ----------------- |
| `«CANAL»` | `«CONTACTO»` | `«HORARIO»` | `«TIPO»` |

### 21.2 Información que debe proporcionar el usuario

- Nombre y usuario: `«DATO»`
- Módulo donde ocurrió: `«DATO»`
- Acción realizada antes del error: `«DATO»`
- Mensaje mostrado por el sistema: `«DATO»`
- Fecha y hora del incidente: `«DATO»`
- `«OTRA_INFORMACIÓN»`

### 21.3 Evidencias recomendadas

- Captura de pantalla completa del error.
- Captura de la información ingresada (sin credenciales).
- `«OTRA_EVIDENCIA»`

### 21.4 Procedimiento de reporte

1. `«PASO_1»`
2. `«PASO_N»`

**Tiempo de respuesta estimado:** `«TIEMPO»`

---

## 22. Glosario

| Término | Definición |
| ------- | ---------- |
| `«TÉRMINO»` | `«DEFINICIÓN»` |

---

## 23. Historial de cambios del manual

| Versión | Fecha | Descripción del cambio | Responsable |
| ------- | ----- | ---------------------- | ----------- |
| `«VERSION_MANUAL»` | `«FECHA»` | `«CAMBIO»` | `«RESPONSABLE»` |

---

## 24. Anexos

### 24.1 Capturas adicionales

`«INSERTAR_CAPTURAS»`

### 24.2 Flujos y diagramas

`«INSERTAR_DIAGRAMAS»`

### 24.3 Tablas de referencia

| Referencia | Descripción | Ubicación |
| ---------- | ----------- | --------- |
| `«REFERENCIA»` | `«DESCRIPCIÓN»` | `«UBICACIÓN»` |

### 24.4 Catálogos

| Catálogo | Valores | Dónde se utiliza |
| -------- | ------- | ---------------- |
| `«CATÁLOGO»` | `«VALORES»` | `«MÓDULO»` |

### 24.5 Instructivos complementarios

| Documento | Propósito | Ubicación |
| --------- | --------- | --------- |
| `«DOCUMENTO»` | `«PROPÓSITO»` | `«UBICACIÓN»` |

### 24.6 Información adicional

`«INFORMACIÓN_ADICIONAL»`

---

## Anexo A. Convención para documentar funcionalidades

Toda funcionalidad documentada en este manual debe seguir esta estructura:

### `«NOMBRE_DE_LA_FUNCIONALIDAD»`

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

Cada funcionalidad debe responder, en este orden:

**¿Qué puedo hacer? → ¿Dónde lo hago? → ¿Qué debo ingresar o seleccionar? → ¿Qué debo hacer? → ¿Qué debe ocurrir? → ¿Qué hago si ocurre un problema?**

---

## Anexo B. Instrucciones de uso de la plantilla

1. Llenar la sección 1 antes que cualquier otra.
2. Borrar las secciones y subsecciones que no apliquen, sin renumerar las que quedan.
3. Duplicar la estructura `10.X` por cada módulo, manteniendo el mismo orden de subsecciones.
4. Documentar cada funcionalidad con la convención del anexo A.
5. Cuando una funcionalidad se comporte de forma distinta según el rol, indíquelo en la subsección correspondiente y refleje la diferencia en la matriz de la sección 9.1.
6. Las capturas de pantalla son apoyo: no deben reemplazar las instrucciones escritas.
7. No duplique información entre módulos; use referencias cruzadas a la sección correspondiente.
8. Describa las acciones en el mismo orden en que aparecen en el sistema.
9. No registre credenciales reales, datos personales ni información sensible.
10. Todos los placeholders deben quedar reemplazados o eliminados antes de aprobar el documento.

### Placeholders estándar

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
