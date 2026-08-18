# Resultado de pruebas — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **HU** | [HU-006](../HU-006-sacar-del-almacen-local.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-006 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Proyectos temporales con su almacén de mentira, y el almacén real de esta máquina **en lectura**. Estándar 23.2.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 2 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). El almacén de esta máquina está **vacío**, el recogido lo vacía y **no deja ni el texto ni un puntero**. Lo que falla es el paso 5 de CP-001 — y falla por una razón que no es un defecto del programa, sino una **contradicción entre el plan y `01·C19`** que hay que resolver decidiendo.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--después-de-recoger-el-almacén-no-tiene-archivos) | CA-01 | Crítica | 2026-08-17 | Almacenes de mentira, con y sin archivos | **Falla en el paso 5** | EV-01 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--el-puntero-puesto-a-mano-también-se-saca) | CA-02 | Crítica | 2026-08-17 | Un puntero escrito a mano en el almacén | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md#cp-003--qué-hay-hoy-en-el-almacén-de-esta-máquina) | CA-01 | Alta | 2026-08-17 | El almacén real, mirado sin tocarlo | Aprobado | EV-02 | — |

---

### Detalle de CP-001 — Después de recoger, el almacén no tiene archivos

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Poner tres recuerdos en el almacén de mentira | Quedan los tres | Quedan |
| 2 | Correr el recogido | Los tres llegan al repositorio de prueba | Llegan |
| 3 | Mirar el almacén | Sin archivos | **Sin archivos** |
| 4 | Correr con el almacén ya vacío | No falla, y no hace nada | No falla, y devuelve la lista vacía de movimientos |
| 5 | Poner un archivo que **no** es recuerdo y correr | No se lo lleva: no le corresponde | **Se lo lleva.** Un `config.json` terminó en `historico-chat/memory/` |
| 6 | Comprobar que el almacén real no se tocó | Intacto | Intacto: los casos corren sobre carpetas temporales |

**Qué salió distinto, y por qué no es obvio quién tiene razón.** `sueltos()` devuelve **todo archivo** del almacén, no solo los `.md`. Eso lleva al repositorio cosas que no son recuerdos — pero dejarlas sería incumplir [`01·C19`](../../../../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto), que exige el almacén **vacío**, y entonces la revisión reprobaría para siempre por un archivo que no es un recuerdo.

**Las dos salidas, y ninguna es limpia:**

| Salida | Qué gana | Qué cuesta |
|---|---|---|
| **A** · el recogido distingue qué es recuerdo y deja lo demás | No mete basura en `historico-chat/memory/` | Hay que relajar `C19`: el almacén ya no queda vacío, y la revisión necesita saber qué ignorar |
| **B** · se acepta que se lleve todo, y se dice en el documento | `C19` se cumple literal y el programa no cambia | Un archivo de configuración puede aparecer entre los recuerdos, y hay que sacarlo a mano |

**Elegir no es del que ejecuta.** Queda como `D-01`, con la prueba escrita en rojo esperado.

---

### Detalle de CP-002 — El puntero puesto a mano también se saca

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Poner el puntero a mano en el almacén | Queda puesto | Un archivo que solo dice dónde quedó el recuerdo |
| 2 | Correr el recogido | El puntero se saca | Se sacó |
| 3 | Comprobar que no quedó **ni el texto ni el puntero** | Ninguno | Ninguno: el almacén quedó sin archivos `.md` |
| 4 | Comprobar que el recuerdo del repositorio sigue intacto | Intacto | Intacto |
| 5 | Comprobar que no hay dos versiones del mismo recuerdo | Una sola | **Una sola** |

> **Por qué el puntero es tan malo como la copia.** Un archivo que dice «esto vive en el repositorio» envejece igual que el texto: el día que el recuerdo se renombre, el puntero manda a un sitio que ya no está. Y quien lo lea creerá que ahí estaba todo.

---

### Detalle de CP-003 — Qué hay hoy en el almacén de esta máquina

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Mirar el almacén sin tocarlo | Se ve qué hay | `~/.claude/projects/c--Ing--Jose-ia-agente/memory/` — **vacío** |
| 2 | Anotar qué había, con la fecha | Queda escrito | **Nada, el 2026-08-17.** Ni un archivo |
| 3 | Si hay algo, **no** borrarlo a mano | Se deja que el programa lo recoja | No hizo falta |
| 4 | Correr el recogido y volver a mirar | Se anota qué quedó | No hizo falta: ya estaba vacío |
| 5 | Si quedó algo, anotarlo como hallazgo | Queda propuesto | Nada que anotar |

