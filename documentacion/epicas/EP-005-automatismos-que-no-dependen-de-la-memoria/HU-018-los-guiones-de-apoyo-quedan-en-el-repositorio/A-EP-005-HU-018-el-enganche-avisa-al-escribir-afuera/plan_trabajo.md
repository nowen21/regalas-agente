# Plan de Trabajo — Fase `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` (módulo Enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-018](../HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio.md) — **una sola** (`F12.1`) |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📋 **Baja del [pendiente 89](../../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md)**, con las salidas **1 y 3 aprobadas** por el usuario y la **2 dejada fuera** — un validador que compare al cierre detecta lo que el enganche evita.

**CA de la HU que cubre esta fase:** los cinco. Son una sola cosa: un aviso que llega en el momento y que no habla de más.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que escribir fuera del proyecto **avise en el momento y diga dónde debía ir**, sin depender de que el agente se acuerde.

**Fuera de alcance:**

- **Los 38 guiones que estaban afuera.** Se trajeron el 2026-08-27. Eso tapó los casos.
- **Mover o borrar nada.** El enganche avisa (`RN-04`).
- **Lo que se escribe por `Bash`.** No se ve, y se dice.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **La línea base se mide antes de crear nada**, que es lo que la `HU-022` enseñó el mismo día.

### 2.0 La línea base

```
118 en total · 32 sin terminar · 86 terminadas,
de las cuales 65 cumplen, 16 no cumplen y 5 no dicen si cumplen
```

### 2.1 Lo que ya existe, comprobado leyendo y no suponiendo

| Pieza | Estado | Cómo se comprobó |
|---|---|---|
| La prohibición `04·S9` | **Existe** | Leída: *«el agente escribe solo dentro de la carpeta del proyecto»* |
| **Dónde sí van** los guiones | **Falta** | Solo vive en `historico-chat/memory/guiones-de-apoyo-dentro-del-repo.md` |
| El canal `PostToolUse` sobre `Write\|Edit` | **Existe** | `.claude/settings.json`, con cinco enganches ya colgados de ese matcher |
| La ruta llega en `tool_input.file_path` | **Existe** | Leído en `adaptadores/claude-code/hook_md.py`, línea 52 |
| El precedente de traer lo de afuera | **Existe** | `hook_recuerdos.py` |

**Nada de esto se supuso.** El defecto de la jornada fue afirmar sobre lo que no se leyó, tres veces.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/rutas_fuera.py` | Crear | Servicio | La lógica, agnóstica de la herramienta |
| `adaptadores/claude-code/hook_rutas.py` | Crear | Adaptador | Lo que habla con esta herramienta |
| `validadores/instalar.py` | Modificar | Servicio | Que el enganche quede colgado, como los otros |
| `validadores/pruebas.py` | Modificar | Test | Los cinco CA |
| `base/04-seguridad.md` | Modificar | Documentación | La mitad positiva de `S9` |
| `CHANGELOG.md` · `VERSION` | Modificar | Documentación | `20·M10` |

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `instalar.py` | **Un enganche más en la configuración** | Las pruebas del instalador, que cuentan o comparan la configuración generada | **Pueden romper si comparan la lista completa.** Se comprueba antes de tocar nada: es la `T-00` |
| `base/04-seguridad.md` | Una regla nueva en el capítulo | `metareglas.py`, el checklist, y el recuento de reglas | No rompen: se agrega, no se renumera (`M11`) |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

El enganche corre solo, después de cada `Write` o `Edit`. No hay comando que correr.

### 2.5 Permisos / roles a sembrar

**Ninguno.** Y **el enganche no cambia ningún estado fuera del proyecto** (`00·N1`): solo lee la ruta que le pasan.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La ruta se **resuelve** antes de comparar | Comparar el texto tal como llega | `C:/proyecto` y `C:/proyecto-viejo` comparten prefijo: comparando texto, el segundo pasa por dentro |
| Se compara por **partes de la ruta**, no por prefijo de cadena | `startswith` sobre la ruta resuelta | Sigue dando el falso de la carpeta hermana |
| El enganche **avisa y no mueve** | Mover el archivo al repositorio | Mover lo que el agente acaba de escribir rompe lo que estaba haciendo, y esconde el incumplimiento en vez de mostrarlo |
| El aviso **nombra el destino** | Decir solo que está mal | Un aviso que no dice qué hacer se aprende a ignorar. Es el defecto más caro de este repositorio |
| **Ningún fallo del enganche detiene la escritura** | Dejarlo reventar | Un enganche que bloquea el trabajo se desinstala el mismo día |
| La regla **declara su dependencia** con `S9` y no la repite | Escribirla completa | `M7` y `M12`: buscar antes de crear |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. El contrato del enganche se leyó en `hook_md.py` | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | **Antes de tocar nada:** ver si alguna prueba compara la configuración generada por el instalador | Test | 0,5 h | — | EV-00 |
| T-01 | Decir si una ruta resuelta está dentro del proyecto, por partes y no por prefijo | Backend | 1 h | — | EV-01 |
| T-02 | El enganche: leer la ruta, avisar con el destino, y no reventar nunca | Adaptador | 1 h | T-01 | EV-02 |
| T-03 | Que el instalador lo cuelgue, como los otros ocho | Backend | 0,5 h | T-02, T-00 | EV-03 |
| T-04 | La regla en `base/`, declarando su dependencia con `S9` | Documentación | 1 h | — | EV-04 |
| T-05 | Los cinco CA, con el caso de la carpeta hermana | Test | 2 h | T-02 | EV-01 a EV-05 |
| T-06 | Correrlo de verdad: escribir un archivo afuera y ver si avisa | Calidad | 0,5 h | T-03 | EV-06 |
| T-07 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-04 | EV-07 |
| T-08 | Sabotear | Calidad | 1 h | T-05 | EV-08 |

**Total estimado:** 8 h

**Versión: MENOR.** La prohibición ya existe en `04·S9`; lo nuevo es la mitad positiva y el enganche que la hace cumplir. **Ningún proyecto tiene que cambiar nada de lo que ya tiene.** Sube a `35.4.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-06

