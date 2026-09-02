# Funcionalidad implementada — Fase `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` (módulo Seguridad)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-tapar-la-clave-al-escribirla.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` |
| **Épica / HU** | [EP-014](../../epica.md) · [HU-001](../HU-001-tapar-la-clave-al-escribirla.md) |
| **Módulo** | Seguridad |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**Lo que se teclea se tapa; lo que se copia no, y se dice.**

`F-031` estaba construida a medias y sin declarar: el puente que tapa claves existía y **lo usaba un solo camino de los seis que escriben**. Ahora tapan los dos que reciben lo que una persona acaba de escribir, y los otros cuatro quedan declarados con su razón.

**Y la medición previa recortó el alcance.** Tapar los seis caminos habría alterado **7 documentos y 21 fragmentos** de los 1 002 guardados, sin vuelta atrás. Ninguno de los 21 era una clave: son los casos de prueba escritos en los documentos de las fases que construyeron el tapador.

El módulo Seguridad, que llevaba meses funcionando, **tiene especificación por primera vez**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se tapa lo que se acaba de escribir» (`RN-1`) | servicio | `llenar` en [plataforma/nucleo/ciclo_de_vida/core.py](../../../../../plataforma/nucleo/ciclo_de_vida/core.py) | ✅ | CP-001 |
| «El nombre de la variable queda intacto» (`RN-2`) | servicio | El enmascarador del estándar | ✅ | CP-001 |
| «Lo importado no se altera» (`RN-3`) | servicio | `parecen_traer_claves` solo lee | ✅ | CP-003 |
| «Sin enmascarador no se escribe» (`RN-4`) | servicio | `NoHayConQueTapar` en [plataforma/nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) | ✅ | CP-005 |
| «El reconocimiento no se duplica» (`RN-5`) | servicio | El puente | ✅ | Por construcción |
| «Todo camino declara si tapa» (`RN-6`) | doc | La §5.1 de la [especificación](../../../../seguridad/spec.md) | ✅ | §4 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | **La medición que recortó el alcance**: 7 documentos, 21 fragmentos, cero claves |
| T-02 · T-03 | Tapar al llenar, devolver cuántas, y contar sin tocar |
| T-04 · T-05 | La orden de consola, y la especificación que el módulo no tenía |
| T-06 · T-07 | 13 pruebas, y la orden corrida sobre los 1 002 documentos |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/seguridad/` | 13 pruebas, en verde |
| `plataforma/nucleo/ciclo_de_vida/` | 50 pruebas, en verde |
| La batería de la plataforma completa | 315 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si el reconocedor reconoce todo lo que hay que reconocer. Eso vive en el estándar.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py revisar_claves <identificador>
```

Dice cuántos documentos parecen traer credenciales, y cuáles. **No toca ninguno.**

Y tapar no se pide: pasa solo, en los caminos que escriben lo que alguien acaba de teclear.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Se tapa lo que se teclea, no lo que se copia** | Medido antes: tapar todo alteraría 7 documentos reales, y ninguno de los 21 fragmentos era una clave |
| **La importación avisa en vez de tapar** | Perder en silencio es perder igual |
| **Se devuelve cuántas se taparon** | Lo que se guardó ya no es lo que el usuario tecleó, y tiene que saberlo |
| **Contar tapa una copia y la descarta** | Así la cuenta y el tapado no se pueden separar |
| **Los seis caminos se declaran** | El camino que nace sin declararse es el que va a dejar pasar la próxima |

Señal registrada: [`S-106`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Los 7 documentos que parecen traer credenciales siguen ahí**, y está bien: son ejemplos escritos. Queda dicho para que nadie se asuste al verlos.
- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **El puente sigue siendo un puente.** El día que la plataforma y el estándar vivan en repositorios distintos, es lo primero que hay que mover, y lo dice su propio archivo.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/seguridad/spec.md](../../../../seguridad/spec.md) | Nace: el módulo no tenía especificación |
| [documentacion/senales.md](../../../../senales.md) | `S-106` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-014` |

El módulo Seguridad ya estaba en el catálogo de [cvds/diseno/README.md](../../../../../cvds/diseno/README.md) §3, con su requisito `RF-31`.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** El módulo pasa a ser aplicación para poder tener órdenes de consola.
