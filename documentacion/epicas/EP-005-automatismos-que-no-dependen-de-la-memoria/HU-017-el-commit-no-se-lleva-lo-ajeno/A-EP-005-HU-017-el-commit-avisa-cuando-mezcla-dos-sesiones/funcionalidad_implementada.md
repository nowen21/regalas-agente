# Funcionalidad implementada — Fase A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el cierre de la fase: **qué quedó hecho, qué se probó, qué se decidió y qué deuda quedó**. El plan dice lo que se iba a hacer; esto dice lo que pasó, para poder comparar los dos.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-017](../HU-017-el-commit-no-se-lleva-lo-ajeno.md) |
| **CA que cierra** | CA-01, CA-02 y CA-03 |
| **Fecha de cierre** | 2026-08-22 |
| **Veredicto** | [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase) |

---

## 1. Qué se implementó — resumen

El enganche anota qué archivo tocó cada sesión, y el `pre-commit` avisa cuando lo que entra al commit lo tocaron dos sesiones distintas. Avisa y deja pasar.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Exigencia | Dónde quedó | Prueba | Evidencia |
|---|---|---|---|
| CA-01 | `sesiones.validar_preparados()` | CP-001 | [resultado_pruebas.md](resultado_pruebas.md) §2 |
| CA-02 | El mensaje del hallazgo, con sus ejemplos | CP-002 | Ídem |
| CA-03 | La vigencia, el filtro de lo preparado y el corte en dos sesiones | CP-003 a CP-007 | Ídem |
| RN-05 | La entrada del `.gitignore` | — | El archivo |

### 2.2 Plan de trabajo → ejecución

Las siete tareas hechas como estaban escritas. Un ajuste que el plan no preveía: el subcomando entraba por defecto en la corrida completa de `validar.py`, y se declaró fuera con su motivo, porque fuera de la hora del commit no tiene nada que mirar.

---

## 3. Qué se probó  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

La suite propia, 10 pruebas, y las tres que dependen de lo que la fase toca: las dos del instalador y la de la corrida completa. Las dos fallas que quedan en esta última son previas a la fase.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Se dispara solo, en el `pre-commit`. A mano:

```
python validadores/validar.py sesiones
```

El registro vive en `historico-chat/.tocado/`, un archivo por sesión, fuera del control de versiones. Borrarlo no rompe nada: lo único que pasa es que el aviso no sale hasta que las sesiones vuelvan a escribir.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)

**No se pregunta de quién es el commit, sino si mezcla.** Averiguar qué sesión lanza el `pre-commit` es imposible: lo lanza `git`, que no sabe nada de sesiones. La pregunta se dio vuelta y el problema desapareció, porque la señal que importa no necesita identidad: un commit legítimo sale de una sola conversación.

**Avisa y deja pasar.** Retomar lo que otra sesión dejó a medias es legítimo, y a veces es justo lo que se quiere. Lo que no es normal es hacerlo sin darse cuenta. Además está medido en el [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md): un enganche que rechaza siempre se apaga en una tarde, y ese es el defecto más caro de esta casa.

**El registro caduca a las doce horas.** Sin caducidad, el registro de la semana pasada haría saltar el aviso en cada commit, y volveríamos al enganche que nadie mira. Doce horas cubre una jornada larga sin alcanzar la del día siguiente.

**Se anota todo lo que se edita, no solo los documentos.** El enganche filtra `.md` para su trabajo de siempre, y la anotación va **antes** de ese filtro: lo que una sesión se llevó por delante la vez que pasó fue un archivo de código a medio corregir.

**El registro no se versiona.** Es estado de trabajo, no memoria. Versionarlo lo convertiría en el próximo archivo que dos sesiones se pisan, que es exactamente el problema que esta fase resuelve.

---

## 6. Deuda técnica y pendientes generados

| Qué queda | Dónde |
|---|---|
| No se pudo probar que el caso real habría avisado: haría falta montar dos sesiones commiteando a la vez | [resultado_pruebas.md](resultado_pruebas.md) §5.1 |
| Los proyectos ya instalados no tienen la línea nueva del `pre-commit` hasta que se corra el instalador | Es el comportamiento normal de cualquier cambio del enganche |

---

## 7. Índices y mapas actualizados

- [HU-017](../HU-017-el-commit-no-se-lleva-lo-ajeno.md), nueva, con su fila de fase.
- [Pendiente 80](../../../../../pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md), cerrado, y su fila en el índice.

---

## 8. Despliegue — si aplica

No aplica más allá de reinstalar el enganche en cada proyecto, que es lo que ya hace el instalador.
