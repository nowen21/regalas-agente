# Funcionalidad implementada — Fase `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-ver-en-que-estacion-va-cada-fase.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` |
| **Épica / HU** | [EP-019](../../epica.md) · [HU-002](../HU-002-ver-en-que-estacion-va-cada-fase.md) |
| **Módulo** | Ciclo de vida |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Las 209 fases del repositorio se leen de una corrida**, y de cada una sale en qué estación va, qué puerta le falta y cuántos días lleva quieta.

**Lo que esta fase enseñó fue a leer.** Tres veces seguidas el lector suponía que todo seguía la convención de hoy, y tres veces los datos reales dijeron que no: hay **dos marcas** de cumplida, hay casillas **con prosa** en vez de marca, y hay **tres modelos** de tabla conviviendo. Ninguna fase cerrada se reescribió.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «La primera sin cumplir» (`RN-1`) | servicio | `de_un_texto` en [plataforma/nucleo/ciclo_de_vida/estaciones.py](../../../../../plataforma/nucleo/ciclo_de_vida/estaciones.py) | ✅ | CP-004 |
| «Manda la tabla» (`RN-2`) | servicio | `coincide` | ✅ | CP-004 |
| «Las dos marcas» (`RN-3`) | servicio | `CUMPLIDAS` | ✅ | CP-007 |
| «Sin marcar no es pendiente» (`RN-4`) | servicio | `_como_quedo` | ✅ | CP-007 |
| «Solo se compara si es de trece» (`RN-5`) | servicio | `comparable` | ✅ | CP-007 |
| «Dice desde cuándo» (`RN-6`) | servicio | `detenida_desde` | ✅ | CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La tabla leída, y las dos marcas reconocidas |
| T-03 · T-04 | «Sin marcar» con su nombre, y la comparación solo entre iguales |
| T-05 · T-06 | Los días quietos, y la orden con su resumen |
| T-07 | **11 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/` | 11 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si las 33 fases que quedan en desacuerdo están mal, ni cuál de las dos versiones tiene razón.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py en_que_va <proyecto>
python manage.py en_que_va <proyecto> --sin-terminar --hoy 2026-09-01
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Manda la tabla sobre la frase** | La tabla se marca al hacer el trabajo; la frase se escribe después |
| **Las dos marcas valen** | Reescribir 76 fases cerradas es peor que reconocer dos marcas |
| **«Sin marcar» tiene su propio nombre** | Decir «pendiente» inventa un estado que el documento no declaró |
| **Solo se compara entre tablas del mismo modelo** | La estación 12 de una tabla de once no existe |
| **La menos avanzada sale primero** | Lo que hay que mirar es lo que lleva más tiempo sin moverse |

Señal registrada: [`S-114`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **33 fases siguen con la frase y la tabla en desacuerdo.** Son reales, y arreglarlas es reescribir fases cerradas.
- **3 fases tienen alguna estación sin marcar**, y así quedan declaradas.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-114` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
