# Plan de Pruebas — Fase `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que la corrida del estándar **también corre la batería de la plataforma**, que cero pruebas allá es rojo, que no tenerla se dice, y que pedir un subconjunto sigue siendo barato.

### 1.2 Alcance

**Entra:** correr la otra batería, contar lo que corrió, distinguir los tres silencios posibles, y el subconjunto.

**No entra:** fundir las dos baterías, ni meter la de la plataforma en el `pre-commit`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones, y el costo aceptado |
| `S-097` | El rojo que estuvo puesto una jornada entera |
| [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/A-EP-005-HU-021-el-corredor-que-si-las-corre/funcionalidad_implementada.md](../A-EP-005-HU-021-el-corredor-que-si-las-corre/funcionalidad_implementada.md) | Lo que hizo la fase A, y lo que no vio |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El corredor de la otra batería | Que corra, y que diga cuántas |
| Los tres silencios | No hay plataforma · la hay y no corre nada · corre y falla |
| El resumen | Que diga las dos cifras, **aparte** |
| El subconjunto | Que no arrastre las 187 |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De silencio** | Es el corazón de la historia: un cero que se lee como verde |
| **De partición** | Los tres estados en que la otra batería puede estar |
| **De sabotaje** | Una prueba de la plataforma en rojo tiene que cazarse; sin esto, todo lo demás pasa igual |
| **Sobre lo de verdad** | Las 187 reales, no una imitación |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-004 | **Si el sabotaje no se caza, la integración no sirve para nada** |
| Crítica | CP-002 | No tener plataforma no puede ser falla: sería un rojo permanente en cada proyecto que hereda |
| Alta | CP-001, CP-003 | Que corra, y que cero sea rojo |
| Media | CP-005 | El subconjunto |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`test_la_bateria_de_la_plataforma_se_corre.py` entera, y la corrida completa del estándar por la no regresión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- La cuenta de hoy: 724 pruebas corridas, 187 sin correr.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- El sabotaje cazado.
- La corrida completa diciendo las dos cifras.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la corrida completa se pasa del doble de lo que tardaba**. Esta historia existe porque un peaje se apaga; construir el peaje sería el mismo defecto con otro nombre.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — corre y dice cuántas | CP-001 | De sistema |
| CA-02 — no tener plataforma se dice, y no es falla | CP-002 | De silencio |
| CA-02 — cero pruebas es rojo | CP-003 | Que **no** pase |
| CA-01 — una prueba en rojo se caza | CP-004 | **De sabotaje** |
| CA-03 — el subconjunto no arrastra | CP-005 | De partición |

---

## 6. Casos de prueba

### CP-001 — Corre la batería que hay, y la cuenta

- **Acción:** pedirle la otra batería a este repositorio.
- **Resultado esperado:** más de cien pruebas corridas y ningún hallazgo de falla.

### CP-002 — No tener plataforma se dice, y **no es falla**

- **Precondición:** un repositorio sin carpeta de plataforma.
- **Resultado esperado:** un **aviso** que dice que no se corrió, y que eso no es lo mismo que estar en verde. Ninguna falla.
- **Por qué es crítico:** cada proyecto que hereda el estándar está en este caso. Si fuera falla, tendría un rojo permanente, y un rojo que siempre está se apaga.

### CP-003 — Cero pruebas es rojo

- **Precondición:** una plataforma de mentiras cuyo punto de entrada no corre nada.
- **Resultado esperado:** falla, diciendo que cero no es verde.

### CP-004 — Una prueba de la plataforma en rojo se caza

- **Acción:** escribir dentro de la plataforma una prueba que falla a propósito, correr, y borrarla.
- **Resultado esperado:** una falla, con la cuenta de cuántas corrieron y cuántas fallaron.
- **Por qué es el caso que decide:** sin él, todo lo demás pasaría igual con un corredor que no mira nada.

### CP-005 — El subconjunto no arrastra la otra batería

- **Acción:** pedir una sola prueba en un repositorio chico.
- **Resultado esperado:** el resumen **no** nombra la plataforma.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

Repositorios de mentiras creados y borrados por la propia prueba, y este repositorio para el caso de verdad.

### 7.2 Datos de prueba

Un punto de entrada vacío, y una prueba de mentiras que pasa.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Una plataforma con otro marco.** Lo que se lee es la línea que su corredor imprime al terminar; si mañana la plataforma cambia de marco, esa línea cambia y hay que volver acá. Queda dicho para que no se descubra en silencio.

---

## 8. Herramientas

`unittest` y el corredor de la plataforma, llamado por su punto de entrada. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Una batería en rojo pasa como verde |
| **Alta** | No tener plataforma se reporta como falla |
| **Media** | El resumen no distingue las dos cifras |

### 9.2 Flujo del defecto · 9.3 Contenido mínimo · 9.4 Registro

Se anota en el `resultado_pruebas.md` de esta fase, con qué se corrió, qué salió y qué se esperaba.

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
| Baterías del repositorio que nada corre | 1 de 2 | 0 de 2 |
| Pruebas que la orden ejecuta | 724 | 911 |
| Cuánto tarda la corrida completa | ~10 min | se mide, y no puede pasar del doble |

### 12.2 Dónde se miden

El resumen de `validar.py internas`, que ahora dice las dos cifras.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por buena la integración sin haberla visto fallar | El `CP-004` la sabotea |
| Probar solo con plataformas de mentiras | El `CP-001` corre las 187 de verdad |

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
