# Plan de Trabajo · Fase `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis` (módulo `validadores/` y el adaptador)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), una sola (`F12.1`) |
| **Módulo** | `validadores/` y el adaptador de la herramienta |
| **Especificación del módulo** | Las reglas de negocio RN-04 a RN-06 de la HU-001 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Continúa la [fase `A`](../A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador/funcionalidad_implementada.md), que dejó la plantilla del análisis; esta fase hace que la conversación pase sola a él.

**Carencias que cierra** (`02·F14` Q3): la última frase del problema del [pendiente](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md): lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis.

**Aprobación** (`02·F4`): el usuario aprobó este plan y el de pruebas el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió seguir con las fases el 2026-10-01 y escribir esta con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-001 | Estado |
|---|---|
| CA-03 · La conversación pasa al análisis en tiempo real | ☐ |
| CA-09 · La conversación copiada cumple `00·ID8` | ☐ |
| CA-10 · La herramienta es del estándar y lee el análisis prendido | ☐ |
| CA-11 · Prender, pausar y apagar | ☐ |
| CA-12 · Cada turno avisa a qué análisis entra | ☐ |
| CA-13 · Las etiquetas de la herramienta no entran | ☐ |
| CA-14 · No se prende otro pendiente con un análisis abierto | ☐ |
| CA-15 · El instalador registra la herramienta | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la conversación pase sola al análisis prendido, que se prenda, se pause y se apague con las palabras acordadas, y que cada proyecto la reciba con el instalador.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-10, CA-15 | La herramienta en el adaptador, registrada por el instalador | Funcional | Media |
| CA-11, CA-14 | Prender, pausar, apagar y no prender otro pendiente | Funcional | Alta |
| CA-03, CA-09, CA-13 | Pasar la conversación sin tocar lo agregado, sin marcas ni etiquetas | Funcional | Media |
| CA-12 | El aviso de cada turno | Funcional | Baja |

**Fuera de alcance:**

- Llenar la copia del hallazgo y del pendiente en el análisis nuevo: la escribe el agente desde la plantilla.
- El análisis principal de Cimiento (fase `C`).
- Los criterios de las HU 2 a 7.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02:

