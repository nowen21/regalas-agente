# Funcionalidad implementada — Fase `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-023](../HU-023-un-rojo-se-puede-cerrar-declarandolo.md): `CA-01` a `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.5.0` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `b3df9f1` |

---

## 1. Qué se implementó — resumen

**Un rojo no tenía forma de cerrarse.** Se descubrió haciéndolo: dos fases verificaron criterios en rojo, midieron que hoy se cumplen, cerraron con «Cumple», **y el número no se movió**.

Ahora una fase puede **declarar qué veredicto anterior deja atrás**, y la cuenta lo lee.

| Antes | Ahora |
|---|---|
| `66 cumplen, 16 no cumplen` | `68 cumplen, 14 no cumplen` |

**Se movieron exactamente dos**, que son las dos que volvieron a verificar. **Las otras catorce siguen contando**, incluidas seis que tienen fase posterior y **no resolvieron su rojo**.

**Se declara, no se deduce del orden**, y eso lo decidió una medición hecha **antes** de diseñar: de las 16 historias con un rojo, ocho tenían fase posterior y **solo dos habían vuelto a verificar**. Deducirlo habría dado por cumplidas seis con el rojo intacto.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` la fase declara qué veredicto deja atrás | documento | El campo del molde `11` | ✅ | CP-001 |
| `RN-02` solo vale si quien declara cumple | servicio | `veredictos_reemplazados` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-002, sabotaje 2 |
| `RN-03` se declara, no se deduce del orden | servicio | Nada mira el orden | ✅ | CP-003, sabotaje 1 |
| `RN-04` solo una fase de la misma historia | servicio | `nombrada in fases` | ✅ | CP-004, sabotaje 4 |
| `RN-05` el veredicto reemplazado no se borra | servicio | Solo se filtra la lista; no se escribe nada | ✅ | CP-005 |
| `RN-06` un nombre que no resuelve avisa | servicio | `reemplazos_que_no_resuelven` | ✅ | CP-004, sabotaje 5 |
| `RN-07` el programa avisa, no corrige | servicio | Solo lee | ✅ | CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-00 · impacto sobre el molde y sus pruebas | ✅ | Ninguna exige la lista de campos |
| T-01 · el campo, opcional | ✅ | CP-000, y una prueba que exige que diga «Opcional» |
| T-02 · leerlo del cierre | ✅ | CP-001 |
| T-03 · las tres condiciones | ✅ | CP-002, CP-004 |
| T-04 · avisar cuando no resuelve | ✅ | CP-004 |
| T-05 · los cinco CA | ✅ | 18 pruebas |
| T-06 · **con cero declaraciones, la línea idéntica** | ✅ | CP-006 |
| T-07 · declararlo en los dos que verificaron | ✅ | Los dos cierres |
| T-08 · medir y nombrar las que se mueven | ✅ | **Exactamente dos** |
| T-09 · `CHANGELOG` y `VERSION` | ✅ | `35.5.0` |
| T-10 · sabotear | ✅ | Cinco; tres pasaron en verde y obligaron a un segundo ciclo |

**Correspondencia:** 11 tareas, 11 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 2 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **484 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` a `DEF-03` corregidos |

**Los tres defectos son de las pruebas, ninguno del código.** Y el principal es el mismo que se escribió como señal **horas antes, el mismo día**: tres pruebas que **no podían fallar** porque miraban la cuenta, donde el resultado coincide.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En el documento de cierre de una fase, una fila:

```
| **Reemplaza el veredicto de** | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
```

**Solo se escribe si esta fase verificó ese criterio**, y solo vale si esta fase cumple. Si el nombre no encaja, `validar.py fases` lo avisa **con el nombre escrito** y no cierra nada.

- **Desde el código:** `fases.veredictos_reemplazados(ruta_hu, fases)` da el conjunto que la cuenta deja fuera.
- **`por_veredicto` no cambió de firma.**

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| Se **declara**, no se deduce del orden | Medido: de ocho candidatas, **seis no resolvieron el rojo**. Deducirlo las daría por cumplidas | `S-065` |
| Solo vale si **quien declara cumple** | Un rojo se taparía con otro rojo | `RN-02` |
| Solo una fase **de la misma historia** | Un rojo ajeno no es de nadie, y abriría cerrarlo desde donde no se verificó | `RN-04` |
| Un nombre que no resuelve **avisa** | Un campo mal escrito que no dice nada es peor que no tenerlo: parece que funcionó | `RN-06` |
| El campo va en el **cierre**, no en el resultado | El resultado dice qué pasó **en esta fase**; el reemplazo es una afirmación **sobre otra**. Y el cierre es el documento que la cuenta ya abre | El plan §2.6 |
| El campo es **opcional** | Obligar a escribir «ninguna» en 130 fases para que dos digan algo es ruido | `CP-000` |
| **El veredicto reemplazado no se toca** | El rastro de que estuvo en rojo es la información | `20·M11` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Las catorce historias que siguen en rojo** | **Abiertas, y ahora con salida.** Ocho no tienen fase posterior; seis la tienen y no resolvieron el rojo. Cada una es trabajo propio |
| Nadie **vuelve a mirar** un rojo por su cuenta | **Abierta.** Es `S-061`: esto da la forma de cerrarlo, no el recordatorio de revisarlo |
| Los guiones de sabotaje guardan su copia fuera del repositorio | **Abierta**, y ahora **el enganche de la `HU-018` la avisa** |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la `HU-023` en sus dos tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] La señal `S-065`.
- [x] El molde [`11-funcionalidad-implementada.md`](../../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md).
- [x] `VERSION` en `35.5.0` y su entrada en el `CHANGELOG`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** **ningún número se le mueve**, porque nadie tiene el campo escrito. Lo que gana es la posibilidad de cerrar un rojo cuando lo arregle.
- **Reversión:** se descarta el commit y se baja `VERSION`. **El campo declarado en los dos cierres queda inerte, no roto**: sin el código que lo lee, es una fila más de una tabla.
