# Funcionalidad implementada — Fase `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` (módulo Avisos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-avisar-lo-que-se-desvia.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` |
| **Épica / HU** | [EP-020](../../epica.md) · [HU-001](../HU-001-avisar-lo-que-se-desvia.md) |
| **Módulo** | Avisos |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Lo que se salió de lo acordado sale solo**, en tres clases —fase detenida, historia sin fase, terminado sin comprobar—, ordenado por lo que más duele, y **cada aviso dice qué lo disparó y dónde mirar**.

**El límite lo puso la ficha:** *demasiados avisos se vuelven ruido, y el ruido se ignora completo*. Por eso son tres clases y no quince, y por eso un aviso que no puede decir qué lo disparó **no se emite**.

**Hubo que definir «vencida»**, porque el estándar nunca le puso fecha a una deuda. Acá quiere decir *sin moverse hace más de 30 días*, y sale escrito para que nadie lo lea como un vencimiento acordado.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Todo aviso dice qué y dónde» (`RN-1`) | servicio | `_aviso` en [plataforma/nucleo/avisos/core.py](../../../../../plataforma/nucleo/avisos/core.py) | ✅ | CP-001 |
| «De lo que más duele a lo que menos» (`RN-2`) | servicio | `GRAVEDAD` | ✅ | CP-001 |
| «Lo atendido no vuelve» (`RN-3`) | servicio | `atendidos` | ✅ | CP-002 |
| «Cuando recorta, lo dice» (`RN-4`) | servicio | `se_recorto` | ✅ | CP-003 |
| «La que no dice desde cuándo no se da por vencida» (`RN-5`) | servicio | `fases_detenidas` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 · T-03 | Las tres clases de aviso |
| T-04 · T-05 | El orden por gravedad, y lo callado a propósito |
| T-06 · T-07 | El recorte y el cero dichos, y la orden de consola |
| T-08 | **13 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/avisos/` | 13 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** a partir de cuántos avisos la gente deja de leer la lista.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py avisos <proyecto> --hoy 2026-09-01
python manage.py avisos <proyecto> --hoy 2026-09-01 --dias 60
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Tres clases, no quince** | El ruido se ignora completo, y con él lo que importaba |
| **El aviso que no puede decir su causa no se emite** | Un aviso sin causa obliga a buscarla, y nadie busca |
| **«Vencida» son 30 días, y se declara** | El estándar nunca le puso fecha a una deuda |
| **Lo callado se escribe en el proyecto** | Una decisión que no viaja con el repositorio se pierde al clonarlo |
| **La que no dice desde cuándo no se da por vencida** | No saber tiene su propio nombre |

Señal registrada: [`S-116`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Cuántos avisos son demasiados no se sabe**, y es el modo en que esto fracasa.
- **Los 30 días son un número puesto acá**, no acordado por el estándar.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/avisos/spec.md](../../../../avisos/spec.md) | Nace: módulo nuevo |
| [documentacion/senales.md](../../../../senales.md) | `S-116` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-020` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
