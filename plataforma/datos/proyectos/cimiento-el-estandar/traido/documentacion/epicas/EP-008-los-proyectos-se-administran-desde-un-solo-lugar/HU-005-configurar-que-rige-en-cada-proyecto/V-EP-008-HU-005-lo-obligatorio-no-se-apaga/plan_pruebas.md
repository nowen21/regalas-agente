# Plan de Pruebas — Fase `V-EP-008-HU-005-lo-obligatorio-no-se-apaga`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-005](../HU-005-configurar-que-rige-en-cada-proyecto.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **lo opcional se enciende y se apaga**, que **lo obligatorio no**, y que **cada proyecto recibe lo suyo**.

### 1.2 Alcance

**Entra:** hallar lo opcional, encender, apagar, rechazar y entregar.

**No entra:** elegir moldes, y la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La lista de opcionales | Marca en la regla, marca en el capítulo, y palabra suelta que no cuenta |
| Encender y apagar | Con fecha y con quién |
| El rechazo | Con el porqué |
| Lo que se entrega | De ese proyecto y de ninguno más |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Que se apague una obligatoria |
| **De aislamiento** | Que lo de un proyecto no llegue al otro |
| **Contra el estándar real** | La lista se leyó nombre por nombre, no solo su tamaño |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Si lo obligatorio se puede apagar, el estándar es una sugerencia** |
| Crítica | CP-004 | **Es el que descubrió que sobraba `02·F0`** |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/proyectos/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El cuerpo de reglas marca lo opcional como el capítulo 20 manda.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una regla obligatoria aparece en la lista de opcionales**. Pasó, y por eso hay un caso propio.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-001 | De ida y vuelta |
| CA-02 | CP-002 | Que **no** pase |
| CA-03 | CP-003 | De aislamiento |
| Transversal | CP-004 | Contra el estándar real |

---

## 6. Casos de prueba

### CP-001 — Lo opcional se prende y se apaga

- De fábrica viene apagado, y **se dice que el proyecto no la encendió**.
- Encender y apagar queda escrito con fecha y con quién.
- Cambiar de estado tres veces **no deja tres filas de la misma regla**.
- Un estado que no existe se rechaza.

### CP-002 — Lo obligatorio no se apaga

**El caso que decide la fase.**

- Apagar una obligatoria **no se hace**, y el motivo dice que volvería el estándar una sugerencia.
- Encenderla tampoco tiene sentido, y se rechaza igual.
- Una obligatoria rige siempre, aunque el proyecto no configure nada.
- **Una regla que no existe se trata como obligatoria:** ante la duda, no se apaga.

### CP-003 — Cada proyecto recibe lo suyo

- Lo encendido en uno no llega al otro.
- Un proyecto sin configurar **se dice así**, no como uno con cero reglas.

### CP-004 — La marca va en la línea de la regla

**Lo que salió al correrlo contra el estándar real.**

- Una palabra suelta en el archivo **no vuelve opcional al capítulo entero**.
- La cabecera del capítulo **sí** rige a todas sus reglas.
- La marca en la línea de una regla vale **solo para esa**.

**14 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un estándar de mentiras con tres capítulos —uno obligatorio, uno opt-in entero y uno con una sola regla marcada—, y dos proyectos en carpetas temporales.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un proyecto que apague muchas reglas a la vez.** Las pruebas encienden y apagan de a una. La ficha advierte que *cada opción que se agrega es una forma más de que dos proyectos no se parezcan*, y eso no lo mide ninguna prueba: se ve cuando dos proyectos dejan de entenderse.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Una obligatoria aparece como opcional · se apaga una obligatoria |
| **Alta** | Lo de un proyecto llega a otro |
| **Media** | El archivo queda con filas repetidas |

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
| Reglas obligatorias en la lista de opcionales | **Cero** |
| Configuraciones que se cruzan entre proyectos | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por buena la lista por su tamaño | Se leyó nombre por nombre, y ahí apareció `02·F0` |
| Probar solo con reglas marcadas a mano | Se corrió contra las 257 reglas reales |

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
