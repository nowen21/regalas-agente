# Plan de Pruebas — Fase `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba cada criterio de aceptación**, con qué datos y en qué ambiente, y cuándo se da por aprobado. Lo que se pide vive en la [HU-009](../HU-009-las-rutas-largas-no-detienen-el-guardado.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el instalador deja puesto el ajuste de rutas largas sin pisar lo que alguien haya decidido, sin escribir en el modo que solo muestra, y sin tocar nada fuera del repositorio.

### 1.2 Alcance

**Entra:** `instalar_git` en `validadores/instalar.py`, sus pruebas, y el texto de despliegue que dice qué hacer al ver el error.

**No entra:** acortar la convención de carpetas, la configuración global de la máquina, y los proyectos ya clonados que no vuelvan a instalar.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [HU-009](../HU-009-las-rutas-largas-no-detienen-el-guardado.md) | Los tres criterios y sus pasos |
| [plan_trabajo.md](plan_trabajo.md) | Lo medido, y por qué acortar nombres no alcanza |
| `S-042` | El tope, con sus números |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `instalar_git` | Que ponga el ajuste, que no pise un `false`, que no repita, y que no escriba en el modo que muestra |
| El texto de despliegue | Que diga qué hacer, con los dos comandos y cuál es opcional |
| Lo que ya funcionaba | Que las clases de EP-007 sigan pasando sin tocarlas |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

**De sistema**: se corre el instalador de verdad, como subproceso, sobre repositorios de prueba con git. Es como ya se prueba `EP-007`, y es lo que corresponde: lo que se comprueba es su conducta, no una función suelta.

### 3.2 Tipos de prueba

| Tipo | Por qué |
|---|---|
| Funcional | Los cuatro escenarios del ajuste |
| **De que no pase** | Que el modo que muestra no escriba, y que un `false` no se pise |
| De no regresión | Las clases de EP-007, sin tocarlas |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.3 Técnicas de diseño de casos

**Partición** por el estado previo del ajuste: sin poner, en `true`, en `false`. **Caso borde**: una carpeta que no es repositorio de git.

### 3.4 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002, CP-003 | Pisar una decisión ajena, o escribir en el modo que muestra, son daños |
| Alta | CP-001, CP-005 | Que haga lo suyo, y que no rompa lo de antes |
| Media | CP-004, CP-006 | Repetición y borde |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, y **con el conteo a la vista**: `Ran 0 tests` sale con el mismo `OK` que una corrida buena.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- `git` disponible. Sin él, las pruebas de `EP-007` se saltan, como ya hacen.

### 4.2 Criterios de salida

- Los seis casos ejecutados, con su resultado escrito.
- Los tres criterios en verde.
- **La configuración global de quien corre la suite, intacta.**
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si alguna prueba resulta tocar la configuración global: eso le cambia la máquina a quien prueba, y hay que resolverlo antes de seguir.

---

## 5. Matriz de trazabilidad

| CA / RNF | Caso | Tipo |
|---|---|---|
| CA-01 — instalar deja el ajuste | CP-001 | Camino feliz |
| CA-01 — y no repite trabajo | CP-004 | Idempotencia |
| CA-02 — un `false` no se pisa | CP-002 | Que **no** pase |
| CA-03 — quien clone sabe qué hacer | CP-006 | Documentación |
| RNF-01 — no toca nada fuera del repositorio | CP-003 | Que **no** pase |
| Transversal · límites | CP-005 | Bordes y no regresión |

---

## 6. Casos de prueba

### CP-001 — Instalar deja el ajuste puesto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Un repositorio de prueba recién iniciado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `core.longpaths` en el repositorio nuevo | No devuelve nada |
| 2 | Correr el instalador con `--aplicar` | Termina sin error |
| 3 | Leer el ajuste | Devuelve `true` |
| 4 | Buscar el paso en la salida del instalador | Lo nombra, como nombra los demás |

---

### CP-002 — Un «false» puesto a propósito no se pisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Un repositorio con `core.longpaths` en `false` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner el ajuste en `false` | Queda en `false` |
| 2 | Correr el instalador con `--aplicar` | Termina sin error |
| 3 | Leer el ajuste | **Sigue en `false`** |
| 4 | Leer la salida | Dice que lo encontró así y que no lo tocó |

**Por qué es crítico:** pisar una decisión ajena sin decirlo es peor que no hacer nada. Y es la misma cortesía que el instalador ya tiene con `core.hooksPath`.

