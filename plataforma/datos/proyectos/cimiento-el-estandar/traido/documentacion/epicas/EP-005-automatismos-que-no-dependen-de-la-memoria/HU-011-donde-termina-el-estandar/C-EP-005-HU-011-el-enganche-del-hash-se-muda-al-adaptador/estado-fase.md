# Estado de fase — Fase `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` |
| **Módulo** | Automatismos — enganches |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) · [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La prueba de la frontera lo venía reportando |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-005 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-011 ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (`02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ La cuenta mira los dos canales |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Dos defectos aparecieron y se cerraron acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `96a356d` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | Movido con `git mv`; la ruta a `validadores/` sube un nivel |
| T-02 | Terminada | La plantilla del `post-commit` apunta al adaptador |
| T-03 | Terminada | `enganches_enchufados()`, derivada de las dos tablas |
| T-04 | Terminada | La prueba compara contra esa función, no contra una tabla |
| T-05 | Terminada | Instalador corrido, y el enganche comprobado con un commit |
| T-06 | Terminada | El mapa dice dónde vive y por qué el recuento no se movió |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

**Dos archivos aparecieron que el plan no declaraba** (`02·F8`): `validadores/estacion_commit.py` y `validadores/rutas_fuera.py`, y **no por esta fase**: los toca la fase `D-EP-004-HU-008`, que corre el mismo día. Acá solo se ajustó cómo nombran a su corredor, porque decir el archivo del enganche los hacía contarse como amarrados a la herramienta.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un enganche se conecta por dos canales, y la comprobación de la frontera miraba uno; la pieza mudada parecía un archivo que nadie usa | [`S-095`](../../../../senales.md) |
| Nombrar un enganche dentro de un mensaje hace que el contador lea ese programa como amarrado a la herramienta | [`S-095`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Los proyectos ya instalados** tienen el `post-commit` apuntando a la ruta vieja hasta que corran el instalador. No rompe el commit: la línea termina en `|| true`. Queda dicho, no abierto.
- **El commit de la fase se llevó la mudanza y no el arreglo de adentro.** `git mv` deja la renombrada preparada, y la corrección de la ruta que el archivo hace a `validadores/` es un cambio **aparte** que el `git add` de esa vuelta no recogió. Lo publicado revienta al correrse, y como el enganche termina en 0 pase lo que pase, **habría fallado en silencio**. Se vio corriendo la versión publicada, no la del disco. Corregido el mismo día, y queda anotado acá porque es el defecto de esta fase.

---

## 4. Si se bloqueó

No se bloqueó.
