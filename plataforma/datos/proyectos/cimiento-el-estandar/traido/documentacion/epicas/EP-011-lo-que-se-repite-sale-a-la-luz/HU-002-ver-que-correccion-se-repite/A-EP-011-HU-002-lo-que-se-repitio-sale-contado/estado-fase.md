# Estado de fase — Fase `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` (módulo Medición)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` |
| **Módulo** | Medición |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 3 720 mensajes indexados por la fase anterior |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-011 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ **Aprobada el 2026-08-31**, junto con la decisión que le faltaba |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/medicion/spec.md](../../../../medicion/spec.md), con su `RN-6` agregada y registrada |
| 6 | Diseñador | diseño coherente | ☑ Se agrupa por frase compartida, no en cadena |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 16 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Un defecto crítico apareció al correrlo sobre lo real, y se cerró acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `9ea244d` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **La puerta que faltaba era una decisión, no un documento.** La lista de listo de la historia tenía sin marcar *«está decidido qué cuenta como corrección»*, y sin eso no hay nada que contar. La tomó el usuario el 2026-08-31, y quedó escrita como `RN-6` de la especificación.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, más el transversal |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | La lista cerrada de confirmaciones, y lo que la herramienta pega |
| T-02 | Terminada | Las parejas de palabras con contenido |
| T-03 | Terminada | Contar, agrupar, ordenar y recortar por período |
| T-04 | Terminada | Los dos silencios, separados |
| T-05 | Terminada | La orden, con la línea que dice que el patrón no es la regla |
| T-06 | Terminada | 16 pruebas, con el caso real del `CA-03` |
| T-07 | Terminada | Corrido sobre lo indexado: 1 389 correcciones, y el reporte escrito |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| El reporte, en su primera corrida, medía lo que la herramienta pega al mensaje y no lo que la persona escribió. Con datos inventados se habría visto perfecto | [`S-099`](../../../../senales.md) |
| Agrupar lo mismo dicho distinto salió contando frases compartidas, sin instalar nada: el riesgo que la historia daba por probable no se materializó | [`S-099`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Si el reporte sirve.** La historia lo dice: *«si no nace una regla nueva, no sirvió»*. Ninguna prueba lo mide; se mide leyendo lo que salió. Queda abierto a propósito, para el usuario.

---

## 4. Si se bloqueó

No se bloqueó.
