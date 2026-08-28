# Plan de Trabajo — Fase `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-022](../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📋 **Baja del [pendiente 88](../../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md)**, con las salidas **1 y 3 aprobadas** por el usuario y la **2 dejada fuera** — que el andamio no cree los cinco documentos de entrada cambia cómo se abre una fase, y eso es hábito, no defecto.

**CA de la HU que cubre esta fase:** los cinco. Son una sola cosa: una comprobación que sabe distinguir un documento escrito de un formulario, y que lo dice por nombre.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que una fase con un documento que **sigue siendo su plantilla** deje de contar como terminada, y que se diga cuál es.

**Fuera de alcance:**

- **Llenar los siete documentos.** Esta fase los hace visibles.
- **Que el andamio cambie.** Salida 2 del pendiente, fuera por decisión del usuario.
- **Documentos que no son de fase** — épicas, historias, planteamiento.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Medido el 2026-08-27 **antes de crear la carpeta de esta fase**, porque abrirla mueve el número que viene a arreglar. Ya confundió una medición el mismo día.

### 2.0 La línea base

```
117 en total · 32 sin terminar · 85 terminadas,
de las cuales 64 cumplen, 16 no cumplen y 5 no dicen si cumplen
```

### 2.1 La medida que no sirve, y por qué se descarta

`S-053` propuso **contar** los marcadores `«…»` y `AAAA-MM-DD` de cada documento, con un umbral. Se comprobó sobre los dieciséis casos del día y separaba limpio.

**Sobre los 664 documentos del árbol da 38, y tres son de una fase escrita, cerrada y publicada media hora antes** — `C-EP-004-HU-021`, con 11, 12 y 13 marcadores.

**La causa:** este repositorio usa comillas angulares en prosa todo el tiempo. `«Cumple»`, `«No cumple»`, `«por criterio de aceptación»`. **La cuenta mide el estilo de la casa**, y la señal y el ruido crecen juntos: un documento largo y bien escrito acumula más marcadores que un molde corto.

Está en `S-059`, y el guion malo se guarda junto al bueno.

### 2.2 La medida que sí sirve, medida

No **cuántos** marcadores hay, sino **cuántos son los de su plantilla**. `«Cumple»` es prosa; `«2-4 líneas en lenguaje claro»` está en el molde y solo ahí.

| Documentos de fase | Cuántos |
|---|---|
| Sin ningún marcador del molde | **577** |
| Con uno o dos | **80** |
| **Con tres o más** | **7** |

**Los siete, verificados uno por uno:**

| Documento | Marcadores del molde | Qué es |
|---|---|---|
| `B-EP-002-HU-003` · `plan_pruebas.md` | 36 | La plantilla `08` sin tocar |
| `B-EP-002-HU-004` · `plan_pruebas.md` | 36 | Igual |
| `B-EP-004-HU-011` · `plan_pruebas.md` | 36 | Igual |
| `B-EP-004-HU-012` · `plan_pruebas.md` | 36 | Igual |
| `B-EP-005-HU-002` · `plan_pruebas.md` | 36 | Igual |
| `A-EP-007-HU-009` · `estado-fase.md` | 16 | La plantilla `10` sin tocar |
| `A-EP-004-HU-021` · `estado-fase.md` | 16 | Igual |

**El corte está en 3, y no es arbitrario:** entre «uno o dos» y «tres o más» hay un salto de 80 a 7, y de 2 marcadores a 16. **No hay ningún documento con entre 3 y 15.**

**Los cinco `plan_pruebas.md` son fases con código y pruebas construidas.** Lo que falta no es papeleo: es que **nadie sabe con qué casos se comprobaron**.

### 2.2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Servicio | Leer los marcadores de las plantillas y comparar |
| `validadores/pruebas.py` | Modificar | Test | Los cinco CA, y el caso de la prosa con comillas |
| `CHANGELOG.md` | Modificar | Documentación | `20·M10` |
| `VERSION` | Modificar | Documentación | `20·M10` |

### 2.3 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `fases.py` · `inventario` | **Ninguno en la firma.** Sigue devolviendo tres valores | 11 pruebas | No rompen por firma. **Sí cambia lo que devuelve**: una fase con un documento sin llenar deja de contar completa |
| `fases.py` · `por_veredicto` | Ninguno | 32 pruebas | Cambia por lo mismo: si la fase no está terminada, no entra al reparto |

**Riesgo real declarado:** hay pruebas que arman árboles con los cinco documentos de mentira. **Si su contenido se parece a la plantilla, dejarían de contar completas y romperían.** Se comprueba antes de tocar nada — es la `T-00`.

### 2.4 Punto de entrada

