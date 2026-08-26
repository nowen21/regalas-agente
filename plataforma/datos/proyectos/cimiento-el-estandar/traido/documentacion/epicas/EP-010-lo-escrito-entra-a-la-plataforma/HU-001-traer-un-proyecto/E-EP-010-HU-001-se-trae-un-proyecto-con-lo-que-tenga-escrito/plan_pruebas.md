# Plan de Pruebas — Fase E-EP-010-HU-001: se trae un proyecto con lo que tenga escrito   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-E-EP-010-HU-001 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que la documentación que un proyecto ya tiene escrita entre a la plataforma **sin tocar el proyecto**, que traerla dos veces no duplique, y que lo que no entró se diga.

**No se prueba** el reporte detallado de lo no reconocido, que es la fase F. Acá basta con que se cuente y se pueda ver.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que reconocer y traer hagan lo suyo | Sí |
| Integración | Que traer pase por la auditoría y por el almacén | Sí |
| Interfaz | Que se muestre qué se va a traer antes de traerlo | Sí |
| Aislamiento | Que el proyecto de origen no cambie | Sí |
| Volumen | Que se pueda con este repositorio, de más de mil archivos | Sí |

### 3.2 Técnicas

- Comparar la carpeta de origen entera antes y después, archivo por archivo.
- **Traer el repositorio real**, que es el caso más grande que hay.
- Casos que buscan el rechazo, no el camino feliz.
- Sabotaje: romper el código a propósito, restaurando con copia y corriendo la suite completa al final.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-1` lo que sigue un molde queda adentro, con su tipo | [CP-001](#cp-001--lo-que-sigue-un-molde-entra-con-su-tipo) | ☐ |
| `CA-5` nada se transforma | [CP-002](#cp-002--lo-traído-dice-lo-mismo-que-el-original) | ☐ |
| `CA-4` lo no reconocido se cuenta y se puede ver | [CP-003](#cp-003--lo-que-no-sigue-ningún-molde-no-entra-y-se-cuenta) | ☐ |
| `CA-6` si todo se reconoció, se dice | [CP-004](#cp-004--si-todo-se-reconoció-se-dice) | ☐ |
| `CA-3` traer dos veces no duplica | [CP-005](#cp-005--traer-dos-veces-no-duplica) | ☐ |
| `00·N1` se muestra qué se va a traer, y se confirma | [CP-006](#cp-006--se-muestra-qué-se-va-a-traer-antes-de-traerlo) | ☐ |
| Una falla a mitad no deja nada | [CP-007](#cp-007--una-falla-a-mitad-no-deja-media-importación) | ☐ |
| El caso real: este repositorio | [CP-008](#cp-008--se-trae-este-mismo-repositorio) | ☐ |
| `CA-2` · que NO pase: que se toque el proyecto de origen | [CP-009](#cp-009--que-no-pase-que-se-toque-el-proyecto-de-origen) | ☐ |

## 5. Los casos

### CP-001 · Lo que sigue un molde entra con su tipo

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que cada documento entre reconocido, no como un archivo cualquiera |
| **Cómo se corre** | Se arma un proyecto de mentira con una épica, una historia, un plan de trabajo, un plan de pruebas, un resultado, un cierre y un estado de fase, y se trae |
| **Resultado esperado** | Los siete entran, **cada uno con su tipo**, y cada uno dice de qué archivo salió |
| **Si falla** | Si entran sin tipo, lo traído es un montón de archivos y no la documentación de un proyecto |

**Se prueban también los tres moldes que faltaban:** el documento de señales, un resultado de segundo ciclo, y un registro de adopción de versión. Salieron de contar sobre el repositorio real, y son la razón por la que se agregaron a la lista.

### CP-002 · Lo traído dice lo mismo que el original

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-5`: nada se transforma sin que el usuario lo diga |
| **Cómo se corre** | Se trae un documento y se compara **carácter por carácter** con el archivo de origen |
| **Resultado esperado** | Idénticos |
| **Si falla** | Cualquier cambio silencioso, aunque sea un salto de línea, es una transformación que nadie pidió |

