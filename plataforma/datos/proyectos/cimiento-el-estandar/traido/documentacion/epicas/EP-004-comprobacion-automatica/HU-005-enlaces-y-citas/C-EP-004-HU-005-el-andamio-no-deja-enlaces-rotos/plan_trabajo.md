# Plan de Trabajo — Fase C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos (módulo Programas de comprobación — el andamio)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-005 Enlaces y citas](../HU-005-enlaces-y-citas.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Programas de comprobación — el andamio |
| **Especificación del módulo** | N/A: no hay especificación de módulo para los programas de comprobación; la HU es la especificación (`02·F2`, excepción declarada en las fases A y B de esta historia) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** 🐛 **Defecto.** Sale del [pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md](../../../../../pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md): el andamio copia `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md` tal cual, y su enlace `../../base/08-pruebas.md` vale desde `plantillas/planes/`, no desde la carpeta de la fase, tres niveles más abajo.

**CA de la HU que cubre esta fase:**

| CA de HU-005 que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-005-enlaces-y-citas.md#ca-05--lo-que-un-programa-del-estándar-escribe-no-nace-con-enlaces-rotos) · lo que un programa escribe no nace con enlaces rotos | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el andamio reescriba, al copiar cada plantilla, los enlaces relativos a la raíz del repositorio y el marcador `«RUTA-ESTANDAR»` con la ruta que corresponde desde la carpeta de la fase, de modo que el esqueleto pase `validar.py estandar` sin tocarlo.

**Fuera de alcance:**

- Cambiar las plantillas: siguen valiendo tal como están para quien las copia a mano desde su carpeta.
- Rellenar contenido: los `«…»` de contenido siguen intactos.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [validadores/andamio.py](../../../../../validadores/andamio.py): `crear()` lee cada plantilla de `DOCUMENTOS`, aplica `_sustituciones()` (solo marcadores estructurales) y escribe. No toca enlaces.
- `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md` línea 118 enlaza `../../base/08-pruebas.md#t4…`; `plantillas/ciclo-vida-proyectos/10-estado-fase.md` y `plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md` usan `«RUTA-ESTANDAR»/base/…`, que el instalador rellena en los proyectos (pendiente 40) y el andamio deja crudo.
- Las cuatro fases levantadas hoy y las tres de la mañana nacieron con el enlace de la línea 118 roto; se corrigió a mano con `sed` las siete veces.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/andamio.py` | Modificar | `_reenlazar(texto, origen_plantilla, destino)`: de `](<prefijo de la plantilla>/` a `](<prefijo de la fase>/`, y `«RUTA-ESTANDAR»` al mismo prefijo |
| `validadores/tests/test_el_andamio_no_deja_enlaces_rotos.py` | Nuevo | Los casos |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo que ya llamaba a estos programas sigue llamándolos igual.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el resultado se ve como texto en la consola o en la sesión.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Reescribir al copiar, calculando el prefijo con `os.path.relpath` | Poner `«RUTA-ESTANDAR»` en la plantilla del resultado y rellenarlo | Las dos plantillas de la fase ya usan formas distintas (`../../` y el marcador); el andamio las atiende a las dos y las plantillas no cambian |
| Solo enlaces que salen de la carpeta de la plantilla hacia la raíz | Reescribir cualquier `](../` | Un `../` que no llega a la raíz no se puede trasladar sin saber adónde iba |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-05 — en la HU: [CA-05](../HU-005-enlaces-y-citas.md#ca-05--lo-que-un-programa-del-estándar-escribe-no-nace-con-enlaces-rotos)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `_reenlazar()` en el andamio, llamada por `crear()` para cada plantilla | Validador | 0,5 h | — | EV-01 |
| T-02 | Los casos: el esqueleto nuevo sin `../../base/` ni marcador, con el prefijo correcto; `validar.py estandar` limpio sobre él; un `../` que no llega a la raíz no se toca | Prueba | 0,5 h | T-01 | EV-01 |

**Total estimado:** 1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-05](../HU-005-enlaces-y-citas.md#ca-05--lo-que-un-programa-del-estándar-escribe-no-nace-con-enlaces-rotos) | Caso automatizado sobre una fase de prueba, más `validar.py estandar` sobre ella | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_el_andamio_no_deja_enlaces_rotos.py` |

## 6. Datos y ambiente de prueba

Una copia temporal de `plantillas/` y una épica y HU de mentira en una carpeta temporal. No se levanta ninguna fase en `documentacion/epicas/` real.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. Las fases ya levantadas no cambian.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

No aplica a los proyectos: el andamio corre en el repositorio del estándar. Entra en la **27.2.0 (MENOR)** del día con las otras tres fases.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Una plantilla nueva con otra forma de enlace | Vuelve a nacer roto | El caso corre `validar.py estandar` sobre el esqueleto: atrapa cualquier forma | Abierto por diseño |

## 11. Definition of Done

- [ ] CA-05 verificado con evidencia
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde
- [ ] Señal registrada
- [ ] Listo para el commit único del día, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
