# Plan de Trabajo — Fase `S-EP-019-HU-001-el-nombre-sale-del-identificador` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `S-EP-019-HU-001-el-nombre-sale-del-identificador` |
| **Épica** | [EP-019](../../epica.md) |
| **HU** | [HU-001 Abrir una fase con sus documentos](../HU-001-abrir-una-fase-con-sus-documentos.md), una sola (`F12.1`) |
| **Módulo** | Ciclo de vida |
| **Especificación del módulo** | [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-011`:** *«que nadie cree carpetas y archivos a mano, ni se salte un documento»*.
- 🩹 **Y una razón de este repositorio:** hay 209 fases, todas abiertas a mano, y el nombre de cada una se escribió a dedo.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que abrir una fase deje sus cinco documentos y su nombre bien puesto, sin escribir nada a mano.

**Lo que la fase decide de verdad es a qué se niega:** una fase sin historia no se abre, y una carpeta que ya existe no se toca.

**Fuera de alcance:** abrir épicas e historias —la fase es donde duele—, y llenar los documentos, que ya lo hace `F-014`.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** los moldes de `plantillas/ciclo-vida-proyectos/`, que el módulo ya sabía leer para decir qué huecos tiene un documento.

**Lo verificado:** las 209 fases del repositorio siguen el patrón `LETRA-EPICA-HU-de-que-trata`, sin tildes ni eñes en la carpeta. El nombre que arma esta fase da exactamente el mismo.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/ciclo_de_vida/apertura.py` | Crear | Servicio | Armar el nombre y escribir los cinco |
| `plataforma/nucleo/ciclo_de_vida/management/commands/abrir_fase.py` | Crear | Consola | La orden |
| `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` | Crear | Prueba | Los tres CA |
| `documentacion/ciclo-de-vida/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración:** lo que se crea son archivos del proyecto.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** El módulo ya leía moldes; ahora también los escribe.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El nombre se arma, no se escribe** | Recibirlo como texto | Escribirlo a mano es de donde salen las fases que no se sabe de dónde cuelgan |
| **Sin historia no se abre** | Crearla igual y avisar | Una fase suelta es trabajo que nadie pidió (`02·F0`) |
| **Si la carpeta existe, no se toca** | Rellenar lo que falte | Es el único daño irreparable de este módulo |
| **El molde se lee al abrir, no se copia dentro** | Guardar una copia del molde | Un molde copiado envejece en cuanto el estándar cambie el original |
| **Las tildes y la eñe se bajan en el nombre** | Dejarlas | Un nombre de carpeta con tilde se rompe distinto en cada sistema |

### 2.7 Dudas por resolver antes de codificar

Ninguna: el nombre lo fija `02·F12.6`.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Armar el nombre desde el identificador | Servicio | 1 h | — | CA-03 | EV-01 |
| T-02 | Hallar la carpeta de la historia | Servicio | 1 h | — | CA-02 | EV-01 |
| T-03 | Escribir los cinco documentos desde el molde | Servicio | 1,5 h | T-02 | CA-01 | EV-01 |
| T-04 | No tocar lo que ya existe | Servicio | 30 min | T-03 | Transversal | EV-01 |
| T-05 | La orden de consola | Consola | 1 h | T-04 | — | EV-01 |
| T-06 | Las pruebas de los tres CA | Test | 2 h | T-05 | Todos | EV-01 |

**Total estimado:** 7 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-02 → T-03 → T-06.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Abriendo y mirando la carpeta | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Intentándolo sin la carpeta de la historia | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Armando nombres, con tildes y con eñes | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con historias y fases de mentiras. **La carpeta real del proyecto no se toca al probar** (`08·T4`).

---

## 7. Reversión / rollback  ·  Q11

Módulo nuevo dentro de uno que ya estaba: se quita el archivo y no queda rastro. **Lo que sí queda son las fases abiertas**, que son archivos del proyecto y los borra quien los abrió.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F0`](../../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) y `02·F12.6`, que fija cómo se llama una fase.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que abrir dos veces pise trabajo escrito** | **Alto: no se recupera** | Si la carpeta existe, no se toca, y hay prueba | Cerrado |
| B-02 | Que se abran fases sueltas | Alto | Sin historia no se abre | Cerrado |
| B-03 | Que un nombre con tilde se rompa en otro sistema | Medio | Se bajan tildes y eñe | Cerrado |
| B-04 | Que los moldes sean tan pesados que nadie los llene | Medio | **Se acepta y se declara:** está en la ficha, y no se resuelve acá | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que sin historia no se abre
- [x] Comprobado que abrir no pisa
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
