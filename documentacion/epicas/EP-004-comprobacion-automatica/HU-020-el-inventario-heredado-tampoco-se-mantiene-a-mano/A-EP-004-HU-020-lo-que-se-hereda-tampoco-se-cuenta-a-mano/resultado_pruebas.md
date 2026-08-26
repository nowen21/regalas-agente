# Resultado de Pruebas — Fase `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado, y si cada criterio de aceptación quedó cumplido**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md); lo que quedó construido, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-26 |
| **Ejecutado por** | El agente |
| **Ciclo** | 2. El ciclo 1 dejó un sabotaje en verde que sí saboteaba |

---

## 2. Veredicto

**Cumple.**

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| Criterios en verde | 4 de 4 | 4 de 4 |
| Sabotajes cazados | Todos | 7 de 7, **en el ciclo 2** |
| Pruebas de la `HU-019` que hubo que tocar | 0 | **1**, y no por su comportamiento — ver §4.4 |
| Fallas en la suite completa | 0 | 0, sobre **381 pruebas** |

---

## 3. Resultado por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 | El inventario en `documentacion/` se vigila | ✅ |
| CP-002 | La misma vigilancia en otra carpeta, y sin corregir | ✅ |
| CP-003 | La plantilla conserva lo que no es derivable | ✅ |
| CP-004 | El comando que la plantilla enseña funciona al copiarlo | ✅ |
| CP-005 | La búsqueda tiene el alcance que se declaró | ✅ |
| CP-006 | Lo de antes no se rompió | ✅ |
| CP-007 | La versión subió y lo dice | ✅ |

### CP-001 y CP-002 — La vigilancia llega a los proyectos

Sobre proyectos de mentira en carpeta temporal:

| Situación | Avisos |
|---|---|
| Inventario en `documentacion/inventario-hu.md` con la cuenta | 1 |
| Inventario llamado `cuanto-falta.md`, no `inventario-hu.md` | 1, y el aviso nombra `documentacion/cuanto-falta.md` |
| Inventario en `pendientes/tablero.md` | 1 |
| Sin la fila de la cuenta | 0 |

**El nombre del archivo no decide nada**, y eso es a propósito: la plantilla no lo fija, cada proyecto lo elige. Lo constante es la forma del defecto.

Y **el archivo no cambió ni un byte** al correr la comprobación, ni se creó ninguno en su carpeta.

### CP-003 — La plantilla conserva lo no derivable

| Qué | Antes | Después |
|---|---|---|
| Rótulos de cuenta como campo | 3 | **0** |
| Tabla de una fila por historia | 1 | **0** |
| Dónde vive el inventario | Sí | Sí |
| Orden en que se escriben los cinco documentos | Sí | Sí |
| Distinción construcción / retrodocumentación | Sí | Sí |
| Cómo se sabe que cerró | Sí | Sí |

**Y ganó una sección que antes no existía:** «Por qué cambió la cuenta». Es lo único del documento que no sale del árbol, y por eso lo único que se sigue escribiendo a mano.

### CP-004 — El comando, copiado literal

Se leyó de la plantilla con una expresión, no se escribió a mano en la prueba: si difieren, se ve. Se reemplazó el marcador `«RUTA-ESTANDAR»` como lo hace `instalar.py`, y se corrió desde la carpeta de un proyecto de mentira. Salida:

```
0 falla(s), 3 aviso(s).
HU: 1 en total · 0 completas · 1 incompletas (F12.2)
```

Lista qué le falta a la historia **y** da la cuenta.

**Este caso encontró un defecto real, y no en el código.** El primer intento no dio salida, y la causa era que el guion partía la orden por espacios — y la ruta de este repositorio tiene uno, `Ing. Jose`. El comando funcionaba; el guion estaba mal. **Pero eso mismo le va a pasar a cualquiera que copie el comando a una terminal**, porque la plantilla lo escribía sin comillas. Se corrigió la plantilla, y `CP-005` de las pruebas automáticas lo vigila.

### CP-005 — El alcance de la búsqueda

| Dónde está el archivo con la cuenta | Se reporta |
|---|---|
| `pendientes/` (primer nivel) | Sí |
| `documentacion/` (primer nivel) | Sí |
| `notas/` | **No** |
| `documentacion/epicas/` (subcarpeta) | **No** |

Y el recorrido, medido contando carpetas abiertas:

| Qué | Cuánto |
|---|---|
| Carpetas que abre la comprobación | **2** |
| Archivos que llega a leer | **7** |
| Carpetas que tendría el árbol de `documentacion/` | **541** |

**Se cuenta el recorrido y no se miden segundos** a propósito: en un árbol de tres carpetas el tiempo no dice nada del tiempo en uno de mil, y el conteo sí.

### CP-006 — Lo de antes no se rompió

| Qué | Antes | Después |
|---|---|---|
| Pruebas de `InventarioDeHU` | 18, verdes | 26, verdes |
| Avisos de `validar.py fases` | 54 | 55 |
| El pendiente 48 reportado | No | No |
| Suite completa | 373, OK | **381, OK** |

**El aviso de más no es una regresión: es un defecto real que este cambio destapó**, y está en §4.5.

### CP-007 — La versión subió y lo dice

