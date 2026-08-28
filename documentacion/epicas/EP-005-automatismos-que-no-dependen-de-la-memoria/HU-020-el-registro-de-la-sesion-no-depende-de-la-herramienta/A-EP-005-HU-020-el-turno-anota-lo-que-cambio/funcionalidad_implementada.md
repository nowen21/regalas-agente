# Funcionalidad implementada — Fase `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` (módulo Enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` |
| **Módulo** | Enganches |
| **Especificación del módulo** | La redacción de los CA de la [HU-020](../HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta.md) es la especificación funcional (`02·F19`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-020 (CA-01, CA-02, CA-03, CA-04, CA-05) |
| **Fecha de cierre** | 2026-08-28 |
| **Versión del estándar al cerrar** | `35.8.0` |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

**El registro de lo que toca cada conversación dejó de depender de con qué herramienta se escribió el archivo.** Antes anotaba solo lo que el agente escribía con sus herramientas de edición; ahora, al terminar cada turno, anota **lo que cambió durante ese turno**, sin mirar quién lo escribió.

Con eso, la comprobación que ya existía —la que avisa cuando un commit mezcla trabajo de dos conversaciones— **empieza a ver el caso para el que se hizo**. No se le tocó ni una línea: se le completó el registro del que se alimenta.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — lo escrito fuera de las herramientas queda registrado | servicio | `validadores/sesiones.py` · `cambios_del_turno`, `anotar_el_turno` | ✅ | `CP-001` |
| CA-02 — no se reclama lo que no se tocó en el turno | servicio | `validadores/sesiones.py` · el filtro por fecha y la primera vuelta vacía | ✅ | `CP-002`, el crítico |
| CA-03 — dos sesiones que tocan lo mismo producen colisión | servicio | `validadores/sesiones.py` · `validar_preparados`, **sin cambios** | ✅ | `CP-003` paso 4 |
| CA-04 — lo que ya se registraba se sigue registrando | servicio | `validadores/sesiones.py` · `anotar`, reutilizada tal cual | ✅ | `CP-004` |
| CA-05 — un fallo del enganche no rompe el turno | adaptador | `adaptadores/claude-code/hook_turno.py` | ✅ | `CP-005` |
| Que el enganche quede colgado | adaptador | `validadores/instalar.py` · `HOOKS_CLAUDE`, evento `Stop` | ✅ | `CP-007` |
| Las pruebas de los cinco criterios | prueba | `validadores/pruebas.py` · `ElTurnoAnotaLoQueCambio` | ✅ | 15 pruebas |
| Versión y registro de cambios (`20·M10`) | doc | `VERSION`, `CHANGELOG.md` | ✅ | `35.8.0` |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-00 | Ver si alguna prueba fija el contenido del registro | ✅ hecha | — | `CP-000`: 11 pruebas lo miran, ninguna lo fija |
| T-01 | Qué entrega git para ignorados y borrados | ✅ hecha | Comentario en `_estado_de_git` | ` M`, ` D`, `??`; los ignorados no se piden a propósito |
| T-02 | Saber qué cambió dentro de la ventana | ✅ hecha | `validadores/sesiones.py` | `_estado_de_git`, `cambios_del_turno` |
| T-03 | Anotarlo sin duplicar | ✅ hecha | `validadores/sesiones.py` | `anotar_el_turno` · `CP-004` |
| T-04 | El enganche, que nunca rompe nada | ✅ hecha | `adaptadores/claude-code/hook_turno.py` | `CP-005` |
| T-05 | Que el instalador lo cuelgue | ✅ hecha | `validadores/instalar.py` | `CP-007` |
| T-06 | Medir cuánto hablaría la comprobación | ✅ hecha | `historico-chat/scripts/2026-08-28/t06-cuanto-hablaria.py` | **0 de 12**, contra 7 de 12 |
| T-07 | Los cinco CA | ✅ hecha | `validadores/pruebas.py` | 15 pruebas |
| T-08 | Correrlo de verdad sobre este repositorio | ✅ hecha | — | Turno 1 sin reclamar nada; turno 2 anotó lo del guion |
| T-09 | `CHANGELOG` y `VERSION` | ✅ hecha | `CHANGELOG.md`, `VERSION` | `35.8.0` |
| T-10 | Sabotear | ✅ hecha | `historico-chat/scripts/2026-08-28/sabotajes-hu020.py` | **7 de 7 cazados** |

**Correspondencia con el plan:** 11 tareas en el plan, 11 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**, `02·F8`:

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `documentacion/senales.md` | Las dos señales que salieron del sabotaje, `S-073` y `S-074` | El propio plan §9 manda registrar como señal lo decidido (`13·DOC5`); las dos aparecieron al ejecutar |
| `documentacion/epicas/EP-005…/README.md` | El índice de la épica venía **cuatro historias atrasado** (HU-017 a HU-020). Se vio al marcar la casilla §7, no antes | Se corrigió en el momento en vez de dejarlo como pendiente: son cuatro filas, y una casilla firmada sin mirar es `S-070` |

**Esfuerzo real contra estimado:** cerca de 9 h contra las 10 h del plan. **Lo que se subestimó fue el sabotaje:** una hora estimada, y las correcciones que destapó —tres defectos— costaron más que escribirlo.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** la suite completa, **515 pruebas, 0 fallas** (4 fallas esperadas, declaradas de antes). La clase de esta fase aporta 15.
- **Verificaciones manuales** — lo que el entorno automático no reproduce (`08·T4`):
  - **Sobre este repositorio de verdad:** turno 1 arrancó el reloj sin reclamar nada, turno 2 anotó el archivo escrito desde la terminal y **no** el que estaba sucio de antes.
  - `historico-chat/.tocado/` no cambió al correr las pruebas: todas usan carpetas temporales.
  - **7 de 7 sabotajes cazados**, tras corregir los dos que se colaron.
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** ninguno a mano. El enganche corre solo al terminar cada turno, colgado del evento `Stop`. Se instala corriendo `python validadores/instalar.py`.
- **Permisos o datos base sembrados:** ninguno. **No se toca la configuración global de git** (`00·N1`).

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| **No se tocó `validar_preparados`** | Se descartó afinar la comprobación: medido contra el historial, habría avisado en **7 de 12** commits. El defecto estaba en el registro, no en quien lo lee | `S-072` |
| **La primera vuelta no reclama nada** | Sin una hora anterior contra la cual comparar, cualquier criterio se lleva todo lo que esté sucio, y la primera conversación del día se atribuye el proyecto entero | — |
| **La ventana se mide desde la fecha del propio registro** | Se descartó guardar la hora de arranque de la sesión: el archivo del registro ya trae su fecha, y así no hace falta estado nuevo que pueda desincronizarse | — |
| **Anotar de más es deliberado** | Que dos conversaciones toquen el mismo archivo es justo lo que hay que ver, aunque una solo lo haya rozado | — |
| **Un borrado se anota siempre** | No tiene fecha que mirar; filtrarlo por fecha lo perdería, y dos sesiones que borran lo mismo es una colisión | — |
| **Cualquier fallo termina en silencio y en 0** | Cuando esto corre, la respuesta ya se dio: lo único que puede lograr un fallo es alarmar. Un enganche que rompe la conversación se desinstala el mismo día | — |
| Se quitó un `os.utime` que no hacía nada | Un sabotaje se coló ahí. La respuesta no era agregarle una prueba: era quitar la línea | `S-074` |
| La suite completa corre entera antes de cerrar | Una aserción quedó pegada en otra clase; correr solo la clase nueva no lo habría visto nunca | `S-073` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **El cero de la `T-06` no prueba que las colisiones se vean**, porque hoy hay una sola conversación viva en el historial: prueba que no avisa por falta de registro. Que se vean lo prueba `CP-003` con repositorios armados a mano | Diferido por el plan | Se vuelve a medir cuando haya un historial con dos conversaciones simultáneas |
| **Los archivos ignorados por git quedan fuera del registro.** Es a propósito —el propio registro vive en uno de ellos— pero significa que dos sesiones que se pisen dentro de una carpeta ignorada no se ven | Atajo decidido, por el agente al resolver la `T-01` | Sin destino: no es trabajo versionado, así que un commit no puede llevárselo |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias vivo actualizado — la matriz del plan §2.4 declara que ningún contrato cambia.
- [x] Catálogo de módulos: no se creó módulo nuevo; el enganche entra en los que ya existen.
- [x] Índice `README.md` de la carpeta de docs actualizado — **estaba cuatro historias atrasado; se completaron las cuatro.**
- [x] Especificación del módulo: los CA de la HU, que no cambiaron al implementar.

---

## 7.1 La cuenta del proyecto, antes y después

| Momento | La cuenta |
|---|---|
| Antes de abrir la carpeta de la fase | `121 en total · 32 sin terminar · 89 terminadas, de las cuales 71 cumplen, 13 no cumplen y 5 no dicen si cumplen` |
| Al cerrarla | `122 en total · 32 sin terminar · 90 terminadas, de las cuales 72 cumplen, 13 no cumplen y 5 no dicen si cumplen` |

**Una historia más, y la historia más cumple.** Se mide corriendo `python validadores/validar.py fases`, no contándolo a mano — el número que responde «cuánto falta» ya mintió seis veces en este repositorio por hacerlo de otra forma.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica: el estándar no se despliega.** Quien ya lo tenga instalado recoge el enganche la próxima vez que corra `python validadores/instalar.py`; hasta entonces nada suyo cambia.
