# Plan de Pruebas — Fase `Z-EP-021-HU-001-lo-vacio-se-dice`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-ver-el-estado-sin-abrir-la-consola.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **las cinco pantallas responden**, que **lo vacío se dice** y que **ninguna convierte un «no se sabe» en un cero**.

### 1.2 Alcance

**Entra:** las cinco pantallas, sus enlaces, su caso vacío y sus advertencias.

**No entra:** cambiar algo desde la pantalla, y los seis módulos sin ella.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/avisos/spec.md](../../../../avisos/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Las cinco direcciones | Que respondan, y que un proyecto inexistente dé 404 |
| Los enlaces | Que no haya que escribir ninguna dirección a mano |
| El caso vacío | Cinco, y cada uno se dice distinto |
| Las advertencias | Que salgan impresas con los datos |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De pantalla completa** | Se pide la dirección y se lee el HTML que sale |
| **De caso vacío** | Es el que decide, y es el que nadie prueba |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Una pantalla en blanco se lee como un error de la plataforma, y casi nunca lo es** |
| Alta | CP-003 | Un cero donde no se sabe hace decidir mal |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/avisos/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `EP-019` y `EP-020` cerradas.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **alguna pantalla sale en blanco** sin decir por qué.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-001 | De pantalla completa |
| CA-02 | CP-002 | De caso vacío |
| CA-03 | CP-003 | De distinción |
| Transversal | CP-004 | De lo que no se muestra |

---

## 6. Casos de prueba

### CP-001 — Las cinco responden y se llega a ellas

- Las cinco direcciones devuelven 200.
- **A las cuatro de un proyecto se llega desde su ficha**, y al tablero desde cualquier pantalla.
- Un proyecto que no existe da **404**, no una pantalla rota.

### CP-002 — Lo vacío se dice

**El caso que decide la fase, y son cuatro casos distintos.**

| Pantalla | Qué dice cuando no hay nada |
|---|---|
| Fases | «no tiene ninguna fase... **no es un error**» |
| Aprobaciones | «la plataforma no ha registrado ninguna todavía» |
| Memoria | responde, y dice lo que pasa, en vez de reventar |
| Funcionalidades | «no hay qué contar» |

### CP-003 — Ninguna escribe cero donde no se sabe

- El tablero escribe **«sin datos»**, y lo explica.
- Una fase sin fecha dice **«no lo dice»**, no cero días.
- La de funcionalidades separa los tres estados con palabras.

### CP-004 — Cada pantalla dice qué no muestra

- Las fases de otro modelo se avisan.
- Las aprobaciones dicen que **no son todos los documentos del proyecto**.
- El tablero dice que **«vencida» es un número puesto acá**.
- La memoria dice que **lo dado de baja no se borra**.

**15 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un proyecto de mentiras en una carpeta temporal, y el cliente de pruebas de Django pidiendo las cinco direcciones.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si las pantallas se entienden.** Las pruebas comprueban que las frases estén; que alguien las lea y sepa qué hacer no lo dice ninguna. Y **no hay prueba de cómo se ven**: se comprueba el texto que sale, no el diseño.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Una pantalla sale en blanco · una ruta no responde |
| **Alta** | Un «no se sabe» sale como cero |
| **Media** | Una pantalla no dice qué deja por fuera |

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
| Pantallas en blanco sin explicación | **Cero** |
| Ceros escritos donde no se sabe | **Cero** |
| Direcciones que hay que escribir a mano | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con datos | La mitad de los casos prueban el proyecto vacío, que es el estado de cualquiera recién conectado |

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
