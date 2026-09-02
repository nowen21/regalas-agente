# Plan de Trabajo — Fase `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` (módulo Instalador)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` |
| **Épica** | [EP-007](../../epica.md) |
| **HU** | [HU-009](../HU-009-las-rutas-largas-no-detienen-el-guardado.md) — **una sola** (`F12.1`) |
| **Módulo** | Instalador |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Fecha apertura** | 2026-08-26 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- ✨ **Funcionalidad nueva:** el instalador deja puesto un ajuste que hoy hay que poner a mano, en medio de un commit que ya falló.

**CA de la HU que cubre esta fase:**

| CA de `HU-009` | Estado |
|---|---|
| CA-01 — instalar deja el ajuste puesto | ☐ |
| CA-02 — un `false` puesto a propósito no se pisa | ☐ |
| CA-03 — quien clone y no instale sabe qué hacer | ☐ |

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que guardar no se detenga por una ruta larga, sin que nadie tenga que acordarse — y que quien quede fuera del alcance del instalador sepa qué hacer.

**Fuera de alcance:**

- **Acortar la convención de carpetas.** Medido: ahorra 14 caracteres donde hacen falta 55.
- **Tocar la configuración global de la máquina.** Es fuera del proyecto, y `00·N1` pide aprobación para eso. Se dice cómo, y decide el usuario.
- **Los proyectos ya clonados que no vuelvan a instalar.** No hay forma de alcanzarlos.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Medido y corrido el 2026-08-26, no leído.

| Qué | Valor verificado | Cómo se obtuvo |
|---|---|---|
| Ruta más larga de este repositorio, **sin anidar** | **252** caracteres | Recorriendo `documentacion/` |
| Holgura del peor caso | **8** caracteres | 260 menos 252 |
| Lo que necesita el prefijo al anidar | **55** | `plataforma/datos/proyectos/<id>/traido/` |
| Archivos que hoy pasan de 260 | **0** | Nada está roto todavía |
| Lo que ahorra acortar la convención de fases | **14** | `EP-NNN-HU-NNN-` repetido en 130 carpetas |
| Que `core.longpaths` resuelva | **Sí** | Es lo que dejó pasar el commit de 1005 archivos con 59 rutas sobre el tope |
| Que la configuración **viaje al clonar** | **No** | Clonando un repositorio de prueba con el ajuste puesto: en el clon no está |
| Dónde pone hoy el instalador configuración de git | `instalar_git`, para `core.hooksPath` | `validadores/instalar.py` |
| Base de pruebas de instalador que ya existe | `_ProyectoDePrueba`, con git y limpieza | `validadores/pruebas.py` |

**Las tres combinaciones que se probaron**, y por qué ninguna sirve sin `core.longpaths`:

| Prefijo | Convención | Resultado |
|---|---|---|
| 55, como está | sin tocar | faltan 47 |
| 55 | acortada | faltan 33 |
| 20, al mínimo | acortada | **cabe, con 2 de margen** |