- La conversación la pasa hoy [`pasar_conversacion.py`](../../../../../historico-chat/scripts/2026-09-30/pasar_conversacion.py), registrado a mano en `.claude/settings.json` en `UserPromptSubmit` y en `Stop`. Lee `historico-chat/.estado/analisis-en-curso.txt` (análisis, transcripción y turno de inicio), cambia la raya del encabezado por coma, quita las etiquetas de texto pegado y de archivo abierto, copia solo entre la sección «Conversación» y la línea «acá termina la conversación», y borra el estado cuando ve la marca «Aprobado». No tiene palabras, aviso ni pausa, y el estado se escribe a mano.
- Los enganches viven en `adaptadores/claude-code/` y cargan los módulos de `validadores/`; el trabajo que no depende de la herramienta va en `validadores/` (modelo: `hook_reglas.py` con `recuperar.py`).
- `validadores/recuperar.py` ya lee con qué palabra abre cada frase (`palabras_de_inicio`).
- `validadores/instalar.py` registra los enganches de la lista `HOOKS_CLAUDE`, con evento, guion, mensaje y argumentos.
- `historico-chat/.estado/` está fuera de git (`.gitignore`).
- `anatomia/que-esta-amarrado-a-la-herramienta.md` clasifica cada enganche (lo revisa `validar.py amarre`) y `anatomia/mapa-del-sitio.md` los lista.
- `VERSION` dice 40.0.0.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/analisis_en_curso.py` | Nuevo | Validador | Estado, prender, pausar, apagar, pasar la conversación, análisis abiertos y plan cumplido |
| `adaptadores/claude-code/hook_analisis.py` | Nuevo | Adaptador | Lee el mensaje, llama al módulo y entrega el aviso |
| `validadores/instalar.py` | Modificar | Validador | Suma el enganche en `UserPromptSubmit` y en `Stop` |
| `.claude/settings.json` | Modificar | Adaptador | El instalador cambia las dos entradas del guion intermedio por el enganche |
| `validadores/tests/test_analisis_en_curso.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` y `anatomia/mapa-del-sitio.md` | Modificar | Documentación | Clasifican y nombran el enganche y el módulo |
| `VERSION` y `CHANGELOG.md` | Modificar | Estándar | 40.1.0, MENOR |
| Los documentos de esta fase, la HU-001 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo | Cambio de contrato | Lo que depende | Dónde rompe |
|---|---|---|---|
| `validadores/instalar.py` | Suma dos entradas a `HOOKS_CLAUDE` | Las pruebas que cuentan enganches | Se ajustan si cuentan |
| `pasar_conversacion.py` | Deja de estar registrado | Nada: no lo importa nadie | No rompe; se conserva como guion de apoyo (`04·S18`) |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: no hay rutas.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: las palabras del mensaje son el punto de entrada.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La lógica va en `validadores/analisis_en_curso.py` y el enganche solo habla con la herramienta | Todo en el enganche | Así están hechos los demás; si mañana cambia la herramienta, se rehace solo el enganche |
| Al prender, si el análisis siguiente no existe, la herramienta lo crea desde `plantillas/analisis.md`; la copia del hallazgo y del pendiente la escribe el agente | Que la herramienta copie también el hallazgo | Qué hallazgo origina el análisis lo sabe la conversación, no un programa |
| La marca «Aprobado» con la fecha y el último turno la escribe la herramienta al recibir «Apruebo el análisis» | Que la escriba el agente | Es el control de apagar (análisis 2, conclusión 2) y no debe depender de que alguien se acuerde |
| Un análisis está abierto si no tiene la marca «Aprobado», o si la tiene y alguna HU de su columna «Pasó a» no está terminada | Mirar solo la marca | Confirma el punto 4 del análisis 3: el plan se cumple cuando sus HU terminan, y eso se lee con enlaces que ya existen |
| `00·ID8` se cumple en lo que escribe la herramienta: encabezados, líneas de pausa y marca. Las palabras del usuario y del agente se copian literales | Corregir las palabras copiadas | La conversación no se edita (análisis 1, conclusión 21) |
| El enganche espera a que el histórico anote el turno antes de leerlo | Leer enseguida | Los dos corren en el mismo evento; así lo hace ya el guion intermedio |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| `analisis_en_curso.py` | No existe | `leer_estado`, `prender(raiz, pendiente, turno)`, `pausar(raiz, turno)`, `aprobar(raiz, turno, fecha)`, `pasar(raiz)`, `abiertos(raiz)` y `aviso(raiz)` | `20·M9` |
| `hook_analisis.py` | No existe | En `UserPromptSubmit` lee la palabra y entrega el aviso por `additionalContext`; en `Stop` pasa la conversación | `00·N9` |
| `HOOKS_CLAUDE` | Sin el análisis | Dos entradas de `hook_analisis.py` | `01·C29` |
| `VERSION` | 40.0.0 | 40.1.0 | `20·M10` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-10 · La herramienta es del estándar y lee el análisis prendido

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Crear el módulo con el estado (análisis, transcripción, turno de inicio y pausas) y `pasar`, que reemplaza solo lo que va entre la sección «Conversación» y su línea de cierre | `validadores/analisis_en_curso.py` | CA-10 y CA-03 | Ninguno sobre lo existente | 1,5 h | Ninguna | CP-001, CP-002 |

### CA-03 · La conversación pasa al análisis en tiempo real

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | La misma tarea de arriba: `pasar` reemplaza solo lo que va entre la sección «Conversación» y su línea de cierre | `validadores/analisis_en_curso.py` | CA-03 | Ninguno | Incluida en T-01 | Ninguna | CP-002 |

### CA-09 · La conversación copiada cumple `00·ID8`

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | En `pasar`: la raya del encabezado de turno pasa a coma y se quitan las etiquetas de texto pegado y de archivo abierto | `validadores/analisis_en_curso.py` | CA-09 y CA-13 | Ninguno | 0,5 h | T-01 | CP-003 |

### CA-13 · Las etiquetas de la herramienta no entran

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | La misma tarea de arriba: `pasar` quita las etiquetas de texto pegado y de archivo abierto | `validadores/analisis_en_curso.py` | CA-13 | Ninguno | Incluida en T-02 | T-01 | CP-003 |

### CA-11 · Prender, pausar y apagar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | `prender`: con «Analicemos: el pendiente N» busca la carpeta del pendiente, toma el análisis siguiente (lo crea desde la plantilla si no existe) y escribe el estado desde ese turno. Sin pendiente, no hace nada. `pausar` con «Pare» anota desde qué turno; al volver a prender, `pasar` deja la línea «turnos X a Y en pausa». `aprobar` con «Apruebo el análisis» escribe la marca con la fecha y el último turno, y `pasar` borra el estado cuando la respuesta ya entró | `validadores/analisis_en_curso.py` | CA-11 | Ninguno | 2 h | T-01 | CP-004 |

### CA-14 · Un solo análisis abierto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | `abiertos`: los análisis sin la marca, o con la marca y alguna HU de su «Pasó a» sin terminar. `prender` no prende el de otro pendiente si hay uno abierto, y dice cuál | `validadores/analisis_en_curso.py` | CA-14 | Ninguno | 1,5 h | T-03 | CP-005 |

### CA-12 · El aviso de cada turno

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `aviso` y el enganche: en cada mensaje lee la palabra, llama a `prender`, `pausar` o `aprobar`, y entrega por `additionalContext` a qué análisis entra la conversación o que ninguno está prendido; en `Stop` llama a `pasar`. Sale siempre con código 0 | `validadores/analisis_en_curso.py` y `adaptadores/claude-code/hook_analisis.py` | CA-12 | Un enganche más en cada mensaje | 1 h | T-03, T-04 | CP-006 |

### CA-15 · El instalador registra la herramienta

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Sumar las dos entradas a `HOOKS_CLAUDE`; correr el instalador sobre el estándar, que cambia las entradas del guion intermedio; clasificar y nombrar el enganche y el módulo en los dos mapas | `validadores/instalar.py`, `.claude/settings.json`, `anatomia/que-esta-amarrado-a-la-herramienta.md`, `anatomia/mapa-del-sitio.md` | CA-15 | Todo proyecto que instale recibe el enganche | 1 h | T-05 | CP-007 |

### RNF · Requisitos no funcionales

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Escribir los casos del plan de pruebas sobre una carpeta temporal con una transcripción y un pendiente de prueba | `validadores/tests/test_analisis_en_curso.py` | CA-03, CA-09 a CA-15 | Ninguno | 2 h | T-01 a T-06 | CP-001 a CP-007 |
| T-08 | `VERSION` en 40.1.0 y su entrada en el CHANGELOG | `VERSION` y `CHANGELOG.md` | RNF de la HU: versionar según `20·M10` | Los proyectos reciben la versión MENOR | 0,3 h | T-07 | CP-008 |

## 4. Secuencia de ejecución

T-01 a T-08 en orden. Al final, `test_analisis_en_curso.py`, las pruebas del instalador, y `validar.py amarre`, `estandar`, `metareglas` y `analisis` (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-10 | El estado nombra un análisis y el turno entra en ese | CP-001 |
| CA-03 | Lo agregado a mano en el análisis sigue igual después de pasar | CP-002 |
| CA-09, CA-13 | Sin rayas en los encabezados, sin etiquetas, cero marcas en lo que escribe la herramienta | CP-003 |
| CA-11 | Prender, pausar, volver a prender, aprobar y «Analicemos» sin pendiente | CP-004 |
| CA-14 | Con un análisis abierto, el de otro pendiente no prende | CP-005 |
| CA-12 | El aviso con y sin análisis prendido | CP-006 |
| CA-15 | El instalador deja el enganche en un proyecto de prueba | CP-007 |

## 6. Datos y ambiente de prueba

Carpeta temporal con una transcripción, un pendiente y la plantilla del análisis. Para el CP-007, un proyecto de prueba vacío con git.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y volver a correr el instalador, que vuelve a dejar las entradas anteriores. El guion intermedio sigue en su carpeta.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Los proyectos que heredan lo reciben con el instalador. Nada se migra: un proyecto sin análisis prendido solo ve el aviso de que ninguno lo está.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`00·ID8`, `00·N9`, `01·C28`, `01·C29`, `02·F5`, `02·F8`, `02·F18`, `04·S18`, `20·M9`, `20·M10`, `13·DOC24`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el enganche lea la transcripción antes de que el histórico anote el turno | Espera, como el guion intermedio (§2.6) |
| Que cambiar `.claude/settings.json` pida autorización de la herramienta | Lo cambia el instalador; si la pide, se pide al usuario |
| Que el aviso en cada mensaje se vuelva ruido | Una línea corta, por `additionalContext`, que va al agente y no a la pantalla |

## 11. Definition of Done

- [ ] Los ocho CA con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas que la fase toca, en verde.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
