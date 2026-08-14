# Plan de Pruebas — Fase A-EP-004-HU-010-declaracion-y-comprobacion

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el [resultado_pruebas.md](resultado_pruebas.md) de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md) de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-004-010 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-010-declaracion-y-comprobacion` de [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md) |
| **Fecha** | 2026-08-14 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

> Por proporcionalidad, una fase usa solo las secciones 3, 5, 6, 9 y 12 de la plantilla `planes/pruebas.md`. El resto es para un release o una épica entera.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | Cada comprobación sobre un texto ya leído, sin tocar disco | Desarrollo | Local | Sí |
| Integración | La comprobación completa sobre un proyecto de prueba en carpeta temporal | Desarrollo | Local | Sí |
| Regresión | Que las comprobaciones que ya existían sigan dando lo mismo | Desarrollo | Local | Sí |

No hay pruebas de sistema ni de aceptación de usuario: no hay interfaz ni servicio desplegado. La aceptación la da quien aprueba la fase leyendo el resultado.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los cinco criterios de aceptación de HU-010 |
| Seguridad | ☑ | Ninguna comprobación escribe en disco ni sale a la red |
| Rendimiento | ☐ | No aplica en esta fase: el volumen lo fija el proyecto que se revise |
| Usabilidad | ☑ | El mensaje del hallazgo dice la convención esperada, no solo que está mal |
| Compatibilidad | ☑ | Rutas de Windows con espacios y tildes |
| Migración de datos | ☐ | No aplica |
| Recuperación | ☐ | No aplica |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — proyecto sin declaración, con declaración a medias, con declaración completa.
- **Valores límite** — declaración vacía, clave desconocida, celda que aún trae el marcador de la plantilla, proyecto sin migraciones.
- **Tabla de decisión** — combinación de entidad declarada como dominio o no, e inmutable o no.
- **Transición de estados** — no aplica: las comprobaciones no tienen estado.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Crítica | Que sin declaración no se invente ninguna convención | 100% |
| Alta | Cada uno de los cinco criterios de aceptación | 100% |
| Media | Mensajes y compatibilidad de rutas | ≥ 80% |

### 3.5 Alcance de la corrida automatizada  ·  `02·F5`

Se corre la suite completa de `validadores/pruebas.py`. Es la suite del módulo que esta fase toca y hoy tarda segundos, así que separar un subconjunto costaría más de lo que ahorra. No se corre nada fuera de ella.

---

## 5. Matriz de trazabilidad

> Ningún criterio de aceptación puede quedar sin al menos un caso de prueba.

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-010 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-010 | CA-02 | CP-003, CP-004, CP-005 | Funcional | Alta | Sí | ☐ |
| HU-010 | CA-03 | CP-006, CP-007 | Funcional | Alta | Sí | ☐ |
| HU-010 | CA-04 | CP-008, CP-009 | Funcional | Alta | Sí | ☐ |
| HU-010 | CA-05 | CP-010 | Funcional | Alta | Sí | ☐ |
| HU-010 | RNF-01 | CP-011, CP-012 | Seguridad | Crítica | Sí | ☐ |

**Cobertura:** 6 criterios cubiertos de 6 totales = 100%

---

## 6. Casos de prueba

### CP-001 — Un proyecto sin declaración no produce hallazgos de nombres

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Proyecto de prueba en carpeta temporal, con migraciones y sin los archivos de declaración |
| **Datos de entrada** | Una migración que crea una tabla con nombre en cualquier forma |
| **Diseñado por** | Ing. José Dúmar Jiménez Ruíz |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de estructura sobre ese proyecto | No aparece ningún hallazgo sobre nombres |
| 2 | Leer la salida | Dice que el proyecto no declara su convención |

**Resultado esperado final:** ninguna convención inventada.
**Postcondiciones:** ningún archivo modificado.

### CP-002 — Se dice qué queda sin comprobar por cada clave sin declarar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Proyecto de prueba con la declaración presente y todas las claves en blanco |
| **Datos de entrada** | La plantilla recién copiada, sin llenar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de la declaración | Un aviso por cada clave sin declarar |
| 2 | Leer cada aviso | Cada uno nombra la regla que queda sin comprobar |

### CP-003 — Una tabla con nombre fuera de la convención se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Declaración con la convención de tablas y de columnas |
| **Datos de entrada** | Una migración que crea una tabla que no sigue esa forma |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de estructura | Reporta la tabla, con archivo, línea y la convención esperada |
| 2 | Corregir el nombre y volver a correr | No reporta nada |

### CP-004 — Clave foránea, booleano y fecha de evento fuera de convención

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Tipo** | Funcional — caso borde |
| **Prioridad** | Alta |
| **Precondiciones** | Declaración con sufijo de clave foránea, prefijo de booleano y sufijo de fecha |
| **Datos de entrada** | Una migración con una columna de cada tipo, mal nombrada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación | Tres hallazgos, uno por columna, cada uno con lo que se esperaba |

### CP-005 — El código heredado no se revisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Alta |
| **Precondiciones** | Declaración que incluye la migración vieja como código heredado |
| **Datos de entrada** | La misma migración mal nombrada de CP-003 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación | No reporta nada sobre esa migración |
| 2 | Quitar la migración de lo heredado y volver a correr | Vuelve a reportarla |

### CP-006 — Tabla de dominio sin columnas de auditoría

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-03 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Una entidad declarada con su tabla, y las columnas de auditoría declaradas |
| **Datos de entrada** | Migración que crea esa tabla sin esas columnas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de entidades | Reporta cuáles columnas de auditoría faltan, nombrándolas |
| 2 | Agregarlas y volver a correr | No reporta nada |

### CP-007 — La tabla que no se declaró no se revisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-03 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Alta |
| **Precondiciones** | La misma declaración de CP-006 |
| **Datos de entrada** | Una migración que crea una tabla del marco de trabajo, sin auditoría y sin declarar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación | Esa tabla no aparece en la salida |

### CP-008 — Entidad inmutable sin campos de anulación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-04 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Entidad declarada como inmutable, con estados y campos de anulación declarados |
| **Datos de entrada** | Migración de esa tabla sin los campos de anulación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de entidades | Nombra cada campo de anulación que falta |
| 2 | Quitar además los estados del esquema y volver a correr | Reporta también que no aparece ninguno de los estados declarados |

### CP-009 — Entidad inmutable sin permiso propio de anular

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-04 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Alta |
| **Precondiciones** | Entidad inmutable declarada y forma del permiso declarada |
| **Datos de entrada** | Código del proyecto sin el permiso de anular de esa entidad |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación | Reporta que no encuentra el permiso, escribiéndolo tal como debería llamarse |
| 2 | Agregar el permiso al código y volver a correr | No reporta nada |

### CP-010 — Módulo sin declarar y módulo declarado sin código

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-05 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Declarada la ruta donde viven los módulos, y dos módulos declarados |
| **Datos de entrada** | Código con un tercer módulo sin declarar, y uno de los declarados sin código |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de estructura | Dos hallazgos: el módulo sin declarar y el declarado sin código |
| 2 | Declarar el tercero y crear el código del que faltaba | No reporta nada |

### CP-011 — Ninguna comprobación modifica archivos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / RNF-01 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Proyecto de prueba con declaración completa e incumplimientos sembrados |
| **Datos de entrada** | El proyecto entero |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la huella de cada archivo del proyecto de prueba | Queda el registro previo |
| 2 | Correr las tres comprobaciones | Reportan hallazgos |
| 3 | Volver a calcular las huellas | Ninguna cambió |

### CP-012 — Todo hallazgo de esta familia es aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / RNF-01 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | El mismo proyecto de CP-011 |
| **Datos de entrada** | Incumplimientos de los cinco criterios a la vez |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las tres comprobaciones | Todos los hallazgos salen como aviso |
| 2 | Mirar el código con que terminó la corrida | Termina sin error |

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Crítica** | La comprobación inventa una convención que nadie declaró, o modifica un archivo | Inmediato |
| **Alta** | Un incumplimiento real no se reporta, o se reporta uno que no existe | Antes de cerrar la fase |
| **Media** | El mensaje no dice qué se esperaba | Antes de cerrar la fase |
| **Baja** | Redacción del mensaje | Backlog |

### 9.2 Flujo del defecto

```
Nuevo → En corrección → Listo para pruebas → Verificado → Cerrado
                                            ↘ Reabierto ↗
```

### 9.3 Contenido mínimo de un reporte

- Caso de prueba que lo destapó y criterio de aceptación asociado.
- Qué se esperaba y qué pasó.
- La entrada exacta con que se reproduce.

### 9.4 Registro

El registro de los defectos que aparezcan va en el [resultado_pruebas.md](resultado_pruebas.md), §4. Acá no se anota nada de la ejecución.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de criterios de aceptación | CA con caso / CA totales | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |
| Tasa de aprobación | Aprobados / ejecutados | 100% |
| Falsos positivos | Hallazgos sobre código que sí cumple | 0 |

La meta de aprobación es 100% y no 95% porque son doce casos automáticos: uno rojo es un defecto, no una desviación estadística.

### 12.2 Dónde se miden

El resumen de la corrida, el veredicto por criterio y el concepto final van en el [resultado_pruebas.md](resultado_pruebas.md) de la fase. Este plan define qué se va a medir; aquel documento dice cuánto dio.
