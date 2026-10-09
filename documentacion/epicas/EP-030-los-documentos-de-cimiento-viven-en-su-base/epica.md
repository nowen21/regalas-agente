# EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 142](../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), aprobado el 2026-10-08. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-030 |
| **Planteamiento de origen** | El [pendiente 142](../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/pendiente.md): los documentos de Cimiento viven en su base, con un comando fijo por cada tipo, y dejan de ser archivos .md |
| **Iniciativa / Objetivo estratégico** | Que Cimiento guarde todo en su base y deje de resolver cada operación con un guion nuevo |
| **Producto / Sistema** | Cimiento, sus enganches, sus validadores y el instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | XXL: nueve HU |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | En curso |

## 2. Resumen ejecutivo

Cada tipo de documento de Cimiento (pendiente, análisis, épica, HU, documentos de fase, transcripción, resumen, plantilla, nota) pasa a una tabla de la base, partido en campos, con un comando fijo para crearlo, verlo, editarlo y listarlo. Los cambios se revisan y se aprueban en la pantalla de Cimiento. Los programas que hoy escriben y leen .md pasan a usar esas tablas por un solo camino, y los archivos se borran tipo por tipo. Al final, los proyectos que heredan guardan sus documentos en la misma base.

## 3. Problema y oportunidad

### 3.1 Situación actual

Hay 3.005 .md (24,9 MB). La base guarda `base/` y la memoria, pero no las épicas, HU, fases, análisis, pendientes, transcripciones ni resúmenes. Unos 25 programas escriben .md y 28 de los 53 validadores los leen buscando marcas de texto. Sin comando fijo, cada operación termina en un guion: hay 250 en `historico-chat/scripts/`.

### 3.2 Impacto de no hacerlo

Sigue el código repetido de un solo uso, y donde hay archivo y base a la vez una copia se queda vieja.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-1 de la sesión del 2026-10-08](../../../historico-chat/resumenes/2026-10-08/los-documentos-de-cimiento-pasan-a-su-base.md) | Los documentos de Cimiento pasan a la base y dejan de ser archivos .md |

## 4. Objetivo y propuesta de valor

**Objetivo:** que ningún documento de Cimiento sea un archivo .md y que cada operación sobre ellos sea un comando fijo.

**Hipótesis de valor:**
> Creemos que tablas con campos y comandos fijos por tipo lograrán que no haga falta escribir guiones para operar los documentos. Lo sabremos cuando `historico-chat/scripts/` deje de recibir guiones para crear o cambiar documentos.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien administra Cimiento | Ve, busca y aprueba los documentos en la pantalla | Cualitativo |
| El mantenimiento de Cimiento | Menos código repetido | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un solo camino para leer y escribir documentos, y comandos fijos por tipo.
- La revisión y aprobación de los cambios en la pantalla.
- Tablas con campos para pendientes, análisis, épicas, HU, documentos de fase, transcripciones, resúmenes, plantillas, notas, prompts, anatomía, `CHANGELOG.md` y señales.
- Pasar los .md existentes y borrarlos tipo por tipo.
- Quitar los README de índice y `CLAUDE.md`.
- Reescribir las reglas que hablan de archivos.
- Los proyectos que heredan.

### 5.2 Fuera del alcance

- Los `.py`, que siguen como archivos (acuerdo 1).

### 5.3 Diferido a fases posteriores