**El resultado que importa: el almacén está vacío, y no porque nadie lo use.** Los 18 recuerdos están en el repositorio, y `hook_recuerdos.py` corre al abrir la sesión y cada vez que se escribe un archivo. Que esté vacío es la prueba de que el automatismo trabaja, no de que nadie guarde nada.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Qué hay en el almacén real | Listándolo sin escribir nada | **Vacío**, el 2026-08-17 |
| 2 | Que el recogido no borre nunca | Leyendo `recuerdos.migrar` | No borra: mueve, y si el nombre está ocupado entra como `<nombre>-local.md` |
| 3 | Que no queden dos versiones | Contando los dos lados tras recoger | 0 en el almacén, 1 en el repositorio |
| 4 | Que la suite entera siga verde | `python validadores/pruebas.py` | 260 pruebas · verde, con 2 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Media | El recogido **se lleva todo archivo** del almacén, no solo los recuerdos. Un `config.json` acabaría en `historico-chat/memory/` | Probado con fallo esperado en [`validadores/pruebas.py`](../../../../../validadores/pruebas.py). **No se parcheó**: las dos salidas están en §2 y elegir entre ellas toca `01·C19`, que es `base/` — decisión del usuario |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-006-sacar-del-almacen-local.md#ca-01--el-almacén-queda-vacío) | CP-001, CP-003 | El almacén queda vacío, y el de esta máquina lo está. **Pero se lleva también lo que no es recuerdo**, y el caso lo pedía al revés | **No** |
| [CA-02](../HU-006-sacar-del-almacen-local.md#ca-02--no-queda-un-puntero-en-lugar-del-texto) | CP-002 | Ni el texto ni el puntero sobreviven, y el recuerdo del repositorio queda intacto y único | Sí |
| RNF · que no haya dos versiones | CP-002, verificación 3 | 0 en el almacén, 1 en el repositorio | Sí |
| Transversal · Límites | Prueba ya existente | Nombres que solo difieren en mayúsculas se tratan como el mismo archivo — probado, y por eso el recogido no pisa el índice en Windows | Sí |
| Transversal · Privacidad | CP-002, y `IndiceDeLosRecuerdos` | Lo movido queda en la misma carpeta que el resto y pasa por el mismo detector de secretos: 0 hallazgos | Sí |

**El que no cumple:** el **CA-01**, en su paso 5. No se corrige acá: las dos salidas están escritas y elegir toca `01·C19`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | Plan §12 | 3 de 3 | 3 de 3 | Sí |
| Recuerdos del almacén real borrados a mano | Plan §12 | **0** | **0** — el almacén ya estaba vacío | Sí |
| Punteros que sobreviven al recogido | Plan §12 | **0** | **0** | Sí |
| Archivos que no son recuerdos llevados por error | Plan §12 | **0** | **1** en la prueba: un `config.json` | **No** |
| Estado del almacén de esta máquina | Plan §12 | Anotado, con su fecha | Vacío, el 2026-08-17 | Sí |

**Lo que no se cumplió:** la quinta meta, y el plan la había puesto bien. Lo que no está resuelto es qué debe hacer el recogido con lo que no es un recuerdo.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-02 quedó verificado a fondo —ni el texto ni el puntero sobreviven, y no quedan dos versiones— y el almacén de esta máquina está **vacío**, que es la prueba de que el automatismo trabaja. El CA-01 falla en un solo punto: el recogido **se lleva todo**, también lo que no es un recuerdo.

**Qué falta para que cumpla:** elegir entre las dos salidas de §2 —que el recogido distinga y `C19` acepte lo que queda, o que se lleve todo y quede dicho—. **Toca `01·C19`, que es `base/`: es decisión del usuario.**

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `ElAlmacenLocalQuedaVacio` (6 pruebas, 1 fallo esperado) y `Recuerdos` (12, ya existentes) |
| EV-02 | Lectura del almacén real | §2 y §3: vacío el 2026-08-17 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 260 pruebas, verde, 2 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
