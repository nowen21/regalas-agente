# Plan de Pruebas — Fase `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** lo que esta fase cambia y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **lo genérico deja de encabezar el reporte** sin llevarse por delante lo que sí importa, y que en un proyecto con pocas conversaciones el filtro no deja el reporte vacío.

### 1.2 Alcance

**Entra:** el vocabulario de la casa calculado sobre el corpus, las rutas pegadas, el mínimo de sesiones distintas, el orden, y el resguardo de corpus chico.

**No entra:** pantalla, ni decidir la regla que el patrón sugiera.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las tres formas que se midieron, y por qué se descartaron dos |
| [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/A-EP-011-HU-002-lo-que-se-repitio-sale-contado/resultado_pruebas.md](../A-EP-011-HU-002-lo-que-se-repitio-sale-contado/resultado_pruebas.md) | El reporte de la fase anterior |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El vocabulario de la casa | Que se calcule, que atrape «debe» y que **no** atrape el tema |
| El resguardo | Que con pocas sesiones no se filtre |
| Las rutas pegadas | Que no cuenten, y que el resto del mensaje sí |
| El mínimo de sesiones | Que repetir en un solo día no entre |
| El orden | Primero lo que aparece en más días distintos |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De medición previa** | Las tres formas se compararon **antes** de escribir el código |
| **De que no se lleve lo bueno** | Un filtro que limpia demasiado deja un reporte limpio y vacío |
| **De borde** | Un proyecto con dos conversaciones |
| **Sobre lo real** | El corpus de 67 sesiones, que es donde el defecto se vio |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Si el filtro se lleva «español colombiano», el reporte queda limpio y sin valor** |
| Crítica | CP-004 | Un reporte vacío en un proyecto nuevo se lee como «no hubo nada» |
| Alta | CP-001, CP-003 | Que lo genérico salga, y que las rutas no cuenten |
| Media | CP-005 | El orden |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/medicion/` entera, y las dos baterías por la no regresión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El plan aprobado, y **las tres formas ya medidas**.
- El reporte anterior, escrito, para comparar.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- El reporte corrido sobre lo real, con su salida escrita.
- «Español colombiano» sigue estando.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el filtro se lleva lo que sí importa**. Un reporte del que desapareció el único caso conocido de regla que faltaba es peor que el reporte ruidoso: el ruidoso se puede leer con paciencia; el otro miente por omisión.

---

## 5. Matriz de trazabilidad

| Qué | Caso | Tipo |
|---|---|---|
| Lo genérico sale del reporte | CP-001 | De filtro |
| Lo que sí es tema queda | CP-002 | **De que no se lleve lo bueno** |
| Las rutas pegadas no cuentan | CP-003 | De ruido |
| Con pocas sesiones no se filtra | CP-004 | De borde |
| Repetir en un solo día no cuenta, y el orden | CP-005 | De partición |

---

## 6. Casos de prueba

### CP-001 — Lo dicho en muchas sesiones no es tema

- **Precondición:** diez sesiones, con «debe quedar» en todas.
- **Resultado esperado:** no aparece en el reporte, y `vocabulario_de_la_casa` incluye «debe».

### CP-002 — Lo que sí es tema queda

- **Precondición:** las mismas diez, con el tema en dos.
- **Resultado esperado:** el tema **sí** aparece, y su palabra **no** está en el vocabulario.
- **Y sobre lo real:** «español colombiano» sigue en el reporte después del filtro.

### CP-003 — Las rutas pegadas no cuentan

| Entrada | Se espera |
|---|---|
| «mire c:/Ing. Jose/ia/agente y arregle» | queda «mire y arregle» |
| «revise historico-chat/2026-01-02.md y me dice» | quedan «revise» y «me dice» |

### CP-004 — Con pocas sesiones no se filtra

- **Precondición:** dos sesiones.
- **Resultado esperado:** el vocabulario sale vacío, y el reporte no queda mudo.

### CP-005 — Repetir en un solo día no cuenta, y primero lo de más días

| Entrada | Se espera |
|---|---|
| Lo mismo tres veces el mismo día | no entra |
| Lo mismo en dos días distintos | entra |
| Cuatro días contra diez veces en dos días | primero el de cuatro días |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

La base de prueba de la plataforma, con conversaciones que la propia prueba escribe; y lo indexado de verdad para la corrida final. No aplican usuarios.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si de las primeras filas nace una regla.** Eso es juicio, y es el riesgo 2 de la HU. Lo mide el usuario leyendo, no una prueba.

**Y un corpus de otro tema.** El umbral del cuarto de las sesiones se calibró contra este trabajo; en un proyecto que hable de otra cosa habrá que volver a mirarlo.

---

## 8. Herramientas

El corredor de la plataforma. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El filtro se lleva un tema de verdad |
| **Alta** | El reporte queda vacío en un proyecto con pocas conversaciones |
| **Media** | El orden no refleja los días distintos |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Después |
|---|---|---|
| Filas genéricas entre las cinco primeras | 3 de 5 | se cuenta |
| «Español colombiano» | puesto 21 | se cuenta |

### 12.2 Dónde se miden

La salida de la orden, escrita en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Calibrar el umbral contra las pruebas y no contra lo real | El `CP-002` corre además sobre el corpus de verdad |
| Dar por buena la mejora sin comparar | El resultado trae el reporte **antes y después** |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
