# -*- coding: utf-8 -*-
"""Escribe la fase B de EP-007 HU-002 y pone la historia al dia.

Vive en el repositorio, no en una carpeta temporal: es el guion que escribio
los documentos de esa fase, y sin el las cifras no tienen de donde salir
(`04·S9`).
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas",
                  "EP-007-instalacion-y-actualizacion",
                  "HU-002-mostrar-antes-de-hacer")
F = "B-EP-007-HU-002-el-registro-de-version-se-anuncia"
M = u"Instalación"
D = os.path.join(HU, F)
if not os.path.isdir(D):
    os.makedirs(D)


def w(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


w("estado-fase.md", u"""# Estado de fase — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Planteamiento / Épica / HU** | [EP-007](../../epica.md) · [HU-002](../HU-002-mostrar-antes-de-hacer.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó el defecto `D-01` de la fase `A` y su prueba |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA-02 |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 4 de 4 de la clase, sin fallos esperados |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el CA-02 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. El `D-02` de la fase `A` sigue abierto y no deja ningún CA en «No» |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · reproducir el defecto | Terminada | La prueba estaba escrita como fallo esperado desde el 2026-08-22 |
| T-02 · que la simulación mire la huella que va a quedar | Terminada | `_huellas_previstas`, en `instalar.py` |
| T-03 · que anuncie el archivo, no la carpeta | Terminada | `versiones.nombre_previsto` |
| T-04 · sacar la prueba del fallo esperado | Terminada | 4 de 4 en verde |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La simulación no mentía sobre lo que iba a hacer: se miraba en el espejo equivocado | Este cierre, §5 |
| Anunciar la carpeta y no el archivo deja el registro fuera de lo que se compara | §3 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Lo que bloqueaba a la fase `A` era `02·F8`: su plan aprobado no
declaraba `instalar.py`, y por eso el arreglo quedó propuesto y no hecho. El
plan de esta fase sí lo declara.
""".format(F=F, M=M))

w("plan_trabajo.md", u"""# Plan de Trabajo — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Épica** | [EP-007](../../epica.md) |
| **HU** | [HU-002](../HU-002-mostrar-antes-de-hacer.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-02 y el defecto `D-01` de la fase [`A`](../A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md).** La simulación del instalador anunciaba 12 de 13 archivos. El que faltaba era `documentacion/versiones/<fecha>-<version>.md`, **el que deja constancia de qué se instaló**.

**Por qué la fase `A` no lo arregló:** el arreglo toca `instalar.py`, y el §2.1 de su plan aprobado no lo declaraba. `02·F8` no deja tocar lo que el plan no nombra, así que quedó propuesto. **El plan de esta fase lo declara**, y con eso se destraba.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que lo que la simulación anuncia sea exactamente lo que aparece al aplicar, incluido el registro de versión.

**Fuera de alcance:**

- El defecto `D-02` de la fase `A`, sobre la línea que muestra la orden literal de git. No deja ningún CA en «No».
- Cambiar **cuándo** se escribe el registro. Lo que estaba mal era el anuncio, no la regla de cuándo registrar.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
103 cumplen, 6 no cumplen, 5 sin veredicto
```

### 2.1 La causa, y por qué no era una mentira del anuncio

`registrar_version` decide si hay algo que registrar comparando dos juegos de
huellas: las de antes de la corrida y las del proyecto **en ese momento**.

Al aplicar, «ese momento» es después de copiar, y la comparación ve los
cambios. **Al simular, no se ha copiado nada todavía**, así que las dos son
iguales y la respuesta es «no hay actualización que registrar». Después, al
aplicar de verdad, el registro se escribe.

La simulación no estaba mintiendo sobre lo que iba a hacer: **se estaba mirando
en el espejo equivocado**. Lo que tiene que comparar es la huella que va a
quedar, que es la central de cada componente: al terminar de instalar, el
proyecto tiene esa.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Instalación | `_huellas_previstas` y su uso en `registrar_version` |
| `validadores/versiones.py` | Modificar | Instalación | `nombre_previsto`, para poder anunciar el archivo |
| `validadores/pruebas.py` | Modificar | Pruebas | La prueba sale del fallo esperado |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-002-mostrar-antes-de-hacer.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

**Los dos primeros son los que la fase `A` no podía tocar.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Al simular se compara la huella **prevista** | Escribir el registro también en simulación | Simular no escribe nada, y eso es el CA-01, que ya cumplía |
| Se anuncia **el archivo**, no la carpeta | Dejar «registrar la actualización en `versiones/`» | Anunciar el sitio y no la cosa deja el registro fuera de la lista que después se compara |
| El nombre se predice con la misma función que lo elige | Inventar el nombre en el anuncio | Si el nombre se calculara en dos sitios, el anuncio y el archivo se separarían el día que uno cambie |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reproducir el defecto | Calidad | 0,25 h | — | EV-01 |
| T-02 | Que la simulación mire la huella que va a quedar | Instalación | 1 h | T-01 | EV-02 |
| T-03 | Que anuncie el archivo, no la carpeta | Instalación | 0,5 h | T-02 | EV-02 |
| T-04 | Sacar la prueba del fallo esperado | Pruebas | 0,25 h | T-03 | EV-02 |

**Total estimado:** 2 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-03` no es cosmética: sin ella la `T-02` sola no cierra el criterio, porque
la prueba compara **nombres de archivo**, y un anuncio que solo nombra la
carpeta no contiene ninguno.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02, lo que muestra es lo que hace | Simular, aplicar, y comparar los archivos nuevos contra lo anunciado | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Un proyecto de prueba que la propia prueba arma y borra. Ningún proyecto real se
toca.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. El instalador no deja estado fuera del
proyecto que instala.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** El cambio se nota la próxima vez que alguien corra el
instalador sin `--aplicar`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8`, solo se tocan los archivos que el plan declara. Es la regla que dejó este defecto sin arreglar, y por eso este plan los nombra.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la simulación empiece a escribir algo | Rompería el CA-01, que ya cumplía | La prueba de «no escribe ni un archivo» sigue corriendo | Cerrado |
| B-02 | Que el nombre anunciado y el escrito se separen | Volvería el mismo defecto por otra puerta | Los dos salen de `_nombre_libre` | Cerrado |

---

## 11. Definition of Done

- [x] El defecto, reproducido
- [x] Las cuatro pruebas de la clase, en verde
- [x] Ningún fallo esperado en la clase
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
""".format(F=F, M=M))

w("plan_pruebas.md", u"""# Plan de Pruebas — Fase `{F}`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-02 de la HU-002: **cada archivo que la simulación anuncia aparece al aplicar, y no aparece ninguno que no se hubiera anunciado.**

### 1.2 Alcance

**Dentro:** la corrida simulada y la corrida aplicada sobre el mismo proyecto de prueba, comparadas archivo por archivo.

**Fuera:** el defecto `D-02` de la fase `A`, y el CA-01, que ya cumplía y solo se cuida de no romper.

### 1.3 Documentos de referencia

- [HU-002](../HU-002-mostrar-antes-de-hacer.md)
- [Resultado de la fase A](../A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md), defecto `D-01`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Los archivos nuevos tras aplicar, contra lo anunciado | Es lo que el CA-02 mide |
| Que simular siga sin escribir nada | El arreglo toca el mismo código; romper el CA-01 sería peor que el defecto |
| Que un proyecto al día siga sin anunciar trabajo | La huella prevista es igual a la que hay, y no debe inventar cambios |

---

## 3. Estrategia de pruebas

De sistema: se corre el instalador de verdad, dos veces, sobre un proyecto de
prueba que la prueba arma y borra.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El defecto, reproducido: la prueba existía como fallo esperado.

### 4.2 Criterios de salida

- Ningún archivo aparece sin haberse anunciado.
- Las cuatro pruebas de la clase en verde, **sin ningún fallo esperado**.

### 4.3 Criterios de suspensión y reanudación

Si al arreglar el anuncio la simulación empezara a escribir, se suspende: el
CA-01 pesa más que el CA-02.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-02 | CP-003 |
| CA-01 (no romper) | CP-002, CP-004 |

---

## 6. Casos de prueba

### CP-003 — Lo que muestra es lo que hace

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | De sistema |
| **Prioridad** | **Crítica** |
| **Cómo** | Simular sobre un proyecto nuevo, guardar la salida, aplicar, y comprobar que el nombre de cada archivo nuevo aparece en la salida simulada |
| **Resultado esperado** | Ninguno sin anunciar |

### CP-002 — El modo que muestra no escribe ni un archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Simular y comparar el árbol antes y después |
| **Resultado esperado** | Idéntico |

### CP-004 — Un proyecto al día no anuncia trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / transversal de límites |
| **Tipo** | De borde |
| **Prioridad** | Alta |
| **Cómo** | Aplicar y volver a simular |
| **Resultado esperado** | Ninguna línea «(simulado) crear» |

---

## 7. Datos y ambientes de prueba

Un proyecto de prueba temporal, armado y borrado por la propia prueba.

---

## 8. Herramientas

`python -m unittest pruebas.MostrarAntesDeHacer`

---

## 9. Gestión de defectos

Un fallo en CP-002 detiene la fase: significa que el arreglo del anuncio rompió
la promesa de no tocar nada.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 4 de 4 |
| Pruebas marcadas como fallo esperado | **0** |
| Archivos que aparecen sin anunciarse | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
""".format(F=F))

w("resultado_pruebas.md", u"""# Resultado de Pruebas — Fase `{F}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{F}` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-02 se cumple. La simulación compara ahora la huella que
va a quedar y nombra el archivo del registro, así que ningún archivo aparece sin
haberse anunciado. El CA-01 sigue en pie: simular no escribe nada.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 4 de 4 | **4 de 4** |
| Pruebas marcadas como fallo esperado | 0 | **0** |
| Archivos que aparecen sin anunciarse | 0 | **0** |

---

## 3. Resultado por caso

### CP-003 — Lo que muestra es lo que hace

```
Ran 4 tests in 3.941s
OK
```

**Los dos cambios hicieron falta, y por razones distintas.** Comparar la huella
prevista hace que la simulación **sepa** que va a registrar. Nombrar el archivo
hace que lo **diga**: el anuncio anterior nombraba la carpeta, y la prueba
compara nombres de archivo, así que con solo el primer cambio el criterio
seguía sin cumplirse.

**Resultado: pasa.**

### CP-002 — El modo que muestra no escribe ni un archivo

Sigue en verde. El arreglo toca la comparación y el texto del anuncio; no toca
nada que escriba.

**Resultado: pasa.**

### CP-004 — Un proyecto al día no anuncia trabajo

Sigue en verde. Cuando el proyecto está al día, la huella prevista es igual a la
que hay, y la simulación no inventa cambios.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El defecto no era una mentira del anuncio

Vale dejarlo dicho porque cambia dónde se busca. La simulación no estaba
diciendo algo distinto de lo que iba a hacer: estaba comparando el proyecto
consigo mismo antes de tocarlo, y desde ahí **no había ningún cambio que ver**.
El anuncio era correcto sobre un estado que no era el que importaba.

### 4.2 Por qué el nombre se predice con la misma función que lo elige

Si el anuncio calculara el nombre por su cuenta, el día que cambie la forma del
nombre los dos se separan y vuelve el mismo defecto por otra puerta. Los dos
salen de `_nombre_libre`.

---

## 5. Defectos encontrados

**Ninguno nuevo.**

---

## 6. Evidencias

- `validadores/instalar.py`, `_huellas_previstas` y `registrar_version`
- `validadores/versiones.py`, `nombre_previsto`
- `validadores/pruebas.py`, clase `MostrarAntesDeHacer`
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-002](../HU-002-mostrar-antes-de-hacer.md): el CA-02 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |

> **Por qué se declara el reemplazo:** el defecto `D-01` de aquella fase quedó cerrado, con su prueba fuera del fallo esperado. Aquel rojo era cierto el 2026-08-22. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que la simulación del instalador anuncie el registro de versión.**

Anunciaba 12 de 13 archivos. El que faltaba era el que deja constancia de qué se
instaló. La causa: `registrar_version` comparaba el proyecto **consigo mismo**,
y en simulación todavía no se ha copiado nada, así que no había ningún cambio
que ver.

| Antes | Ahora |
|---|---|
| «ni las plantillas ni la versión cambiaron, no hay actualización que registrar» | `registrar documentacion/versiones/<fecha>-<versión>.md` |
| Al aplicar, el registro aparecía sin anunciarse | Aparece el que se anunció |

Dos cambios, y los dos hacían falta: comparar la huella **prevista** para que la
simulación sepa que va a registrar, y nombrar **el archivo** para que lo diga.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-02 | servicio | `validadores/instalar.py`, `validadores/versiones.py` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · reproducir el defecto | ✅ | La prueba, escrita como fallo esperado |
| T-02 · comparar la huella prevista | ✅ | `_huellas_previstas` |
| T-03 · anunciar el archivo | ✅ | `versiones.nombre_previsto` |
| T-04 · sacar la prueba del fallo esperado | ✅ | 4 de 4 en verde |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.MostrarAntesDeHacer`: 4 pruebas, 4 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno nuevo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo:

```
python validadores/instalar.py <proyecto>              ← simula, y ahora lo dice completo
python validadores/instalar.py <proyecto> --aplicar    ← instala
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Al simular se compara la huella **prevista** | Simular no escribe, así que mirar el proyecto de ahora es mirarse en el espejo equivocado |
| Se anuncia el archivo, no la carpeta | Anunciar el sitio deja la cosa fuera de lo que después se compara |
| El nombre se predice con la función que lo elige | Calculado en dos sitios, el anuncio y el archivo se separan el día que uno cambie |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El defecto `D-02` de la fase `A`: una línea del anuncio es la orden literal de git | **Abierto.** No deja ningún CA en «No» |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Se nota la próxima vez que alguien corra el instalador
sin `--aplicar`.
""".format(F=F, M=M))

# La historia, al dia.
R = os.path.join(HU, "HU-002-mostrar-antes-de-hacer.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
viejo = (u"| **Estado** | En curso \u2014 CA-01 y los transversales cumplidos; "
         u"el CA-02, no |")
nuevo = (u"| **Estado** | Terminada \u2014 el CA-02 se cerr\u00f3 en la fase `B`: la "
         u"simulaci\u00f3n anuncia tambi\u00e9n el registro de versi\u00f3n |")
if viejo in t:
    t = t.replace(viejo, nuevo, 1)
    print("estado al dia")
sep = u"| Fase | Qu\u00e9 CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | CA-02 | **Ejecutada el 2026-08-30.** "
        u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
        u"\u2014 la simulaci\u00f3n compara la huella que va a quedar y nombra el "
        u"archivo del registro. Declara reemplazar el veredicto de la fase `A` |\n"
        % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase escrita:", F)
