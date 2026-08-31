# -*- coding: utf-8 -*-
"""Escribe las fases B de EP-006 HU-002 y HU-005, y pone las historias al dia.

Las dos cierran por decision del usuario del 2026-08-30, no por medicion: una
relee su criterio y la otra aplica cual de las dos copias manda.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
EP = os.path.join(RAIZ, "documentacion", "epicas", "EP-006-memoria-de-lo-aprendido")
M = u"Memoria"

CASOS = [
    dict(
        hu_dir="HU-002-guardar-en-el-repositorio",
        hu_md="HU-002-guardar-en-el-repositorio.md",
        hu="HU-002",
        fase="B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento",
        roja="A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio",
        fecha_rojo="2026-08-17",
        criterio=u"CA-01, lo guardado vive en el repositorio con su historial",
        estado_viejo=u"| **Estado** | En curso — CA-02 y transversales cumplidos; el CA-01 solo para los recuerdos, no para las señales |",
        estado_nuevo=u"| **Estado** | Terminada — el CA-01 se cumple para los recuerdos, y para las señales se releyó en la fase `B`: viven en la base de Cimiento |",
        fila_cubre=u"CA-01, releído",
        fila_estado=u"el criterio se releyó: los recuerdos viven en el repositorio y las señales en la base de Cimiento, que es la línea base de todos los proyectos. Declara reemplazar el veredicto de la fase `A`",
    ),
    dict(
        hu_dir="HU-005-separar-aprendizaje-de-preferencia",
        hu_md="HU-005-separar-aprendizaje-de-preferencia.md",
        hu="HU-005",
        fase="B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza",
        roja="A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia",
        fecha_rojo="2026-08-17",
        criterio=u"CA-01, nada está guardado en los dos sitios diciendo cosas distintas",
        estado_viejo=u"| **Estado** | En curso — CA-02 y transversales cumplidos; el CA-01 no: hay algo guardado en los dos sitios |",
        estado_nuevo=u"| **Estado** | Terminada — el CA-01 se cerró en la fase `B`: manda el recuerdo, y la señal que decía lo contrario quedó reemplazada |",
        fila_cubre=u"CA-01",
        fila_estado=u"la señal `S-002` quedó `reemplazada` por la `S-269`, que dice lo mismo que el recuerdo. Declara reemplazar el veredicto de la fase `A`",
    ),
]

CUERPOS = {}

CUERPOS["HU-002"] = dict(
    que_decia=u"las **237 señales** no estaban versionadas: `memoria/senales.db` está en `.gitignore` a propósito y no tiene ningún historial. Los 18 recuerdos sí cumplían",
    decision=u"**Las señales se quedan en su propia base, la de Cimiento.** Cimiento es la línea base de todos los proyectos, y su memoria es de todos: hoy la base guarda **268 señales**, de las cuales **186 son de siete proyectos distintos** y 82 son de organización. Meterla al control de versiones de este repositorio la ataría a uno solo de los proyectos que sirve.",
    porque=u"""**Por qué el criterio se relee y no se incumple.** El `CA-01` se escribió pensando en un solo repositorio, cuando la memoria era una carpeta de archivos. Al crecer resultaron ser dos cosas con dueños distintos:

- **Los recuerdos** son de este repositorio y de quien trabaja en él. Viven en `historico-chat/memory/`, versionados, y ahí el criterio se cumple entero: 23 archivos con su índice.
- **Las señales** son de Cimiento, que es la línea base de todos los proyectos. Su base es compartida, y por eso no puede vivir dentro del control de versiones de uno.

Lo que este repositorio sí versiona de señales es [`documentacion/senales.md`](../../../../../documentacion/senales.md), las suyas: 85 al cerrar esta fase.

