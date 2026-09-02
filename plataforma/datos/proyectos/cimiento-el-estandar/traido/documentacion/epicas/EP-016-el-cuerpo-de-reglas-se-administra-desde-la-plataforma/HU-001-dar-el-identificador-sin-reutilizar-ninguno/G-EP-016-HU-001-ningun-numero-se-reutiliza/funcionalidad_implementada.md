# Funcionalidad implementada — Fase `G-EP-016-HU-001-ningun-numero-se-reutiliza` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-dar-el-identificador-sin-reutilizar-ninguno.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `G-EP-016-HU-001-ningun-numero-se-reutiliza` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-001](../HU-001-dar-el-identificador-sin-reutilizar-ninguno.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**Cada regla nueva recibe un identificador que nadie tuvo antes.** Se cuentan las vigentes y **las derogadas**, y el siguiente es el que sigue al mayor: rellenar huecos es la única forma de reutilizar un número sin darse cuenta.

Sobre este repositorio: **257 reglas en 24 capítulos, 9 derogadas, y ningún hueco de numeración**.

**Es el cuarto puente de la plataforma hacia el estándar**, después del que tapa credenciales, el que parte una conversación en turnos y el que corre las comprobaciones. **Ya no es una excepción: es la forma.**

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El siguiente es el que sigue al mayor» (`RN-1`) | servicio | `siguiente_libre` en [plataforma/nucleo/reglas/numeracion.py](../../../../../plataforma/nucleo/reglas/numeracion.py) | ✅ | CP-002 |
| «Las derogadas cuentan» (`RN-2`) | servicio | `usados` | ✅ | CP-004 |
| «Se comprueba antes de guardar» (`RN-3`) | servicio | `comprobar_libre` | ✅ | CP-003 |
| «El lector no se duplica» (`RN-4`) | servicio | [plataforma/nucleo/reglas/catalogo.py](../../../../../plataforma/nucleo/reglas/catalogo.py) | ✅ | Por construcción |
| «Sin lector se revienta» (§4) | servicio | `NoHayCuerpoDeReglas` | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El puente, y los usados con las derogadas adentro |
| T-03 · T-04 | El siguiente libre, y la comprobación previa |
| T-05 | Los huecos, para mirar y no para usar |
| T-06 · T-07 | La orden de consola, y 15 pruebas |
| T-08 | **257 reglas, 24 capítulos, cero huecos** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests.py` | 15 pruebas, en verde |
| La batería de la plataforma completa | 382 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La corrida sobre este repositorio | 257 reglas, cero huecos |

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py reglas <identificador>
python manage.py reglas <identificador> --prefijo M
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El lector de reglas se usa por un puente** | Dos lectores se separan, y uno va a leer mal sin avisar |
| **El siguiente es el que sigue al mayor** | Rellenar huecos es la única forma de reutilizar un número sin darse cuenta |
| **Las derogadas cuentan** | Su identificador sigue citado en documentos de hace años |
| **Sin lector se revienta** | Una lista vacía se leería como «no hay reglas», y el siguiente sería el uno |
| **Un identificador con punto no consume número** | `F12.1` es parte de `F12`, no una regla aparte |

Señal registrada: [`S-109`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **Los huecos se muestran y no se usan.** Si algún día hiciera falta reutilizar uno, tendría que ser una decisión escrita, no un descuido.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | Nace: módulo nuevo |
| [documentacion/senales.md](../../../../senales.md) | `S-109` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-016` |

El módulo Reglas ya estaba en el catálogo de [cvds/diseno/README.md](../../../../../cvds/diseno/README.md) §3, con sus requisitos `RF-05` a `RF-10`.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
