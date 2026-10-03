# Plan de Trabajo · Fase `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis` (módulo `base/`, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md), una sola (`F12.1`) |
| **Módulo** | `base/02-flujo-de-trabajo/`, `base/13-documentacion/`, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Los CA-01 a CA-07 de la HU-004 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): primera fase de la HU-004. Sale de los puntos 6, 13, 14, 17, 18 y 24 de «Lo que se tiene que hacer» del [análisis 1](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (conclusiones 9, 10, 18, 19, 24, 31, 33 y 41) y del punto 7 del [análisis 2](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-2.md) (conclusión 7).

**Carencias que cierra** (`02·F14` Q3): nada detiene al agente cuando aparece un hallazgo al ejecutar el plan; el plan se amplía y sigue, la fase cerrada no se reabre, y no se sabe cuántos hallazgos salieron.

**Aprobación** (`02·F4`): el usuario aprobó el plan el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-004 | Estado |
|---|---|
| CA-01 · Versiones en el mismo archivo y análisis numerados | ☑ |
| CA-02 · Un hallazgo detiene la ejecución y nada cierra | ☑ |
| CA-03 · El análisis siguiente trata solo lo que falló | ☑ |
| CA-04 · `02·F8` y `02·F9` detienen y vuelven al análisis | ☑ |
| CA-05 · El plan pasa de versión y la fase cerrada se reabre | ☑ |
| CA-06 · El plan registra sus hallazgos | ☑ |
| CA-07 · El análisis del hallazgo decide primero si es parte del plan | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que un hallazgo al ejecutar un plan lo detenga y vuelva al análisis, que nada cierre mientras no se resuelva, que el documento que cambia lo haga en su mismo archivo, y que el plan diga cuántos hallazgos salieron.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | `02·F28` dice que cada documento cambia en su mismo archivo y el análisis no se reescribe | Regla | Baja |
| CA-02 | El estado de la fase anota el hallazgo; el validador no deja cerrar la fase ni la HU mientras el análisis que abrió siga sin aprobar | Plantilla y validador | Media |
| CA-03 | `13·DOC24` y la plantilla del análisis: el siguiente trata solo lo que falló | Regla y plantilla | Baja |
| CA-04 | `02·F8` y `02·F9` detienen y vuelven al análisis | Regla | Baja |
| CA-05 | `02/base.md`, el anexo de `02·F12` y `13·DOC12`: el plan pasa de versión y la fase cerrada se reabre | Regla | Baja |
| CA-06 | La plantilla del plan pide cuántos hallazgos salieron | Plantilla | Baja |
| CA-07 | `13·DOC24` y la plantilla del análisis: decide primero si el hallazgo es parte del plan | Regla y plantilla | Baja |

**Fuera de alcance:** las fases ya cerradas no se reabren por esta fase; la regla nueva rige desde que se adopta la versión.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 46.0.0:

- `02·F8` dice que descubrir otro archivo detiene, se reporta, «se propone ampliar el plan y se espera el OK». `02·F9` lo trata como «hallazgo derivado» y deja retomar al usuario.
- `02/base.md` dice que «el plan aprobado no se modifica para anotarle resultados».
- El anexo de `02·F12` (`nomenclatura-de-fases.md`, F12.12) crea una fase que complementa a otra; es texto literal del usuario, que el análisis 1 aprobado (punto 18) manda ajustar.
- `13·DOC12` tiene la excepción «una fase ya cerrada no se reabre para ponerle ORIGEN».
- `13·DOC24` dice que lo que aparezca después de aprobar un análisis abre el siguiente; no dice qué trata ni qué decide primero. La nota de la plantilla del análisis dice que el siguiente «trata solo lo que falló y sus implicaciones».
- `02·F28` dice que el cambio se escribe donde nace y baja en orden; no dice que sea en el mismo archivo.
- La sección 13 de la plantilla del plan dice que el cierre va en `funcionalidad_implementada.md` y que el plan se queda como se aprobó. No pide cuántos hallazgos salieron.
- La sección 4 de la plantilla del estado de la fase anota el bloqueo, sin el motivo «hallazgo al ejecutar».
- `validadores/fases.py` no relaciona una fase con el análisis del que sale.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md` | Modificar | Regla | El mismo archivo |
| `base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md`, `base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md` | Modificar | Regla | Detienen y vuelven al análisis |
| `base/02-flujo-de-trabajo/base.md`, `base/02-flujo-de-trabajo/nomenclatura-de-fases.md`, `base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md` | Modificar | Regla | El plan pasa de versión; la fase cerrada se reabre |
| `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` | Modificar | Regla | Qué trata el análisis siguiente y qué decide primero |
| `plantillas/analisis.md`, `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `plantillas/ciclo-vida-proyectos/10-estado-fase.md` | Modificar | Plantilla | La nota del análisis siguiente, los hallazgos del plan y el motivo del bloqueo |
| `validadores/fases.py`, `validadores/tests/test_hallazgo_detiene_la_fase.py` | Modificar y nuevo | Validador | La fase y la HU no cierran con el análisis abierto |
| `base/reglas-por-tarea/` y `base/mapa-de-tareas.md` | Regenerar | Regla | Con `mapa_tareas.py` |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 47.0.0 |
| Los documentos de esta fase y la HU-004 | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `fases.py` lee el ORIGEN del plan | La revisión de fases | Solo cuenta los enlaces a un `analisis-N.md` dentro de una carpeta de pendiente |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-01 va en `02·F28`, que ya dice dónde se escribe el cambio | Una regla nueva | `20·M12`: se busca antes de crear, y `F28` es la dueña del tema |
| Una fase está detenida por un hallazgo cuando el pendiente del que sale (el que cita su ORIGEN) tiene un análisis posterior sin aprobar; mientras tanto, `fases.py` falla si la fase dice «Cumple» o la HU dice «Terminada» | Una marca escrita a mano | El análisis abierto es el hallazgo (análisis 1, conclusión 10); la marca a mano se olvida |
| El anexo de `02·F12` se ajusta en F12.12 con una línea fechada, como las demás del usuario | Dejarlo sin tocar | El usuario aprobó el ajuste en el análisis 1 (punto 18) |
| La sección 13 del plan pide solo el número de hallazgos y el enlace a cada análisis que abrieron; el resto del cierre sigue en `funcionalidad_implementada.md` | Llevarlo al resultado de pruebas | Así lo decidió el análisis 1 (conclusión 41 y punto 18) |
| La versión sube a 47.0.0, MAYOR | MENOR | Cambia qué hace el agente ante un hallazgo |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Hallazgo al ejecutar | Se amplía el plan y sigue | Se detiene y vuelve al análisis | `02·F8`, `02·F9` |
| Fase cerrada con hallazgo | Se crea otra que la complementa | Se reabre | `02·F12`, `13·DOC12` |
| Plan con hallazgo | No se modifica | Pasa a la versión siguiente con aprobación nueva | `02/base.md`, `02·F28` |
| Cierre de fase y HU | Nada lo impide | No cierran con el análisis del hallazgo abierto | `fases.py` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Versiones en el mismo archivo y análisis numerados

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `F28` dice que el hallazgo, el pendiente, la HU y el plan cambian en su mismo archivo, que pasa a su versión siguiente, y que el análisis no se reescribe: se numera el siguiente; checklist contra 47.0.0 | `base/02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md` | CA-01 | Todo proyecto que adopte la versión | 0,3 h | Ninguna | CP-001 |

### CA-02 · Un hallazgo detiene la ejecución y nada cierra

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | La sección 4 del estado de la fase suma el motivo «hallazgo al ejecutar», con el enlace al análisis que abrió | `plantillas/ciclo-vida-proyectos/10-estado-fase.md` | CA-02 | Las fases nuevas | 0,2 h | Ninguna | CP-002 |
| T-03 | `fases.py` falla si una fase dice «Cumple» o su HU dice «Terminada» mientras el pendiente del que sale tiene un análisis posterior sin aprobar (2.6) | `validadores/fases.py` | CA-02 | La revisión de fases | 1 h | Ninguna | CP-002 |

### CA-03 · El análisis siguiente trata solo lo que falló

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | `DOC24` dice que el análisis siguiente trata solo lo que falló y sus implicaciones sobre lo ya hecho; checklist contra 47.0.0 | `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` | CA-03 | Todo proyecto que adopte la versión | 0,3 h | Ninguna | CP-003 |

### CA-04 · `02·F8` y `02·F9` detienen y vuelven al análisis

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `F8`: descubrir a mitad que hace falta otro archivo detiene la ejecución y vuelve al análisis. `F9`: el hallazgo que el plan no anticipó detiene y vuelve al análisis. Checklists contra 47.0.0 | `base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md`, `base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md` | CA-04 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-004 |

### CA-05 · El plan pasa de versión y la fase cerrada se reabre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | `02/base.md`: el plan no se modifica para anotarle resultados, y si aparece un hallazgo pasa a su versión siguiente con aprobación nueva. Anexo F12.12: un hallazgo sobre lo construido reabre la fase; el complemento queda para trabajo nuevo. `DOC12`: la fase cerrada se reabre si aparece un hallazgo sobre lo que construyó; checklist contra 47.0.0 | `base/02-flujo-de-trabajo/base.md`, `base/02-flujo-de-trabajo/nomenclatura-de-fases.md`, `base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md` | CA-05 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-005 |

### CA-06 · El plan registra sus hallazgos

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | La sección 13 del plan pide «Hallazgos al ejecutar: «número»», con el enlace a cada análisis que abrieron | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-06 | Los planes nuevos | 0,2 h | Ninguna | CP-006 |

### CA-07 · El análisis del hallazgo decide primero si es parte del plan

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | `DOC24` y la nota de la plantilla del análisis: el análisis del hallazgo decide primero si es parte del plan en curso; si lo es, mejora el pendiente y se resuelve antes de seguir; si no, se crea su pendiente y el plan continúa | `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md`, `plantillas/analisis.md` | CA-07 | Los análisis nuevos | 0,3 h | T-04 | CP-007 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-09 | Regenerar el mapa de tareas; escribir los casos del plan de pruebas; subir a 47.0.0 con «⚠ obliga a migrar» | `base/`, `validadores/tests/test_hallazgo_detiene_la_fase.py`, `VERSION`, `CHANGELOG.md` | CA-01 a CA-07 | Todo proyecto adopta la versión | 0,7 h | T-01 a T-08 | CP-001 a CP-008 |

## 4. Secuencia de ejecución

Las reglas y las plantillas primero: T-01, T-04, T-05, T-06, T-08, T-02 y T-07. Después T-03. Al final T-09, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer `02·F28` | CP-001 |
| CA-02 | Una fase y una HU de prueba cerradas con el análisis del hallazgo abierto | CP-002 |
| CA-03 | Leer `13·DOC24` | CP-003 |
| CA-04 | Leer `02·F8` y `02·F9` | CP-004 |
| CA-05 | Leer `02/base.md`, el anexo de `02·F12` y `13·DOC12` | CP-005 |
| CA-06 | Leer la plantilla del plan | CP-006 |
| CA-07 | Leer `13·DOC24` y la plantilla del análisis | CP-007 |

## 6. Datos y ambiente de prueba

El repositorio del estándar, y una carpeta temporal con una épica, una HU, una fase y un pendiente de prueba.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 47.0.0 con el instalador. Las fases cerradas no cambian; la regla rige para lo que se ejecute desde esa versión.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `02·F9`, `02·F12`, `02·F28`, `13·DOC12`, `13·DOC24`, `20·M10`, `20·M12`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que una fase cerrada de antes empiece a fallar | Solo falla si su pendiente tiene hoy un análisis abierto posterior al que cita; lo prueba el CP-002 sobre el repositorio |

## 11. Definition of Done

- [ ] CA-01 a CA-07 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 47.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
