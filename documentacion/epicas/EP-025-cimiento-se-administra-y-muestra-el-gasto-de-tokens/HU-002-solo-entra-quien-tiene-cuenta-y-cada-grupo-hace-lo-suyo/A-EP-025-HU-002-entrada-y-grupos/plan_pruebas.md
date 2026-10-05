# Plan de Pruebas · Fase `A-EP-025-HU-002-entrada-y-grupos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-002: CA-01 a CA-04 |
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
| Integración | Entrada, permisos, grupos y la orden | Claude | Base de pruebas en MariaDB | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03, CA-04 |
| Seguridad | ☑ | CA-02, CA-03 |

### 3.3 Técnicas de diseño de casos

- Partición por quién pide: sin cuenta, consulta, administrador, superusuario.
- Partición por lo que se escribe en la entrada: correcto, contraseña equivocada, usuario inexistente.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-03 | 100% |
| Media | CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.cuentas core.inicio`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-002 | CA-02 | CP-002 | Seguridad | Alta | Sí | ☐ |
| HU-002 | CA-03 | CP-003 | Seguridad | Alta | Sí | ☐ |
| HU-002 | CA-04 | CP-004 | Funcional | Media | Sí | ☐ |

**Cobertura:** 4 de 4 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Sin cuenta, se pide entrar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Una cuenta de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/` sin cuenta | Redirección a `/entrar/?next=/` |
| 2 | Entrar con la cuenta y `next=/` | Redirección a `/`; la página muestra el usuario y «Salir» |
| 3 | Salir por POST | Redirección a `/entrar/`; `/` vuelve a pedir entrar |
| 4 | Pedir `/` sin cuenta con la base que no responde | 503 con el mensaje de prender MariaDB, sin pedir entrar |

### CP-002 · Una contraseña equivocada no deja entrar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Una cuenta de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Entrar con la contraseña equivocada | 200 en `/entrar/` con el mensaje de error; sin sesión |
| 2 | Entrar con un usuario que no existe | El mismo mensaje |

### CP-003 · El grupo consulta no puede cambiar nada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Una vista de prueba con `SoloAdministrador`; cuentas de consulta, administrador y superusuario |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | La pide la cuenta de consulta | 403 «No tiene permiso», sin el contenido de la vista |
| 2 | La pide la cuenta de administrador | 200 con el contenido |
| 3 | La pide el superusuario | 200 con el contenido |

### CP-004 · Grupos y la orden `crear_cuenta`

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Precondiciones** | T-06 y T-07 terminadas |
| **Datos de entrada** | Contraseñas escritas por la orden sustituida |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar los grupos de la base de pruebas | Existen `administrador` y `consulta` |
| 2 | `crear_cuenta --usuario u --grupo consulta` con la misma contraseña dos veces | La cuenta existe, está en consulta y la contraseña no queda en claro |
| 3 | Las dos contraseñas no coinciden | Error, sin crear la cuenta |
| 4 | Un grupo que no existe | Error con los grupos que valen |
| 5 | Un usuario que ya existe | Error, sin cambiar la cuenta |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se entra sin cuenta, o consulta abre una pantalla de administración | Antes de cerrar la fase |
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
