# Funcionalidad implementada — Fase `S-EP-019-HU-001-el-nombre-sale-del-identificador` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-abrir-una-fase-con-sus-documentos.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `S-EP-019-HU-001-el-nombre-sale-del-identificador` |
| **Épica / HU** | [EP-019](../../epica.md) · [HU-001](../HU-001-abrir-una-fase-con-sus-documentos.md) |
| **Módulo** | Ciclo de vida |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Una fase se abre con sus cinco documentos, tomados del molde del estándar, y con el nombre armado desde el identificador.**

Lo que más cuidado costó no fue crear: fue **negarse**. Sin la historia no se abre, porque una fase suelta es trabajo que nadie pidió; y sobre una carpeta que ya existe no se escribe nada, porque puede tener trabajo adentro y eso no se recupera.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El nombre sale del identificador» (`RN-1`) | servicio | `nombre_de_fase` en [plataforma/nucleo/ciclo_de_vida/apertura.py](../../../../../plataforma/nucleo/ciclo_de_vida/apertura.py) | ✅ | CP-003 |
| «Sin historia no se abre» (`RN-2`) | servicio | `donde_iria` | ✅ | CP-001 |
| «Los cinco con el molde» (`RN-3`) | servicio | `LOS_CINCO` y `_texto_inicial` | ✅ | CP-002 |
| «Si existe, no se toca» (`RN-4`) | servicio | `abrir_fase` | ✅ | CP-002 |
| «Abrir queda registrado» (`RN-5`) | servicio | `con_constancia` | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El nombre armado, y la carpeta de la historia hallada por su prefijo |
| T-03 · T-04 | Los cinco documentos desde el molde, y la negativa a tocar lo que existe |
| T-05 · T-06 | La orden de consola, y **12 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/` | 12 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si los moldes son cómodos de llenar.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py abrir_fase <proyecto> S EP-019 HU-001 "de qué trata"
python manage.py abrir_fase <proyecto> S EP-019 HU-001 "de qué trata" --donde-iria
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El nombre se arma, no se recibe** | Escribirlo a mano es de donde salen las fases que no se sabe de dónde cuelgan |
| **Sin historia no se abre** | `02·F0`: cada eslabón cuelga del anterior |
| **Si la carpeta existe, no se toca** | Es el único daño irreparable de este módulo |
| **El molde se lee al abrir** | Uno copiado envejece en cuanto el estándar cambie el original |
| **Las tildes se bajan en el nombre** | Un nombre de carpeta con tilde se rompe distinto en cada sistema |

Señal registrada: [`S-114`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Épicas e historias siguen abriéndose a mano.** Se abren una vez cada varias semanas; la fase es la que se repite.
- **Los moldes reales son largos**, y eso no lo mide ninguna prueba.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Su §13 nombra esta fase |
| [documentacion/epicas/README.md](../../../README.md) | `EP-019` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
