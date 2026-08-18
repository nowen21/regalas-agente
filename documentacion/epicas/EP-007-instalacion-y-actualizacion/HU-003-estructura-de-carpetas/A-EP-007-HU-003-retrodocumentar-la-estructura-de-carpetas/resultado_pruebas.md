# Resultado de pruebas — Fase A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |
| **HU** | [HU-003](../HU-003-estructura-de-carpetas.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-007-HU-003 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales con git, instalados de verdad. Estándar 23.3.0 · Windows |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). La estructura queda completa, instalar dos veces da lo mismo, lo que ya existía no se toca, y funciona con rutas con espacios y tildes.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un proyecto vacío con git | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Crítica | Archivos con contenido propio, ya presentes | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Alta | Dos instalaciones seguidas | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-01 | Alta | La revisión sobre un proyecto al que le falta algo | Aprobado | EV-02 |
| [CP-005](plan_pruebas.md) | — | Media | La revisión en esta casa | Aprobado | EV-02 |

---

### Detalle de CP-001 — La instalación en carpeta vacía deja la estructura completa

Sobre un proyecto vacío con git, la instalación deja **13 archivos**:

| Grupo | Archivos |
|---|---|
| Capa de proyecto | `.agente/stack.md` · `dominio.md` · `mapeo-nombres.md` · `marco-normativo.md` · `stack-instalacion.md` |
| Automatismos | `.claude/settings.json` |
| Control de versiones | `.gitignore` |
| Instrucciones | `CLAUDE.md` |
| Histórico y memoria | `historico-chat/README.md` · `resumenes/README.md` · `memory/memory.md` |
| Versionado | `documentacion/versiones/README.md` y su registro del día |

Más las carpetas `proyectos/`, `documentacion/` y `prompts/`, y los enganches de git en `.githooks/`.

---

### Detalle de CP-002 y CP-003 — Lo que ya existía no se toca, y dos veces da lo mismo

| Qué se probó | Qué salió |
|---|---|
| Instalar dos veces y comparar **el conjunto de archivos** | Idéntico: la segunda pasada no crea ni borra |
| Comparar **el contenido** de cada uno | Idéntico, salvo el registro de versión, que lleva la fecha |
| Un `.agente/stack.md` con texto propio agregado | **Conserva el texto** tras reinstalar |
| Un `CLAUDE.md` con una regla propia | **Conserva la regla** |

**La excepción del registro de versión está bien:** ese archivo existe para decir *cuándo* se actualizó, así que cambiar de fecha es su trabajo. Se dejó explícito en la prueba en vez de compararlo como si fuera igual que los demás.

---

### Detalle de CP-004 y CP-005 — Cómo se lee la revisión, y qué pasa en esta casa

`validar.py checklist` dice qué le falta a un proyecto. Sobre un proyecto al que se le quita una carpeta, lo reporta.

**En esta casa se lee distinto, y conviene dejarlo escrito:** el estándar **no se instala a sí mismo**. `instalar.py` excluye su propio repositorio a propósito —hay una prueba que lo comprueba, `test_el_propio_estandar_no_se_trata_como_un_proyecto`—, así que la revisión de instalación no aplica acá. Lo que en un proyecto heredero es «falta el `CLAUDE.md` generado», acá es «el `CLAUDE.md` lo escribe una persona y dice otra cosa».

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Qué deja la instalación en vacío | Listando el proyecto | **13 archivos**, más carpetas y enganches de git |
| 2 | Que la segunda pasada no cambie nada | Comparando contenido archivo por archivo | Solo cambia el registro de versión, por su fecha |
| 3 | Ruta con espacios y tildes | Instalando en `proyecto de prueba con tildes áéíóú` | **Funciona**: el `CLAUDE.md` queda puesto |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 328 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-003-estructura-de-carpetas.md#ca-01--las-carpetas-quedan-creadas-y-con-su-índice) | CP-001, CP-004 | 13 archivos y sus carpetas, con sus índices | Sí |
| [CA-02](../HU-003-estructura-de-carpetas.md#ca-02--lo-que-ya-existía-no-se-toca) | CP-002, CP-003 | El texto propio sobrevive; dos pasadas dan lo mismo | Sí |
| Transversal · Límites | CP-003 | Un proyecto con toda la estructura no cambia en nada, y la simulación no anuncia trabajo | Sí |
| Transversal · Compatibilidad | Verificación 3 | Ruta con espacios y tildes: instala igual | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 5 de 5 | 5 de 5 | Sí |
| Archivos con contenido que cambien al reinstalar | **0** | **0** (salvo el registro de versión, por diseño) | Sí |
| Diferencias entre la primera y la segunda instalación | **0** | **0** en el conjunto de archivos | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los dos criterios de aceptación quedaron verificados y los dos transversales también. Lo que más se puso a prueba es el segundo, porque es el que puede hacer daño: **instalar dos veces no cambia nada**, y un archivo con texto propio lo conserva. La compatibilidad con rutas raras se probó donde de verdad falla —espacios **y** tildes juntos, en Windows—, no leyendo el código.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `EstructuraDeCarpetas` (3 nuevas) e `Instalador` (16, ya existentes) |
| EV-02 | Cómo se lee la revisión acá | §2, CP-005 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 328 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
