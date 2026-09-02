# Plan de Trabajo — Fase `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` (módulo Enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-020](../HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta.md) — **una sola** (`F12.1`) |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Sale de un daño medido.** Un commit se llevó **712 líneas ajenas** y la comprobación que existe para eso dijo OK (`S-071`). **Y la medición descartó el arreglo obvio**: avisar de los archivos sin registro habría hablado en **7 de 12 commits** (`S-072`).

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el registro de la sesión anote **lo que cambió en el turno**, mire quien lo mire, para que la comprobación que ya existe tenga con qué comparar.

**Fuera de alcance:**

- **Tocar `validar_preparados`.** Empieza a funcionar sola cuando el registro se completa.
- **Identificar quién escribió cada archivo.** No se puede, y no hace falta.
- **Los archivos que ninguna sesión toca.** Siguen sin registro, y es correcto.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase.**

### 2.0 La línea base

```
121 en total · 32 sin terminar · 89 terminadas,
de las cuales 71 cumplen, 13 no cumplen y 5 no dicen si cumplen
```

### 2.1 Por qué no se afina la comprobación

| Commit | Archivos | Sin registro | ¿Habría avisado? |
|---|---|---|---|
| `6abffdc` | 55 | **31** | Sí |
| `b3df9f1` | 34 | **13** | Sí |
| `ef22e79` | 34 | **11** | Sí |
| `011754b` | 27 | **8** | Sí |

**Siete de doce commits, con hasta 31 archivos.** Un aviso así se apaga en una tarde, y con él lo que sí importaba.

**La causa:** el registro se llena desde las herramientas de escritura, y **la mayoría de los archivos los escriben guiones que se corren en la terminal**. *«Sin registro»* significa *«escrito como se escribe casi todo»*.

### 2.2 Lo que ya existe, leído y no supuesto

| Pieza | Estado | Cómo se comprobó |
|---|---|---|
| `sesiones.anotar(raiz, sesion, archivo)` | **Existe** | Anota sin duplicar y refresca la fecha |
| El registro en `historico-chat/.tocado/`, fuera del control de versiones | **Existe** | Y caduca a las 12 horas |
| `validar_preparados`, que cruza lo preparado con los registros | **Existe** | Calla si menos de dos sesiones coinciden |
| Enganches de fin de turno con `session_id` y `cwd` | **Existen** | Dos ya corren ahí: histórico y presupuesto |
| Qué archivos cambian en un turno | **Medido** | 2 en diez minutos; 20 sucios en el árbol ahora |

### 2.3 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/sesiones.py` | Modificar | Servicio | Qué cambió en la ventana, y anotarlo |
| `adaptadores/claude-code/hook_turno.py` | Crear | Adaptador | Lo que habla con esta herramienta |
| `validadores/instalar.py` | Modificar | Servicio | El enganche nuevo |
| `validadores/pruebas.py` | Modificar | Test | Los cinco CA |
| `CHANGELOG.md` · `VERSION` | Modificar | Documentación | `20·M10` |

### 2.4 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `sesiones.py` | **Ninguno.** Se agregan funciones; `anotar`, `registros` y `validar_preparados` quedan igual | Las pruebas de sesiones, y el `pre-commit` | No rompen. **Sí cambia lo que el registro contiene**, y con eso pueden aparecer colisiones donde antes no había |

**Riesgo real declarado:** si el registro pasa a contener mucho más, **`validar_preparados` puede empezar a avisar seguido**. Se mide antes de dar por buena la fase — es la `T-06`.

### 2.5 Punto de entrada

El enganche corre solo al terminar cada turno. Ninguno nuevo a mano.

### 2.6 Permisos / roles a sembrar

**Ninguno.** Y **no se toca la configuración global de git** (`00·N1`).

### 2.7 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se anota **lo modificado dentro del turno** | Todo lo que esté sucio | Lo sucio de antes es de otro. La primera sesión del día reclamaría el árbol entero |
| La ventana se mide desde **la última corrida del propio registro** | Desde el arranque de la sesión | El registro ya guarda su fecha de escritura: no hace falta estado nuevo |
| Se pregunta a **git** qué cambió | Recorrer el árbol comparando fechas | Git ya lo sabe, y recorrer el árbol en cada turno cuesta |
| **Anotar de más se acepta a propósito** | Afinar hasta no equivocarse | Dos sesiones que tocan el mismo archivo **es** lo que hay que ver, aunque una solo lo haya rozado |
| **No se toca `validar_preparados`** | Arreglar la comprobación | El defecto está en el registro. Afinar el instrumento que mide otra cosa es lo que este repositorio hizo cuatro veces con el número de avance |
| **Cualquier fallo termina en silencio y código 0** | Dejarlo reventar | Un enganche que rompe la conversación se desinstala el mismo día |

