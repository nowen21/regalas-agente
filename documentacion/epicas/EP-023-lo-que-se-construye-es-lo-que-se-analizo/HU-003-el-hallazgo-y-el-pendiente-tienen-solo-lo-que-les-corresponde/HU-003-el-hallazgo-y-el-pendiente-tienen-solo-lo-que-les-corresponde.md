# HU-003 · El hallazgo y el pendiente tienen solo lo que les corresponde

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), puntos 7, 10, 11, 12, 19, 20 y 21, del [análisis 8](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), punto 10, del [análisis 11](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-11.md), punto 4, y del [análisis 13](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-13.md), puntos 1 a 4. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `base/13-documentacion/`, `base/20-meta-reglas/`, `plantillas/`, `validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 4 de 7 |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Lista: aprobada el 2026-10-02 |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que el hallazgo y el pendiente tengan solo lo que les corresponde
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Del [problema de la épica](../epica.md#31-situación-actual), esta HU resuelve que el hallazgo y el pendiente cargan campos que son del análisis ([análisis 4](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Son las conclusiones de las que salen los puntos de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | El hallazgo tiene solo «Qué pasó» y «Por qué importa», más el enlace a su pendiente | Análisis 1, conclusiones 14 y 34 |
| RN-02 | El pendiente tiene solo «De dónde sale», «El problema» y «Por qué importa» | Análisis 1, conclusión 15 |
| RN-03 | Quien dice que algo cerró es el plan, al cumplirse | Análisis 1, conclusión 16 |
| RN-04 | El pendiente vive dentro de lo que lo genera; mientras no se sepa, en la carpeta del resumen del día. Es una carpeta con `pendiente.md` y sus análisis | Análisis 1, conclusiones 11 y 20 |
| RN-05 | Si un hallazgo quedó anotado, si se resolvió y por dónde se retoma se calcula siguiendo los enlaces | Análisis 1, conclusión 35 |
| RN-06 | Un pendiente cierra cuando cierra el plan que salió de él, también entre proyectos | Análisis 1, conclusión 36 |
| RN-07 | Los pendientes cerrados no se tocan; los abiertos pasan a la forma nueva cuando se vayan a trabajar; los nuevos nacen con ella | Análisis 1, conclusión 38 |
| RN-08 | Cada análisis aprobado mejora a su pendiente: lo deja en su versión siguiente, con su hallazgo y lo que precisó | Análisis 11, acuerdo 5 |
| RN-09 | El proyecto reporta el pendiente a la HU del estándar que citan la regla o el programa que fallan; si no la citan, va al resumen del día del estándar. La HU de origen se cita cuando el análisis de un pendiente decide a cuál pertenece | Análisis 13, acuerdos 1 y 2 |
| RN-10 | El aviso de resuelto sale cuando la fase que cumple el plan del pendiente anota su commit, y va al lado del pendiente de seguimiento del proyecto; el seguimiento cierra cuando el proyecto comprueba la corrección | Análisis 13, acuerdos 3 y 4 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · El pendiente vive dentro de lo que lo genera

**Sale de:** análisis 1, punto 7.

```gherkin
Dado un pendiente nuevo
Cuando se anota
Entonces vive dentro de lo que lo genera, y no en pendientes/
```

**Cómo validarlo:**
1. Leer la regla que dice dónde vive el pendiente.

**Aprobado cuando:** dice lo del criterio.

### CA-02 · Las plantillas del hallazgo y del pendiente tienen solo sus campos

**Sale de:** análisis 1, punto 10.

```gherkin
Dado que se abren las plantillas del hallazgo y del pendiente
Cuando se leen sus campos
Entonces el hallazgo tiene «Qué pasó» y «Por qué importa»
Y el pendiente tiene «De dónde sale», «El problema» y «Por qué importa»
```

**Cómo validarlo:**
1. Abrir las plantillas del hallazgo y del pendiente en `plantillas/`.

**Aprobado cuando:** no piden otros campos.

### CA-03 · Los validadores no exigen los campos viejos

**Sale de:** análisis 1, punto 11.

```gherkin
Dado un hallazgo y un pendiente con solo sus campos
Cuando se corren los validadores
Entonces pasan
```

**Cómo validarlo:**
1. Correr los validadores del hallazgo y del pendiente sobre un hallazgo y un pendiente con solo sus campos.

**Aprobado cuando:** pasan.

### CA-04 · El cierre lo marca el plan

**Sale de:** análisis 1, punto 12.

```gherkin
Dado un plan que se cumplió
Cuando se consulta el estado del hallazgo y del pendiente de los que salió
Entonces aparecen cerrados sin que nadie lo haya escrito en ellos
```

**Cómo validarlo:**
1. Consultar el estado de un pendiente cuyo plan se cumplió.

**Aprobado cuando:** aparece cerrado y su archivo no cambió.

### CA-05 · El hallazgo de dos campos, con estado y retoma calculados

**Sale de:** análisis 1, punto 19.

```gherkin
Dado que 13·DOC22, la plantilla sesion.md y resumen.py piden el hallazgo de dos campos más el enlace a su pendiente
Cuando resumen.py revisa un hallazgo
Entonces calcula su estado y por dónde se retoma siguiendo los enlaces
```

**Cómo validarlo:**
1. Abrir [`13·DOC22`](../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) y `plantillas/sesion.md`.
2. Correr `validadores/resumen.py` sobre un resumen.

**Aprobado cuando:** la regla y la plantilla piden lo del criterio, y el programa da el estado y la retoma.

### CA-06 · El pendiente sin «Proyecto de origen»

**Sale de:** análisis 1, punto 20.

```gherkin
Dado que las plantillas del pendiente, pendientes.py y 02·F24 se ajustan al pendiente reducido
Cuando se busca «Proyecto de origen»
Entonces ninguno lo exige
Y el pendiente de seguimiento cierra cuando cierra el plan de su padre
```

**Cómo validarlo:**
1. Buscar «Proyecto de origen» en las plantillas del pendiente, en `validadores/pendientes.py` y en [`02·F24`](../../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md).
2. Consultar un pendiente de seguimiento cuyo padre cerró su plan.

**Aprobado cuando:** ninguno lo exige y el seguimiento aparece cerrado.

### CA-07 · `pendientes/` queda como historia

**Sale de:** análisis 1, punto 21.

```gherkin
Dado un proyecto con la versión nueva
Entonces pendientes/ no recibe pendientes nuevos
Y los validadores aceptan ahí el formato viejo
Y el instalador no la crea en proyectos nuevos
Y 02·F13 y 20·M13 lo dicen
Y los pendientes cerrados y sus enlaces no se tocan
```

**Cómo validarlo:**
1. Leer [`02·F13`](../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) y `20·M13`.
2. Correr `validadores/pendientes.py` sobre `pendientes/`.
3. Correr `validadores/instalar.py` sobre un proyecto nuevo.

**Aprobado cuando:** las reglas dicen lo del criterio, los pendientes viejos pasan, el proyecto nuevo no tiene `pendientes/` y los cerrados no cambiaron.

### CA-08 · La carpeta `pendientes/` vive dentro de lo que origina cada pendiente

**Sale de:** análisis 8, punto 10.

```gherkin
Dado un pendiente
Entonces vive en una carpeta pendientes/ dentro de lo que lo origina: una épica, una HU o el resumen del día mientras su análisis no decide a dónde va
Y dentro de ella, en su propia carpeta, con pendiente.md y sus análisis
Y el número es uno solo en todo el proyecto
Y un programa arma el índice de todos, con su número, dónde viven y si su plan cerró
Y el validador de fases acepta pendientes/ dentro de una épica, de una HU o de un resumen del día
Y los cerrados no se tocan (CA-07)
```

**Cómo validarlo:**
1. Correr el validador de fases.
2. Correr el programa del índice.

**Aprobado cuando:** el validador de fases pasa y el índice lista todos.


### CA-09 · Cada análisis deja el pendiente en su versión siguiente

**Sale de:** análisis 11, punto 4.

```gherkin
Dado un análisis que se va a aprobar
Cuando su hallazgo no está en «De dónde sale» de su pendiente
Entonces el análisis no se aprueba, y el aviso dice qué falta
Y al aprobarse, el pendiente queda en su versión siguiente, con el hallazgo sumado y «El problema» y «Por qué importa» con lo que el análisis precisó
```

**Cómo validarlo:**
1. Intentar aprobar un análisis cuyo hallazgo falta en el pendiente.
2. Leer la «Propuesta final» de la plantilla del análisis.

**Aprobado cuando:** la aprobación se niega y dice qué falta, y la plantilla pide el pendiente en su versión siguiente.

### CA-10 · El proyecto reporta el pendiente a la HU que lo originó

**Sale de:** análisis 13, puntos 1 y 2.

```gherkin
Dado un proyecto que encuentra un defecto del estándar
Cuando la regla o el programa que falla cita su HU
Entonces el pendiente nace en esa HU del estándar
Y si no la cita, nace en el resumen del día del estándar
Y cuando el análisis de un pendiente decide a qué HU pertenece, la regla o el programa la citan desde ahí
```

**Cómo validarlo:**
1. Leer `02·F24`.
2. Reportar un defecto de una regla que cita su HU y otro de una que no la cita.

**Aprobado cuando:** `02·F24` lo dice, el primero queda en la HU y el segundo en el resumen del día.

### CA-11 · El proyecto se entera cuando su pendiente se resuelve

**Sale de:** análisis 13, puntos 3 y 4.

```gherkin
Dado un pendiente que reportó un proyecto
Cuando la fase que cumple su plan anota su commit
Entonces queda un aviso al lado del pendiente de seguimiento del proyecto, encontrado por los enlaces
Y el seguimiento cierra solo cuando el proyecto comprueba la corrección
```

**Cómo validarlo:**
1. Anotar el commit de la fase que cumple el plan de un pendiente reportado.
2. Consultar el estado del seguimiento antes y después de comprobarlo.

**Aprobado cuando:** el aviso aparece al lado del seguimiento, y este cierra solo después de comprobarlo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | N/A |
| RNF-02 | **Seguridad** | N/A |
| RNF-03 | **Auditoría** | N/A |
| RNF-04 | **Accesibilidad** | N/A |
| RNF-05 | **Compatibilidad** | N/A |
| RNF-06 | **Trazabilidad** | Cada criterio cita el punto de lo que se tiene que hacer del que sale (análisis 1, conclusión 39) |

---

## 6. Diseño y referencias

| Campo | Valor |
|---|---|
| Documento funcional | [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md). |
| Mockup / Prototipo | N/A |
| Contrato de API | N/A |

---

## 7. Tareas técnicas derivadas

Las fija el plan de cada fase (`02·F14`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo`](A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo/estado-fase.md) | CA-01 a CA-08 | HU-001 | [plan](A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo/plan_trabajo.md) | [pruebas](A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo/plan_pruebas.md) | [resultado](A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo/resultado_pruebas.md) | Cumple |
| [`B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente`](B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente/estado-fase.md) | CA-09 | Fase A | [plan](B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente/plan_trabajo.md) | [pruebas](B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente/plan_pruebas.md) | [resultado](B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente/resultado_pruebas.md) | Cumple |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [ ] Diseño / mockup disponible: N/A
- [ ] Dependencias identificadas y desbloqueadas: depende de la HU-001
- [x] Estimada
- [ ] Cumple criterios INVEST: no es independiente

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Pruebas pasando
- [ ] `VERSION` y `CHANGELOG.md` actualizados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☐ | Depende de la HU-001 |
| **N**egociable | ✅ | |
| **V**aliosa | ✅ | |
| **E**stimable | ✅ | Talla M |
| **S**mall (pequeña) | ☐ | Siete criterios: puede pedir más de una fase |
| **T**esteable | ✅ | Cada criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU, corregida según el análisis 3 |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Nace el CA-08, sobre la carpeta `pendientes/` dentro de lo que origina cada pendiente, según el análisis 8. La aprobación queda sin efecto hasta que se revise |
| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con los cambios del análisis 8 |
| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Sale del CA-08 el traslado de los pendientes viejos y del 103: lo agregó el agente sin origen en el análisis 8. Lo acordado es que pasan a la forma nueva cuando se vayan a trabajar (análisis 1, conclusión 38). La aprobación queda sin efecto hasta que se revise |
| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con el CA-08 sin el traslado |
| 2026-10-03 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Nace el CA-09, según el análisis 11. La aprobación queda sin efecto hasta que se revise |
| 2026-10-03 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con el CA-09 del análisis 11 |
| 2026-10-03 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Nacen el CA-10 y el CA-11, según el análisis 13. La aprobación queda sin efecto hasta que se revise |
| 2026-10-03 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con el CA-10 y el CA-11 del análisis 13 |
