# Estado de fase — Fase `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-023](../HU-023-un-rojo-se-puede-cerrar-declarandolo.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ La opción A, elegida por el usuario |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 11 tareas, 11 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Cinco sabotajes |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-065` |
| 12 | Commit | 👤 autorizado | ☐ **Esperando aprobación del usuario** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 · impacto sobre el molde y sus pruebas | Terminada | El validador compara encabezados y líneas copiadas: una fila opcional no rompe |
| T-01 · el campo en el molde | Terminada | Opcional, con su porqué |
| T-02 · leerlo del cierre | Terminada | `_declara_reemplazar` |
| T-03 · las condiciones que lo hacen válido | Terminada | Tres, y las tres hacen falta |
| T-04 · avisar cuando no resuelve | Terminada | Con el nombre escrito y el motivo |
| T-05 · los cinco CA | Terminada | 15 pruebas, **8 de que NO cierre** |
| T-06 · **con cero declaraciones, la línea idéntica** | Terminada | Los cinco números iguales |
| T-07 · declararlo en los dos que verificaron | Terminada | `EP-003·HU-002` y `EP-005·HU-001` |
| T-08 · medir y nombrar las que se mueven | Terminada | **Exactamente dos** |
| T-09 · `CHANGELOG` y `VERSION` | Terminada | `35.5.0`, MENOR |
| T-10 · sabotear | Terminada | Cinco, contra la mitad que importa |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un estado que solo tiene camino de entrada no es un estado: es una marca | [`S-065`](../../../../senales.md) |
| La salida se **declara**, no se infiere del orden: lo implícito tapa por accidente | `S-065` |
| Un veredicto puede estar mal el día que se escribe, no solo envejecer | [`S-063`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del commit**, que se pide aparte de la aprobación del cambio.
- **Las catorce historias que siguen en rojo.** Ocho no tienen fase posterior; seis la tienen y **no resolvieron el rojo**. Cada una es trabajo propio.

---

## 4. Si se bloqueó

No se bloqueó.

**Y el `T-06` es lo que hace creíble el resto:** con el código puesto y **cero declaraciones escritas**, los cinco números de la línea dieron exactamente lo mismo que la base. Si hubiera cambiado uno solo, el reemplazo se estaría deduciendo de algo, y el plan decía parar ahí.