`VERSION` pasó de `34.1.0` a `34.2.0`. La entrada del `CHANGELOG` está marcada **MENOR**, nombra la plantilla y la comprobación, y dice que **el inventario de un proyecto no se toca ni se migra**: el aviso informa. `validar.py versionado` pasa.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Siete. Restaurados **con copia**.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | La búsqueda vuelve a una ruta fija | Cazado (3) | Cazado (3) |
| 2 | Recorre el árbol entero, no el primer nivel | Cazado (1) | Cazado (1) |
| 3 | El aviso nombra una ruta fija | Cazado (1) | Cazado (1) |
| 4 | La comprobación se descuelga de la corrida | Cazado (1) | Cazado (1) |
| 5 | La plantilla vuelve a pedir la cuenta | **En verde** | Cazado (1) |
| 6 | La plantilla vuelve a traer la tabla | Cazado (1) | Cazado (1) |
| 7 | El comando pierde las comillas | Cazado (1) | Cazado (1) |

### 4.2 El sabotaje que pasó en verde, y sí saboteaba

`S-033` pide correr el escenario y mirar el estado final antes de decidir. Se hizo, y el diagnóstico fue **prueba floja**, no sabotaje malo.

La comprobación busca el rótulo **con un número al lado** — `| **Total de HU** | 113 |` — porque en un inventario de verdad el defecto es un número escrito. El sabotaje devolvió el campo a la plantilla como **`| **Total de HU** | «N» |`**, que es la forma que tiene en una plantilla: el hueco por llenar. Sin número, no había coincidencia.

**El mismo defecto tiene dos formas, y una sola expresión no caza las dos.** Y era invisible justo en el archivo donde más caro sale, porque la plantilla es la que se copia.

**No se arregló haciendo la expresión más laxa.** Que el inventario de verdad exija un número es correcto: su narrativa tiene cifras, y marcarlas volvería el aviso ruido. Son dos comprobaciones con dos formas. Queda `S-046`.

### 4.3 Rastros

Ninguno. Los siete sabotajes editan un archivo que se restaura con copia, y las pruebas escriben solo en carpeta temporal.

### 4.4 Una prueba de la `HU-019` sí se tocó, y conviene decir por qué

La meta era **cero**. Fue **una**, y **no por su comportamiento**: `test_avisar_de_la_cuenta_no_toca_el_archivo` abría el archivo sin cerrarlo y la corrida lanzaba un `ResourceWarning`. Se envolvió en `with`. **Lo que comprueba, sus datos y su veredicto son los mismos**; ninguna otra se tocó, y las siete siguen pasando contra la comprobación generalizada, que es lo que `RNF-02` pedía demostrar.

### 4.5 Un defecto que este cambio destapó, y que no estaba en el plan

Al subir `VERSION`, apareció un aviso nuevo sobre el cierre de la fase anterior: **no dice bajo qué versión del estándar cerró**.

La causa es propia. En ese cierre se escribió «la versión que declara `VERSION`» en vez del número, aplicando —en el sitio equivocado— la regla que esa misma fase venía de instalar. **La cuenta de historias es derivable y el puntero la mejora; la versión al cerrar es una foto, y el puntero la falsifica** el día que la fuente cambia. Que es hoy.

**No se corrigió**: el archivo no está declarado en §2.1 de esta fase, y `02·F8` prohíbe editar lo que el plan no declara. Se reporta para que el usuario decida. Queda `S-047`.

### 4.6 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Trazabilidad criterio a evidencia

| CA / RNF | Evidencia | Estado |
|---|---|---|
| CA-01 — la plantilla no pide mantener una cuenta | CP-003, CP-004 | ✅ |
| CA-02 — se vigila donde el proyecto lo tenga | CP-001, CP-002 | ✅ |
| CA-02 — y sigue sin corregir | CP-002 | ✅ |
| CA-03 — lo no derivable se conserva | CP-003 | ✅ |
| CA-04 — la versión sube y lo dice | CP-007 | ✅ |
| RNF-01 — no recorre el proyecto entero | CP-005: 2 carpetas contra 541 | ✅ |
| RNF-02 — un inventario en `pendientes/` sigue igual | CP-006, y §4.4 | ✅ |

---

## 6. Veredicto final

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno de esta fase. Uno **reportado y no corregido**, por estar fuera de lo declarado: §4.5 |
| **Suite** | `python validadores/pruebas.py`: **381 pruebas, OK** |

### Defectos encontrados

| ID | Qué era | Cómo se cazó | Estado |
|---|---|---|---|
| DEF-01 | La prueba de la plantilla no veía el defecto en su forma de plantilla (`«N»` en vez de un número) | Sabotaje 5 | Corregido. `S-046` |
| DEF-02 | El comando de la plantilla, sin comillas, se parte si la ruta tiene espacios | `CP-004`, corriéndolo | Corregido, y con prueba que lo vigila |
| DEF-03 | El cierre de la fase anterior apunta a `VERSION` en vez de decir su número | El validador, al subir la versión | **Reportado, no corregido**: fuera de §2.1. `S-047` |

---

## 7. Lo que este resultado NO dice

- **No dice que los inventarios de proyectos existentes estén bien.** Dice que ahora se avisan. Arreglarlos es decisión de cada proyecto, y así quedó escrito en el `CHANGELOG`.
- **No cubre otras plantillas.** Si alguna enseña a mantener a mano algo derivable, sigue enseñándolo.
- **No dice que la búsqueda encuentre un inventario en cualquier sitio.** Encuentra el del primer nivel de `pendientes/` y `documentacion/`, y `CP-005` lo fija a propósito para que ampliarlo sea una decisión y no un accidente.
