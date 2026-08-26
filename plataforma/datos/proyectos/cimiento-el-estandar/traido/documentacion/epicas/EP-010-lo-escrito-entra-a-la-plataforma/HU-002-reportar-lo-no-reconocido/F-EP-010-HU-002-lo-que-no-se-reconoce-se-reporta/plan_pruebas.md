# Plan de Pruebas — Fase F-EP-010-HU-002: lo que no se reconoce se reporta   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-F-EP-010-HU-002 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que lo que no entró **se pueda volver a mirar sin traer otra vez**, y que el reporte diga la verdad completa: qué no se reconoció, qué no se miró, y cuándo.

**Se prueban los cuatro criterios, no solo el que falta.** Tres ya estaban construidos por la fase E, y un plan que solo mirara lo nuevo daría por probado lo que nadie probó contra esta historia.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que el reporte se escriba con lo que debe decir | Sí |
| Integración | Que la auditoría lo enlace | Sí |
| Persistencia | Que se pueda volver a mirar sin traer | Sí |
| Interfaz | Que los reportes se vean desde el proyecto | Sí |

### 3.2 Técnicas

- **Volver a mirar el reporte en otro momento**, sin traer: es la única forma de probar que quedó guardado.
- Comparar dos reportes de traídas distintas.
- Casos con nada que reportar, no solo con problemas.
- Sabotaje: romper el código a propósito, restaurando con copia, limpiando rastros, y corriendo la suite al final.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-01` lo no reconocido se lista con su ruta y cuántos son | [CP-001](#cp-001--el-reporte-lista-lo-no-reconocido-con-su-ruta) | ☐ |
| Transversal: el reporte queda guardado | [CP-002](#cp-002--el-reporte-se-puede-volver-a-mirar-sin-traer-otra-vez) | ☐ |
| `CA-03` si todo se reconoció, se dice | [CP-003](#cp-003--cuando-no-quedó-nada-afuera-el-reporte-lo-dice) | ☐ |
| El reporte dice qué carpetas no se miraron | [CP-004](#cp-004--el-reporte-dice-qué-carpetas-no-se-miraron-y-por-qué) | ☐ |
| El registro de auditoría enlaza el reporte | [CP-005](#cp-005--el-registro-de-auditoría-dice-dónde-está-el-reporte) | ☐ |
| Dos traídas dejan dos reportes comparables | [CP-006](#cp-006--dos-traídas-dejan-dos-reportes-y-se-ve-qué-cambió) | ☐ |
| Los reportes se ven desde el proyecto | [CP-007](#cp-007--los-reportes-se-ven-desde-la-pantalla-del-proyecto) | ☐ |
| `CA-02` · que NO pase: que lo no reconocido entre o se toque | [CP-008](#cp-008--que-no-pase-que-lo-no-reconocido-entre-o-se-toque) | ☐ |

## 5. Los casos

### CP-001 · El reporte lista lo no reconocido, con su ruta

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-01` sobre el documento guardado, no sobre la pantalla |
| **Cómo se corre** | Se trae un proyecto con dos documentos con molde y tres sin él, y se abre el reporte |
| **Resultado esperado** | Dice **cuántos** quedaron afuera y **cuáles**, con su ruta completa |
| **Si falla** | Un reporte que dice el número sin los nombres no sirve para corregir nada |

### CP-002 · El reporte se puede volver a mirar sin traer otra vez

| Campo | Valor |
|---|---|
| **Qué comprueba** | El transversal, que es lo único que esta fase construye de cero |
| **Cómo se corre** | Se trae un proyecto, **se borra su carpeta de origen**, y se pide el reporte |
| **Resultado esperado** | El reporte sale completo. No hace falta el proyecto ni volver a traer |
| **Si falla** | Es lo que pasaba antes de esta fase: para saber qué quedó afuera había que traer el proyecto entero otra vez |

**Se borra la carpeta a propósito.** Es la forma dura de comprobar que el reporte quedó guardado y no se recalcula al vuelo.

### CP-003 · Cuando no quedó nada afuera, el reporte lo dice

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-03`, y que el reporte se escriba **siempre** |
| **Cómo se corre** | Se trae un proyecto donde todo tiene molde, y se busca su reporte |
| **Resultado esperado** | **El reporte existe** y dice que no quedó nada afuera |
| **Si falla** | Si no se escribe reporte, su ausencia no distingue entre «salió perfecto» y «no se corrió» |

### CP-004 · El reporte dice qué carpetas no se miraron, y por qué

| Campo | Valor |
|---|---|
| **Qué comprueba** | La otra mitad de lo que no entró, que hoy solo se ve en la pantalla |
| **Cómo se corre** | Se trae un proyecto que tenga `base/` y `pendientes/`, y se lee el reporte |
| **Resultado esperado** | Las nombra, **con la razón de cada una** |
| **Si falla** | El reporte estaría diciendo «esto quedó afuera» sin decir que además hubo carpetas enteras que ni se abrieron |

### CP-005 · El registro de auditoría dice dónde está el reporte

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que se pueda llegar del registro al reporte |
| **Cómo se corre** | Se trae un proyecto y se lee el registro de la acción |
| **Resultado esperado** | El registro trae la **ruta** del reporte, y **no repite la lista** |
| **Si falla** | Si repite la lista, hay dos copias de lo mismo que se van a separar. Si no la enlaza, el registro sigue diciendo cuántos sin decir cuáles |

### CP-006 · Dos traídas dejan dos reportes, y se ve qué cambió

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que cada traída deje el suyo, con su fecha |
| **Cómo se corre** | Se trae un proyecto con tres archivos sin molde; se corrige uno; se vuelve a traer |
| **Resultado esperado** | Quedan **dos** reportes. El segundo dice dos sin reconocer; el primero sigue diciendo tres |
| **Si falla** | Si el segundo pisa al primero, se pierde la historia y no se puede ver qué se corrigió |

### CP-007 · Los reportes se ven desde la pantalla del proyecto

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que se pueda llegar a ellos sin buscar en el disco |
| **Cómo se corre** | Con dos traídas hechas, se abre la pantalla del proyecto |
| **Resultado esperado** | Se ven los dos, del más nuevo al más viejo, con su fecha. **Sin traídas, se dice**, en vez de una lista vacía |
| **Si falla** | Un reporte que hay que buscar en el disco es un reporte que nadie mira |

### CP-008 · Que NO pase: que lo no reconocido entre o se toque

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-02`, ahora con el reporte de por medio |
| **Cómo se corre** | Se retrata la carpeta del proyecto, se trae, y se comprueba lo traído y la carpeta |
| **Resultado esperado** | Los documentos sin molde **no entraron**, y **ningún archivo del proyecto cambió** |
| **Si falla** | Escribir el reporte no puede volverse una excusa para tocar lo que se reporta |

## 6. Lo que este plan NO puede probar

- **Que el reporte se entienda sin conocer el proyecto.** Se prueba que diga lo que debe; si se entiende lo dice el usuario al leerlo.
- **Que los reportes no estorben con el tiempo.** Uno por traída. Con cientos habría que decidir algo, y hoy no hay cómo saberlo.

## 7. Criterios de salida

- Los ocho casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- El reporte del repositorio real leído y pegado en la evidencia.
- Las pruebas validadas con sabotaje, restaurando con copia y limpiando rastros.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
