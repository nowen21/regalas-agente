# Plan de Pruebas · Fase `A-EP-025-HU-003-registro-de-proyectos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-003: CA-01 a CA-04 |
| **Fecha** | 2026-10-04 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El cálculo de la carpeta de Claude Code | Claude | Sin base | Sí |
| Integración | Pantallas, validaciones y permisos | Claude | Base de pruebas en MariaDB | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03 |
| Validación | ☑ | CA-02 |
| Seguridad | ☑ | CA-04 |

### 3.3 Técnicas de diseño de casos

- Valores límite en los límites de aviso: 0, 1 y negativo.
- Partición de rutas: existe, no existe, repetida con otras mayúsculas.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-04 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.proyectos core.cuentas core.inicio`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-003 | CA-02 | CP-002 | Validación | Alta | Sí | ☐ |
| HU-003 | CA-03 | CP-003 | Funcional | Media | Sí | ☐ |
| HU-003 | CA-04 | CP-004 | Seguridad | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Registrar un proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Una cuenta administradora; una carpeta temporal |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `carpeta_de_claude` con `C:\Ing. Jose\ia\agente` y con una ruta con `ó` y `-` | `c--Ing--Jose-ia-agente`; cada carácter que no es letra o número da `-` |
| 2 | Registrar con nombre y ruta, sin límites | En la lista, activo, con su carpeta y los límites 2000 y 10 000 |
| 3 | Registrar con límites escritos | Los límites escritos |

### CP-002 · Lo que no vale no se guarda

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Un proyecto ya registrado |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ruta que no existe | Mensaje en la ruta; nada guardado |
| 2 | La misma ruta con otras mayúsculas | Mensaje de ruta ya registrada |
| 3 | Nombre repetido | Mensaje en el nombre |
| 4 | Límite 0 o negativo | Mensaje en el límite |
| 5 | Nombre vacío | Mensaje de campo obligatorio |

### CP-003 · Editar y desactivar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Un proyecto registrado |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar el límite por enganche | La lista muestra el nuevo |
| 2 | Desmarcar «Activo» | La lista lo muestra «Inactivo»; sigue en la base |
| 3 | Editar sin cambiar la ruta | No dice que la ruta está repetida |

### CP-004 · El grupo consulta solo ve

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-04 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Una cuenta de consulta |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la lista | 200, sin «Registrar» ni «Editar» |
| 2 | Pedir el registro y la edición | 403 en los dos |
| 3 | Enviar el registro por POST | 403; nada guardado |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se guarda un proyecto inválido, o consulta cambia algo | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
