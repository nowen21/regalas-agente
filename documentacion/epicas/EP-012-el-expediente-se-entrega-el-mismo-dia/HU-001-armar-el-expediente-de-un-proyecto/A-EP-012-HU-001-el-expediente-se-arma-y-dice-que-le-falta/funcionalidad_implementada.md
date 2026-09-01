# Funcionalidad implementada — Fase `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` (módulo Expediente)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` |
| **Épica / HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) · [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md) |
| **Módulo** | Expediente |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**El expediente de un proyecto se arma al pedirlo**, en el orden del ciclo. Sobre este repositorio: **762 documentos en ocho grupos**, de planificación a registros de versión.

Y dice en qué estado está, que es lo que armarlo a mano nunca dijo:

| | Cuántos |
|---|---|
| Falta | **22**, todos el documento de cierre de una fase |
| A medio llenar | **31** |
| No encaja en ningún grupo | 0 |

Los 22 son un hallazgo sobre el propio repositorio: veintidós fases de retro-documentación nunca escribieron su `funcionalidad implementada`, y nadie lo había visto.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se agrupan por el orden de la §5.1» (§6) | servicio | `armar` en [plataforma/nucleo/expediente/core.py](../../../../../plataforma/nucleo/expediente/core.py) | ✅ | CP-001 |
| El orden del ciclo, tipo por tipo (§5.1) | servicio | [plataforma/nucleo/expediente/orden.py](../../../../../plataforma/nucleo/expediente/orden.py) | ✅ | CP-001 |
| «Lo que falta, con su nombre» (§6) | servicio | `_lo_que_falta` | ✅ | CP-002 |
| «Lo incompleto, con cuántas» (§6) | servicio | `_lo_incompleto` y `huecos_de` | ✅ | CP-003 |
| «Lo que no encaja» (§6) | servicio | `armar` | ✅ | CP-004 |
| «`RN-4` la auditoría y la memoria no entran» (§4) | servicio | `orden.FUERA` | ✅ | CP-004 |
| «Recortar por alcance dice qué quedó fuera» (§4, `RN-7`) | servicio | `armar(hasta=…)` | ✅ | CP-005 |
| «`RN-5` armar no modifica ningún documento» (§4) | servicio | El módulo solo lee | ✅ | CP-006 |
| «El expediente se calcula al pedirlo» (§5) | modelo | **No hay modelo ni migración** | ✅ | Por construcción |
| Pantalla (§7) | vista | — | **no aplica** | La §7 lo permite |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-00 | La línea base: 1 002 documentos traídos |
| T-01 · T-02 | El orden declarado, y el expediente agrupado con él |
| T-03 a T-07 | Las cuatro listas: falta, incompleto, no encaja, fuera del alcance |
| T-08 · T-09 · T-10 | La orden, 20 pruebas, y la corrida sobre lo real |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/expediente/tests.py` | 20 pruebas, en verde |
| La batería de la plataforma completa | 232 pruebas, en verde |
| La batería interna del estándar | Sin fallas |

**Lo que las pruebas no dicen:** si lo traído está al día. El expediente refleja lo que Importación trajo el 25 de agosto, no lo que el proyecto tiene hoy.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py armar_expediente <identificador>
python manage.py armar_expediente <identificador> --detalle
python manage.py armar_expediente <identificador> --hasta A-EP-001-HU-003-lo-que-sea
```

**Las cuatro listas salen siempre**, aunque estén vacías: un silencio no distingue «no falta nada» de «no se miró».

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El orden vive en su propio archivo** | Es lo que hay que abrir el día que aparezca un tipo nuevo |
| **El orden también rige dentro del grupo** | Por nombre de archivo, los cinco de una fase salen al revés: el cierre antes que el plan |
| **Un hueco es la marca de la casa, no unas comillas** | Contando las comillas, 559 documentos salían incompletos donde hay 31 |
| **Lo que falta se calcula contra lo que el ciclo espera** | Una lista escrita al lado envejece con el proyecto |
| **La memoria se excluye por tipo, no por ruta** | La ruta cambia entre proyectos; el tipo lo asigna Importación |
| **Lo excluido no se reporta como «no encaja»** | Se excluye a propósito; ponerlo ahí lo haría ver como un defecto |
| Sin modelo y sin migración | El expediente se calcula: guardarlo sería una segunda verdad |

Señal registrada: [`S-101`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Lo traído puede estar viejo.** Armar el expediente sobre una importación de hace días da un retrato de hace días, y el módulo no lo advierte. Es una mejora natural para la fase siguiente.
- **Algunos «a medio llenar» son documentos que hablan de la marca.** Distinguirlos exige leer.
- **Sin pantalla**, permitido por la especificación.
- **Los 22 faltantes son deuda del repositorio**, no del módulo: veintidós fases sin su documento de cierre.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/expediente/spec.md](../../../../expediente/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-101` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración**: el módulo no guarda nada. Basta con que la aplicación esté en la lista.
