# Funcionalidad implementada — Fase `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-003](../HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` |
| **Épica / HU** | [EP-017](../../epica.md) · [HU-003](../HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md) |
| **Módulo** | Aprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Editar un documento aprobado le quita la aprobación**, se dice cuánto cambió, y **la aprobación anterior no se borra**.

Es la fase que cierra el caso real escrito en la ficha de `F-017`: se aprobaron tres documentos, al día siguiente el cambio de producto los dejó sin valor, y **nada avisó**. Ahora avisa.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Editar caduca la aprobación» (`RN-1`) | servicio | `estado_de` en [plataforma/nucleo/aprobaciones/core.py](../../../../../plataforma/nucleo/aprobaciones/core.py) | ✅ | CP-003 |
| «Se dice cuánto cambió» (`RN-2`) | servicio | `que_cambio` | ✅ | CP-003 |
| «La anterior no se borra» (`RN-3`) | modelo | Cada aprobación se agrega | ✅ | CP-004 |
| «Un documento que ya no está también caduca» (`RN-4`) | servicio | `estado_de` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La comparación de huellas, y la medida del cambio |
| T-03 · T-04 | La historia conservada, y el documento que desapareció |
| T-05 | **6 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/aprobaciones/` | 6 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si el cambio importaba.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py aprobaciones <proyecto>
```

Los documentos cuya aprobación caducó salen con la frase que dice desde cuándo y cuánto cambió.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **La huella decide, no la fecha** | Una fecha cambia al tocar el archivo aunque el texto sea el mismo |
| **Nada se borra al caducar** | Es la historia de qué se autorizó y cuándo |
| **El cambio se mide en caracteres** | El diff lo da el control de versiones; acá alcanza para decidir si mirar |
| **Un documento borrado también caduca** | Una aprobación sobre algo que no está no cubre nada |
| **Un cambio de tipografía caduca** | Se acepta: una aprobación responde por el texto exacto, no por lo que significa |

Señal registrada: [`S-111`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Arreglar una coma caduca la aprobación.** Declarado y aceptado.
- **No se vuelve a aprobar solo.** Caducar avisa; volver a firmar lo hace una persona, que es el punto.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | Su §13 nombra esta fase, y con ella cierra `EP-017` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