**Y lo que no se decidió acá:** cómo se respalda esa base. Que no vaya al control de versiones de este repositorio no significa que no tenga que tener respaldo, y eso es de Cimiento como producto.""",
    metricas=[(u"Señales en la base de Cimiento", u"268"),
              (u"De ellas, de otros proyectos", u"186"),
              (u"Señales de este repositorio, versionadas en texto", u"85"),
              (u"Recuerdos versionados, con su índice", u"23")],
    caso_titulo=u"CP-001 — Qué hay en cada sitio, contado",
    caso_cuerpo=u"""Contado sobre la base y sobre el árbol:

| Sitio | Qué guarda | Cuánto | Versionado acá |
|---|---|---|---|
| `historico-chat/memory/` | recuerdos de este repositorio | 23 | Sí |
| `documentacion/senales.md` | señales de este repositorio | 85 | Sí |
| `memoria/senales.db` | señales de Cimiento, de todos los proyectos | 268 | No, y es lo decidido |

**Resultado: pasa.** Lo de este repositorio está versionado; lo que es de todos los proyectos vive donde sirve a todos.""",
    decision_tabla=[
        (u"Las señales se quedan en la base de Cimiento",
         u"Versionar el `.db` en este repositorio",
         u"Es binario, dos sesiones se lo pisan sin fusión posible, y 186 de sus 268 señales son de otros proyectos"),
        (u"El criterio se relee, no se incumple",
         u"Dejar la historia en rojo para siempre",
         u"Fue escrito cuando la memoria era una carpeta de un solo repositorio. Lo que cambió es el alcance, no la exigencia"),
    ],
    deuda=[(u"El respaldo de la base de Cimiento no está decidido",
            u"**Abierta.** Es de Cimiento como producto, no de este cuerpo de reglas")],
)

CUERPOS["HU-005"] = dict(
    que_decia=u"**una cosa estaba guardada en los dos sitios y las dos versiones ya decían cosas distintas**: el recuerdo de terminología decía «Cimiento» desde el 2026-08-14, y la señal `S-002` seguía diciendo «el agente = Claude Code»",
    decision=u"**Manda el recuerdo.** El usuario lo decidió el 2026-08-30 con la frase que zanja el caso: *«el agente (Cimiento) no es Claude Code»*.",
    porque=u"""**Por qué manda el recuerdo y no la señal.** El recuerdo es lo que el agente carga al abrir cada sesión: es lo que rige mientras trabaja. La señal es historia de por qué se decidió algo. Cuando las dos se contradicen, la que manda es la que se está leyendo.

**Y la señal no se borra.** El propio [`documentacion/senales.md`](../../../../../documentacion/senales.md) lo tiene escrito en su cabecera desde el principio: *«una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva»*. Nadie lo había aplicado a esta.

**Lo que hizo daño mientras tanto.** No es hipotético: el 2026-08-13 esa misma frase llevó a responder que el agente maneja machine learning. Quien lo maneja es Claude, que no es el agente. El recuerdo lo cuenta con fecha.""",
    metricas=[(u"Señales activas diciendo lo contrario del recuerdo", u"0"),
              (u"La señal vieja, conservada", u"Sí, como `reemplazada`"),
              (u"La nueva, enlazada a la que reemplaza", u"Sí")],
    caso_titulo=u"CP-001 — Las dos copias ya no se contradicen",
    caso_cuerpo=u"""Antes:

```
S-002  activa   Terminologia: 'el agente' = Claude Code; 'el estandar' = las reglas
```

Después:

```
S-002  reemplazada  Terminologia: 'el agente' = Claude Code; 'el estandar' = las reglas
S-269  activa       reemplaza=S-002  Terminologia: el agente es Cimiento, y no es Claude Code
```

