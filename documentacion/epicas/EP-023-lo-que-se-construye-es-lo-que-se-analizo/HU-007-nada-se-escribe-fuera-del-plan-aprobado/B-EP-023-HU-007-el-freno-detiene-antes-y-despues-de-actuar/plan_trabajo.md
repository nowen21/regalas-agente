# Plan de Trabajo · Fase `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar` (módulo `validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), una sola (`F12.1`) |
| **Módulo** | `validadores/`, `adaptadores/claude-code/` |
| **Especificación del módulo** | El CA-02 de la HU-007, en sus capas 1 y 2 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda de tres fases de la HU-007. Sale del punto 26 del [análisis 1](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (acuerdos 18, 44 y 46), del punto 1 del [análisis 8](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md) (acuerdos 1, 2 y 3) y del punto 3 del [análisis 10](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md) (acuerdo 6). **Versión 2**, del [análisis 11](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-11.md) (puntos 1 a 3): suma `autorizado.py` y su prueba, por el hallazgo H-14. La capa 3, el commit, quedó en la fase `A`; la capa 4 y el contrato de cada adaptador van en la fase `C`.

**Carencias que cierra** (`02·F14` Q3): el freno solo mira la herramienta de escritura y solo frena lo que sale del proyecto; no compara con el plan, no ve la consola, el segundo plano ni lo que publica, y nadie anota el hallazgo.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 50.0.0. La versión 2 la aprobó con el análisis 11, que fija lo que cambia (acuerdo 1).

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-007 | Estado |
|---|---|
| CA-02 · El freno detiene lo que no está en el plan ni autorizado, por cualquier canal | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que antes de cada acción el freno detenga lo que no está en el plan de la fase en curso ni lo autoriza una regla, por cualquier canal; que después de cada orden de consola compare lo que cambió con el plan; y que al detener anote el hallazgo y mande volver al análisis.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-02 (capa 1) | Antes de actuar: herramienta de escritura, consola, segundo plano, instalaciones, procesos que quedan corriendo y lo que se publica | Enganche y programa | Alta |
| CA-02 (capa 2) | Después de cada orden de consola: lo que cambió en git contra el plan | Enganche y programa | Media |
| CA-02 (fase activa) | La fase en curso decide contra qué se compara | Programa | Baja |

**Fuera de alcance:** la integración continua y el contrato de cada adaptador (fase `C`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 50.0.0:

- `adaptadores/claude-code/hook_antes.py` corre antes de `Write`, `Edit`, `MultiEdit` y `NotebookEdit`, y solo detiene la escritura que sale de la carpeta del proyecto. No ve la consola ni el segundo plano.
- `validadores/acuerdos.py` ya dice qué fases están en curso; `validadores/autorizado.py` dice qué regla autoriza una ruta, y `validadores/plan_vs_hecho.py` lee las rutas exactas del plan y su aprobación.
- Ningún programa anota hallazgos; el resumen de la sesión lo encuentra `hook_resumen.py` por la marca de sesión de la transcripción.
- Las HU, las épicas y los pendientes se escriben fuera de una fase, y ninguna regla autoriza escribirlos: ni `13·DOC15`, ni `13·DOC16`, ni `02·F23` traen la línea «Autoriza escribir».
- Los análisis 9 y 10 mandaron corregir cosas «de una y sin fase»; sus filas de «Lo que se tiene que hacer» no nombran las rutas que tocan.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/freno.py` | Nuevo | Programa | Clasifica la acción, saca sus destinos, decide si se permite y anota el hallazgo |
| `adaptadores/claude-code/hook_antes.py` | Modificar | Enganche | Capa 1, sobre toda acción |
| `adaptadores/claude-code/hook_despues.py` | Nuevo | Enganche | Capa 2, después de cada orden de consola |
| `validadores/instalar.py` | Modificar | Instalador | El enganche de antes sobre toda acción y el de después sobre la consola |
| `base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md`, `base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md`, `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | Modificar | Regla | Su línea «Autoriza escribir» y su sello |
| `plantillas/analisis.md` | Modificar | Plantilla | La fila que se hace «de una y sin fase» nombra sus rutas exactas |
| `validadores/autorizado.py` | Modificar | Programa | Solo la regla vigente autoriza: la derogada y la *opt-in* apagada no (versión 2) |
| `validadores/tests/test_nada_fuera_del_plan.py` | Modificar | Pruebas | Lo autorizado se prueba con reglas de ejemplo, sin nombres ni cantidad fijos (versión 2) |
| `validadores/tests/test_el_freno.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa nuevo |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 51.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| El freno compara con el plan de la fase en curso | Todo proyecto con la versión nueva | Fuera de una fase en curso solo deja lo que una regla autoriza |
| `hook_antes.py` corre sobre toda acción | Todo proyecto, al reinstalar | El de hoy sigue frenando lo que sale del proyecto |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El freno corre antes de toda acción y la clasifica por su efecto: escribe, borra, ejecuta o publica | Mirar solo la herramienta de escritura | Una regla rige en todas partes, no solo donde un programa la mira | Análisis 8, acuerdos 1 y 3 |
| Compara con la fase en curso: antes de aprobarse su plan, deja solo los documentos de la fase y lo que una regla autoriza; aprobado, también lo que el plan declara; sin fase en curso, solo lo autorizado | Comparar solo cuando hay plan aprobado | Así lo acordó el usuario | Análisis 10, acuerdo 6 |
| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |
| Solo la regla vigente autoriza: la que lleva `[DEROGADA…]` en su título y la *opt-in* de un capítulo apagado no | Leer todas las líneas | Una regla que sale deja de autorizar sin tocar el programa | Análisis 11, acuerdos 2 y 3 |
| La prueba de lo autorizado usa reglas de ejemplo, sin nombres ni cantidad fijos | Una lista fija de reglas | Si entra o sale una regla, nada se rompe | Análisis 11, acuerdo 4 |
| `13·DOC15`, `13·DOC16` y `02·F23`, que mandan escribir la HU, la épica y el pendiente, suman su línea «Autoriza escribir» | Frenarlos hasta que haya una fase | Lo que una regla manda hacer no se frena, y su entrada se agrega en el mismo cambio | Análisis 1, acuerdo 46 |
| Lo que un análisis aprobado manda hacer «de una y sin fase» no se frena: mientras ese análisis está prendido, el freno deja pasar las rutas exactas que nombra su fila, y la plantilla del análisis pide nombrarlas | Exigir una fase para todo | El usuario ya lo autorizó en el análisis; falta que un programa lo pueda leer | Propuesta del agente |
| Al detener, anota el hallazgo en el resumen de la sesión y el mensaje dice que la ejecución vuelve al análisis | Solo detener | El hallazgo detiene y vuelve al análisis | Análisis 1, acuerdos 18 y 44 |
| En la consola lee la orden: redirecciones, órdenes que crean, copian, mueven o borran, y las de git que descartan cambios; resuelve la ruta real antes de comparar (`..`, `~`, variables y enlaces) | Comparar el texto de la orden tal cual | Las rutas que engañan hacen creer que algo queda adentro | Análisis 8, acuerdo 3 |
| Detiene la corrida en segundo plano, la instalación de paquetes, la configuración global y el proceso que queda corriendo después del turno | Dejarlos pasar | Escriben fuera del proyecto o actúan sin que nadie mire | Análisis 8, acuerdo 3 |
| Lo que se publica fuera del proyecto se pregunta cada vez | Dejarlo pasar | Publicar no se deshace | Análisis 8, acuerdo 3 |
| La capa 2 compara lo que cambió en git con una foto tomada justo antes de la orden, guardada en `.git/` | Comparar todo lo que está sin guardar | Lo que ya estaba cambiado, por ejemplo de otra sesión, no lo hizo esta orden | Propuesta del agente |
| Antes de correr pruebas no hay un paso aparte: la orden pasa por la capa 1, y lo que escribió la revisa la capa 2 | Un paso que compare todo antes de las pruebas | Con la capa 2 después de cada orden, lo escrito antes de las pruebas ya quedó comparado | Propuesta del agente |
| Lo que un programa escribe por dentro fuera del proyecto no se ve; queda declarado en el contrato del adaptador | Prometer que se ve | Leyendo la orden no se puede saber | Análisis 8, acuerdo 3 |
| La versión sube a 51.0.0, MAYOR | MENOR | El agente deja de poder escribir fuera del plan | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Las dos que había las resuelve el acuerdo 46 del análisis 1: el freno solo detiene lo que no está autorizado en ninguna parte.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Antes de actuar | Solo la escritura fuera del proyecto | Toda acción, contra el plan de la fase en curso y lo autorizado | `02·F8`, `04·S9` |
| Después de actuar | Nada | Lo que cambió en git contra el plan | `02·F8` |
| Hallazgo del freno | Nadie lo anota | Queda en el resumen de la sesión | `13·DOC22` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-02 · El freno detiene lo que no está en el plan ni autorizado, por cualquier canal

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `freno.py`: qué permite la fase en curso; la ruta real; los destinos de una orden de consola; lo que nunca se deja (segundo plano, instalaciones, configuración global, procesos que quedan corriendo); qué herramienta publica | `validadores/freno.py` | CA-02 | Lo usan los dos enganches | 3 h | Ninguna | CP-001 a CP-003 |
| T-02 | `freno.py` anota el hallazgo en el resumen de la sesión: qué pasó y por qué importa | `validadores/freno.py` | CA-02 | El resumen de cada sesión | 1 h | T-01 | CP-005 |
| T-03 | Sumar la línea «Autoriza escribir» a `13·DOC15` (las HU), `13·DOC16` (las épicas) y `02·F23` (los pendientes), con sus sellos contra 51.0.0, y regenerar el mapa de tareas | Las tres reglas de la tabla 2.1 | CA-02 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001 |
| T-04 | La plantilla del análisis pide que la fila «de una y sin fase» nombre sus rutas exactas; `freno.py` las deja pasar mientras ese análisis está prendido | `plantillas/analisis.md`, `validadores/freno.py` | CA-02 | Los análisis nuevos | 1 h | T-01 | CP-001 |
| T-05 | `hook_antes.py` corre sobre toda acción: detiene lo no permitido, pregunta lo que se publica, y al detener anota el hallazgo; toma la foto de git antes de cada orden de consola | `adaptadores/claude-code/hook_antes.py` | CA-02 | Toda acción del agente | 1,5 h | T-02 | CP-001 a CP-003, CP-005 |
| T-06 | `hook_despues.py`: después de cada orden de consola compara lo que cambió con la foto y avisa el hallazgo | `adaptadores/claude-code/hook_despues.py` | CA-02 | Toda orden de consola | 1 h | T-05 | CP-004 |
| T-07 | El instalador pone el enganche de antes sobre toda acción y el de después sobre la consola | `validadores/instalar.py` | CA-02 | Todo proyecto, al reinstalar | 0,3 h | T-06 | CP-001 |

### Versión 2 · El H-14

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-09 | `autorizado.py` lee el estado de cada regla en ella misma y solo usa la vigente | `validadores/autorizado.py` | CA-02 | Lo usan el `pre-commit` y el freno | 0,5 h | T-03 | CP-001 |
| T-10 | La prueba de lo autorizado comprueba con reglas de ejemplo que la vigente autoriza y la derogada o apagada no | `validadores/tests/test_nada_fuera_del_plan.py` | CA-02 | Ninguno | 0,5 h | T-09 | CP-001 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Escribir los casos del plan de pruebas; el programa en el mapa del sitio; la fila de la fase en la HU; subir a 51.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_el_freno.py`, `anatomia/mapa-del-sitio.md`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md`, `CHANGELOG.md`, `VERSION` | CA-02 | Todo proyecto adopta la versión | 1 h | T-01 a T-07 | CP-001 a CP-006 |

## 4. Secuencia de ejecución

T-01 a T-03, T-09 y T-10, y T-04; después T-05, T-06 y T-07; al final T-08, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-02 | Intentar escribir fuera del plan con la herramienta, la consola, un programa y en segundo plano; escribir algo autorizado; escribir código con el plan sin aprobar | CP-001 a CP-005 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba con git en una carpeta temporal, con una épica, una HU, una fase en curso con su plan, y reglas que autorizan escribir.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y reinstalar.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 51.0.0 con el instalador, que pone los dos enganches. Desde ahí, el agente solo escribe lo que el plan de la fase en curso declara o lo que una regla autoriza.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `02·F9`, `04·S9`, `04·S10`, `00·N1`, `13·DOC22`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el freno detenga una lectura | Las órdenes que no escriben pasan; la prueba cubre las de lectura más comunes |
| Que una orden escriba por una forma que el freno no reconoce | La capa 2 la ve después, dentro del proyecto |
| Que un error del freno detenga el trabajo | Si algo falla adentro, deja pasar y lo avisa |

## 11. Definition of Done

- [ ] CA-02, en sus capas 1 y 2, con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 51.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
