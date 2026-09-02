# Resultado de Pruebas — Fase `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. **El primero dejó dos sabotajes en verde y una prueba que no tocaba su rama** |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** avisa al escribir fuera, **calla en las nueve formas de escribir dentro**, y **está colgado** — comprobado escribiendo un archivo de verdad.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| **Rutas de dentro que producen aviso** | 0 de 6 | **0 de 9** |
| El enganche colgado y probado escribiendo de verdad | Sí | **Sí** |
| Entradas malas que detienen el trabajo | 0 de 4 | **0 de 4** |
| Sabotajes cazados | Todos | **5 de 5**, tras cerrar dos huecos |
| Fallas en la suite completa | 0 | 0, sobre **466 pruebas** |

---

## 3. Resultado por caso

### CP-000 — Las pruebas del instalador no comparan la configuración completa

**Se corrió antes de tocar código**, que es lo que el plan exigía.

| Qué se miró | Resultado |
|---|---|
| `test_los_enganches_quedan_registrados_con_su_momento` | Comprueba que **estén** seis enganches concretos, con `assertIn` |
| `test_no_se_duplican_al_instalar_dos_veces` | Compara la configuración **consigo misma**, no con una lista fija |
| `test_un_enganche_que_se_cae_no_detiene_el_trabajo` | Corre cuatro enganches nombrados |

**Ninguna compara la lista completa ni cuenta cuántos hay.** Agregar uno no las rompe, así que se pudo seguir sin replantear.

### CP-001 — Escribir fuera avisa, y dice dónde iba

| Paso | Resultado |
|---|---|
| Una ruta de la carpeta temporal del sistema | **Avisa** |
| El mensaje | Nombra el archivo **y** `historico-chat/scripts/AAAA-MM-DD/` |
| El archivo después | **Sigue ahí**: avisa, no mueve ni borra |

### CP-002 — Escribir dentro **no** avisa

**Nueve rutas de dentro, silencio en las nueve:**

| Qué se le puso delante | Qué hizo |
|---|---|
| `validadores/`, `historico-chat/scripts/`, `README.md`, la raíz misma | **No avisó** |
| Una ruta **relativa** del proyecto, en tres formas | No avisó |
| Una con `..` que sale y **vuelve a entrar** | No avisó |
| La misma ruta con los dos separadores | No avisó, y se decide igual |

**Por qué son nueve y no seis:** las tres relativas salieron de un sabotaje que pasó en verde, y estaban en el plan sin escribirse. Está en el §4.2.

### CP-003 — El borde que un `startswith` no ve

| Qué se le puso delante | Qué hizo |
|---|---|
| **`…/agente-viejo/x.py` frente al proyecto `…/agente`** | **Avisó** |
| Una que empieza dentro y termina fuera con `..` | Avisó |

**El primero es el que decide.** `…/agente` es prefijo de `…/agente-viejo`: comparando cadenas, la carpeta hermana pasa por dentro y **el aviso calla justo donde debía hablar**. Por eso se comparan los tramos de la ruta.

### CP-004 — La regla dice dónde van los guiones

| Paso | Resultado |
|---|---|
| Buscar `historico-chat/scripts/` en `base/` | Aparece, en `04·S18` |
| Que declare su dependencia con `04·S9` y no lo repita | Lo hace |
| `validar.py metareglas` | Sin incumplimientos |

### CP-005 — El enganche está colgado, no solo escrito

| Paso | Resultado |
|---|---|
| El instalador lo registra | **Sí**, y hay una prueba que lo comprueba en la tabla, no en el texto |
| **Se escribe un archivo de verdad fuera y se corre el enganche como lo llama la herramienta** | **Avisa**, código 0 |
| El archivo sigue ahí | Sí. Se borró después, sin rastros |
| Lo mismo con un archivo del propio repositorio | **Silencio**, código 0 |

**No es teoría:** la fase `B` de `EP-002·HU-004` existió porque el aviso de desfase estaba construido, probado y en verde **y el arranque no lo llamaba**.

### CP-006 — Ninguna entrada mala detiene el trabajo

