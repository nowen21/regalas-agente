# Funcionalidad implementada — Fase `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` |
| **Épica / HU** | [EP-015](../../epica.md) · [HU-001](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md) |
| **Módulo** | Comprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**La plataforma ya dice si un proyecto cumple, sin entrar a él.** Corre las **32 comprobaciones** del estándar contra la carpeta del proyecto y devuelve el veredicto **con el archivo y la línea** de lo que no cumple.

**No duplica ni una comprobación.** Le pide al estándar que corra las suyas, por su punto de entrada y en un proceso aparte. Es la tercera vez que la plataforma usa esta forma, después del reconocedor de credenciales y del que parte una conversación en turnos.

**Y distingue lo que nadie distinguía:** un proyecto sin el estándar instalado **no está en verde, está sin comprobar**. Son cosas distintas, y confundirlas hace que nadie mire los rojos de verdad.

Sobre este repositorio: **32 comprobaciones en 116,9 segundos**, y encontró dos enlaces rotos reales en su primera corrida.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se comprueba, no se corrige» (`RN-1`) | servicio | `comprobar` en [plataforma/nucleo/comprobaciones/core.py](../../../../../plataforma/nucleo/comprobaciones/core.py) | ✅ | CP-004 |
| «Lo que no cumple sale con archivo y línea» (`RN-2`) | servicio | `_FALLA` | ✅ | CP-002 |
| «Sin comprobar no es no cumplir» (`RN-3`) | servicio | `Veredicto.se_pudo` | ✅ | CP-003 |
| «Las comprobaciones no se duplican» (`RN-4`) | servicio | Se corre el punto de entrada del estándar | ✅ | Por construcción |
| «Cero corridas es rojo» (`RN-5`) | servicio | `Veredicto.cumple` | ✅ | CP-005 |
| «El veredicto no se guarda» (`RN-6`) | servicio | Ninguna entidad | ✅ | Por construcción |
| «La salida se tapa antes de mostrarse» (§9) | servicio | `claves.tapar` sobre la salida | ✅ | §4 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La detección previa, y el punto de entrada en un proceso aparte |
| T-03 · T-04 | El resumen y las fallas, y la salida tapada |
| T-05 · T-06 | El veredicto con «cero es rojo», y la orden de consola |
| T-07 | **13 pruebas** |
| T-08 | **32 comprobaciones en 116,9 s**, con dos fallas reales encontradas |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/comprobaciones/` | 13 pruebas, en verde |
| La batería de la plataforma completa | 328 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La corrida sobre este repositorio | 32 comprobaciones, 116,9 s |

**Lo que las pruebas no dicen:** si las comprobaciones del estándar reconocen lo que deben. Eso vive allá.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py comprobar <identificador>
python manage.py comprobar <identificador> --cuantas 0
```

Sin `--cuantas` salen las primeras quince fallas; con `0`, todas.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Se corre el punto de entrada del estándar, en un proceso aparte** | Es como se corren de verdad. Importar sus módulos daría un número que nadie más obtiene |
| **«Sin comprobar» es una respuesta propia** | Confundirla con «no cumple» hace que nadie mire los rojos de verdad |
| **Cero comprobaciones es rojo** | Una corrida que no comprobó nada y termina bien se lee como éxito |
| **La salida se tapa antes de devolverla** | Trae fragmentos de los archivos del proyecto, y uno puede traer una clave |
| **Si no aparece el resumen del estándar, no se da veredicto** | Suponer que cumple porque no se entendió la respuesta es el peor error posible acá |
| **El veredicto no se guarda** | El proyecto cambia y el veredicto envejece sin avisar |

Señal registrada: [`S-107`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **116,9 segundos.** Se aguantan para pedirlo a mano; no para pedirlo seguido. Quien lo enchufe en algún sitio tendrá que decidirlo con el número delante. **Declarado, sin pendiente**, porque hoy no está enchufado en ninguna parte.
- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **`F-021` y `F-022` siguen sin construir.** Sus historias están nombradas en la épica y sin escribir.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | Nace: módulo nuevo |
| [documentacion/senales.md](../../../../senales.md) | `S-107` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-015` |
| [cvds/analisis-requisitos/inventario-funcionalidades.md](../../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) | La vuelta de la columna, explicada |

El módulo Comprobaciones ya estaba en el catálogo de [cvds/diseno/README.md](../../../../../cvds/diseno/README.md) §3, con sus requisitos `RF-20` a `RF-22`.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** Una aplicación más en la lista.
