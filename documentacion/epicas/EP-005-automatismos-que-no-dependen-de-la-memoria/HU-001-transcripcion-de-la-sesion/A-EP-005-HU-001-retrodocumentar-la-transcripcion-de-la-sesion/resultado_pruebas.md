# Resultado de pruebas — Fase A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion` |
| **HU** | [HU-001](../HU-001-transcripcion-de-la-sesion.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-001 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales, y esta misma sesión como caso vivo. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Los tres criterios numerados quedaron verificados —el archivo nace solo, la hora sale del reloj y la sesión entra al índice—. Lo que falla es el **transversal de privacidad**: la HU pide que lo enmascarado no quede en claro, y **nada enmascara**.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un proyecto temporal, y esta sesión | Aprobado | EV-01, EV-02 |
| [CP-002](plan_pruebas.md) | CA-02 | Crítica | Un mensaje que **contiene** una hora falsa | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-01 | Alta | El enganche disparado dos veces | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-03 | Alta | El índice, y una sesión renombrada | Aprobado | EV-02 |

---

### Detalle de CP-002 — La hora viene del reloj, no del texto

**El caso está armado para que un programa perezoso falle.** Se manda un mensaje cuyo texto dice «eran las 03:33 de la madrugada» y se comprueba que la hora anotada **no es esa**: es la del reloj de la máquina.

Si el programa copiara lo que dice el texto, bastaría con escribir una hora en un mensaje para falsear el histórico entero — y nadie lo notaría, porque el archivo se vería perfectamente coherente.

---

### Detalle de CP-001, CP-003 y CP-004 — Nace solo, no duplica, y entra al índice

| Qué se probó | Qué salió |
|---|---|
| El archivo nace con el primer mensaje, aunque sea un «hola» | Nace |
| Un proyecto **sin** la carpeta del histórico | **No se ve afectado**: no crea nada |
| El enganche disparado dos veces por el mismo mensaje | **No duplica** |
| La sesión entra al índice al nacer | Entra |
| Renombrar la sesión corrige archivo **e** índice | Los dos |

**Y el caso vivo:** esta misma sesión se está transcribiendo mientras se ejecutan las 51 fases, en `historico-chat/2026-08-17-sesion-3.md`, escrita por el programa, no por el agente.

---

## 3. Lo que no cumple: nada enmascara

El transversal de privacidad de la HU dice: «lo que se enmascara no queda escrito en claro en la transcripción».

**No hay nada que enmascare.** Se comprobó mandando un texto con forma de clave: queda escrito **tal cual** en la transcripción, que además se versiona. La prueba está escrita al revés —afirma que el texto se guarda literal— para que **falle el día que se construya el enmascarado** y obligue a volver a este documento.

Es [EP-005 · HU-002](../../HU-002-enmascarar-claves/HU-002-enmascarar-claves.md), sin construir. Ya estaba dicho en la fase `A-EP-001-HU-003`: la mitad automática del `N6` no existe.

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **Nada enmascara.** Una clave pegada en el chat queda escrita en claro en la transcripción, y la transcripción se versiona | Probado. Es [HU-002](../../HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) de esta épica, sin construir y **bloqueada por dos dudas de su §2.7** |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los tres transversales**. Se probaron igual, y por eso apareció `D-01` | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-001-transcripcion-de-la-sesion.md#ca-01--la-sesión-se-escribe-sola-desde-el-primer-intercambio) | CP-001, CP-003 | Nace con el primer mensaje y no duplica | Sí |
| [CA-02](../HU-001-transcripcion-de-la-sesion.md#ca-02--cada-intercambio-lleva-su-hora-real) | CP-002 | La hora sale del reloj, no del texto | Sí |
| [CA-03](../HU-001-transcripcion-de-la-sesion.md#ca-03--la-sesión-aparece-en-el-índice) | CP-004 | Entra al índice y sobrevive al renombrado | Sí |
| Transversal · Privacidad | §3 | **Nada enmascara** | **No** |
| Transversal · Límites | CP-001 | Un proyecto sin la carpeta no se ve afectado | Sí |
| Transversal · Errores | Prueba propia | El enganche no revienta cuando no puede escribir; termina en 0 | Sí |

**El que no cumple:** el transversal de **privacidad**, y su destino ya existe: HU-002 de esta misma épica.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** los tres criterios numerados quedaron verificados, incluido el que más fácil se falsearía —la hora—, probado con un mensaje que contiene una hora falsa a propósito. Pero el transversal de privacidad no se cumple: **nada enmascara**, y una clave pegada en el chat queda escrita en claro en un archivo que se versiona.

**Qué falta para que cumpla:** construir [HU-002](../../HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) de esta épica, que hoy está **bloqueada por dos dudas de su §2.7** — con qué marca se tapa, y qué se hace con las transcripciones viejas. **Las dos son del usuario.**

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `TranscripcionDeLaSesion` (3 nuevas) e `Historico` (5, ya existentes) |
| EV-02 | Caso vivo | Esta misma sesión, en `historico-chat/2026-08-17-sesion-3.md` |
| EV-03 | Lo escrito | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md) §4.2 |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
