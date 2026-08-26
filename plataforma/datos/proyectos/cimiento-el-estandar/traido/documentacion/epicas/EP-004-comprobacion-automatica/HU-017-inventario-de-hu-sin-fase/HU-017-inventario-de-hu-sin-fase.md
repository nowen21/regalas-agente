# HU-017 — Decir cuántas HU quedan sin su fase completa

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-017 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Cumplida — los cuatro CA y los dos transversales verificados el 2026-08-17 (v23.3.0) |

---

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que la comprobación de fases termine diciendo cuántas HU hay, cuántas completas y cuántas incompletas
- **Para** responder «cuánto falta» leyendo una línea, en vez de contar 54 avisos a mano

---

## 3. Contexto y descripción

**Lo que ya está hecho.** `validar.py fases` recorre el árbol de épicas y reporta las dos cosas que hacen falta saber: la HU que no tiene ninguna carpeta de fase ([`02·F12.2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) y la fase a la que le falta alguno de sus cinco documentos (`F12.13`), nombrando cuál. Sale como aviso, no como falla, que es lo correcto: una HU recién escrita todavía no tiene por qué tener fase.

**Lo que falta es el número.** La corrida termina en `0 falla(s), 54 aviso(s)`. Ese `54` mezcla las HU sin fase con las fases incompletas, y no dice sobre cuántas HU se está hablando. Para saber que eran **52 de 66** —49 sin ninguna fase y 3 a medias— el 2026-08-16 hubo que escribir un script aparte y contar. El script no quedó en el repositorio, así que la próxima vez se vuelve a escribir.

Es la diferencia entre una lista y un tablero. La lista dice qué le falta a cada una, y ya la hay. El tablero dice cuánto falta en total, y esa es la pregunta que se hace al abrir el repositorio.

**Y hay dónde escribirlo.** [`plantillas/inventario-hu.md`](«RUTA-ESTANDAR»/plantillas/inventario-hu.md) tiene los tres campos —total, completas, incompletas— que hoy se llenan a mano contra lo que uno haya contado. Que los llene una corrida es lo que evita que el tablero envejezca en silencio.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | La corrida termina diciendo cuántas HU hay, cuántas completas y cuántas incompletas | Hallazgo H-1 del 2026-08-16 |
| RN-02 | Una HU está completa cuando tiene al menos una fase y **todas** sus fases tienen los cinco documentos | `02·F12.2` y `F12.13` |
| RN-03 | Completas más incompletas da el total | Aritmética; se comprueba porque es lo que delata un error de conteo |
| RN-04 | La cuenta sale del mismo recorrido que ya hacen las comprobaciones de fases, no de uno nuevo | `EP-004 §10.2`: un solo insumo, un solo resultado |
| RN-05 | Sigue siendo aviso y no falla | Regla ya vigente en `fases.py`, que esta historia no cambia |
| RN-06 | El programa reporta y no crea nada | `EP-004 §10.2` |

### 3.2 Supuestos

- Las fases seguirán viviendo como carpetas dentro de la carpeta de su HU, con los nombres de `02·F12.6`.

### 3.3 Fuera de alcance

- Volver a listar lo que ya lista `fases`: qué HU están sin fase y qué documento le falta a cada una. Eso ya funciona y no se toca.
- Llenar la tabla del inventario. El programa da la cuenta; el tablero lo escribe una persona.
- Juzgar el contenido de los documentos. Que el `plan_pruebas` exista no dice que sirva.
- Crear la fase que falta.

---

## 4. Criterios de aceptación

### CA-01 — La corrida dice el total, las completas y las incompletas

```gherkin
Dado el árbol completo de épicas
Cuando se corre la comprobación de fases
Entonces la salida termina diciendo cuántas HU hay, cuántas completas y cuántas incompletas
Y las dos últimas suman el total
```

**Cómo validarlo:**

1. Correr `python validadores/validar.py fases` desde la raíz del repositorio.
2. Leer la última línea. Resultado esperado: además del conteo de fallas y avisos, dice los tres números.
3. Sumar completas más incompletas. Resultado esperado: da el total declarado.
- **Aprobado cuando:** los tres números aparecen y cuadran entre sí.

### CA-02 — El total coincide con las carpetas que hay

```gherkin
Dado que se cuentan a mano las carpetas HU del árbol
Cuando se compara con el total que reporta la corrida
Entonces son el mismo número
```

**Cómo validarlo:**

1. Contar las carpetas `HU-*` que tienen su archivo `.md` adentro.
2. Correr la comprobación y leer el total. Resultado esperado: coinciden.
3. Crear una HU nueva con su archivo y volver a correr. Resultado esperado: el total sube uno, y las incompletas también.
- **Aprobado cuando:** el número que reporta es el que hay, no uno aproximado.

### CA-03 — Una HU con dos fases cuenta como completa solo si las dos lo están

```gherkin
Dado una HU con dos carpetas de fase, una completa y la otra sin su resultado_pruebas
Cuando se corre la comprobación
Entonces esa HU cuenta como incompleta
```

**Cómo validarlo:**

1. Tomar una HU con dos fases —hoy `EP-005 · HU-008` y `EP-007 · HU-001`— y quitar de una de ellas el `resultado_pruebas.md`, guardándolo aparte.
2. Correr la comprobación. Resultado esperado: las completas bajan uno y las incompletas suben uno.
3. Devolver el archivo a su sitio y volver a correr. Resultado esperado: los números vuelven a lo que eran.
- **Aprobado cuando:** una fase incompleta arrastra a toda su HU, sin importar cuántas hermanas tenga.

### CA-04 — Caso borde: la épica sin HU y la carpeta HU sin su archivo

```gherkin
Dado una carpeta de épica sin HU, o una carpeta HU-000 sin su archivo .md
Cuando se corre la comprobación
Entonces no se cae
Y esa carpeta no entra en el total
```

**Cómo validarlo:**

1. Crear una carpeta de épica vacía y una `HU-000-prueba` sin archivo adentro.
2. Correr la comprobación. Resultado esperado: termina sin error y el total no cambia.
3. Borrar las dos carpetas de prueba. Resultado esperado: la salida vuelve a ser la de antes.
- **Aprobado cuando:** una carpeta a medias no rompe la corrida ni ensucia el conteo.

### Criterios de aceptación transversales

- [ ] **Límites** — árbol vacío, épica sin HU y HU sin archivo tienen comportamiento definido (`08`).
- [ ] **No regresión** — los avisos que `fases` ya emitía siguen saliendo igual, uno por uno (`08`).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Determinismo** | El mismo árbol da los mismos números siempre |
| RNF-02 | **Autonomía** | Sin internet, sin IA y sin dependencias fuera de la biblioteca estándar |
| RNF-03 | **Rendimiento** | La cuenta no agrega un segundo recorrido del árbol |
| RNF-04 | **Compatibilidad** | Corre en Windows, con rutas que llevan espacios y tildes |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md).
- **Contrato de API:** no aplica; se corre por línea de comandos, como las demás comprobaciones.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Contar, en el recorrido que ya hace `fases.py`, cuántas HU quedan completas y cuántas no.
- [ ] Escribir la línea de resumen al final de la corrida.
- [ ] Prueba de que completas más incompletas da el total.
- [ ] Prueba de la HU con dos fases, una incompleta.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase](A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase/README.md) | CA-01, CA-02, CA-03 y CA-04 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase/resultado_pruebas.md#6-veredicto-de-la-fase) — los cuatro CA y los dos transversales verificados. Pendiente el commit |

**La fase construye, y es la más chica de la épica.** `fases.py` ya sabe qué HU no tiene fase; lo único que no hace es sumar. La cuenta del 2026-08-16 se hizo con un script que no quedó en el repositorio.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La comprobación de fases, que ya existe y ya recorre el árbol. Esta historia le agrega la cuenta, no la reemplaza | Alto |
| Dependencia | HU-009, el conteo por regla, que es la misma idea aplicada a otra cosa | Bajo |
| Riesgo | Que la cuenta se calcule aparte y termine diciendo algo distinto de los avisos de la misma corrida | RN-04: sale del mismo recorrido |
| Riesgo | Que el número cambie entre dos corridas porque otra sesión está trabajando | Ya pasó el 2026-08-16, dos veces en una jornada. Es real y no lo evita el programa |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La corrida de fases termina con total, completas e incompletas
- [ ] Los tres números cuadran y coinciden con las carpetas
- [ ] Los avisos que ya salían siguen saliendo igual
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Se apoya en la comprobación de fases, que ya existe |
| **N**egociable | Sí | Dónde va la línea y qué más muestre |
| **V**aliosa | Sí | Es la pregunta que se hace al abrir el repositorio, y hoy cuesta un script |
| **E**stimable | Sí | Dos contadores sobre un recorrido que ya está escrito |
| **S**mall (pequeña) | Sí | La más pequeña de la épica |
| **T**esteable | Sí | Se prueba moviendo un archivo de sitio |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, desde el hallazgo H-1 de la sesión «las HU sin su fase» |
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Recortada a lo que falta de verdad: `fases.py` ya lista las HU sin fase y los documentos que faltan; lo que no da es la cuenta |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A y se construye la línea del inventario (v23.3.0). Los cuatro CA verificados; los tres números del programa coinciden con los del pendiente 48, y una prueba los compara en cada corrida |
