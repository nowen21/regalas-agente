# Funcionalidad implementada — Fase `H-EP-016-HU-002-derogar-marca-y-no-borra` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-escribir-corregir-y-derogar-una-regla.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `H-EP-016-HU-002-derogar-marca-y-no-borra` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-002](../HU-002-escribir-corregir-y-derogar-una-regla.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**Una regla se escribe y se deroga desde la plataforma.** Derogar **marca y conserva**: la regla se queda escrita entera, con su marca arriba y su identificador ocupado para siempre.

**Y antes de escribir se ven las que hablan de lo mismo.** Contra las 248 vigentes, preguntando por un título casi idéntico al de una regla real, encontró esa misma regla: **habría evitado escribir un duplicado**.

**Lo que más cuidado costó no fue el código, sino una frase.** El aviso dice, cada vez, que esto **no detecta contradicciones**. Sin ella la funcionalidad sería peor que no existir: quien confía en un detector deja de mirar.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «La fuente es el texto» (`RN-1`) | servicio | `crear` en [plataforma/nucleo/reglas/redaccion.py](../../../../../plataforma/nucleo/reglas/redaccion.py) | ✅ | CP-005 |
| «Nada se borra: se deroga» (`RN-2`) | servicio | `derogar` | ✅ | CP-006 |
| «Se muestran las que se parecen» (`RN-3`) | servicio | `parecidas_a` en [plataforma/nucleo/reglas/parecidas.py](../../../../../plataforma/nucleo/reglas/parecidas.py) | ✅ | CP-007 |
| «Una blindada no se deroga desde acá» (`RN-4`) | servicio | `NoSePuedeTocar` | ✅ | CP-006 |
| «La regla nace con sus huecos» (`RN-5`) | servicio | `molde` | ✅ | CP-005 |
| «Escribir queda registrado» (`RN-6`) | orden | `con_constancia` | ✅ | Por construcción |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El molde con sus huecos, y escribir pidiendo el identificador antes |
| T-03 · T-04 | Derogar marcando, y las tres razones por las que no se deroga |
| T-05 · T-06 | Las parecidas, y **el aviso de lo que no puede decir** |
| T-07 · T-08 | Las dos órdenes, y 14 pruebas |
| T-09 | **Corrido sobre las 248 vigentes: encontró el duplicado** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests_redaccion.py` | 14 pruebas, en verde |
| La batería de la plataforma completa | 382 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| Las parecidas sobre el cuerpo real | Encontró `M11` y `DOC19` |

**Lo que las pruebas no dicen:** si la regla escrita es buena. El criterio es de una persona.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py nueva_regla <proyecto> --prefijo M --titulo "..."
python manage.py nueva_regla <proyecto> --prefijo M --titulo "..." --capitulo base/20-meta-reglas --nombre "20 · Meta-reglas" --igual-la-escribo
python manage.py derogar_regla <proyecto> M20 --en 38.0.0 --ver M5 --porque "..."
```

**Sin `--igual-la-escribo` no escribe nada:** la orden sirve primero para mirar qué identificador tocaría y qué reglas hablan de lo mismo.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Se muestran las parecidas, y se dice que no detecta contradicciones** | Quien confía en un detector deja de mirar |
| **La regla nace con sus huecos puestos** | Una regla incompleta que no se nota se publica incompleta |
| **Derogar reescribe el encabezado y conserva el texto** | Lo que se mueve se pierde de vista; lo que se marca se sigue leyendo donde estaba |
| **Una blindada no se deroga desde acá** | Sostienen a las demás, y hacerlo por una orden de consola es demasiado fácil |
| **Sin `--igual-la-escribo` no se escribe** | La orden sirve primero para mirar |
| **Las palabras vacías son las del vocabulario de las reglas** | Sin quitar «regla», «debe» y «queda», todo se parece a todo |

Señal registrada: [`S-109`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Corregir una regla ya escrita** no está: se escribe y se deroga. Editar el cuerpo de una regla se hace por el módulo Ciclo de vida, que llena huecos.
- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **`F-007` a `F-010` siguen sin construir.** Sus historias están nombradas en la épica.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-109` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
