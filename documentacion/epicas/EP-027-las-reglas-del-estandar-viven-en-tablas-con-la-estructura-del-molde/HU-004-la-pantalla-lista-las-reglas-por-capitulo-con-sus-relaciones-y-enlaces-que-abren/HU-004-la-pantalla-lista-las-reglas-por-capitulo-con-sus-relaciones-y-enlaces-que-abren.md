# HU-004 · La pantalla lista las reglas por capítulo, con sus relaciones y enlaces que abren

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | Estándar en la base: `core/estandar/` y sus plantillas |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien consulta o administra el estándar en Cimiento
- **Quiero** ver las reglas por capítulo y con su nombre, leer cada una como una página ordenada y seguir sus relaciones con un clic
- **Para** entender qué exige cada regla sin leer el texto crudo del archivo ni conocer cómo está guardado

---

## 3. Contexto y descripción

Hoy la pantalla «Estándar» lista las rutas de los archivos, y cada documento se muestra como texto crudo: se ven los `#`, las barras de las tablas, los asteriscos y las comillas invertidas, y los enlaces no abren. Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 3, y de la corrección del usuario del 2026-10-07: el estándar se ve como una interfaz HTML que aplica la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`) con los componentes de Tabler.

Esta HU se hace antes que la HU-001 y la HU-002 porque no necesita las tablas: lee el texto que la base guarda hoy. Cuando la HU-003 arme el texto desde las tablas, la página lo muestra igual.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La lista agrupa los documentos por capítulo, con el nombre del capítulo y el código y el título de cada regla; no muestra rutas de archivo (acuerdo 3) |
| RN-02 | Un capítulo de un solo documento, con sus reglas como secciones, lista cada regla y lleva a su sección |
| RN-03 | Cada documento se muestra como página: títulos, párrafos, listas, tablas de Tabler, citas como avisos y el ejemplo INCORRECTO / CORRECTO en dos tarjetas, roja y verde, con su texto |
| RN-04 | La conversión del texto a la página es código propio, sin la librería `markdown` (acuerdo 3) |
| RN-05 | Un enlace a otro documento del estándar abre ese documento en Cimiento, en la sección que nombra; un enlace a un archivo que no está en la base se muestra como texto, sin enlace roto |
| RN-06 | La página de cada documento tiene un espacio de relaciones que muestra por separado sus dependencias (`extiende`, `depende de`, `deroga`, de `20·M7`), las reglas que nombra su texto y los documentos que la nombran (acuerdo 3) |
| RN-07 | Quien administra cambia el texto en una pestaña aparte; leer es lo primero que se ve |

### 3.2 Supuestos

- Los documentos de la base siguen el molde de la regla (`20·M5`): un encabezado `## <código> · <título>` y el ejemplo en un bloque con INCORRECTO y CORRECTO.

### 3.3 Fuera de alcance

- Armar el texto desde las tablas: es de la HU-003.
- Propuestas, historia y memoria: HU-005.

---

## 4. Criterios de aceptación

### CA-01 · La lista va por capítulo y por nombre

**Sale de:** acuerdo 3 del análisis 1 del pendiente 136

```gherkin
Dado el estándar guardado en la base
Cuando se abre la pantalla «Estándar → Reglas y documentos»
Entonces cada capítulo es un grupo con su nombre
Y cada regla aparece con su código y su título, sin la ruta del archivo
```

**Cómo validarlo:**
1. Entrar a Cimiento y abrir el menú «Estándar», opción «Reglas y documentos».
2. Buscar el grupo «02 · Flujo de trabajo» → resultado esperado: lista «F1 · Carga el contexto antes de actuar», sin `base/` ni `.md`.
3. Buscar el grupo «01 · Conducta del agente» → resultado esperado: lista «C1 · Avisa antes de tocar», y al pulsarla abre esa sección.
- Se aprueba cuando ningún renglón de la lista muestra una ruta, y la prueba `core.estandar.tests_vista_estandar` pasa.

### CA-02 · El documento se lee como página

**Sale de:** corrección del usuario del 2026-10-07

```gherkin
Dado un documento del estándar
Cuando se abre su página
Entonces se ven títulos, tablas y listas con el estilo de Tabler
Y el ejemplo se ve en una tarjeta «Incorrecto» y otra «Correcto»
Y no se ve ninguna marca del texto: ni #, ni |---|, ni **, ni ```
```

**Cómo validarlo:**
1. Abrir la regla «F1 · Carga el contexto antes de actuar» desde la lista.
2. Mirar el ejemplo → resultado esperado: dos tarjetas, roja «Incorrecto» y verde «Correcto».
3. Mirar el sello → resultado esperado: una tabla con sus columnas, no barras.
- Se aprueba cuando la prueba `core.estandar.tests_vista_estandar` pasa.

### CA-03 · Los enlaces abren y las relaciones se ven

**Sale de:** acuerdo 3 del análisis 1 del pendiente 136

```gherkin
Dado un documento que nombra otras reglas
Cuando se abre su página
Entonces cada enlace a otra regla abre esa regla en Cimiento
Y el espacio de relaciones muestra por separado sus dependencias, las reglas que nombra y las que la nombran
```

**Cómo validarlo:**
1. Abrir la regla «C1 · Avisa antes de tocar».
2. Mirar el espacio «Relaciones» → resultado esperado: «Depende de: N1» y la lista de las que la nombran.
3. Pulsar el enlace a `00·N1` → resultado esperado: abre el núcleo blindado en la sección N1.
- Se aprueba cuando la prueba `core.estandar.tests_vista_estandar` pasa.

### Criterios de aceptación transversales

- [ ] Autorización: la pestaña para cambiar el texto solo la ve el grupo administrador.
- [ ] No regresión: las suites de `core.estandar` y `core.ayuda` quedan verdes.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | Ninguna nueva: código propio y Tabler ya instalado |
| RNF-02 | **Seguridad** | El texto se escapa antes de convertirlo: nada del documento entra como HTML sin escapar |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §2, §3, §4, §6 y §12 |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] La conversión del texto a página y la lectura de títulos y relaciones.
- [ ] La lista por capítulo y la página del documento.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-004-el-estandar-se-lee-como-pagina` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-027-HU-004-el-estandar-se-lee-como-pagina/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-004-el-estandar-se-lee-como-pagina/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-004-el-estandar-se-lee-como-pagina/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Ninguna: lee el texto de hoy; con la HU-003, ese texto sale de las tablas | Bajo |
| Riesgo | Un documento que no sigue el molde se ve mal | Lo que no se reconoce se muestra como párrafo |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Lee el texto de hoy |
| **N**egociable | Sí | |
| **V**aliosa | Sí | El estándar se entiende sin leer el archivo crudo |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 y la corrección del usuario del 2026-10-07 |
