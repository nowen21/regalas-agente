# Funcionalidad implementada — Fase `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-003](../HU-003-impedir-avanzar-sin-la-puerta-cumplida.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` |
| **Épica / HU** | [EP-019](../../epica.md) · [HU-003](../HU-003-impedir-avanzar-sin-la-puerta-cumplida.md) |
| **Módulo** | Ciclo de vida |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Una fase no pasa a la estación siguiente sin lo que esa puerta exige, y el rechazo dice cuál falta.**

**Son tres puertas y no trece**, y eso es lo que la fase decidió. La ficha advertía que *una puerta que estorba se termina saltando*: comprobar las trece habría hecho que se saltaran todas. Se comprueban las que dejan daño —código sin plan aprobado, cierre sin veredicto, publicación sin commit— y las otras diez se marcan a mano.

**Y no es un candado**, y así queda escrito. Cualquiera puede escribir el archivo a mano. Lo que se logra es que saltarse la puerta sea un acto deliberado en vez de un olvido.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Sin plan aprobado no se ejecuta» (`RN-1`) | servicio | `LAS_QUE_SE_COMPRUEBAN` en [plataforma/nucleo/ciclo_de_vida/puertas.py](../../../../../plataforma/nucleo/ciclo_de_vida/puertas.py) | ✅ | CP-006 |
| «Sin veredicto no se cierra» (`RN-2`) | servicio | `veredicto_de` | ✅ | CP-006 |
| «Sin commit no se publica» (`RN-3`) | servicio | `se_puede_pasar` | ✅ | CP-006 |
| «El rechazo nombra la puerta» (`RN-4`) | servicio | El motivo de `se_puede_pasar` | ✅ | CP-006 |
| «La que no se comprueba lo dice» (`RN-5`) | servicio | `se_puede_pasar` | ✅ | CP-006 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Las tres puertas, y el veredicto de las pruebas |
| T-03 · T-04 | El motivo siempre, y la orden de consola |
| T-05 | **7 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/` | 7 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si lo marcado es cierto, ni nada sobre quien se salte la puerta a propósito.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py puerta_de_fase <proyecto>
python manage.py puerta_de_fase <proyecto> --fase D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Tres puertas, no trece** | Una puerta que estorba se salta, y con ella todas |
| **El motivo va también en el sí** | Quien lee un sí tiene que poder comprobarlo |
| **La estación sin puerta comprobable lo dice** | Un sí callado se lee como «lo comprobé» |
| **Se declara que no es un candado** | Una ayuda que se presenta como garantía hace que la gente deje de mirar |

Señal registrada: [`S-114`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **No impide de verdad**, y así se declara.
- **Las otras diez estaciones no se comprueban**, a propósito.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Su §13 nombra esta fase, y con ella cierra `EP-019` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