### 2.8 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| 1 | **¿Qué pasa con los archivos que git no ve —los ignorados— y con los borrados?** | **Se resuelve en la `T-01`, midiendo.** Un borrado tocado por dos sesiones también es una colisión, y hay que ver si `git status` lo entrega |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | **Antes de tocar nada:** ver si alguna prueba fija el contenido del registro | Test | 0,5 h | — | EV-00 |
| T-01 | **Resolver la duda 1**: qué entrega git para ignorados y borrados | Calidad | 0,5 h | — | EV-01 |
| T-02 | Saber qué cambió dentro de la ventana del turno | Backend | 1,5 h | T-01 | EV-02 |
| T-03 | Anotarlo en el registro, sin duplicar | Backend | 0,5 h | T-02 | EV-02 |
| T-04 | El enganche de fin de turno, que nunca rompe nada | Adaptador | 1 h | T-03 | EV-03 |
| T-05 | Que el instalador lo cuelgue | Backend | 0,5 h | T-04, T-00 | EV-04 |
| T-06 | **Medir cuánto hablaría `validar_preparados` con el registro nuevo** | Calidad | 1 h | T-03 | EV-05 |
| T-07 | Los cinco CA, con el caso del archivo viejo | Test | 2,5 h | T-03 | EV-01 a EV-05 |
| T-08 | **Correrlo de verdad**: escribir con un guion y ver si queda anotado | Calidad | 0,5 h | T-05 | EV-06 |
| T-09 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-06 | EV-07 |
| T-10 | Sabotear | Calidad | 1 h | T-07 | EV-08 |

**Total estimado:** 10 h

**Versión: MENOR.** Aditivo: un enganche más y un registro más completo. **Nadie tiene que cambiar nada de lo que ya tiene.** Sube a `35.8.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-06 → T-05 → T-08

**La `T-06` es la que puede tumbar la fase, y va antes de darla por buena.** Si con el registro completo la comprobación pasa a avisar en la mayoría de los commits, **el arreglo cambió un silencio inútil por un ruido inútil** — y eso es peor, porque el ruido apaga también lo que servía.

**Y la `T-08` no es opcional:** es la lección de `EP-002·HU-004`, construido y no colgado.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · lo escrito con un guion queda registrado | Escribir sin las herramientas y correr el enganche | EV-02, EV-06 | | ☐ |
| CA-02 · no se reclama lo de antes del turno | Un archivo con fecha anterior | EV-02 | | ☐ |
| CA-03 · dos sesiones producen colisión | Dos registros con el mismo archivo | EV-05 | | ☐ |
| CA-04 · lo que ya se registraba sigue igual | Escribir con la herramienta y con el enganche | EV-02 | | ☐ |
| CA-05 · un fallo no rompe el turno | Romperlo, y correrlo sin git | EV-03 | | ☐ |

---

## 6. Datos y ambiente de prueba

**Repositorios de git de verdad**, creados y borrados por la prueba, con fechas controladas para poder distinguir «dentro del turno» de «antes». **Ninguna prueba usa credenciales** (`00·N6`), y **no se escribe en el registro real**.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`. **El enganche se quita volviendo a correr el instalador**, y el registro caduca solo a las doce horas.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** no ve cambiar nada hasta su próximo turno. **Ningún archivo suyo se toca**; lo que cambia es qué se anota en un registro que no se versiona.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base y el reparto de los doce commits, medidos antes de planear.
- `00·N1` — no se toca la configuración global de git.
- `20·M10` — versión y registro de cambios.
- `13·DOC5` — lo decidido se registra como señal: `S-071`, `S-072`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la comprobación pase a avisar siempre | **Cambiar un silencio inútil por un ruido inútil** | La `T-06`, antes de dar la fase por buena | Abierto |
| B-02 | Que reclame archivos viejos | La primera sesión del día se llevaría el árbol | `CA-02` | Abierto |
| B-03 | Que un fallo rompa el turno | Se desinstala el mismo día | `CA-05` | Abierto |
| B-04 | Que se construya y no quede colgado | Es `EP-002·HU-004` otra vez | La `T-08` | Abierto |
| B-05 | Que abrir esta fase mueva la medición | `S-053` | La línea base está en el §2.0 | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados
- [ ] **La duda 1 resuelta midiendo**, y su respuesta escrita
- [ ] **La `T-06` con su número**: cuántos commits avisarían con el registro nuevo
- [ ] El enganche colgado y probado escribiendo con un guion
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] `VERSION` en `35.8.0` y su entrada en el `CHANGELOG`
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