`python validadores/validar.py fases`. La línea dirá otros números, y habrá siete avisos nuevos.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se compara **contra la plantilla** | Un umbral de cuántos marcadores hay | Ya se probó y falla: señaló tres documentos escritos el mismo día. `S-059` |
| Los marcadores de cada plantilla se leen **una vez**, al empezar | Leerlas por cada documento | Son 664 documentos y 5 plantillas. `RNF-01` |
| El corte es **tres o más** | Uno o más | Con uno o dos hay 80 documentos, y son prosa que coincide por casualidad con un marcador corto del molde. Con tres, siete, y los siete son el molde |
| Si falta la plantilla, **no se señala nada** de ese tipo | Suponer una lista | `04·R4`: no afirmar sobre lo que no se leyó. Sin plantilla no hay con qué comparar |
| El aviso nombra **la fase, el documento y un marcador de ejemplo** | Solo la cuenta | `S-040`: un registro que dice cuántos sin decir cuáles no demuestra nada |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. El corte se eligió mirando el reparto real, y no hay casos entre 3 y 15 | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | **Antes de tocar nada:** comprobar si algún árbol de prueba existente quedaría señalado | Test | 0,5 h | — | EV-00 |
| T-01 | Leer los marcadores de las cinco plantillas, una sola vez | Backend | 0,5 h | — | EV-01 |
| T-02 | Decir si un documento conserva tres o más de los suyos | Backend | 0,5 h | T-01 | EV-01 |
| T-03 | Que una fase con un documento así no cuente terminada | Backend | 0,5 h | T-02 | EV-02 |
| T-04 | Un aviso por documento, con fase, archivo y un ejemplo | Backend | 0,5 h | T-02 | EV-03 |
| T-05 | Los cinco CA, con el caso de la prosa con comillas | Test | 2 h | T-03 | EV-01 a EV-05 |
| T-06 | Medir la línea antes y después, y **nombrar los siete** | Documentación | 0,5 h | T-03 | EV-06 |
| T-07 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-06 | EV-07 |
| T-08 | Sabotear | Calidad | 1 h | T-05 | EV-08 |

**Total estimado:** 6,5 h

**Versión: MENOR.** Es aditivo — nadie tiene que hacer nada; lo que cambia es que el número deja de contar como escrito lo que no lo está. Sube a `35.3.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-05

**La `T-00` va primero y puede cambiar el plan.** Once pruebas arman árboles con los cinco documentos de mentira. Si alguno de esos cuerpos falsos se parece a una plantilla, la comprobación nueva los señalaría y romperían once pruebas **por una razón que no es un defecto**. Hay que saberlo antes, no descubrirlo al final.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · una fase con un documento sin llenar no cuenta terminada | Árbol que cambia de cuenta según el documento | EV-02 | | ☐ |
| CA-02 · se compara contra la plantilla, no contra un umbral | El documento real de prosa con comillas, y el molde real | EV-01 | | ☐ |
| CA-03 · el aviso dice cuáles | La corrida contra el árbol real | EV-03 | | ☐ |
| CA-04 · las plantillas se leen del repositorio | Un marcador nuevo en un árbol de prueba | EV-04 | | ☐ |
| CA-05 · avisa y no corrige | Comparar el documento antes y después | EV-05 | | ☐ |

---

## 6. Datos y ambiente de prueba

Árboles de mentira en carpeta temporal, **con sus propias plantillas**, para que `CA-04` se pueda probar sin tocar las de verdad. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** verá **subir** sus historias sin terminar. No perdió trabajo: **tiene documentos que nunca se escribieron y hasta hoy contaban como escritos.** El aviso le dice cuáles son, así que puede ir a arreglarlos sin buscar.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base, medida **antes** de crear la carpeta.
- `04·R4` — sin plantilla no se afirma nada sobre ese tipo de documento.
- `20·M10` — versión y registro de cambios.
- `13·DOC5` — lo decidido se registra como señal.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se señalen documentos escritos | Es el defecto que se está corrigiendo, repetido | `CA-02` con el documento real de prosa, y la `T-00` antes de tocar nada | Abierto |
| B-02 | Que los árboles de prueba existentes queden señalados | Once pruebas rojas por algo que no es defecto | La `T-00` lo mide primero | Abierto |
| B-03 | Que subir las «sin terminar» se lea como retroceso | Se descartaría el arreglo por dar peor número | La entrada del `CHANGELOG` dice qué son los siete, con nombre |
| B-04 | Que abrir esta fase mueva la medición | Es literalmente el defecto que arregla | La línea base está anotada en el §2.0 y en la historia | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados
- [ ] Las pruebas de `inventario` y `por_veredicto`, pasando
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] Los siete documentos nombrados uno por uno
- [ ] `VERSION` en `35.3.0` y su entrada en el `CHANGELOG`
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
