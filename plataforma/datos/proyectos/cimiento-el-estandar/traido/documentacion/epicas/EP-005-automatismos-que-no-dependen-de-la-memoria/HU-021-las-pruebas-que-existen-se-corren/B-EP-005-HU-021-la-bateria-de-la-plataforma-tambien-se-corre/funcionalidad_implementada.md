# Funcionalidad implementada — Fase `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` (módulo Pruebas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` |
| **Épica / HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) · [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md) |
| **Módulo** | Pruebas |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**Este repositorio ya no tiene ninguna batería que nada ejecute.** La orden que corre las pruebas del estándar corre también las 187 de la plataforma, y dice las dos cifras por separado.

Y los tres silencios quedaron distinguidos: **no tener plataforma** se avisa, **tenerla y no correr nada** es rojo, y **correrla y fallar** dice cuántas y por dónde ir a verlo.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| CA | Qué lo cumple | Dónde | Evidencia |
|---|---|---|---|
| [CA-01](../HU-021-las-pruebas-que-existen-se-corren.md#ca-01--la-carpeta-se-corre-con-una-orden-y-es-la-documentada) | `correr_la_plataforma`, y su entrada en `validar` | `validadores/corredor.py` | CP-001, CP-004 |
| [CA-02](../HU-021-las-pruebas-que-existen-se-corren.md#ca-02--cero-pruebas-no-pasa-por-verde) | Cero es falla; no tenerla es aviso | `correr_la_plataforma` | CP-002, CP-003 |
| [CA-03](../HU-021-las-pruebas-que-existen-se-corren.md#ca-03--se-puede-pedir-un-subconjunto) | La otra batería solo entra en la corrida entera | `validar` | CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El corredor de la otra batería y su cifra en el resumen |
| T-03 | Los tres silencios, cada uno con su severidad |
| T-04 | El subconjunto sigue costando lo mismo |
| T-05 · T-06 | 9 pruebas, y el sabotaje cazado |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `test_la_bateria_de_la_plataforma_se_corre.py` | 9 pruebas, en verde |
| Sabotaje: una prueba de la plataforma en rojo | **Se caza** |
| La corrida completa del estándar | Las dos cifras a la vista |

**Lo que las pruebas no dicen:** qué pasa si la plataforma cambia de marco. Lo que se lee es la línea que su corredor imprime al terminar.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

```
python validadores/validar.py internas              # las dos baterías
python validadores/validar.py internas --solo X.py  # solo lo que la fase toca
```

La segunda es la del día a día, y **sigue costando lo mismo que antes**: la batería de la plataforma no entra ahí.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| Se le pide **por su punto de entrada** | Su marco arma la base de prueba y descubre las aplicaciones; cargar sus archivos a mano daría otro número |
| **No tener plataforma es aviso, no falla** | Cada proyecto que hereda está en ese caso, y un rojo permanente se apaga |
| Las dos cifras, aparte | Un total escondería cuál de las dos se cayó |
| La otra batería solo en la corrida entera | Arrastrar 187 pruebas ajenas volvería un peaje la orden que `02·F5` obliga a usar en cada fase |
| Se acepta que corra **dos veces** en la corrida completa | Una es el producto y otra su prueba de integración. Medio minuto sobre diez, y esconderlo dejaría la integración sin prueba propia |

Señales registradas: [`S-097`](../../../../senales.md) y [`S-098`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Ninguno.** Lo que queda dicho es que la línea que se lee es la de un marco concreto.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/senales.md](../../../../senales.md) | `S-098` |

No se creó módulo nuevo ni cambió ninguna ruta.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: el estándar no se despliega. Un proyecto que hereda recibe un aviso nuevo que dice que no tiene plataforma, y eso no le rompe nada.
