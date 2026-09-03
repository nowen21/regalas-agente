# Funcionalidad implementada — Fase `AB-EP-022-HU-002-el-agente-no-aprueba` (módulo Acceso)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-separar-lo-que-cada-grupo-puede-hacer.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `AB-EP-022-HU-002-el-agente-no-aprueba` |
| **Épica / HU** | [EP-022](../../epica.md) · [HU-002](../HU-002-separar-lo-que-cada-grupo-puede-hacer.md) |
| **Módulo** | Acceso |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Dos grupos —`usuario` y `agente`— con lo que cada uno puede hacer, y el agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas.**

**Son dos y no cuatro, y eso es lo que la fase decidió.** El análisis define cuatro actores, pero dos no entran: «un proyecto administrado» es una carpeta que se observa, y «quien recibe un proyecto» tiene escrito que no puede entrar. Construir cuatro grupos habría dejado dos sin usar.

**Y `aprobar --quien` dejó de aceptar cualquier texto.** Ese era el mismo hueco que `EP-017` vino a tapar en los documentos, un nivel más abajo: una aprobación decía quién la dio **y no lo probaba**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Dos grupos» (`RN-1`) | servicio | `poner_al_dia` en [plataforma/nucleo/acceso/grupos.py](../../../../../plataforma/nucleo/acceso/grupos.py) | ✅ | CP-003 |
| «El agente no puede las cuatro» (`RN-2`) | servicio | `SOLO_DEL_USUARIO` | ✅ | CP-003 |
| «El usuario puede todo» (`RN-3`) | servicio | `poner_al_dia` | ✅ | CP-003 |
| «Solo una cuenta que exista» (`RN-4`) | servicio | `cuenta` en `core.py` | ✅ | CP-004 |
| «El rechazo dice el porqué» (`RN-5`) | servicio | `exigir` y `por_que_no` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Los dos grupos, y la pregunta de si una cuenta puede |
| T-03 · T-04 | El rechazo con su porqué, y `aprobar` exigiendo cuenta |
| T-05 · T-06 | Las 17 pruebas de aprobaciones al día, y **10 pruebas nuevas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/acceso/` | 10 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 610 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** nada sobre quien pueda editar la base o el código.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py aprobar <proyecto> <documento> --quien jose
python manage.py crear_cuenta el-agente --grupo agente
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Dos grupos, no cuatro** | Dos de los cuatro actores no entran |
| **El agente no aprueba** | `00·N1`: la aprobación es de una persona |
| **El porqué vive con el permiso** | Copiado en dos lados, un día dice dos cosas |
| **Los permisos cuelgan del modelo de Proyecto** | Django exige colgarlos de alguno, y ese es sobre el que se actúa |
| **El superusuario puede sin grupo** | Es la cuenta de rescate de la máquina |

Señal registrada: [`S-125`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **No hay permisos por proyecto:** un grupo rige en toda la plataforma.
- **Quien pueda editar la base puede darse cualquier permiso.** Lo que se logra es que saltárselo sea deliberado.
- **Lo registrado antes de que hubiera cuentas no se reescribe.**

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/acceso/spec.md](../../../../acceso/spec.md) | Su §13 nombra esta fase, y con ella cierra `EP-022` |
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | `quien` deja de ser texto libre |
| [pendientes/94-el-control-de-acceso-esta-definido-y-no-construido.md](../../../../../pendientes/94-el-control-de-acceso-esta-definido-y-no-construido.md) | Cerrado |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
