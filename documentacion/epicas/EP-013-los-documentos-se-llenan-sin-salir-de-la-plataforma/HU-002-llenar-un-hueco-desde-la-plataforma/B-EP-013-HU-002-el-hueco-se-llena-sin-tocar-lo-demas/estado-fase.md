# Estado de fase — Fase `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` (módulo Ciclo de vida)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` |
| **Módulo** | Ciclo de vida |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma.md](../HU-002-llenar-un-hueco-desde-la-plataforma.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Verificado que hoy la plataforma no escribe en ningún proyecto |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: se escribe en el archivo original |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-013 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Sin entidades; se escribe aparte y se pone en su sitio de un golpe |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01, y ampliado el mismo día con `huecos.py` |
| 8 | Implementador | implementado + pruebas verdes | ☑ 24 pruebas nuevas, 50 en el módulo |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Dos defectos, los dos cerrados acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **Es la primera fase que escribe fuera de `datos/`.** Hasta hoy la plataforma lee los proyectos y escribe solo sus propias copias. Un error acá no da un número equivocado: toca el repositorio del usuario.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Los dos que salieron se cerraron acá |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

> **El alcance se amplió en marcha, con el usuario.** Correr sobre un documento real destapó que la cuenta de la fase anterior estaba inflada, y arreglarlo pedía tocar `huecos.py`, que este plan no declaraba. Se le dijo, con los dos caminos y el número delante, y autorizó sumarlo. Queda escrito porque `02·F8` exige que lo tocado sea lo declarado.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | El reemplazo que no toca nada más |
| T-02 | Terminada | Guardado de un golpe, y **sin traducir los finales de línea** |
| T-03 | Terminada | La huella y el aviso del cambio ajeno |
| T-04 | Terminada | `llenar`, con la constancia antes del efecto |
| T-05 | Terminada | La copia al día |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 24 pruebas, más 2 de la cuenta corregida |
| T-08 | Terminada | **Un documento real llenado: cero caracteres cambiados fuera del hueco** |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los cinco bloqueos del plan quedaron cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Se escribe en el archivo original del proyecto, no en la copia: la copia se rehace al importar | Está en la §6 de la especificación |
| Un documento que **habla de** una convención parece incumplirla: 51 de 77 marcas no eran huecos | [`S-105`](../../../../senales.md) |
| Traducir los finales de línea cambia todos los renglones sin que se vea | [`S-105`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Si llenar por huecos resulta cómodo sigue sin responderse.** El documento que se llenó tenía un hueco, y el que más tiene hoy tiene dos. La pregunta la responde quien llene uno de veinte.
- **Quedan 25 documentos con 26 espacios por llenar.** Llenarlos es trabajo de contenido, no de una fase.
- **Los números de la fase A quedaron viejos** por el defecto que esta corrigió. No se reescriben: la corrección vive acá.

---

## 4. Si se bloqueó

No se bloqueó.
