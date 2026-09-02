# Plan de Trabajo — Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` (módulo Enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-019](../HU-019-el-hash-del-commit-se-anota-solo.md) — **una sola** (`F12.1`) |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📋 **Baja del [pendiente 87](../../../../../pendientes/hecho/el-hash-del-commit-se-anota-solo.md)**, con las salidas **1 y 3 aprobadas** y la **2** —que la estación 12 deje de ser casilla— dejada fuera: cambia el ciclo.

**CA de la HU que cubre esta fase:** los cinco.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la casilla del commit **se marque sola**, solo donde hay dónde, y que el conteo diga **sobre cuántas fases alcanza**.

**Fuera de alcance:**

- **Rellenar las 106 fases sin la fila.** Se cuentan y se nombran.
- **Marcar las 22 pendientes de hoy.** Se decide aparte, con el número a la vista.
- **Que la estación 12 deje de ser casilla.** Salida 2, fuera por decisión del usuario.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase.**

### 2.0 La línea base

```
120 en total · 32 sin terminar · 88 terminadas,
de las cuales 69 cumplen, 14 no cumplen y 5 no dicen si cumplen
```

### 2.1 El reparto de las estaciones, contado

| Qué | Cuántas |
|---|---|
| `estado-fase.md` en el árbol | **140** |
| Estación 12 **marcada** | 11 |
| Estación 12 **sin marcar** | 23 |
| **Sin la fila de la estación 12** | **106** |

**De las 23 sin marcar:** **22 tienen su cierre en git** —comprobado contra el historial— y **una no**. Son dos trabajos distintos que hoy se cuentan juntos.

### 2.2 Lo que ya existe, leído y no supuesto

| Pieza | Estado | Cómo se comprobó |
|---|---|---|
| `.githooks/` con `commit-msg`, `pre-commit`, `pre-push` | **Existe** | `HOOKS` en `validadores/instalar.py` |
| El instalador los escribe y apunta `core.hooksPath` | **Existe** | `instalar_git`, que además **no pisa** un `hooksPath` ajeno |
| Un enganche que corra **después** del commit | **Falta** | No está en `HOOKS` |
| La tabla de estaciones del molde | **Existe** | `plantillas/ciclo-vida-proyectos/10-estado-fase.md` |

### 2.2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/estacion_commit.py` | Crear | Servicio | La lógica, agnóstica de la herramienta |
| `validadores/instalar.py` | Modificar | Servicio | El enganche nuevo en `HOOKS` |
| `validadores/fases.py` | Modificar | Servicio | El conteo con sus tres grupos |
| `validadores/pruebas.py` | Modificar | Test | Los cinco CA |
| `CHANGELOG.md` · `VERSION` | Modificar | Documentación | `20·M10` |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

El enganche corre solo al commitear. El conteo, en `python validadores/validar.py fases`.

### 2.5 Permisos / roles a sembrar

**Ninguno.** Y **no se toca la configuración global de git** (`00·N1`): el instalador ya usa `core.hooksPath` local y no pisa uno ajeno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se escribe **solo donde hay fila** | Insertar la tabla donde falte | Son **106 de 140**. Un programa que invente estructura en documentos viejos hace más daño que el problema |
| **No se pisa un hash ya puesto** | Escribir siempre el último | El hash dice **qué commit cerró la fase**; reescribirlo la haría apuntar a una corrección de una coma |
| **No se marca si el cierre no está en git** | Marcar por estar en la estación 12 | Diría que se commiteó algo que no se commiteó |
| El enganche corre **después** del commit | Antes, y adivinar el hash | Antes del commit el hash **no existe**. Y un enganche previo que falle **bloquea el commit** |
| **Cualquier fallo del enganche termina en silencio y código 0** | Dejarlo reventar | Un automatismo que rompe un commit se desinstala el mismo día |
| El conteo dice **tres grupos**, no uno | «Fases sin commitear» | 22 son marcas y 1 es trabajo. Juntarlos da 23 donde hay uno |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| 1 | ¿El enganche escribe en el mismo commit o deja el archivo sucio después? | **Resuelta el 2026-08-27, midiendo.** El enganche corre **después** de que el commit se cerró: el hash queda en el árbol de trabajo y **no dentro de ese commit**. Ver §2.8 |

### 2.8 La duda 1, resuelta — y por qué la salida elegida es la única

**Medido en un repositorio de mentira**, antes de escribir código:

| Qué | Resultado |
|---|---|
| El commit se hace | Sí |
| El archivo se modifica, con el hash correcto | Sí |
| **Queda sin guardar después del commit** | **Sí** |
| Lo que quedó **dentro** del commit | Sigue diciendo `PENDIENTE` |

**Es una consecuencia del orden, no un defecto que se pueda pulir:** antes del commit el hash no existe.

| Salida | Por qué se descarta o se elige |
|---|---|
| Reescribir el commit con `--amend` | **Se muerde la cola:** cambia el hash, y el documento apuntaría a un commit que ya no existe |
| Un segundo commit automático | **Cruza [`00·N1`](../../../../../base/00-nucleo-blindado.md):** un cambio de estado sin aprobación, y eso es núcleo blindado |
| **Dejar el archivo modificado** | **Elegida.** La única donde nada se reescribe y nada se guarda sin que el usuario lo apruebe |

