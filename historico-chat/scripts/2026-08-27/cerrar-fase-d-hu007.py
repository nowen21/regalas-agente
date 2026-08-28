# -*- coding: utf-8 -*-
"""Escribe el resultado, el estado y el cierre de la fase D de EP-001-HU-007."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
D = os.path.join(RAIZ, "documentacion", "epicas",
                 "EP-001-cuerpo-de-reglas-heredable",
                 "HU-007-regla-de-las-reglas",
                 "D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide")


def escribir(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


escribir("resultado_pruebas.md", u"""# Resultado de Pruebas \u2014 Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide`   \u00b7   `[CAPA 3]`

**Para qu\u00e9 sirve este documento.** Dice **qu\u00e9 se ejecut\u00f3 de verdad y qu\u00e9 sali\u00f3**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificaci\u00f3n

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versi\u00f3n 1 |
| **Fecha de ejecuci\u00f3n** | 2026-08-27 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificaci\u00f3n:** el `CA-04` pide **tres cosas** y las tres se cumplen, comprobadas corriendo `vigencia.py` y no citando a nadie.

| M\u00e9trica | Meta | Real |
|---|---|---|
| Casos ejecutados | 5 de 5 | 5 de 5 |
| Exigencias del criterio comprobadas | 3 de 3 | **3 de 3** |
| **Mediciones heredadas de la fase `A`** | 0 | **0** |
| Archivos que cambian al correrlo | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 \u2014 Se obtiene la lista

```
251 reglas \u00b7 251 sin revisar de fondo \u00b7 0 con fecha

REGLA    REVISADA     SELLO DE     FALLA HOY
```

Cubre **las 251**, y lo dice en su propia salida.

### CP-002 \u2014 La lista dice cu\u00e1ndo y cu\u00e1ntos

| Lo que el criterio nombra | Columna |
|---|---|
| Cu\u00e1ndo se revis\u00f3 | **`REVISADA`** |
| Cu\u00e1ntos incumplimientos produce hoy | **`FALLA HOY`** |

**Se comprueban por separado** en vez de dar por buena \u00abla tabla\u00bb.

### CP-003 \u2014 Est\u00e1 ordenada de la m\u00e1s vieja a la m\u00e1s nueva

**25 sellos le\u00eddos en el orden en que salen, y la secuencia no retrocede.** Las que no tienen sello van primero, que es lo correcto: son las que m\u00e1s llevan.

**Es el \u00fanico caso que pod\u00eda fallar de verdad.** Que la lista exista es f\u00e1cil de ver; que est\u00e9 ordenada es lo que el criterio exige y lo que nadie mira.

### CP-004 \u2014 El programa avisa, no corrige

Correrlo **no cambia ning\u00fan archivo**, comprobado contra el estado del repositorio antes y despu\u00e9s.

### CP-005 \u2014 La ausencia de fechas es deliberada

El procedimiento lo dice en una l\u00ednea:

> *\u00abArranca ausente en todas las reglas, a prop\u00f3sito. Pon\u00e9rsela de una vez a las doscientas habr\u00eda sido escribir doscientas fechas que no responden por ninguna revisi\u00f3n: el sello vac\u00edo que este documento viene a evitar.\u00bb*

Y el `CA-04`, le\u00eddo entero, **no pide reglas revisadas** en ninguna parte.

---

## 4. Verificaciones manuales  \u00b7  `08\u00b7T4`

### 4.1 Por qu\u00e9 la fase `A` se equivoc\u00f3

Su `CA-04` pide que **se sepa qu\u00e9 reglas llevan m\u00e1s tiempo sin revisarse**. Cerr\u00f3 en rojo citando *\u00ab249 de 249 sin dato\u00bb* \u2014 **una cifra que el criterio no menciona**.

**La lista exist\u00eda, estaba ordenada y dec\u00eda las dos cosas.** Lo que no exist\u00eda era el trabajo de revisar, que es otra historia y ni siquiera es deuda: el procedimiento dice que arranca as\u00ed a prop\u00f3sito.

**Es el segundo veredicto del d\u00eda que mide algo de al lado**, y el primero \u2014`EP-003\u00b7HU-002`\u2014 fall\u00f3 exactamente igual: encontr\u00f3 un hueco real y lo cobr\u00f3 en la factura equivocada.

### 4.2 Y el agente lo repiti\u00f3, sabi\u00e9ndolo

**Este trabajo se recomend\u00f3 tres veces** como \u00abla deuda de las 250 reglas\u00bb, sin abrir el criterio ni el procedimiento. Se cay\u00f3 en la primera lectura, y lo que oblig\u00f3 a leerlo fue **ir a ejecutarlo**.

`S-063` \u2014 *un veredicto puede estar mal el d\u00eda que se escribe\u2014* se hab\u00eda escrito **dos horas antes**. Nombrarlo no evit\u00f3 repetirlo. Est\u00e1 en `S-069`.

### 4.3 El hallazgo de la fase `A` se conserva

Que **nadie hubiera revisado ninguna regla de fondo** era cierto, y sigue si\u00e9ndolo. Lo que se corrige es d\u00f3nde se cobra: **no es un incumplimiento del `CA-04`**, es trabajo por hacer cuando el usuario lo decida.

