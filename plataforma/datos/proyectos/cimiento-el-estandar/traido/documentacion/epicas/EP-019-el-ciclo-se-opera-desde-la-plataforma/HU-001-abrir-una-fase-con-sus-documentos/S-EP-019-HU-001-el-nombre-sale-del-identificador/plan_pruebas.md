# Plan de Pruebas — Fase `S-EP-019-HU-001-el-nombre-sale-del-identificador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-abrir-una-fase-con-sus-documentos.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **una fase se abre con sus cinco documentos**, que **sin historia no se abre**, y que **el nombre sale del identificador**.

### 1.2 Alcance

**Entra:** armar el nombre, hallar la historia, escribir los cinco documentos y no pisar.

**No entra:** llenar los documentos, que ya lo hace `F-014`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El nombre | Con tildes, con eñes y con un título que no deja letras |
| La historia | Que exista y que no |
| Los cinco documentos | Que estén y que traigan el molde |
| La carpeta que ya existe | **Que no se toque** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Que se abra una fase sin historia, y que abrir pise lo escrito |
| **De contenido** | Se lee cada uno de los cinco documentos después de crearlos |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Pisar trabajo escrito es el único daño irreparable de este módulo** |
| Crítica | CP-001 | Una fase suelta es trabajo que nadie pidió |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/ciclo_de_vida/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Un proyecto conectado, y los moldes en `plantillas/`.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una prueba escribe en la carpeta real del proyecto**. Se reanuda cuando todas trabajen sobre carpetas temporales.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-002 | De contenido |
| CA-02 | CP-001 | Que **no** pase |
| CA-03 | CP-003 | De formato |

---

## 6. Casos de prueba

### CP-001 — Sin historia no se abre

**El caso que decide la fase.**

- Sin la carpeta de la historia, no se crea nada y se dice por qué.
- Con ella, se abre.
- Un proyecto que no está conectado también se dice, y distinto.

### CP-002 — Abrir no pisa

- Se abre, se escribe algo en un documento, y se vuelve a abrir.
- **El texto escrito sigue igual, carácter por carácter.**
- Quedan los cinco documentos, y cada uno trae el molde y el nombre de la fase.
- Abrir queda registrado en la auditoría.

### CP-003 — El nombre sale del identificador

- `D` + `EP-009` + `HU-001` + «La constancia va antes que el efecto» da el nombre que ya existe en el repositorio.
- «El año que vino con NADA» baja la tilde, la eñe y las mayúsculas.
- Un título que no deja ninguna letra **se rechaza**: el nombre dice de qué trata, no solo a qué historia pertenece.

**12 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con historias y fases de mentiras. **La carpeta real del proyecto no se toca al probar** (`08·T4`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un molde del estándar de verdad.** Las pruebas usan moldes de mentiras, cortos. Los reales tienen decenas de secciones, y la ficha advierte que *es donde más se nota si los moldes son pesados*. Eso no lo dice ninguna prueba: lo dice quien los llena.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se pisa trabajo escrito · se abre una fase sin historia |
| **Alta** | Falta alguno de los cinco documentos |
| **Media** | El nombre no coincide con los que ya están |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-09-01.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Documentos pisados al abrir | **Cero** |
| Fases abiertas sin historia | **Cero** |
| Archivos de la carpeta real tocados al probar | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo el camino feliz | La mitad de los casos comprueban que algo **no** pase |
| Probar sobre el proyecto real | Todas usan carpetas temporales |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada la épica entera el 2026-09-01 |