### CP-003 · Lo que no sigue ningún molde no entra, y se cuenta

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-4`: nada se pierde en silencio |
| **Cómo se corre** | Se arma un proyecto con dos documentos con molde y tres sin él, y se trae |
| **Resultado esperado** | Entran dos. Los tres sin molde **no entran**, se cuentan, y se puede ver la ruta de cada uno |
| **Si falla** | Si entran igual, se está adivinando su forma, que es lo que la especificación descartó |

### CP-004 · Si todo se reconoció, se dice

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-6`: una lista vacía no explica nada |
| **Cómo se corre** | Se trae un proyecto donde todo tiene molde |
| **Resultado esperado** | Se dice que no quedó nada afuera, con esas palabras |
| **Si falla** | Una sección vacía se lee como «el reporte no se generó» |

### CP-005 · Traer dos veces no duplica

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-3` |
| **Cómo se corre** | Se trae un proyecto, se cuenta lo que entró, y se trae otra vez |
| **Resultado esperado** | La cuenta no sube, y la segunda pasada **dice cuántos ya estaban** |
| **Si falla** | Se revisa por qué se identifica cada documento: tiene que ser su ruta de origen, no su contenido |

**Y si el documento cambió en el origen, se trae la versión nueva sin crear otro documento.** Es el caso que distingue «no duplicar» de «no actualizar».

### CP-006 · Se muestra qué se va a traer antes de traerlo

| Campo | Valor |
|---|---|
| **Qué comprueba** | `00·N1` sobre una acción que trae cientos de documentos de una vez |
| **Cómo se corre** | Se pide traer sin confirmar |
| **Resultado esperado** | Sale el **recuento por tipo**, cuántos no se reconocieron, y **qué carpetas no se miraron**. Nada entró todavía |
| **Si falla** | Si algo entró antes de confirmar, la pregunta era decorativa |

**El recuento por tipo, no la lista entera.** Un número por tipo se lee; mil líneas se confirman sin mirar, y entonces la confirmación deja de proteger.

### CP-007 · Una falla a mitad no deja media importación

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que media importación no sea peor que ninguna |
| **Cómo se corre** | Se hace fallar la escritura a mitad de la pasada, a propósito |
| **Resultado esperado** | No queda **nada** de esa pasada, y el proyecto de origen intacto |
| **Si falla** | Con media documentación adentro, nadie sabe qué falta ni por dónde seguir |

### CP-008 · Se trae este mismo repositorio

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el módulo pueda con el caso más grande que existe hoy |
| **Cómo se corre** | Se conecta este repositorio y se trae su documentación |
| **Resultado esperado** | Entran los documentos del ciclo, **con el recuento por tipo escrito**, y el tiempo que tardó |
| **Si falla** | Se mira si es volumen, memoria o un molde que aparece solo acá |

**Los números se escriben aunque salga bien.** Al planear se contó: 969 archivos en `documentacion/`, 966 con molde. Si la corrida da otra cosa, la diferencia es el hallazgo.

### CP-009 · Que NO pase: que se toque el proyecto de origen

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-2` y `RN-1`: traer copia, nunca mueve ni modifica |
| **Cómo se corre** | Se retrata la carpeta del proyecto entera, se trae, y se compara **archivo por archivo** |
| **Resultado esperado** | Ningún archivo cambió, se creó ni se borró. Tampoco cambió su fecha |
| **Si falla** | Es el peor error posible de este módulo: traer es la operación que más archivos ajenos lee |

**También se comprueba después de una falla a mitad**, que es cuando un código escrito con prisa podría dejar restos.

## 6. Lo que este plan NO puede probar

- **Que el reconocimiento sirva para otros proyectos.** Se mide sobre este repositorio, que sigue el estándar al pie de la letra. Un proyecto que lo siga a medias va a reconocer menos, y eso se sabrá al conectarlo.
- **Que reconocer por nombre no deje pasar nada.** Un archivo con el nombre correcto y otra cosa adentro entraría igual. Se acepta a sabiendas, y está declarado como riesgo en el plan.
- **Que lo traído sirva para gobernar el proyecto.** Eso se ve cuando la plataforma opere el ciclo, en la versión 5.

## 7. Criterios de salida

- Los nueve casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- Los números del caso real escritos: cuántos entraron, de qué tipo, cuántos no, y cuánto tardó.
- Las pruebas validadas con sabotaje, restaurando con copia y corriendo la suite completa al final.
- El repositorio de origen comprobado intacto después de traerlo.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
