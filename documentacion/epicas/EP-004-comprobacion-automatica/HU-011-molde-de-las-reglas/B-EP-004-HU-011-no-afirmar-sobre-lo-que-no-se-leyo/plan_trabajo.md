# Plan de Trabajo — Fase B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo` |
| **Épica** | `EP-004` |
| **HU** | `HU-011` |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:** 📝 **Modifica fase.** Cierra en rojo lo que la fase A de esta misma historia dejó al ejecutarse el 2026-08-22, anotado entonces en el [pendiente 81](../../../../../pendientes/hecho/metareglas-sobre-un-proyecto-da-veredictos-falsos.md).

---

## 1. Objetivo y alcance

**El problema.** Apuntar la comprobación de meta-reglas a un proyecto corría las del estándar contra una carpeta que no tiene cuerpo de reglas. Buscaba allí cuatro archivos que un proyecto no tiene, no los encontraba y **reportaba igual**: una falla y cuatro avisos, los cinco falsos. Y la falla decía «`VERSION` dice  y el CHANGELOG», con el hueco donde iba el dato que no pudo leer.

**Lo que entra:**

- Se reconoce si la carpeta es el estándar, por lo que solo el estándar tiene.
- Si no lo es, se dice en una línea y se nombra la bandera correcta.
- Y la comprobación de la versión calla cuando no pudo leer su archivo.

**Fuera de alcance:** no se revisaron los demás subcomandos. `--raiz` significa «el proyecto» en casi todos, y si el mismo problema aparece en otro sale como pendiente aparte.

---

## 2. Análisis previo — línea base verificada

Sobre AgroSystem, apuntar con `--raiz` pasó de una falla y cuatro avisos falsos a **un aviso que dice qué usar en su lugar**. Sobre el estándar sigue comprobando igual, sin incumplimientos. Y `--catalogo` sigue encontrando las 56 reglas propias sin respaldo, que era lo que sí servía.

### 2.1 Archivos que se crean o modifican

- `validadores/metareglas.py`
- `validadores/tests/test_metareglas_no_afirma_sobre_un_proyecto.py`

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `--raiz` rechaza lo que no es el estándar | Que `--raiz` haga lo de `--catalogo` | Cambiar lo que significa la bandera obliga a revisar quién la llama hoy; rechazar es barato y quita el veredicto falso |
| El aviso nombra la bandera correcta | Solo decir que no aplica | Sin decirla, el aviso deja a quien lo lee igual de perdido |
| Sin el dato no se afirma | Reportar con el hueco vacío | La lectura devuelve vacío cuando el archivo no está, así que atrapar el error de disco no bastaba |

---

## 3. Verificación

Los casos del `resultado_pruebas` §2, y las suites que la fase toca. **La batería entera no**, que es lo que `02·F5` pone como INCORRECTO y que en esta misma jornada ya costó catorce minutos y once rojos que ya existían.

---

## 4. Reversión

Revertir el commit de la fase. Todo es aditivo sobre funciones que ya existían.

---

## 5. Reglas aplicadas

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), por el alcance de la corrida.
- [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), porque se midió antes de dejar el criterio.
- `20·M10`, por la versión y el registro.

---

## 6. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