- Ninguno.

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Quien administra Cimiento | Revisa y aprueba los cambios | Verlos en la pantalla |
| Claude | Crea y cambia documentos | Un comando fijo por operación |

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01**: cada tipo de documento tiene su tabla con campos y sus comandos fijos.
- [ ] **CAE-02**: los cambios de documentos se revisan y se aprueban en la pantalla.
- [ ] **CAE-03**: ningún documento de Cimiento queda como archivo .md.
- [ ] **CAE-04**: los proyectos que heredan guardan sus documentos en la base de Cimiento.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Archivos .md de Cimiento en git | 3.005 | 0 | Al cerrar la HU-007 | `git ls-files '*.md'` |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo/HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md) | Un solo camino para leer y escribir documentos, con un comando fijo por tipo | Must | L | No aplica | Terminada |
| [HU-002](HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla/HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md) | Los cambios de los documentos se revisan y se aprueban en la pantalla | Must | M | No aplica | Terminada |
| [HU-003](HU-003-los-pendientes-y-los-analisis-viven-en-la-base/HU-003-los-pendientes-y-los-analisis-viven-en-la-base.md) | Los pendientes y los análisis viven en la base, partidos en campos | Must | L | No aplica | Pendiente |
| [HU-004](HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base/HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base.md) | Las épicas, las HU y los documentos de cada fase viven en la base, partidos en campos | Must | XL | No aplica | Pendiente |
| [HU-005](HU-005-las-transcripciones-y-los-resumenes-de-sesion-viven-en-la-base/HU-005-las-transcripciones-y-los-resumenes-de-sesion-viven-en-la-base.md) | Las transcripciones y los resúmenes de sesión viven en la base | Must | M | No aplica | Pendiente |
| [HU-006](HU-006-las-plantillas-notas-prompts-y-senales-viven-en-la-base/HU-006-las-plantillas-notas-prompts-y-senales-viven-en-la-base.md) | Las plantillas, notas, prompts, anatomía, CHANGELOG y señales viven en la base | Must | M | No aplica | Pendiente |
| [HU-007](HU-007-los-indices-readme-y-claude-md-desaparecen/HU-007-los-indices-readme-y-claude-md-desaparecen.md) | Los índices README y CLAUDE.md desaparecen | Must | S | No aplica | Pendiente |
| [HU-008](HU-008-las-reglas-hablan-de-registros-de-la-base-no-de-archivos/HU-008-las-reglas-hablan-de-registros-de-la-base-no-de-archivos.md) | Las reglas hablan de registros de la base, no de archivos | Must | M | No aplica | Pendiente |
| [HU-009](HU-009-los-proyectos-que-heredan-guardan-sus-documentos-en-la-base/HU-009-los-proyectos-que-heredan-guardan-sus-documentos-en-la-base.md) | Los proyectos que heredan guardan sus documentos en la base de Cimiento | Must | L | No aplica | Pendiente |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Una app nueva para los documentos | Nuevo | Las tablas, el camino único y los comandos |
| `core/herramientas/` (andamio, fase, cerrar, instalar) | Modificado | Escriben en la base |
| `core/enganches/` (freno, historico, resumen, analisis_en_curso, plan_vs_hecho, acuerdos, origen) | Modificado | Leen y escriben en la base |
| `core/validadores/` | Modificado | 28 subcomandos leen de la base |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: están en «Lo acordado» del análisis 1 del pendiente 142.

### 10.3 Integraciones

Ninguna nueva.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Usabilidad** | La pantalla se entiende sin saber del tema (`00·ID7`) |
| **Rendimiento** | Los enganches leen de la base sin arrancar Django |
| **Seguridad** | N/A |
| **Disponibilidad** | Sin base, los enganches avisan y no se caen |
| **Auditoría y trazabilidad** | Cada cambio queda en `Cambio`, con su antes y su después |
| **Escalabilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- Se paga: los guiones de un solo uso y los 404 README de índice.

## 11. Cumplimiento y normativa

N/A.

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | El botón de la EP-026·HU-007 | Interna | Agente | HU-002 | Abierta |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | Al cambiar un tipo, un programa que lo lee queda leyendo archivos que ya no existen | Alta | Alto | En cada etapa se buscan todos los que leen ese tipo antes de borrar | Agente |
| R-02 | Se pierde la historia que hoy guarda git | Media | Alto | `Cambio` guarda cada cambio y la base se copia cada día (EP-026·HU-010) | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- La base de Cimiento está disponible donde se trabaja.

**Restricciones**
- `20·M10`: la HU-009 es un cambio MAYOR.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | Todo lo demás se apoya en ella | Terminada |
| 2 | HU-002 | HU-001 | Ningún documento pasa sin poder revisarse | Terminada |
| 3 | HU-003 | HU-001, HU-002 | Etapa 2 del acuerdo 3 | Pendiente |
| 4 | HU-004 | HU-003 | Etapa 3 | Pendiente |
| 5 | HU-005 | HU-003 | Etapa 4 | Pendiente |
| 6 | HU-006 | HU-004 | Etapa 5 | Pendiente |
| 7 | HU-007 | HU-006 | Etapa 6 | Pendiente |
| 8 | HU-008 | HU-007 | Las reglas se reescriben cuando lo que describen ya cambió | Pendiente |
| 9 | HU-009 | HU-008 | Acuerdo 4: al final | Pendiente |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | Tablas nuevas; un comando pasa los .md existentes antes de borrarlos |
| Plan de reversión | Revertir el commit de la HU; los .md se recuperan de git |
| Capacitación y gestión del cambio | N/A |
| Soporte post-despliegue | N/A |

## 17. Definition of Ready (épica)

- [x] Problema y objetivo validados con el negocio
- [x] Alcance delimitado (dentro y fuera)
- [x] Métricas de éxito definidas y medibles
- [x] Historias de usuario identificadas
- [x] Dependencias y riesgos registrados
- [x] Viabilidad técnica evaluada
- [x] Capacidad confirmada

## 18. Definition of Done (épica)

- [ ] Todas las HU obligatorias completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica entregada
- [ ] Métricas midiendo

## 19. Referencias

- [Análisis 1 del pendiente 142](../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | Agente | Creación de la épica desde el análisis aprobado |
