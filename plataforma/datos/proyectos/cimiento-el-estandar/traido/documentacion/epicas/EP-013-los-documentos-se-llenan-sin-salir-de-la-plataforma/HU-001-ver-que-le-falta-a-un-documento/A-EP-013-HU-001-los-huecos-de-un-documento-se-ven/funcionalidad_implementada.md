# Funcionalidad implementada — Fase `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-ver-que-le-falta-a-un-documento.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` |
| **Épica / HU** | [EP-013](../../epica.md) · [HU-001](../HU-001-ver-que-le-falta-a-un-documento.md) |
| **Módulo** | Ciclo de vida |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**La plataforma ya dice qué le falta por llenar a un documento del ciclo.** De cualquiera se sabe qué molde sigue, cuántos espacios le quedan y dónde está cada uno, con el texto que lo rodea.

Sobre este repositorio: **54 documentos con espacios por llenar, 77 en total**, de 1 002 traídos.

**Y una cuenta que no infla.** El diseño original contaba también los huecos con nombre; medirlo antes de construir mostró que en un documento escrito no se distinguen de una cita, y que de 341 marcas reales **ninguna** era un hueco. Contarlas habría dado por incompleto todo documento bien escrito.

Es el primer módulo del Ciclo de vida, y **sin una sola dependencia nueva**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El molde de un documento se decide por su tipo» (`RN-1`) | servicio | `molde_de` en [plataforma/nucleo/ciclo_de_vida/moldes.py](../../../../../plataforma/nucleo/ciclo_de_vida/moldes.py) | ✅ | CP-001 |
| «Solo el hueco cierto entra en la cuenta» (`RN-2`) | servicio | `encontrar` en [plataforma/nucleo/ciclo_de_vida/huecos.py](../../../../../plataforma/nucleo/ciclo_de_vida/huecos.py) | ✅ | CP-003 |
| «Lo que llena la instalación no se le pregunta al usuario» (`RN-3`) | servicio | La clase `INSTALACION`, contada aparte | ✅ | CP-004 |
| «Los huecos se calculan al pedirlos» (§5) | servicio | Ninguna entidad, ninguna migración | ✅ | Por construcción |
| «Un tipo que no se reconoce lo dice» (`RN-8`) | servicio | `sin_tipo`, `sin_molde` y `molde_perdido`, separados | ✅ | CP-005 |
| «Mirar no modifica nada» (`RN-5` de la HU) | servicio | El módulo solo lee | ✅ | CP-006 |
| «Se lee el molde cuando se pide» (§12) | servicio | `texto_del_molde` | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El módulo registrado, y la tabla de moldes con los cinco casos que no son directos |
| T-03 · T-04 | Las tres clases, y la línea y el contexto de cada hueco |
| T-05 · T-06 | `que_le_falta`, con las cuentas aparte, y la orden de consola |
| T-07 | **26 pruebas** |
| T-08 | **Medido: 54 documentos y 77 huecos**, y comparado con el expediente |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/` | 26 pruebas, en verde |
| La batería de la plataforma completa | 278 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La medición sobre los documentos reales | 54 documentos, 77 huecos |

**Lo que las pruebas no dicen:** si la lista sirve para llenar. Eso lo dice la `HU-002`.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py que_le_falta <identificador>
python manage.py que_le_falta <identificador> --documento documentacion/x/plan_trabajo.md
python manage.py que_le_falta <identificador> --documento <ruta> --posibles
```

Sin `--documento` sale la lista del proyecto entero, del que más le falta al que menos. **Los completos no salen:** la lista es de trabajo por hacer.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Solo `«…»` entra en la cuenta** | Medido antes de construir: de 341 marcas en las 130 historias reales, ninguna era un hueco con nombre sin llenar |
| **El posible se lista aparte, no se descarta** | Cuando `F-011` cree documentos desde el molde, el documento será el molde y entonces sí serán ciertos |
| **Una marca dentro de un bloque cercado no se cuenta** | Ahí se escribe para que se vea. Es la única diferencia con la cuenta del expediente, y esta fase la corrige |
| **La tabla de moldes se declara** | Tres moldes viven fuera de la carpeta del ciclo y dos tipos no tienen. Deducirla fallaría en cinco de 19 |
| **El molde se lee cuando se pide** | Copiado dentro del módulo, envejece en cuanto el estándar cambie el original |
| **Tres razones separadas para no tener molde** | Tipo desconocido, tipo sin molde y molde ilegible se arreglan distinto |
| **Cada hueco lleva su contexto y no solo su línea** | La `HU-002` va a escribir ahí, y la posición sola no dice si el documento se movió |

Señal registrada: [`S-104`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **24 documentos con huecos que el expediente nunca mostró**, todos índices. Aparecieron al comparar las dos cuentas. Llenarlos es trabajo de la `HU-002`.
- **Sin pantalla**, como las fases anteriores de Medición y Expediente.
- **La cuenta vale para lo traído**, que refleja la importación del 2026-08-25. Es la misma deuda que dejó el Expediente.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-104` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-013` |

El módulo Ciclo de vida ya estaba en el catálogo de [cvds/diseno/README.md](../../../../../cvds/diseno/README.md) §3, con sus requisitos `RF-11` a `RF-14`.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** Una aplicación más en la lista, y un ajuste que dice dónde viven los moldes.