**El costo se declara:** después de cada commit el árbol queda sucio — un archivo, una línea — que entra en el commit siguiente. **Puede confundirse con trabajo sin guardar**, y por eso el conteo del `CA-04` tiene que decir por nombre cuáles son.

Está en `S-067`.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | **Antes de tocar nada:** ver si alguna prueba compara la lista de enganches de git | Test | 0,5 h | — | EV-00 |
| T-01 | **Resolver la duda 1**: probar en un repositorio de mentira qué pasa al escribir desde el enganche | Calidad | 1 h | — | EV-01 |
| T-02 | Encontrar la fase que un commit cierra, por los archivos que toca | Backend | 1 h | T-01 | EV-02 |
| T-03 | Escribir el hash solo si hay fila, está vacía, y el cierre está en git | Backend | 1,5 h | T-02 | EV-02 |
| T-04 | El enganche, que nunca deshace ni bloquea un commit | Adaptador | 1 h | T-03 | EV-03 |
| T-05 | Que el instalador lo escriba, como los otros tres | Backend | 0,5 h | T-04, T-00 | EV-04 |
| T-06 | El conteo con sus tres grupos y sus nombres | Backend | 1 h | — | EV-05 |
| T-07 | Los cinco CA, con el caso de las 106 sin fila | Test | 2,5 h | T-03, T-06 | EV-01 a EV-05 |
| T-08 | **Correrlo de verdad:** commitear en un repositorio de prueba y mirar el archivo | Calidad | 0,5 h | T-05 | EV-06 |
| T-09 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-06 | EV-07 |
| T-10 | Sabotear | Calidad | 1 h | T-07 | EV-08 |

**Total estimado:** 10 h

**Versión: MENOR.** Aditivo: un enganche más y un conteo más. **Nadie tiene que cambiar nada de lo que ya tiene**, y las fases sin la fila siguen igual. Sube a `35.6.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-04 → T-05 → T-08

**La `T-01` va antes de escribir código y puede cambiar el diseño.** Escribir un archivo del repositorio **desde dentro de un enganche de git** tiene un efecto que hay que ver, no suponer: el archivo puede quedar modificado y sin guardar justo después del commit. **Se prueba en un repositorio de mentira y se elige con el resultado delante.**

**Y la `T-08` no es opcional.** Es la lección de `EP-002·HU-004`: una funcionalidad construida y probada **que nadie llamaba**.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · el hash se escribe solo | Commitear de verdad en un repositorio de prueba | EV-02, EV-06 | | ☐ |
| CA-02 · no se pisa un hash puesto | Commitear dos veces | EV-02 | | ☐ |
| CA-03 · una fase sin la fila no se toca | Comparar byte por byte | EV-02 | | ☐ |
| CA-04 · el conteo separa los tres grupos | La corrida contra el árbol real | EV-05 | | ☐ |
| CA-05 · un fallo no rompe el commit | Romper el enganche y commitear | EV-03 | | ☐ |

---

## 6. Datos y ambiente de prueba

**Repositorios de git de verdad**, creados y borrados por la prueba: un enganche de git no se puede comprobar sin commits reales. **Ninguna prueba usa credenciales** (`00·N6`), y **no se commitea nada en el repositorio del estándar**.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`. **El enganche se quita volviendo a correr el instalador.**

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** no ve cambiar nada hasta su próximo commit de una fase. **Sus documentos viejos no se tocan**, y el conteo le dirá cuántos de los suyos no tienen dónde marcar.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base y el reparto de las 140, medidos antes de planear.
- `00·N1` — no se toca la configuración global de git.
- `04·R4` — no se afirma sobre una fase que no tiene el campo.
- `20·M10` — versión y registro de cambios.
- `13·DOC5` — lo decidido se registra como señal: `S-066`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que escriba donde no hay estructura | Daña 106 documentos viejos | `CA-03`, con comparación byte por byte | Abierto |
| B-02 | Que pise un hash ya puesto | La fase apuntaría al commit equivocado | `CA-02` | Abierto |
| B-03 | Que un fallo del enganche rompa un commit | Se desinstala el mismo día | `CA-05`: se rompe a propósito y se commitea | Abierto |
| B-04 | Que escribir desde el enganche deje el archivo sucio | Descubrirlo al final costaría el doble | La `T-01`, antes de escribir código | Abierto |
| B-05 | Que se lea como resuelto para las 140 | El conteo del `CA-04` dice sobre cuántas actúa | Abierto |
| B-06 | Que abrir esta fase mueva la medición | `S-053` | La línea base está en el §2.0 | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados
- [ ] **La duda 1 resuelta midiendo**, y su respuesta escrita
- [ ] **El enganche probado commiteando de verdad**
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] `VERSION` en `35.6.0` y su entrada en el `CHANGELOG`
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