Y hay un dato que ese rojo tapaba: **la columna \u00abfalla hoy\u00bb est\u00e1 vac\u00eda en todas**. El procedimiento dice que ese n\u00famero se lee en las dos direcciones \u2014 *\u00abuna regla vieja que no ha fallado nunca hay que mirarla por el motivo contrario: puede que ya nadie la est\u00e9 aplicando\u00bb*.

### 4.4 Rastros

Ninguno. No se edit\u00f3 ning\u00fan documento para probar.

### 4.5 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00\u00b7N6`).

---

## 5. Defectos encontrados

**Ninguno propio.** El \u00fanico hallazgo es sobre el veredicto de la fase `A`, y est\u00e1 en el \u00a74.1.

---

## 6. Evidencias

- La salida de `python validadores/vigencia.py`, con sus 251 reglas y sus columnas
- El `CA-04` transcrito palabra por palabra en el \u00a72.1 del [plan de trabajo](plan_trabajo.md)
- El guion que lo midi\u00f3, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
""")

escribir("estado-fase.md", u"""# Estado de fase \u2014 Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` (m\u00f3dulo Meta-reglas)   \u00b7   `[CAPA 3]`

---

## 0. Identificaci\u00f3n

| Campo | Valor |
|---|---|
| **Fase** (identificador \u00b7 `02\u00b7F12.6`) | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **M\u00f3dulo** | Meta-reglas |
| **Planteamiento / \u00c9pica / HU** | [EP-001](../../epica.md) \u00b7 [HU-007](../HU-007-regla-de-las-reglas.md) |
| **\u00daltima actualizaci\u00f3n** | 2026-08-27 |

---

## 1. En qu\u00e9 estaci\u00f3n va

**Estaci\u00f3n actual:** 12 \u00b7 Commit. **\u00daltima puerta pasada:** 11.

| # | Estaci\u00f3n | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador \u00b7 an\u00e1lisis | contexto entendido | \u2705 |
| 2 | Proponente \u00b7 alcance | \U0001F464 alcance aprobado | \u2705 2026-08-27 |
| 3 | Escritor de \u00e9pica | \U0001F464 \u00e9pica aprobada | \u2705 Ya exist\u00eda |
| 4 | Escritor de historia | \U0001F464 HUs aprobadas | \u2705 Ya exist\u00eda |
| 5 | Escritor de especificaci\u00f3n | \U0001F464 especificaci\u00f3n aprobada | \u2705 `02\u00b7F19` |
| 6 | Dise\u00f1ador | dise\u00f1o coherente | \u2705 No se toca c\u00f3digo |
| 7 | Planificador de tareas | \U0001F464 plan + pruebas aprobados | \u2705 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | \u2705 |
| 9 | Verificador | trazabilidad sin faltantes | \u2705 5 tareas, 5 con resultado |
| 10 | Cr\u00edtico | sin hallazgos graves | \u2705 |
| 11 | Cierre documental + se\u00f1ales | docs y se\u00f1ales al d\u00eda | \u2705 `S-069` |
| 12 | Commit | \U0001F464 autorizado | \u2610 **Esperando aprobaci\u00f3n del usuario** |
| 13 | Publicaci\u00f3n / despliegue | \U0001F464 autorizado | \u2610 |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 \u2014 el `CA-04`, en sus tres exigencias |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) \u00a72 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 \u00b7 correr y comprobar que da una lista | Terminada | 251 reglas |
| T-02 \u00b7 que diga cu\u00e1ndo y cu\u00e1ntos | Terminada | `REVISADA` y `FALLA HOY` |
| T-03 \u00b7 que est\u00e9 **ordenada** | Terminada | 25 sellos, sin retroceder |
| T-04 \u00b7 que avise y no corrija | Terminada | Ning\u00fan archivo cambia |
| T-05 \u00b7 declarar el veredicto y el reemplazo | Terminada | \u2014 |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y se\u00f1ales generadas  \u00b7  [`13\u00b7DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisi\u00f3n / aprendizaje | Se\u00f1al registrada (id/enlace) |
|---|---|
| Recomendar trabajo sin leer el criterio repite el error que uno acaba de se\u00f1alar | [`S-069`](../../../../senales.md) |
| Un veredicto puede estar mal el d\u00eda que se escribe | [`S-063`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobaci\u00f3n del commit**, que se pide aparte de la aprobaci\u00f3n del cambio.
- **Revisar reglas de fondo sigue siendo trabajo \u00fatil**, y ahora es trabajo normal en vez de deuda. Cu\u00e1ndo empezar lo decide el usuario.

---

## 4. Si se bloque\u00f3

No se bloque\u00f3.

**Lo que m\u00e1s cost\u00f3 no fue medir: fue darse cuenta de que hab\u00eda que leer el criterio.** Este trabajo se recomend\u00f3 tres veces como \u00abla deuda de las 250 reglas\u00bb, y se cay\u00f3 en la primera lectura \u2014 la que se hizo **para ejecutarlo**, no para revisarlo.
""")
print("resultado y estado escritos")