---

### CP-003 — El modo que muestra no escribe, y nada fuera del repositorio cambia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-01, `RNF-01` |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Repositorio de prueba, y la configuración global anotada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar `git config --global --get core.longpaths` | Queda su valor, o su ausencia |
| 2 | Correr el instalador **sin** `--aplicar` | Nombra el paso entre lo que haría |
| 3 | Leer el ajuste del repositorio | **Sigue sin estar** |
| 4 | Leer la configuración global | **Idéntica** a la del paso 1 |
| 5 | Correr con `--aplicar` y volver a leer la global | **Idéntica** |

**Los pasos 4 y 5 no son adorno.** Un `git config --global` escrito por error le cambiaría la máquina a quien corra la suite, y eso no se ve en ninguna otra prueba.

---

### CP-004 — Correrlo dos veces no repite trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-01 |
| **Tipo** | Idempotencia |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador con `--aplicar` | Dice que pone el ajuste |
| 2 | Correrlo otra vez con `--aplicar` | Dice que **ya estaba puesto** |
| 3 | Leer el ajuste | Sigue en `true` |

---

### CP-005 — Lo de antes no se rompió

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / transversal |
| **Tipo** | No regresión y bordes |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las clases de `EP-007` **sin tocarlas** | Todas en verde |
| 2 | Correr el instalador sobre una carpeta que **no** es repositorio de git | No revienta; se comporta como ya se comportaba |
| 3 | Correr la suite completa | En verde, **y con conteo distinto de cero** |

---

### CP-006 — Quien clone y no instale sabe qué hacer

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-03 |
| **Tipo** | Documentación |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `Filename too long` en el documento de despliegue | Aparece |
| 2 | Leer lo que dice, sin conocer el proyecto | Se entiende qué pasó y qué correr |
| 3 | Buscar el comando del repositorio | Está, copiable |
| 4 | Buscar el comando global | Está, **marcado como opcional y como decisión de quien lee** |
| 5 | Buscar si dice **por qué** el instalador no pudo hacerlo por uno | Lo dice: la configuración de git no viaja al clonar |

**El paso 5 es el que importa.** Sin él, alguien va a creer que el instalador falló.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La máquina de quien trabaja, con git. Sin git, las pruebas se saltan.

### 7.2 Datos de prueba

Repositorios en carpeta temporal, con la base `_ProyectoDePrueba` que ya existe y limpia lo suyo.

### 7.3 Usuarios de prueba

No aplica. **Ninguna prueba usa credenciales** (`00·N6`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

**Ninguna prueba crea rutas de más de 260 caracteres.** No hace falta: lo que se comprueba es que el ajuste quede puesto, y que el ajuste sirve ya está comprobado en la realidad — es lo que dejó pasar el commit de 1005 archivos con 59 rutas sobre el tope. Fabricar el caso extremo en una prueba probaría a git, no al instalador.

---

## 8. Herramientas

| Herramienta | Para qué |
|---|---|
| `unittest`, de la biblioteca estándar | La suite |
| `git`, como subproceso | Leer y poner el ajuste en los repositorios de prueba |
| Un guion de sabotaje | Romper cada pieza a propósito |

**El guion se restaura con copia**, declara y limpia sus rastros, y **se cae si su corrida final reporta cero pruebas**.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué la define |
|---|---|
| Crítica | Se toca la configuración global, o se pisa un `false` puesto a mano |
| Alta | El modo que muestra escribe |
| Media | Se repite trabajo al correrlo dos veces |
| Baja | Redacción del paso o del texto de despliegue |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

### 9.3 Contenido mínimo de un reporte

Qué se esperaba, qué pasó, con qué datos, y en qué archivo y línea.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Casos ejecutados | 6 de 6 |
| Criterios en verde | 3 de 3 |
| **Cambios en la configuración global** | **0** |
| Clases de EP-007 que hubo que tocar | **0** |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

### 12.2 Dónde se miden

En el `resultado_pruebas.md`, con la salida pegada.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que una prueba le cambie la configuración global a quien la corre | `CP-003` la anota antes y la compara después. Es el único que puede verlo |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final: puede ser que el sabotaje no saboteara |
| Que se pruebe a git en vez de al instalador | No se fabrican rutas largas. Que el ajuste sirva ya está comprobado en la realidad |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-26 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
