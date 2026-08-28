# Resultado de Pruebas — Fase `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. **El primero dejó un sabotaje en verde y tumbó el guion con el código roto puesto** |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** se señalan **exactamente los siete** documentos medidos, **ninguno escrito**, y el aviso dice cuál es cada uno.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 6 de 6 | 6 de 6 |
| **Documentos escritos señalados** | 0 | **0** |
| **Documentos señalados** | exactamente 7, con nombre | **7, con nombre** |
| Pruebas de `inventario` y `por_veredicto` que hubo que tocar | 0 | **0** |
| Sabotajes cazados | Todos | **6 de 6** — el quinto, tras arreglar una comprobación falsa |
| Fallas en la suite completa | 0 | 0, sobre **450 pruebas** |

---

## 3. Resultado por caso

### CP-000 — Los árboles de prueba de hoy no quedan señalados

**Se corrió antes de tocar código**, que es lo que el plan exigía.

| Qué se midió | Resultado |
|---|---|
| Literales de `pruebas.py` mirados | **2.299** |
| Con cero marcadores de plantilla | 2.292 |
| Con uno | 7 |
| **Con tres o más** | **0** |

**Ninguno llega al corte.** La comprobación nueva no toca los árboles de mentira, así que se pudo seguir sin replantear.

### CP-001 — Una fase con un documento sin llenar no cuenta terminada

| Paso | Resultado |
|---|---|
| Los cinco escritos | Cuenta terminada |
| Uno reemplazado por su plantilla | **Sale de terminadas** |
| Vuelto a escribir | Vuelve a contar terminada |
| La historia sale también del reparto de veredictos | **Sí** — no se queda en «no dice si cumple» |

**El último importa:** `por_veredicto` solo mira las terminadas. Dejar ahí una historia que ya no lo está sería afirmar sobre algo que ni siquiera terminó.

### CP-002 — No se señala un documento escrito

| Lo que se le puso delante | Qué hizo |
|---|---|
| **Los tres documentos reales de `C-EP-004-HU-021`**, que la medida vieja marcó el mismo día en que se escribieron | **No los señaló** |
| Prosa con veinte comillas angulares — `«Cumple»`, `«terminada»`, `«bloqueada»`... | No la señaló |
| Un documento con **dos** marcadores del molde | No lo señaló: el corte es tres |
| El `plan_pruebas.md` de `B-EP-004-HU-011`, que es la plantilla | **Lo señaló** |
| Los 666 documentos del árbol | **Exactamente 7 señalados** |

**Los tres primeros son el caso crítico**, porque son los que hicieron fracasar la medida anterior.

### CP-003 — El aviso dice cuáles

Los siete avisos, con su fase, su documento y **un marcador de ejemplo**:

| Documento | Marcadores del molde |
|---|---|
| `B-EP-002-HU-003` · `plan_pruebas.md` | 36 |
| `B-EP-002-HU-004` · `plan_pruebas.md` | 36 |
| `B-EP-004-HU-011` · `plan_pruebas.md` | 36 |
| `B-EP-004-HU-012` · `plan_pruebas.md` | 36 |
| `B-EP-005-HU-002` · `plan_pruebas.md` | 36 |
| `A-EP-004-HU-021` · `estado-fase.md` | 16 |
| `A-EP-007-HU-009` · `estado-fase.md` | 16 |

**Los cinco primeros son fases con su código y sus pruebas construidas.** Lo que falta no es papeleo: **nadie sabe con qué casos se comprobaron.**

### CP-004 — Las plantillas se leen del repositorio

| Paso | Resultado |
|---|---|
| Agregar un marcador nuevo a una plantilla de prueba | **Se reconoce solo**, sin tocar código |
| Quitar una plantilla | **No se afirma nada** de ese documento, y no revienta |
| Quitar **todas** las plantillas | `marcadores_de_los_moldes` devuelve vacío: **no hay lista de reserva** |

**El tercero reemplazó a una prueba mala.** La primera buscaba el texto de un marcador dentro de `fases.py`, **y falló por un comentario que cita un marcador para explicarse**. Una prueba así se rompe al documentar. Se cambió por comportamiento.

### CP-005 — Avisa y no corrige

El documento sin llenar queda **idéntico** después de correr `validar`.

### CP-006 — El número

| Antes | Ahora |
|---|---|
| `117 en total · 32 sin terminar · 85 terminadas` | `118 en total · 40 sin terminar · 78 terminadas` |
| `64 cumplen, 16 no cumplen, 5 no dicen` | `59 cumplen, 14 no cumplen, 5 no dicen` |

