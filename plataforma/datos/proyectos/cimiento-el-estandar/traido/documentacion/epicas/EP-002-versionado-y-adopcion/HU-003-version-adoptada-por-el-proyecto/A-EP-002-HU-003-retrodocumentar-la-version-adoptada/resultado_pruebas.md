# Resultado de Pruebas — Fase A-EP-002-HU-003-retrodocumentar-la-version-adoptada   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **Proyecto de prueba** | **shopnest-mesa** (`C:\DesarrollosClaude\personales\shopnest-mesa`), Django 5.2.11 |

---

## 1. Ejecución caso por caso

### CA-01 · El proyecto declara su versión y su fecha

`shopnest-mesa` lo declara en su `CLAUDE.md`:

```
- **Versión del estándar adoptada:** `27.2.0` · sellada `2026-08-20`.
```

Y `validar.py version --raiz <proyecto>` lo lee y avisa del desfase: *«el proyecto declara v27.2.0, el estándar va en v32.0.0: subir es decisión del usuario»*. Avisa y no detiene, que es lo previsto.

**Resultado del criterio: Cumple** en la forma. Lo que dice ese número es otra cosa, y está en el D-02.

### CA-02 · Una versión que no existe se detecta

Se copió el `CLAUDE.md` del proyecto a una carpeta temporal, se le puso una versión inventada y se corrió la comprobación. La decisión 35 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) manda hacerlo así y no sobre el proyecto real:

```
- **Versión del estándar adoptada:** `99.9.9` · sellada `2026-08-20`

$ python validadores/validar.py version --raiz C:/tmp/prueba-version
== Versión del estándar · C:/tmp/prueba-version ==
OK: sin incumplimientos.
```

**No la detecta.** Y no es solo que la deje pasar: **la premia con silencio**. Como `99.9.9` es mayor que la vigente, el programa concluye que el proyecto está al día y **deja de avisar del desfase**. Declarar una versión falsa hacia adelante apaga la única comprobación que había.

**Resultado del criterio: No cumple.**

### CA-03 · Queda el historial de adopciones

Existe, y en los tres proyectos del registro:

| Proyecto | Registros en `documentacion/versiones/` |
|---|---|
| shopnest-mesa | 18 |
| RNI | 16 |
| AgroSystem | 12 |

Cada registro dice desde cuándo el proyecto usa una versión, cuál era la anterior y cuál se instaló.

**Resultado del criterio: Cumple.**

---

## 2. Verificaciones manuales

**El historial de shopnest-mesa contradice lo que el proyecto declara.** Su registro más reciente dice:

```
# Actualización a 28.0.0 — 2026-08-20
Desde 2026-08-20 18:35:16 este proyecto usa la versión 28.0.0 del estándar.
| Versión anterior | 27.2.0 |
| Versión instalada | **28.0.0** |
```

Y su `CLAUDE.md`, sellado el mismo día, sigue declarando **27.2.0**. **Nada compara las dos cosas**, así que la contradicción lleva dos días sin que nadie la vea, y el aviso de desfase se calcula sobre el número equivocado.

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Crítica** | Una versión adoptada que no existe pasa sin reporte, y además **silencia el aviso de desfase** si es mayor que la vigente. La comprobación se apaga sola con un número inventado | **Abierto**, necesita pendiente |
| D-02 | **Alta** | La versión declarada y el último registro de adopción pueden contradecirse, y nada los compara. Caso real: shopnest-mesa declara `27.2.0` y su historial dice `28.0.0`, los dos del 2026-08-20 | **Abierto**, mismo pendiente |
| D-03 | Baja | [`plantillas/CLAUDE.md.plantilla`](../../../../../plantillas/CLAUDE.md.plantilla) nombra la carpeta de dos formas: `documentacion/versiones/` en la línea 25 y `versiones/` en la 65. Hizo buscar el historial donde no está, y viaja a cada proyecto instalado | **Abierto** |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, declara versión y fecha | Lectura del `CLAUDE.md` del proyecto y corrida de `validar.py version` | Cumple |
| CA-02, una versión que no existe se detecta | Copia temporal con `99.9.9` | **No cumple** |
| CA-03, queda el historial | 18, 16 y 12 registros en los tres proyectos | Cumple |

## 4.1 Lo que el plan exigía

El plan ya anticipaba el D-01: su «Lo que no existe», punto 1, decía que la comprobación compara contra la vigente y no contra la lista de versiones. **Lo que el plan no anticipaba es que la falta no fuera neutra**: una versión inventada hacia adelante no solo pasa, sino que apaga el aviso que sí funcionaba.

El D-02 no estaba previsto por nadie, y es el que tiene daño hoy.

---

## 5. Veredicto de la fase

**Concepto:** No cumple.

**Justificación:** el CA-02 quedó en rojo y la fase no cierra con un criterio así. Los otros dos cumplen, y de paso la fase encontró en un proyecto real una contradicción que llevaba dos días sin que nadie la viera.

**Qué falta para que cumpla:** que la comprobación mire si la versión declarada existe en el registro de cambios del estándar, y que compare la declarada con el último registro de adopción del proyecto.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La declaración del proyecto | `CLAUDE.md` de shopnest-mesa, línea 41 |
| EV-02 | La versión inventada que pasa | §1, CA-02 |
| EV-03 | El historial y su contradicción | `documentacion/versiones/2026-08-20-28.0.0.md` del proyecto |
| EV-04 | Los dos nombres de la carpeta | `plantillas/CLAUDE.md.plantilla`, líneas 25 y 65 |

---

## 7. Ciclos anteriores

Ninguno: la fase estaba aprobada desde el 2026-08-17 y nunca se había ejecutado.
