# Plan de Trabajo · Fase `B-EP-023-HU-004-solo-detiene-el-hallazgo-que-obliga-a-salirse-del-plan` (módulo `base/02-flujo-de-trabajo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-004-solo-detiene-el-hallazgo-que-obliga-a-salirse-del-plan` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md), una sola (`F12.1`) |
| **Módulo** | `base/02-flujo-de-trabajo/` |
| **Especificación del módulo** | El CA-08 de la HU-004 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda fase de la HU-004. Sale del punto 1 del [análisis 12](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-12.md) (acuerdo 1). La fase `A` cubrió los criterios anteriores. Va después de la fase `B` de la HU-003, de la que depende la HU.

**Carencias que cierra** (`02·F14` Q3): `02·F9` detiene la ejecución ante cualquier hallazgo, aunque no toque el plan en curso. Así se detuvo la fase `B` de la HU-007 por el H-15, que era de la EP-005.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 51.1.0.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-004 | Estado |
|---|---|
| CA-08 · Solo detiene el hallazgo que obliga a salirse del plan | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que `02·F9` diga que solo detiene la ejecución el hallazgo que, para cerrar la fase, obliga a tocar algo que el plan no declara, y que el que no obliga a eso se anota con su pendiente donde pertenece y el trabajo sigue.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-08 | La excepción de `02·F9` | Regla | Baja |

**Fuera de alcance:** el freno, que ya detiene solo lo que el plan no declara (HU-007, fase `B`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 51.0.0:

- La excepción de `02·F9` dice: «interrumpen el flujo el descubrimiento genuino que el plan no anticipó y requiere decisión del usuario, y el hallazgo bloqueante que impide continuar». No distingue si el hallazgo toca el plan en curso.
- El texto de `02·F9` se copia en `base/reglas-por-tarea/trabajar-cadena-2.md`, que escribe `validadores/mapa_tareas.py`. El índice del capítulo, `base/02-flujo-de-trabajo/base.md`, solo trae el título y una línea sobre el volumen, que no cambian.
- `13·DOC24` y la nota de `plantillas/analisis.md` dicen que todo hallazgo abre el análisis siguiente, que decide si es parte del plan. El texto de `13·DOC24` se copia en `base/reglas-por-tarea/escribir-documento-2.md`.
- Ninguna prueba lee el texto de `02·F9` ni el de `13·DOC24`. `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py` lee lo que escribe `mapa_tareas.py`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md` | Modificar | Regla | La excepción y su sello |
| `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` | Modificar | Regla | Qué hallazgo abre el análisis siguiente, y su sello |
| `plantillas/analisis.md` | Modificar | Plantilla | La nota de qué hallazgo abre el análisis siguiente |
| `base/reglas-por-tarea/trabajar-cadena-2.md`, `base/reglas-por-tarea/escribir-documento-2.md` | Modificar | Generado | Lo vuelve a escribir `mapa_tareas.py` |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 52.1.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La excepción de `02·F9` | Todo proyecto con la versión nueva | Nada: detiene menos |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Detiene solo el hallazgo que, para cerrar la fase, obliga a tocar algo que el plan no declara | Detener ante todo hallazgo | Así lo acordó el usuario | Análisis 12, acuerdo 1 |
| El que no obliga a eso se anota con su pendiente donde pertenece y el trabajo sigue, sin análisis | Abrir un análisis por cada hallazgo | Así lo acordó el usuario | Análisis 12, acuerdo 1 |
| El cambio va en la excepción de `02·F9`, que es la que hoy detiene | Una regla nueva | Es la regla que el CA-08 manda leer | Propuesta del agente |
| `13·DOC24` y la nota de `plantillas/analisis.md` dicen lo mismo: solo el hallazgo que obliga a tocar algo fuera del plan abre el análisis siguiente | Dejarlos como están | Si no, la base dice dos cosas distintas | Análisis 12, acuerdo 1 |
| La versión sube a 52.1.0, MENOR | MAYOR | La regla detiene menos: nadie tiene que hacer algo nuevo | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna. La de `13·DOC24` y la plantilla la resolvió el usuario el 2026-10-03: entran en esta fase.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Excepción de `02·F9` | Detiene el descubrimiento que pide decisión y el hallazgo que bloquea | Detiene solo el hallazgo que obliga a tocar algo que el plan no declara; el resto se anota con su pendiente donde pertenece y el trabajo sigue | `02·F9` |
| `13·DOC24` y nota de la plantilla del análisis | Todo hallazgo abre el análisis siguiente | Solo el que obliga a tocar algo que el plan no declara | `13·DOC24` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-08 · Solo detiene el hallazgo que obliga a salirse del plan

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Reescribir la excepción de `02·F9` con lo de 2.8, aplicar el checklist y poner su sello; correr `mapa_tareas.py` | `base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md`, `base/reglas-por-tarea/trabajar-cadena-2.md` | CA-08 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001 |
| T-03 | Ajustar `13·DOC24` con su sello y la nota de la plantilla; correr `mapa_tareas.py` | `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md`, `plantillas/analisis.md`, `base/reglas-por-tarea/escribir-documento-2.md` | CA-08 | Todo análisis nuevo | 0,5 h | T-01 | CP-001 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | La fila de la fase en la HU; subir a 52.1.0 | `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md`, `CHANGELOG.md`, `VERSION` | CA-08 | Todo proyecto adopta la versión | 0,3 h | T-01 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01, T-03 y después T-02, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-08 | Leer `02·F9`, `13·DOC24` y la nota de la plantilla del análisis | CP-001 |

## 6. Datos y ambiente de prueba

El repositorio del estándar.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 52.1.0 al actualizar el estándar. No tiene que hacer nada.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F9`, `20·M5`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que la excepción pase del largo del molde | Se mide con el checklist antes del sello |

## 11. Definition of Done

- [ ] CA-08 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 52.1.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-03, con la versión 52.1.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 0.
