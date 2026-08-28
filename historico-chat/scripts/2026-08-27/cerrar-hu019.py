# -*- coding: utf-8 -*-
"""Escribe el estado-fase y el cierre de la fase A de la HU-019."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
D = os.path.join(RAIZ, "documentacion", "epicas",
                 "EP-005-automatismos-que-no-dependen-de-la-memoria",
                 "HU-019-el-hash-del-commit-se-anota-solo",
                 "A-EP-005-HU-019-el-enganche-de-git-pone-el-hash")


def escribir(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


escribir("estado-fase.md", u"""# Estado de fase \u2014 Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` (m\u00f3dulo Enganches)   \u00b7   `[CAPA 3]`

---

## 0. Identificaci\u00f3n

| Campo | Valor |
|---|---|
| **Fase** (identificador \u00b7 `02\u00b7F12.6`) | `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` |
| **M\u00f3dulo** | Enganches |
| **Planteamiento / \u00c9pica / HU** | [EP-005](../../epica.md) \u00b7 [HU-019](../HU-019-el-hash-del-commit-se-anota-solo.md) |
| **\u00daltima actualizaci\u00f3n** | 2026-08-27 |

---

## 1. En qu\u00e9 estaci\u00f3n va

**Estaci\u00f3n actual:** 12 \u00b7 Commit. **\u00daltima puerta pasada:** 11.

| # | Estaci\u00f3n | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador \u00b7 an\u00e1lisis | contexto entendido | \u2705 |
| 2 | Proponente \u00b7 alcance | \U0001F464 alcance aprobado | \u2705 Salidas 1 y 3 del pendiente 87 |
| 3 | Escritor de \u00e9pica | \U0001F464 \u00e9pica aprobada | \u2705 Ya exist\u00eda |
| 4 | Escritor de historia | \U0001F464 HUs aprobadas | \u2705 2026-08-27 |
| 5 | Escritor de especificaci\u00f3n | \U0001F464 especificaci\u00f3n aprobada | \u2705 `02\u00b7F19` |
| 6 | Dise\u00f1ador | dise\u00f1o coherente | \u2705 La duda 1, resuelta midiendo |
| 7 | Planificador de tareas | \U0001F464 plan + pruebas aprobados | \u2705 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | \u2705 500 de 500 |
| 9 | Verificador | trazabilidad sin faltantes | \u2705 11 tareas, 11 con resultado |
| 10 | Cr\u00edtico | sin hallazgos graves | \u2705 Cinco sabotajes, tres ciclos |
| 11 | Cierre documental + se\u00f1ales | docs y se\u00f1ales al d\u00eda | \u2705 `S-066`, `S-067`, `S-068` |
| 12 | Commit | \U0001F464 autorizado | \u2610 **Esperando aprobaci\u00f3n del usuario** |
| 13 | Publicaci\u00f3n / despliegue | \U0001F464 autorizado | \u2610 |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` a `DEF-04` corregidos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) \u00a72 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 \u00b7 impacto sobre las pruebas del instalador | Terminada | Ninguna compara la lista |
| T-01 \u00b7 **resolver la duda 1 midiendo** | Terminada | El archivo queda sin guardar: `S-067` |
| T-02 \u00b7 encontrar la fase que el commit cierra | Terminada | Por la forma del nombre, no por una lista |
| T-03 \u00b7 escribir solo si hay fila, vac\u00eda y con cierre en git | Terminada | Tres condiciones |
| T-04 \u00b7 el enganche, que nunca deshace un commit | Terminada | Termina en 0 pase lo que pase |
| T-05 \u00b7 que el instalador lo cuelgue | Terminada | `post-commit` en `HOOKS` |
| T-06 \u00b7 el conteo con sus tres grupos | Terminada | `22 \u00b7 1 \u00b7 106`, con nombres |
| T-07 \u00b7 los cinco CA | Terminada | 16 pruebas, seis con git de verdad |
| T-08 \u00b7 **correrlo commiteando** | Terminada | Escribe el hash correcto |
| T-09 \u00b7 `CHANGELOG` y `VERSION` | Terminada | `35.6.0`, MENOR |
| T-10 \u00b7 sabotear | Terminada | Cinco; el cuarto fall\u00f3 de dos formas distintas |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y se\u00f1ales generadas  \u00b7  [`13\u00b7DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisi\u00f3n / aprendizaje | Se\u00f1al registrada (id/enlace) |
|---|---|
| Antes de automatizar el llenado de un campo, contar en cu\u00e1ntos documentos existe | [`S-066`](../../../../senales.md) |
| Un enganche que arregla algo despu\u00e9s del commit no puede meterlo dentro de ese commit | [`S-067`](../../../../senales.md) |
| Un sabotaje que no se pudo aplicar no es un sabotaje que pas\u00f3 | [`S-068`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobaci\u00f3n del commit**, que se pide aparte de la aprobaci\u00f3n del cambio.
- **Las 22 fases con la marca pendiente y las 106 sin la fila.** Se cuentan y se nombran; ponerlas al d\u00eda se decide aparte.

---

## 4. Si se bloque\u00f3

No se bloque\u00f3, y **la duda declarada se resolvi\u00f3 midiendo antes de escribir c\u00f3digo**: el hash no existe hasta que el commit est\u00e1 hecho, as\u00ed que la anotaci\u00f3n llega despu\u00e9s y **el archivo queda sin guardar**. Las otras dos salidas romp\u00edan una regla \u2014 una se muerde la cola, la otra cruza `00\u00b7N1`.
""")
print("estado-fase escrito")
