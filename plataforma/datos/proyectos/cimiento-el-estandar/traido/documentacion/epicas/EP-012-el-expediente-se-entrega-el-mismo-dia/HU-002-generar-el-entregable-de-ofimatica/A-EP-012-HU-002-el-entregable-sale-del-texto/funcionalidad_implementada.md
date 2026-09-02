# Funcionalidad implementada — Fase `A-EP-012-HU-002-el-entregable-sale-del-texto` (módulo Expediente)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-012-HU-002-el-entregable-sale-del-texto` |
| **Épica / HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) · [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md) |
| **Módulo** | Expediente |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**El expediente ya se convierte en un archivo que se abre y se entrega.** El de este repositorio son 762 documentos en un solo archivo, con su índice, sus 6 205 tablas y sus **1 697 listas dentro de celdas** — que era la parte donde estos convertidores dejan la marca del texto a la vista.

**Sin una sola dependencia nueva**, con la librería estándar, como se decidió. Y con el número que lo respalda: **15 marcas del origen quedaron a la vista en 8 093 097 caracteres**, todas del mismo caso.

Con esto, la versión 2 entrega lo que promete: **el expediente el mismo día**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Un solo archivo, con su índice y sus documentos en el mismo orden» (§6) | servicio | `armar_el_texto` en [plataforma/nucleo/expediente/entregable.py](../../../../../plataforma/nucleo/expediente/entregable.py) | ✅ | CP-001 |
| «Las listas dentro de una celda salen como listas» (`CA-7`) | servicio | `celda` en [plataforma/nucleo/expediente/marcado.py](../../../../../plataforma/nucleo/expediente/marcado.py) | ✅ | CP-002 |
| «Generar dos veces da el mismo archivo» (§6) | servicio | Sin fecha adentro | ✅ | CP-003 |
| «Se avisa antes de generar, y se genera igual» (§6) | servicio | `generar` devuelve los avisos | ✅ | CP-004 |
| «Generar queda registrado en la auditoría» (§6) | servicio | `auditoria.con_constancia` | ✅ | Por construcción |
| «`RN-6` la fuente es el texto; la salida se rehace» (§4) | servicio | Todo se genera; nada se edita | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El convertidor completo, con las tablas y las listas dentro de celdas |
| T-03 · T-04 | La envoltura sin nada de la red, el índice, y lo que falta adentro |
| T-05 · T-06 | Guardado con constancia, y la orden con los avisos primero |
| T-07 · T-08 | 20 pruebas, y la medición sobre ocho millones de caracteres |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/expediente/` | 40 pruebas, en verde |
| La batería de la plataforma completa | 252 pruebas, en verde |
| La medición sobre el archivo real | 15 marcas en 8 093 097 caracteres |

**Lo que las pruebas no dicen:** si el archivo se ve presentable. Eso se decide abriéndolo.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py generar_entregable <identificador>
python manage.py generar_entregable <identificador> --hasta A-EP-001-HU-003-lo-que-sea
```

Queda en `datos/proyectos/<identificador>/entregable/`. **Se rehace cuando se quiera y no se edita:** si hay que corregir algo, se corrige el documento y se genera otra vez.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Con la librería estándar**, aun sabiendo que había una instalada | El entregable es lo único que sale hacia un tercero; una actualización cambiaría lo que el cliente ve |
| **Se convierte lo que los documentos usan** | Convertir un lenguaje entero sería rehacer lo que ya existe |
| **Lo que va en código se aparta y no se vuelve a tocar** | `**esto**` dentro de código salía en negrita, que es justo lo contrario de para qué se escribe |
| **El separador no parte una negrita que lo contiene** | Partía «1 · Ver lo que hay» en dos y dejaba 174 marcas a la vista |
| **Lo citado se convierte por dentro** | Una cita con tabla adentro salía cruda: 31 marcas |
| **La fecha no va dentro del archivo** | Haría distintos dos archivos idénticos, y `CA-03` no se podría comprobar |
| **Lo que falta va dentro del archivo** | Quien lo recibe tiene que ver lo mismo que vio quien lo generó |

Señal registrada: [`S-102`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Quince marcas de énfasis dentro de énfasis.** Resolverlo pide un analizador de verdad; por quince en ocho millones no se justifica hoy.
- **Sin pantalla**, como las fases anteriores del módulo.
- **El entregable refleja lo traído**, que puede estar viejo. Es la misma deuda que dejó la fase anterior.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/expediente/spec.md](../../../../expediente/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-102` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** El entregable se guarda en la carpeta de datos, y se rehace cuando se pida.