Sin `file_path`, sin JSON, JSON que no es objeto, ruta vacía, ruta de puros espacios: **silencio y código 0 en todas**.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Cinco, restaurados **con copia** y en `try/finally`.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | Se compara por prefijo: la hermana pasa por dentro | Cazado (1) | Cazado (1) |
| 2 | Se compara el texto crudo, sin resolver | **Verde** | **Cazado (2)** |
| 3 | Ante la duda se acusa en vez de callar | **Verde** | **Cazado (1)** |
| 4 | El aviso dice que está mal pero no dónde iba | Cazado (1) | Cazado (1) |
| 5 | El enganche existe y nadie lo cuelga | Cazado (1) | Cazado (1) |

### 4.2 Los dos huecos, y uno era del plan

**El sabotaje 2 pasó porque faltaba la ruta relativa** — un caso que **el plan exigía en `CA-02` paso 4 y no se escribió**. `normpath` colapsa un `..` sin tocar el disco, así que todos los casos con `..` pasan igual aunque la ruta no se resuelva. **La relativa es la única que distingue resolver de no resolver.**

**El sabotaje 3 pasó porque ninguna prueba tocaba la rama del `except`.**

### 4.3 Y la primera prueba que se escribió para taparlo estaba mal

Usó una ruta con un byte nulo, **creyendo que reventaría al resolverse**. Se comprobó: **no revienta** — se resuelve contra el directorio actual como cualquier otra. **La prueba pasaba sin tocar nunca la rama que decía probar.**

Se reescribió forzando el fallo a propósito, con el porqué escrito encima. Es `S-062`.

### 4.4 Un defecto real, encontrado por una prueba

Una ruta de **puros espacios** pasaba el guardia `not ruta` y **se acusaba de estar fuera del proyecto**. Corregido: `strip()` antes de decidir.

### 4.5 Una regla nueva sin clasificar

`validar.py metareglas` cobró que `04·S18` no declaraba si es validable (`M9`). Quedó en la tabla de las que **nacen con quien las haga cumplir**, con su límite escrito: **no ve lo que se escribe desde una línea de comandos**.

### 4.6 Rastros

**Uno, declarado.** La copia de restauración del guion de sabotaje vive en la carpeta temporal del sistema — **que es justo lo que la regla `S18` viene a evitar**. Queda anotado en el [pendiente 89](../../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md), y **el enganche nuevo lo va a avisar la próxima vez**.

### 4.7 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`). Y **ninguna escribe fuera del proyecto**, salvo el `CP-005` paso 2, que lo hace a propósito, lo declara y borra el archivo.

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | Una ruta de puros espacios se acusaba de estar fuera | Media | **Corregido.** Lo cazó su propia prueba |
| DEF-02 | Faltaba el caso de la ruta relativa, **que el plan exigía** | Alta — hueco de cobertura | **Corregido.** Sabotaje 2 cazado |
| DEF-03 | Ninguna prueba tocaba la rama de «ante la duda se calla» | Alta | **Corregido.** Sabotaje 3 cazado |
| DEF-04 | La prueba escrita para el `DEF-03` **no tocaba la rama que decía probar** | **Crítica** — una prueba que miente en verde | **Corregido** forzando el fallo. `S-062` |
| DEF-05 | La regla `04·S18` no declaraba si es validable | Media | **Corregido** |
| DEF-06 | Se numeró la regla como `S13`, y `S13` ya existía | Baja | **Corregido** a `S18`, tras enumerar las 18 |

**El `DEF-04` es el que más vale**, y es el mismo de la `HU-022`: una prueba que no puede fallar da la misma señal verde que una que funciona.

**El `DEF-06` enseña por dónde se cuela:** los identificadores del capítulo **no están en orden**, y mirar la cola de un `grep` dio `S12` por el último. Lo cazó `validar.py metareglas`.

---

## 6. Evidencias

- `validadores/rutas_fuera.py` y `adaptadores/claude-code/hook_rutas.py`
- La regla `04·S18`, con su checklist aplicado
- **16 pruebas**, de las cuales **9 comprueban que NO avise**
- La `T-00` sobre las pruebas del instalador, corrida antes de tocar código
- La `T-06`: el enganche corriendo con la entrada real de la herramienta
- El guion de sabotaje, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
