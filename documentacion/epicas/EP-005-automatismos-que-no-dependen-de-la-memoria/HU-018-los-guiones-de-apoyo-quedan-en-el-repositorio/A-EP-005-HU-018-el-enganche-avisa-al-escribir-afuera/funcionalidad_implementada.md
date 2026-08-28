# Funcionalidad implementada — Fase `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` (módulo Enganches)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-018](../HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio.md): `CA-01` a `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.4.0` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de aprobación del usuario |

---

## 1. Qué se implementó — resumen

**La regla existía, era del usuario, y se dejó de cumplir al día siguiente de precisarla.** Cuatro días, 38 guiones en una carpeta temporal del sistema.

Ahora **escribir fuera del proyecto avisa en el momento, y dice dónde debía ir**.

| Pieza | Qué hace |
|---|---|
| La regla `04·S18` | Dice **dónde sí** van los guiones de apoyo — la mitad que le faltaba a `04·S9`, que solo dice dónde no |
| `rutas_fuera.py` + `hook_rutas.py` | Avisan al escribir fuera, nombrando el destino. **Avisan: no mueven ni borran** |

**El daño no era de orden.** El **resultado** de cada cambio quedaba versionado y **el cómo se borraba con el temporal**: a *«¿con qué se hizo esto?»* no había respuesta, por segunda vez.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` los guiones van en `historico-chat/scripts/AAAA-MM-DD/` | documento | La regla `04·S18` | ✅ | CP-004 |
| `RN-02` escribir fuera avisa; leer fuera no | servicio | `hook_rutas.py`, colgado de `Write\|Edit` | ✅ | CP-001 |
| `RN-03` el aviso dice **dónde debía ir** | servicio | `rutas_fuera.aviso` | ✅ | CP-001, y el sabotaje 4 |
| `RN-04` avisa, no mueve ni borra | servicio | Solo lee la ruta | ✅ | CP-001 y CP-005 |
| `RN-05` la ruta se resuelve antes de comparar | servicio | `dentro_del_proyecto` | ✅ | CP-003, y los sabotajes 1 y 2 |
| `RN-06` la carpeta del día lleva su README | documento | Los cuatro días ya lo tienen | ✅ | — |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-00 · impacto sobre las pruebas del instalador | ✅ | Ninguna compara la lista completa |
| T-01 · decir si la ruta está dentro, por partes | ✅ | CP-002, CP-003 |
| T-02 · el enganche, que no revienta nunca | ✅ | CP-006 |
| T-03 · que el instalador lo cuelgue | ✅ | CP-005, y el sabotaje 5 |
| T-04 · la regla en `base/` | ✅ | CP-004 |
| T-05 · los cinco CA | ✅ | 16 pruebas |
| T-06 · **correrlo de verdad** | ✅ | §3, `CP-005` paso 2 |
| T-07 · `CHANGELOG` y `VERSION` | ✅ | `35.4.0` |
| T-08 · sabotear | ✅ | Cinco, con cuatro defectos encontrados |

**Correspondencia:** 9 tareas, 9 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): **uno**, `validadores/reglas-validables.md`. Lo exigió `M9` al agregar la regla: toda regla declara si es validable, y `validar.py metareglas` lo cobró. **Se declara acá en vez de callarlo.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 2 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **466 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` a `DEF-06` corregidos |

**Seis defectos, y solo uno en el código.** Los otros cinco están en las pruebas, en la numeración de la regla y en su clasificación. **El peor fue una prueba que no tocaba la rama que decía probar** — pasaba en verde sin comprobar nada.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**No hay comando que correr.** El enganche corre solo después de cada `Write` o `Edit`, y si el archivo cayó fuera del proyecto imprime una línea.

- **Desde el código:** `rutas_fuera.dentro_del_proyecto(ruta, proyecto)` y `rutas_fuera.aviso(ruta, proyecto)`.
- **Para que quede colgado en un proyecto ya instalado:** volver a correr el instalador.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| Se comparan **los tramos** de la ruta | `…/agente` es prefijo de `…/agente-viejo`: con `startswith`, la hermana pasa por dentro y el aviso calla donde debía hablar | `CP-003` |
| **Ante la duda se calla** | `04·R4`, y aritmética: el agente escribe decenas de archivos del proyecto por sesión, así que **un aviso falso vale menos que uno que falta** — el falso apaga el enganche entero | `CP-002` |
| **Avisa, no mueve** | Mover lo que el agente acaba de escribir rompe lo que estaba haciendo, y esconde el incumplimiento en vez de mostrarlo | `RN-04` |
| El aviso **nombra el destino** | Un aviso que no dice qué hacer se aprende a ignorar. Es el defecto más caro de este repositorio | Sabotaje 4 |
| **Cualquier fallo del enganche termina en silencio y código 0** | Lo que protege es una convención de orden; lo que arriesga si revienta es la sesión entera | `CA-05` |
| Regla propia y no una línea dentro de `S9` | `S9` dice **dónde no**; esta dice **dónde sí**. Se incumplen por separado — y eso es exactamente lo que pasó los cuatro días | `04·S18` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Lo que se escribe por `Bash` no se ve** | **Abierta y declarada.** La herramienta no entrega esa ruta. Cubre `Write` y `Edit`, que es por donde se escribieron los 38 |
| Los guiones de sabotaje guardan su copia de restauración fuera | **Abierta**, y ahora **el propio enganche la va a avisar**. Sigue en el [pendiente 89](../../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md) |
| La salida 2 del pendiente — un validador que compare al cierre | **Fuera de alcance por decisión del usuario:** detecta lo que el enganche evita |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-005](../../epica.md): la `HU-018` en sus tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] La señal `S-062`.
- [x] `validadores/reglas-validables.md`, con la regla y su límite.
- [x] `VERSION` en `35.4.0` y su entrada en el `CHANGELOG`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** al volver a instalar, el enganche queda colgado y empieza a avisar. **No cambia ningún archivo suyo.**
- **Reversión:** se descarta el commit, se baja `VERSION`, y se vuelve a correr el instalador para que regenere la configuración sin el enganche.
