# Resultado de Pruebas — Fase `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 1. Los cuatro sabotajes cazados al primer intento |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las tres formas se leen, ninguna de más, y las siete historias que se contaban mal se movieron — exactamente siete, comprobado contra el conjunto real y no contra el número que mostraba la línea.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 4 de 4 | 4 de 4 |
| Formas leídas | 3 de 3 | 3 de 3 |
| Veredictos leídos donde no los hay | 0 | **0** |
| Pruebas de la fase `A` que hubo que tocar | 0 | **0** |
| Bajada de las «no dicen» | exactamente 7 | **7** |
| Sabotajes cazados | Todos | **4 de 4, al primer intento** |
| Fallas en la suite completa | 0 | 0, sobre **425 pruebas** |

---

## 3. Resultado por caso

### CP-001 — Las tres formas se leen

| Forma | Antes | Ahora |
|---|---|---|
| `**Concepto:** Cumple` (67 fases) | Se leía | Se lee |
| Tabla con `\| **Concepto** \|` (16 fases) | Se leía | Se lee |
| **`**Cumple.**` bajo el encabezado (7 fases)** | **No se leía** | **Se lee** |

Y las tres, también para `No cumple`.

### CP-002 — El lector no lee de más

| Lo que se le puso delante | Qué hizo |
|---|---|
| Tabla de criterios que dice `Cumple` en cada fila, **sin encabezado de veredicto** | **No lo leyó** |
| Encabezado de veredicto con nada debajo | No lo leyó |
| La palabra en prosa, lejos del encabezado | No lo leyó |
| Resultado vacío | No lo leyó, y no reventó |

**El primero es el que importa.** Sin exigir el encabezado, el lector habría tomado la primera fila de criterios por el veredicto de la fase — y **daría por cumplida una que no lo está**, que miente en la dirección peor.

### CP-003 — Lo de antes no se rompió

Las **14 pruebas** de la fase `A` pasan **sin haberlas tocado**, y `veredicto_de` y `por_veredicto` conservan su firma.

### CP-004 — El número, y por qué no bajó lo que parecía

| Momento | «No dicen si cumplen» |
|---|---|
| Cuando se midió, antes de abrir esta fase | 22 |
| **Después de abrir esta fase** | **23** |
| Después del arreglo | **16** |

**23 − 7 = 16.** Bajaron exactamente siete, que es lo que el plan exigía.

**La línea, antes y después:**

| Antes | Ahora |
|---|---|
| `52 cumplen, 11 no cumplen, 22 no dicen` | `56 cumplen, 13 no cumplen, 16 no dicen` |

**Y el total y las terminadas no se movieron**, que es lo que separa lo arreglado de lo que se pudo romper: esta fase cambia **quién sabe leer**, no cuánto trabajo hay.

**Y al cerrar esta misma fase la línea volvió a moverse**, a `57 cumplen, 13 no cumplen y 15 no dicen`: la `HU-021` pasó de «no dice» a «cumple» porque ya tiene su veredicto escrito. **Es el mismo efecto del §4.2, ahora en la dirección buena** — y confirma que lo que movía el número era la propia fase, no el lector.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Cuatro, restaurados **con copia**. **Los cuatro cazados al primer intento**, que es la primera vez en la jornada.

| # | Qué se rompió | Resultado |
|---|---|---|
| 1 | La tercera forma vuelve a no leerse | Cazado (2 pruebas) |
| 2 | El lector se afloja y no exige el encabezado | Cazado (2) |
| 3 | Se pierde la forma vieja al agregar la nueva | Cazado (7) |
| 4 | Toma el primer grupo aunque esté vacío | Cazado (1) |

**El 3 es el que más pruebas rompe**, y es el riesgo real de este tipo de arreglo: ampliar un lector suele hacerse **reemplazando** en vez de sumando.

### 4.2 El criterio de suspensión se activó, y se investigó en vez de seguir

El plan decía: **si las «no dicen» no bajan en siete exactamente, se para.** Bajaron **seis** según la línea, así que se paró.

La causa no era el arreglo: **la base de medición se había movido.** Al levantar esta fase con el andamio, sus cinco documentos vacíos volvieron a meter la `HU-021` en «no dicen» — porque la fase `B` todavía no tenía veredicto.

**La fase creada para arreglar el problema volvió a provocarlo**, y eso es `S-053` por tercera vez en el día.

Se recontó el conjunto real con el lector viejo: eran **23**, no 22. Y con el nuevo, **16**. **Siete exactamente.**

**Si el criterio no hubiera estado escrito**, la diferencia de uno se habría atribuido a un redondeo o a un error de mi cuenta anterior, y no se habría entendido nada.

### 4.3 Rastros

Ninguno. Los cuatro sabotajes editan un archivo que se restaura con copia, y las pruebas escriben solo en carpeta temporal.

### 4.4 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

**Ninguno propio.**

---

## 6. Evidencias

- `_VEREDICTO_BAJO_TITULO` en `validadores/fases.py`, con su porqué
- Ocho pruebas nuevas en `LaCuentaMiraElVeredicto`: cuatro de formas y cuatro de **no leer de más**
- La línea del inventario, antes y después