**Dos de margen no es margen.** Es la próxima historia con nombre descriptivo.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Servicio | El bloque de `core.longpaths` en `instalar_git`, junto al de `core.hooksPath` |
| `validadores/pruebas.py` | Modificar | Test | Casos de `CA-01` y `CA-02`, sobre `_ProyectoDePrueba` |
| `cvds/despliegue/README.md` | Modificar | Documentación | Qué hacer al ver `Filename too long`, en su §3 |
| `CHANGELOG.md` | Modificar | Documentación | Entrada de la versión (`20·M10`) |
| `VERSION` | Modificar | Documentación | Sube (`20·M10`) |

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `validadores/instalar.py` | `instalar_git` conserva su firma y devuelve un paso más en su lista | `validadores/pruebas.py` | Las clases de EP-007 leen esa salida. **Tienen que seguir pasando**, y eso comprueba la no regresión |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/instalar.py <ruta> --aplicar`, el de siempre. El paso nuevo sale entre los demás.

### 2.5 Permisos / roles a sembrar

**Ninguno.** Y **no se pide ninguno**: `git config` sin `--global` escribe en `.git/config` del propio repositorio, sin tocar nada de la máquina (`RNF-01`).

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se pone en cualquier sistema, no solo en Windows | Detectar Windows al instalar | Fuera de Windows el ajuste es inerte. Y detectarlo sería peor: la copia puede terminar en otra máquina |
| Un `false` puesto a mano **no se pisa** | Forzarlo a `true` siempre | Es la misma cortesía que el instalador ya tiene con `core.hooksPath`, y quien lo puso así tendrá su motivo |
| **No** se toca la configuración global | Ponerla global, que sí alcanzaría todos los clones | Es fuera del proyecto. `00·N1` pide aprobación, y el instalador no puede darla por sí mismo. Se dice el comando y decide quien lee |
| El texto va en el documento de despliegue | Solo en el `CHANGELOG` | El registro se lee al actualizar; quien clona de cero no pasa por ahí |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién | Estado |
|---|---|---|---|
| — | Ninguna | — | — |

Las dos que había —si el ajuste basta, y si viaja al clonar— **se resolvieron corriéndolas**, no preguntando. Están en §2.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 y CA-02 — El instalador

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer el valor actual del ajuste, sin escribir | Backend | 0.5 h | — | EV-01 |
| T-02 | Ponerlo si no está, y decirlo entre los pasos | Backend | 1 h | T-01 | EV-01 |
| T-03 | Si está en `false`, decirlo y no pisarlo | Backend | 0.5 h | T-01 | EV-02 |
| T-04 | Que el modo que muestra **no escriba** | Backend | 0.5 h | T-02 | EV-01 |
| T-05 | Casos de los cuatro escenarios | Test | 2 h | T-02, T-03 | EV-01, EV-02 |
| T-06 | Comprobar que las clases de EP-007 siguen pasando | Test | 0.5 h | T-02 | EV-03 |

### CA-03 — Quien clone y no instale

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Escribir en el documento de despliegue qué hacer al ver el error | Documentación | 1 h | — | EV-04 |
| T-08 | Decir **los dos** comandos, y cuál es opcional y por qué | Documentación | 0.5 h | T-07 | EV-04 |
| T-09 | Que se entienda sin conocer el proyecto | Documentación | 0.5 h | T-08 | EV-04 |

### Versionar y calidad

| ID | Tarea | Capa | Est. | Ev. |
|---|---|---|:--:|---|
| T-10 | `VERSION` y la entrada del `CHANGELOG` | Documentación | 1 h | EV-05 |
| T-11 | Sabotear cada pieza | Calidad | 1.5 h | EV-06 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-10

**T-07 a T-09 no dependen del código** y avanzan en paralelo.

**T-04 no es un detalle.** El instalador tiene un modo que muestra y no toca nada, y esa promesa ya tiene su propia historia construida (`HU-002`). Un paso nuevo que escriba en el modo que muestra la rompería.

> Solo se tocan los archivos declarados (`02·F8`). Descubrir uno nuevo: PAUSAR, reportar, ampliar el plan con aprobación.

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Cuatro escenarios sobre repositorios de prueba | EV-01 | | ☐ |
| CA-02 | El escenario del `false` | EV-02 | | ☐ |
| CA-03 | Lectura del documento, y de los dos comandos | EV-04 | | ☐ |
| RNF-01 | Que no se toque nada fuera del repositorio | EV-01 | | ☐ |
| Transversal · no regresión | Las clases de EP-007, sin tocarlas | EV-03 | | ☐ |

**Registro de evidencias:** EV-01 a EV-06, en el `resultado_pruebas.md`.

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La máquina de quien trabaja, con git |
| Usuarios de prueba | No aplica. **Ninguna prueba usa credenciales** (`00·N6`) |
| Datos precargados | Repositorios de prueba en carpeta temporal, con `_ProyectoDePrueba` |

**Ninguna prueba toca la configuración global**, que es lo que rompería la máquina de quien corra la suite.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. **El ajuste ya puesto en un repositorio no se deshace solo**, y no hace falta: es inerte donde no aplica, y quitarlo es `git config --unset core.longpaths`.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** obtiene el ajuste la próxima vez que corra el instalador. **Quien no lo corra, no.** Es la limitación declarada, y por eso existe `CA-03`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `00·N1` — no se toca configuración fuera del proyecto sin aprobación. Por eso el global se dice, no se hace.
- `02·F8` — solo los archivos declarados.
- `02·F17` — todo lo que este plan afirma se midió o se corrió; los valores están en §2.
- `08·T4` — las pruebas no tocan la configuración de la máquina.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M10` — versionar.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el paso nuevo escriba en el modo que muestra | Rompería la promesa de `HU-002`, ya construida | T-04, y un caso propio | Abierto |
| B-02 | Que se lea como que el problema quedó resuelto para todos | La limitación se olvidaría | `CA-03`, y el cierre lo dirá con todas las letras | Abierto |
| B-03 | Que una prueba toque la configuración global de quien corre la suite | Le cambiaría la máquina a quien prueba | Todo pasa por `_ProyectoDePrueba`, que trabaja en carpeta temporal. Se comprueba que ninguna prueba use `--global` | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia
- [ ] Pruebas de la fase en verde, y **la suite completa al final, con conteo distinto de cero** (`02·F5`)
- [ ] Trazabilidad sin faltantes (`13·DOC11`)
- [ ] `VERSION` y `CHANGELOG` al día (`20·M10`)
- [ ] Señales registradas (`13·DOC5`)
- [ ] Rama lista para el commit único (`09·G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
