# Funcionalidad implementada — Fase `L-EP-016-HU-006-el-aviso-dice-que-cambio` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-006](../HU-006-avisar-al-proyecto-que-quedo-atras.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `L-EP-016-HU-006-el-aviso-dice-que-cambio` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-006](../HU-006-avisar-al-proyecto-que-quedo-atras.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**El aviso de desfase ya dice qué cambió.** Cuántas versiones pasaron, **cuáles obligan a migrar**, y de qué se trataban. Antes decía solo que había desfase, que no ayuda a decidir.

**Y destapó un aviso que llevaba 54 versiones saliendo vacío.** El lector del registro reconocía **143 de 197** entradas, y la más reciente que entendía era la **34.2.0**: una convención cambió y el lector se quedó atrás. Ahora reconoce 162, y la más reciente es la del día.

**Ninguna de las 197 entradas se reescribió.** El que se adapta es el que lee.

**Y hay una tercera respuesta que antes no existía:** un número que nunca se publicó se dice como lo que es, no como ir adelantado.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El aviso dice qué cambió» (`RN-1`) | servicio | `revisar` en [plataforma/nucleo/reglas/desfase.py](../../../../../plataforma/nucleo/reglas/desfase.py) | ✅ | CP-004 |
| «Lo primero es si alguna obliga a migrar» (`RN-2`) | servicio | El campo `obligan` | ✅ | CP-004 |
| «Un número que no existe se dice» (`RN-3`) | servicio | `existe` | ✅ | CP-005 |
| «No declarar nada no es declarar algo falso» (`RN-4`) | servicio | Lo vacío pasa la comprobación | ✅ | CP-005 |
| El lector acepta los dos órdenes | estándar | `_ENTRADA_CON_TIPO` en [validadores/version.py](../../../../../validadores/version.py) | ✅ | §1 del resultado |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | **La medición que explica la fase**: 143 de 197 |
| T-02 · T-03 | El lector con los dos órdenes, versionado como **PARCHE 37.2.1** |
| T-04 a T-06 | Las tres respuestas, y cuáles obligan a migrar |
| T-07 · T-08 | La orden, y 5 pruebas |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests_entrega.py` | 5 pruebas del desfase, en verde |
| La batería de la plataforma completa | 426 pruebas, en verde |
| **La batería del estándar** | 733 pruebas, en verde: importa más que nunca: se tocó el estándar |

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py desfase <proyecto>
python manage.py desfase <proyecto> --cuantas 20
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El lector acepta los dos órdenes** | Reescribir 54 entradas para que un programa las entienda es al revés |
| **La corrección se versiona como PARCHE** | `20·M10` lo exige, y no cambia qué se le pide a nadie |
| **Tres respuestas, no dos** | Un número inventado no cabe en «al día» ni en «atrasado» |
| **Lo primero es cuáles obligan a migrar** | Es lo único del aviso que cambia qué hacer |
| **La medición fue lo primero** | Sin ella, el arreglo no se ve |

Señal registrada: [`S-110`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **35 entradas del registro siguen sin reconocerse**, todas viejas y escritas de otras formas. Están declaradas: no afectan el tramo de nadie que esté al día.
- **Enchufarlo al aviso que ya da el módulo Proyectos** no está: hoy es una orden aparte.
- **Sin pantalla**, como el resto del módulo.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | Su §13 nombra esta fase |
| [CHANGELOG.md](../../../../../CHANGELOG.md) · [VERSION](../../../../../VERSION) | La 37.2.1, con qué cambió |
| [documentacion/senales.md](../../../../senales.md) | `S-110` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** El estándar sube a **37.2.1**, y un proyecto al día no tiene que hacer nada.
