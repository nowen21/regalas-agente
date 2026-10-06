# Funcionalidad implementada · Fase `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista` |
| **Módulo** | Cuerpo de reglas, capítulo `01 · Conducta del agente` |
| **Especificación del módulo** | Los CA de la [HU-036](../HU-036-el-pedido-dice-que-se-espera.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-036 (CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.2.1 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La tabla de las palabras que no tocan nada, en `base/01-conducta/palabras-clave.md`, suma dos: «Liste», que autoriza listar lo que se indique, y «OK», que no autoriza ninguna acción porque es el acuse de recibo de una explicación. Salió la fila cuya palabra era la pregunta entre signos, que el programa leía como un texto literal y por eso nunca coincidía con un mensaje. El sello del checklist de `01·C28` dejó de decir cuántas palabras tiene el anexo.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02, con palabra clave se hace eso y solo eso | Regla | `base/01-conducta/palabras-clave.md`, filas «Liste» y «OK» | Hecho | CP-001, CP-002 |
| CA-03, la palabra que no está en la lista se trata como ausente | Regla | `base/01-conducta/palabras-clave.md`, sale la fila de la pregunta entre signos | Hecho | CP-003 |

**Faltantes / diferimientos:** que la pregunta escrita entre `¿` y `?` cuente como «Pregunta». Se estudió y el usuario lo descartó el 2026-08-31; pide tocar `_FRASE` y los tres métodos que la usan en `recuperar.py`.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Abrir el mensaje con «Liste» para pedir una lista, o con «OK» para decirle al agente que la explicación se entendió, sin pedirle nada más.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La celda de «OK» dice que no autoriza nada | Decía «Se entiende la explicación», que describe al usuario y no el permiso. Leída así, el agente podía tomarla como «Continúe» | Ninguna |
| La fila de la pregunta entre signos sale, en vez de enseñarle la forma al programa | La forma se descartó, y una fila que no coincide con nada ensuciaba el aviso que lista las palabras válidas | Ninguna |
| El sello de la regla deja de contar las palabras | El número quedaba viejo con cada palabra nueva, y ya había pasado dos veces | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna. La fila malformada de la fase B en la tabla de fases de la HU, que rompe el cuadro, es de esa fase y no se tocó acá.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`README.md` de HU-036 y su tabla de fases, con la fila y la bitácora de la fase C; `CHANGELOG.md` y `VERSION`: la 56.2.0 subió en `634b28a`, y esta fase agrega la 56.2.1 por la celda de «OK».

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