**Resultado: pasa.** La `S-269` dice lo mismo que el recuerdo, y la vieja queda con su rastro.""",
    decision_tabla=[
        (u"Manda el recuerdo", u"Que mande la señal, o decidirlo caso por caso",
         u"El recuerdo es lo que el agente carga al abrir sesión: es lo que rige mientras trabaja"),
        (u"La señal vieja se marca `reemplazada`, no se borra",
         u"Corregirla en su sitio", u"Reescribirla borraría el rastro de que se creyó lo contrario, y de que eso causó un error"),
        (u"La nueva se escribe en la misma base",
         u"Marcar la vieja apuntando al recuerdo", u"Una señal reemplazada por nada deja al lector sin dónde ir"),
    ],
    deuda=[(u"`memoria.py supersede` recibe `--by` y no lo guarda: solo lo imprime",
            u"**Abierta.** Acá se rodeó escribiendo la nueva con `--reemplaza`, que sí queda")],
)


def w(D, nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


for c in CASOS:
    b = CUERPOS[c["hu"]]
    D = os.path.join(EP, c["hu_dir"], c["fase"])
    if not os.path.isdir(D):
        os.makedirs(D)
    d = dict(c, M=M)

    w(D, "estado-fase.md", u"""# Estado de fase — Fase `{fase}` (módulo {M})   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {M} |
| **Planteamiento / Épica / HU** | [EP-006](../../epica.md) · [{hu}](../{hu_md}) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se midió el estado de los dos sitios |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ La decisión del usuario, en esta sesión |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 3 tareas, 3 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el {criterio} |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · medir el estado de los dos sitios | Terminada | Contado, no leído |
| T-02 · aplicar la decisión del usuario | Terminada | — |
| T-03 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Este rojo no se cerraba midiendo: pedía una decisión del usuario | `S-085` |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Estuvo trece días esperando una decisión que no era del que ejecuta.
""".format(**d))

    w(D, "plan_trabajo.md", u"""# Plan de Trabajo — Fase `{fase}` (módulo {M})   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [{hu}](../{hu_md}), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el {criterio}**, que dejó la fase [`{roja}`](../{roja}/resultado_pruebas.md) en «No cumple» el {fecha_rojo}, porque {que_decia}.

{decision}

**Este rojo no se cerraba midiendo.** Es de los que piden una decisión del usuario, y estuvo trece días esperándola.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** aplicar la decisión y dejarla escrita donde se lee.