**La aritmética cuadra sin sobras:** `32 + 7 fases + 1 (esta historia, todavía sin sus cinco documentos) = 40`. `85 − 7 = 78`. Y del reparto salen 5 + 2 = 7, que son las mismas siete.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Seis, restaurados **con copia**. **Cinco cazados al primer intento; el quinto pasó en verde.**

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | Vuelve a bastar con que el documento exista | Cazado (4) | Cazado (4) |
| 2 | Se cuentan los marcadores, no los del molde | Cazado (2) | Cazado (2) |
| 3 | El corte baja a uno | Cazado (2) | Cazado (2) |
| 4 | Sin plantilla se supone una lista de reserva | Cazado (2) | Cazado (2) |
| 5 | El aviso dice cuántos pero no cuáles | **Verde** | **Cazado (1)** |
| 6 | La comprobación se desconecta de `validar()` | Cazado (1) | Cazado (1) |

### 4.2 Por qué el sabotaje 5 pasó: la comprobación era cierta siempre

La prueba decía `assertIn("«", mensaje + "«")`. **Compara contra un texto al que se le acaba de pegar lo que busca**, así que pasa con cualquier mensaje, incluso con uno vacío.

Corregida: se exige que el aviso traiga **un marcador de los que el documento conserva de verdad**, sacado de la plantilla. Con eso, el sabotaje 5 rompe.

**Es un defecto de la prueba, no del código** — pero de la peor clase: una comprobación que no puede fallar da la misma señal verde que una que funciona.

### 4.3 El guion de sabotaje se cayó con el código roto puesto

En el ciclo 1, un `print` de una línea de resultado con caracteres que la consola de Windows no sabe escribir **reventó entre romper `fases.py` y restaurarlo**. **El repositorio quedó con el sabotaje puesto.**

Y **no se notó**, que es la mitad peor: el guion se lanzó con `| tail -45`, así que el código de salida que se leyó fue el de `tail` — cero.

Los dos arreglos, en `S-060`:

- La restauración va en `try/finally`. No puede depender de que el guion llegue vivo hasta ella.
- La salida se limpia antes de imprimirse.
- Y el guion **no se canaliza**: se redirige a un archivo y se lee.

**Lo que salvó el repositorio fue restaurar con copia**, no con git: el archivo bueno estaba en la carpeta de copias, intacto.

### 4.4 La corrida final del ciclo 1, y por qué falló

Cuatro fallas. **Tres por una causa inocente:** este documento y el de cierre no estaban escritos, y el `estado-fase` y el plan ya los enlazaban.

**La cuarta la cazó el propio estándar, contra el agente:** la `HU-022` declaraba `Estado: Aprobada`, y el glosario **no define ese estado para una historia**. Los que valen son `Pendiente · Lista · En curso · En prueba · Terminada`. Corregido a `En curso`.

**La guardia nueva del guion funcionó**: dijo `ATENCION: la corrida final no salió limpia`, que es exactamente lo que la vieja no sabía decir.

### 4.5 Rastros

**Uno, declarado.** La copia de restauración vive en la carpeta temporal del sistema. Es el resto anotado en el [pendiente 89](../../../../../pendientes/89-nada-hace-cumplir-que-los-guiones-queden-en-el-repositorio.md).

### 4.6 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | Una prueba buscaba el texto de un marcador dentro de `fases.py`, y falló por un comentario que lo cita | Media — la prueba se rompe al documentar | **Corregido.** Se comprueba por comportamiento |
| DEF-02 | `assertIn("«", mensaje + "«")` es cierta siempre | Alta — **una comprobación que no puede fallar** | **Corregido.** Sabotaje 5 cazado |
| DEF-03 | El guion de sabotaje dejó el repositorio roto al caerse, y el fallo no se vio por correrlo con `\| tail` | **Crítica** | **Corregido.** `try/finally`, salida limpia, sin tubería. `S-060` |
| DEF-04 | La `HU-022` declaraba un estado que el glosario no define | Baja | **Corregido** a `En curso` |

**El `DEF-03` es el que más vale**, y no es de esta fase: es de la herramienta con que se comprueban todas.

---

## 6. Evidencias

- `marcadores_de_los_moldes`, `sigue_siendo_el_molde` y `documentos_que_siguen_siendo_el_molde` en `validadores/fases.py`
- 16 pruebas nuevas, **de las cuales 6 comprueban que NO se señale**
- La `T-00` sobre los 2.299 literales de `pruebas.py`, corrida antes de tocar código
- Los guiones de medición y sabotaje, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
