# Funcionalidad implementada — Fase `A-EP-005-HU-021-el-corredor-que-si-las-corre` (módulo Pruebas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-021-el-corredor-que-si-las-corre` |
| **Módulo** | Pruebas |
| **Especificación del módulo** | La redacción de los CA de la [HU-021](../HU-021-las-pruebas-que-existen-se-corren.md) es la especificación funcional (`02·F19`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-021 (CA-01 a CA-05) |
| **Fecha de cierre** | 2026-08-28 |
| **Versión del estándar al cerrar** | `35.9.0` |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

**Las 650 pruebas que ningún comando corría ahora se corren con una orden, y esa orden dice cuántas corrió.** Cero pruebas es rojo, se puede pedir un subconjunto, y la orden que la documentación nombraba —y que se caía antes de correr nada— vuelve a funcionar.

**La corrida completa no se cuelga de nada, y eso se decidió midiendo:** tarda 9,6 minutos y este repositorio hace 16 commits por día. Lo que se cuelga del `pre-push` es **el reclamo**: mira una fecha y avisa si hay commits que esas pruebas no vieron.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — una orden, y es la documentada | servicio | `validadores/corredor.py` · `validadores/tests/__init__.py` · `validar.py internas` | ✅ | `CP-003`, `CP-004` |
| CA-02 — cero pruebas es rojo | servicio | `corredor.correr`, el bloque de `testsRun == 0` | ✅ | `CP-002`, el crítico |
| CA-03 — subconjunto | servicio | `corredor.correr(solo=…)` · `validar.py internas <nombres>` | ✅ | `CP-005` |
| CA-04 — colgado de algo | adaptador | `corredor.sellar` / `corredor.reclamo` · `instalar.PLANTILLA_PRE_PUSH` | ✅ | `CP-006`, `CP-007` |
| CA-05 — los seis rojos declarados | doc | §6 de este documento | ✅ | `CP-008` |
| Las pruebas de los cinco criterios | prueba | `validadores/pruebas.py` · `LasPruebasQueExistenSeCorren` | ✅ | 22 pruebas |
| Versión y registro de cambios (`20·M10`) | doc | `VERSION`, `CHANGELOG.md` | ✅ | `35.9.0` |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-00 | La línea base, archivo por archivo | ✅ hecha | `linea-base-t00.txt` | 61 verdes, 6 rojos, con nombres |
| T-01 | ¿El `__init__.py` rompe alguno? | ✅ hecha | `t01-con-init.txt` | **No.** La subida a 5 fallas era de `corredor.py` |
| T-02 | El corredor y su conteo | ✅ hecha | `validadores/corredor.py` | `650 prueba(s) en 67 archivo(s)` |
| T-03 | Cero en rojo, y el subconjunto | ✅ hecha | el mismo | `CP-002`, `CP-005` |
| T-04 | ¿Dónde cuelga, con el número? | ✅ hecha | `t04-donde-cuelga.py` | **Ninguna opción que corra cabe.** Se cuelga el reclamo |
| T-05 | Colgarlo | ✅ hecha | `instalar.py` · `.githooks/pre-push` | `CP-007` |
| T-06 | La orden documentada, corregida | ✅ hecha | `validadores/README.md` | Las dos suites, con su tiempo y su motivo |
| T-07 | Declarar los seis rojos | ✅ hecha | §6 de este documento | Uno cerrado, cinco enrutados |
| T-08 | Las pruebas de los CA | ✅ hecha | `validadores/pruebas.py` | 22 pruebas |
| T-09 | Correrlo de verdad | ✅ hecha | — | El instalador corrido; el enganche real, línea 46 |
| T-10 | `CHANGELOG` y `VERSION` | ✅ hecha | — | `35.9.0` |
| T-11 | Sabotear | ✅ hecha | `sabotajes-hu021.py` | **12 de 12 cazados** |

**Correspondencia con el plan:** 12 tareas en el plan, 12 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**, `02·F8`:

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | **Toda pieza nueva de `validadores/` exige su fila ahí, y `corredor.py` es una.** Lo reclamó su propia prueba, que sumó 4 fallas hasta que la fila estuvo | Es requisito del repositorio, no una decisión: sin la fila, `validar.py amarre` queda en rojo |
| `documentacion/senales.md` | `S-076`, el sello de la estación 12 puesto sobre una fase recién abierta | El plan §9 manda registrar como señal lo decidido (`13·DOC5`) |
| Los dos planes y la HU | **Sus citas al pendiente 90 se rompieron cuando el pendiente se cerró y se movió a `hecho/`.** Se arrastraron a la ruta nueva; el texto no cambió | No es cambiar un plan aprobado: es que su cita apunte al mismo documento donde quedó |
| `validadores/README.md` | Estaba en el plan como T-06, pero declarado como «el `README` de `validadores/`» sin nombrar el archivo | Es el mismo archivo; se anota por precisión |

**El pendiente se movió a mano, y existe un programa para eso.** `cerrar.py` arrastra las citas al cerrar un pendiente; acá se movió con `os.remove` y se escribió el destino, así que **cuatro enlaces quedaron rotos** — tres apuntando al archivo viejo y tres salientes que subían un nivel de menos. Los cerró `validar.py estandar`, no la revisión. **Es el mismo error de esta semana: hacer a mano lo que un programa ya hace.**

**Esfuerzo real contra estimado:** cerca de 10 h contra las 11,5 del plan. **Lo que se subestimó fue el tiempo de correr las 650** — 3 minutos estimados contra 9,6 reales — y ese error no costó horas: **cambió el diseño del enganche**.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** las **dos**, que es lo que esta fase vino a hacer posible.
  - `pruebas.py`: **537 pruebas, 0 fallas** (4 esperadas, declaradas de antes). Esta fase aporta 22.
  - `validar.py internas`: **650 pruebas en 67 archivos, 8 fallas en 5 archivos** — contra 8 fallas en 6 archivos de la línea base. **Un archivo menos en rojo; las fallas quedaron igual**, y la octava la causó cerrar el pendiente 90 a mano (`DEF-05`).
- **Verificaciones manuales** (`08·T4`):
  - El enganche quedó en `.githooks/pre-push`, no solo en la plantilla.
  - El reclamo responde de inmediato: lee una fecha.
  - **12 de 12 sabotajes cazados**, tras corregir tres mal armados — uno de ellos se reportaba como cazado y solo rompía la sintaxis (`S-078`).
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py internas              # las 650, ~10 min
python validadores/validar.py internas test_x       # solo esas (02·F5)
python validadores/validar.py internas --reclamo    # no corre: dice si hace falta
```

- **Lo que corre solo:** el `pre-push` pregunta si hace falta correrlas. **Avisa y no detiene.**
- **Permisos o datos base sembrados:** ninguno. El sello vive en `historico-chat/.tocado/`, que no se versiona.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| **El enganche reclama, no corre** | Se descartó correr las 650 al publicar: 9,6 min × 245 commits en 14 días = **39,3 horas**. Un peaje así se apaga en una tarde, y deja algo peor que su ausencia | `S-075` |
| **Se creó el `__init__.py` igual, aunque el corredor no lo necesite** | Cargar por ruta habría bastado. Pero la orden documentada desde la primera prueba del repositorio tenía que funcionar: **que la documentación mienta es la otra mitad del defecto** | — |
| **Cero pruebas es rojo** | `discover` da 0 y por eso el defecto duró semanas. Se dejó una prueba que **comprueba que `discover` sigue dando 0**: si cambia, avisa de que la razón de esta pieza cambió | — |
| **Un solo proceso** | Medido: los 650 juntos dan las mismas fallas que uno por uno. 67 arranques de Python para el mismo resultado | — |
| **El sello solo lo pone la corrida entera y limpia** | Sellar un subconjunto diría «esto se comprobó» sobre lo que no se miró — el defecto del que sale toda la pieza | — |
| **Las dos suites siguen separadas** | Juntarlas daría 1165 pruebas y 13 minutos en cada fase, justo lo que `02·F5` evita. `internas` queda fuera de `validar.py todo`, declarado con su motivo | — |
| **El sello guarda el conteo de fallas, no solo el verde** | La primera versión sellaba solo la corrida limpia, y el reclamo decía «nunca corrieron» sobre unas pruebas que habían corrido dos veces. **Lo destapó el primer push de verdad, no las pruebas** | `S-077` |
| **Un archivo que no carga se reporta y no tumba el resto** | `EP-004·HU-003`: un archivo roto no puede llevarse lo que ya se sabía | — |

---

## 6. Los seis rojos, declarados  ·  `CA-05`

**Uno se cerró en el camino.** El mapa del amarre decía «26 amarrad**a**s de 82» y su prueba busca la frase exacta «26 amarrad**o**s». Una letra.

**Los cinco que quedan, con lo que dice cada uno y adónde va:**

| Archivo | Qué falla | De dónde viene | Adónde va |
|---|---|---|---|
| `test_ninguno_termina_en_silencio` (3 fallas) | `estacion_commit.py` no dice por dónde se corre; y códigos de salida que no distinguen «no comprobé» de «hay fallas» | `A-EP-005-HU-019` | **Fase de arreglo sobre `HU-019`** |
| `test_la_frontera_del_adaptador` | `hook_estacion.py` se quedó en `validadores/` y su sitio es `adaptadores/claude-code/` | `A-EP-005-HU-019` | **La misma** |
| `test_el_texto_del_enlace_dice_donde_vive` | **98 enlaces entre carpetas mal escritos**, donde el criterio exige 0 | Acumulado, muchas fases | **Pendiente propio:** es limpieza grande y mecánica, no cabe dentro de otra fase |
| `test_el_andamio_levanta_la_historia_y_el_pendiente` | El andamio escribe contenido donde el criterio pide que no | `EP-004`, el andamio | **Pendiente propio** |
| `test_la_corrida_completa_en_una_linea` | La corrida no termina con un resumen único | `EP-004·HU-008` | **Pendiente propio** |

**Cuatro de las siete fallas salen de una sola fase**, `A-EP-005-HU-019`. Agrupar por causa y no por archivo convierte cinco rojos sueltos en **dos destinos**: una fase de arreglo y tres pendientes.

**Ninguno queda como «se verá».**

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias vivo — la matriz del plan §2.4; ningún contrato cambió.
- [x] **Mapa del amarre a la herramienta** — `corredor.py` entró con su fila, y su prueba lo reclamó.
- [x] Catálogo de módulos: no se creó módulo nuevo.
- [x] Índice `README.md` de la carpeta de docs — el de `EP-005` quedó al día en el commit anterior.
- [x] `validadores/README.md` — **las dos órdenes, con su tiempo y el motivo de estar separadas.**

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica: el estándar no se despliega.** Quien lo tenga instalado recoge el reclamo la próxima vez que corra `python validadores/instalar.py`; hasta entonces nada suyo cambia, y el reclamo **nunca detiene un push**.