**Fuera de alcance:** los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
105 cumplen, 4 no cumplen, 5 sin veredicto
```

### 2.1 Lo que hay, contado

{porque}

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `{hu_md}` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
{tabla_decisiones}

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Medir el estado de los dos sitios | Análisis | 0,5 h | — | EV-01 |
| T-02 | Aplicar la decisión del usuario | Memoria | 0,5 h | T-01 | EV-02 |
| T-03 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-02 | EV-02 |

**Total estimado:** 1,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| {criterio} | Contar lo que hay en cada sitio, y comprobar el resultado de aplicar la decisión | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

El propio repositorio y la base de señales. Ninguna prueba usa credenciales.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `01·C4`, decidir no es del que ejecuta. Es lo que tuvo detenida esta historia.
- `20·M11`, lo publicado no se reescribe: se deja atrás.
- `04·R4`, se cuenta en vez de afirmar sobre lo leído.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el agente decidiera esto por su cuenta | Es `01·C4`, y era el motivo del rojo | Se esperó la decisión | Cerrado |
| B-02 | Que aflojar el criterio tape el problema en vez de resolverlo | Un criterio releído sin motivo es un criterio borrado | El motivo queda escrito acá y en el cierre | Cerrado |

---

## 11. Definition of Done

- [x] La decisión, aplicada
- [x] El motivo, escrito
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
""".format(tabla_decisiones="\n".join(
        u"| %s | %s | %s |" % t for t in b["decision_tabla"]),
        que_decia=b["que_decia"], decision=b["decision"], porque=b["porque"], **d))

    w(D, "plan_pruebas.md", u"""# Plan de Pruebas — Fase `{fase}`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el {criterio} después de aplicar la decisión del usuario.

### 1.2 Alcance

**Dentro:** contar lo que hay en cada sitio, y comprobar el resultado de aplicar la decisión.

**Fuera:** los otros criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [{hu}](../{hu_md})
- [Resultado de la fase A](../{roja}/resultado_pruebas.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Lo que hay en cada sitio | El criterio habla de dónde vive cada cosa |
| El resultado de aplicar la decisión | Una decisión escrita y no aplicada no cierra nada |

---

## 3. Estrategia de pruebas

De ejecución: se cuenta sobre el árbol y sobre la base, no se lee el documento de la fase anterior.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario, escrita.

### 4.2 Criterios de salida

- Las cuentas de cada sitio, tomadas.
- La decisión, aplicada y comprobada.

### 4.3 Criterios de suspensión y reanudación

Si al contar apareciera algo que la decisión no cubre, la fase se detiene y se pregunta.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| {criterio} | CP-001 |

---

## 6. Casos de prueba

### {caso_titulo}

| Campo | Valor |
|---|---|
| **HU / CA** | {hu} / {criterio} |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Resultado esperado** | Que lo contado coincida con lo que la decisión dice que debe pasar |

---

## 7. Datos y ambientes de prueba

El repositorio y la base de señales, tal como están.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cuentas tomadas leyendo en vez de contando | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30, con la decisión del usuario.
""".format(caso_titulo=b["caso_titulo"], **d))

    w(D, "resultado_pruebas.md", u"""# Resultado de Pruebas — Fase `{fase}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{fase}` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la decisión del usuario está aplicada y comprobada. Lo que la fase `{roja}` declaró en rojo el {fecha_rojo} era cierto entonces, y siguió siéndolo hasta que hubo decisión: no era trabajo pendiente, era una pregunta sin responder.

| Métrica | Real |
|---|---|
{metricas}

---

## 3. Resultado por caso

### {caso_titulo}

{caso_cuerpo}

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué este rojo no se cerraba midiendo

Es de los que pedían una decisión, no trabajo. Medirlo otra vez habría dado el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él. Está en `S-085`.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- La decisión del usuario, en la transcripción del 2026-08-30
- Las cuentas del §3, tomadas sobre el árbol y la base
""".format(metricas="\n".join(u"| %s | %s |" % t for t in b["metricas"]),
           caso_titulo=b["caso_titulo"], caso_cuerpo=b["caso_cuerpo"], **d))

    w(D, "funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{fase}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [{hu}](../{hu_md}): el {criterio} |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `{roja}` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y aplicada. Aquel rojo era cierto el {fecha_rojo}. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`{roja}`](../{roja}/resultado_pruebas.md) cerró en rojo porque {que_decia}.

{decision}

{porque}

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| {criterio} | decisión aplicada | Este cierre | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · medir los dos sitios | ✅ | §3 del resultado |
| T-02 · aplicar la decisión | ✅ | §3 del resultado |
| T-03 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia código |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
{tabla_decisiones_corta}

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
{deuda}

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""".format(que_decia=b["que_decia"], decision=b["decision"], porque=b["porque"],
           tabla_decisiones_corta="\n".join(
               u"| %s | %s |" % (t[0], t[2]) for t in b["decision_tabla"]),
           deuda="\n".join(u"| %s | %s |" % t for t in b["deuda"]), **d))

    # La historia, al dia.
    R = os.path.join(EP, c["hu_dir"], c["hu_md"])
    with io.open(R, encoding="utf-8") as f:
        t = f.read()
    if c["estado_viejo"] in t:
        t = t.replace(c["estado_viejo"], c["estado_nuevo"], 1)
        print("estado al dia:", c["hu"])
    sep = u"| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
    fila = (u"| [%s](%s/estado-fase.md) | %s | **Ejecutada el 2026-08-30.** "
            u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
            u"— %s |\n" % (c["fase"], c["fase"], c["fila_cubre"], c["fase"],
                           c["fila_estado"]))
    if sep in t:
        t = t.replace(sep, sep + fila, 1)
        print("fila puesta:", c["hu"])
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    print("fase escrita:", c["fase"])