**La `T-00` va primero y puede cambiar el plan.** Si una prueba compara la configuración completa que genera el instalador, agregar un enganche la rompe **por algo que no es un defecto**. Hay que saberlo antes.

**Y la `T-06` no es opcional.** El defecto que corrige la `HU-004` de la `EP-002` era exactamente este: una funcionalidad construida y probada que **nadie llamaba**. Un enganche que pasa sus pruebas y no está colgado no sirve de nada.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · escribir fuera avisa, y dice dónde iba | Entrada con una ruta temporal | EV-02 | | ☐ |
| CA-02 · escribir dentro **no** avisa | Cuatro rutas de dentro, una relativa y una con `..` | EV-01 | | ☐ |
| CA-03 · la ruta se resuelve antes de comparar | La carpeta hermana con prefijo compartido | EV-01 | | ☐ |
| CA-04 · la regla dice dónde van los guiones | `base/`, y `validar.py metareglas` | EV-04 | | ☐ |
| CA-05 · no revienta con entrada mala | Sin `file_path`, sin JSON, ruta vacía | EV-05 | | ☐ |

---

## 6. Datos y ambiente de prueba

Entradas JSON de mentira, y carpetas temporales creadas y borradas por la prueba. **Ninguna prueba usa credenciales** (`00·N6`), y **ninguna escribe fuera del proyecto** — que sería incumplir lo que esta fase construye.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`. **El enganche colgado se quita volviendo a correr el instalador**, que regenera la configuración.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** no tiene que hacer nada. Al volver a instalar, el enganche queda colgado y empieza a avisar. **No cambia ningún archivo suyo.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base y el contrato del enganche, **leídos** antes de planear.
- `04·S9` — la regla de la que esta cuelga.
- `00·N1` — el enganche no cambia estado fuera del proyecto: solo lee la ruta.
- `20·M7`, `M12` — se busca antes de crear, y la regla nueva declara su dependencia.
- `20·M10` — versión y registro de cambios.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que avise de más y se aprenda a ignorar | El enganche se apaga y no queda nada | `CA-02`, con cuatro rutas de dentro | Abierto |
| B-02 | Que una carpeta hermana pase por dentro | Deja de avisar donde debe | `CA-03` paso 3, comparando por partes | Abierto |
| B-03 | Que se construya y **no quede colgado** | Es el defecto de `EP-002·HU-004`, repetido | La `T-06`: se escribe un archivo afuera y se mira | Abierto |
| B-04 | Que las pruebas del instalador comparen la configuración completa | Rompen por algo que no es defecto | La `T-00`, antes de tocar nada | Abierto |
| B-05 | Que un fallo del enganche detenga el trabajo | Se desinstala el mismo día | `CA-05` y `RNF-02` | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados
- [ ] **El enganche colgado y probado escribiendo un archivo de verdad**
- [ ] La regla en `base/`, pasando su checklist
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] `VERSION` en `35.4.0` y su entrada en el `CHANGELOG`
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
