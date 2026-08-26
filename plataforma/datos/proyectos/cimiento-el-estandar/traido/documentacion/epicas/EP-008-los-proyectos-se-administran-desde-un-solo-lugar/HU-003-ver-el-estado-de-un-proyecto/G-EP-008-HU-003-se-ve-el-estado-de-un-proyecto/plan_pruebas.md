# Plan de Pruebas — Fase G-EP-008-HU-003: se ve el estado de un proyecto   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-G-EP-008-HU-003 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que el estado de un proyecto se pueda ver **sin abrir su carpeta**, que diga lo que no se pudo leer en vez de suponerlo, y que un proyecto sin nada no muestre una pantalla vacía.

**No se prueba** abrir un documento traído para leerlo, que es de la versión 2.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que el estado se calcule bien desde lo traído | Sí |
| Integración | Que traer y calcular encajen | Sí |
| Interfaz | Que el estado se vea, con palabras | Sí |
| Rendimiento | Que cincuenta proyectos con estado listen bajo un segundo | Sí |
| Aislamiento | Que calcular no lea la carpeta del proyecto | Sí |

### 3.2 Técnicas

- **Borrar la carpeta del proyecto y volver a pedir el estado.** Es la única forma de comprobar que el estado sale de lo traído y no de leerla.
- Casos con datos que no se dejan leer, no solo con datos limpios.
- Sabotaje: romper el código a propósito, restaurando con copia, limpiando rastros, y corriendo la suite completa al final.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| Se trae también `cvds/`, el hueco de la fase E | [CP-001](#cp-001--las-etapas-del-ciclo-entran-al-traer) | ☐ |
| `CA-01` el estado dice qué etapas tienen documento | [CP-002](#cp-002--el-estado-dice-qué-etapas-tienen-documento) | ☐ |
| `CA-01` el estado dice qué fases hay y en qué van | [CP-003](#cp-003--el-estado-dice-cuántas-fases-hay-y-en-qué-estación) | ☐ |
| `04·R4` lo que no se pudo leer se dice | [CP-004](#cp-004--una-estación-que-no-se-deja-leer-se-dice-no-se-supone) | ☐ |
| `CA-03` lo aprobado se distingue, con palabras | [CP-005](#cp-005--lo-aprobado-se-distingue-y-se-dice-con-palabras) | ☐ |
| `CA-02` un proyecto sin nada dice qué haría falta | [CP-006](#cp-006--un-proyecto-sin-nada-dice-qué-haría-falta) | ☐ |
| Transversal: la ruta perdida no oculta el estado | [CP-007](#cp-007--con-la-ruta-perdida-el-estado-se-ve-igual) | ☐ |
| `RNF-02` cincuenta proyectos con estado bajo un segundo | [CP-008](#cp-008--cincuenta-proyectos-con-estado-listan-bajo-un-segundo) | ☐ |
| `CA-01` · que NO pase: que calcular lea la carpeta del proyecto | [CP-009](#cp-009--que-no-pase-que-calcular-el-estado-lea-la-carpeta-del-proyecto) | ☐ |

## 5. Los casos

### CP-001 · Las etapas del ciclo entran al traer

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el hueco de la fase E quedó cerrado |
| **Cómo se corre** | Se arma un proyecto con sus siete etapas en `cvds/` y se trae |
| **Resultado esperado** | Las siete entran, reconocidas como etapas. Y `cvds/` **ya no se salta en silencio** |
| **Si falla** | El estado no puede decir qué etapas tienen documento, porque no las tiene |

**Este caso existe porque una fase cerrada tenía un defecto.** La fase E declaraba que recorría la documentación del ciclo y no recorría las etapas del ciclo. Se descubrió acá, al ser esta la primera fase que necesitaba leerlas.

### CP-002 · El estado dice qué etapas tienen documento

| Campo | Valor |
|---|---|
| **Qué comprueba** | La primera mitad de `CA-01` |
| **Cómo se corre** | Se trae un proyecto con cuatro de las siete etapas escritas |
| **Resultado esperado** | Dice cuáles cuatro tienen y **cuáles tres no**. Las que faltan también son información |
| **Si falla** | Un estado que solo lista lo que hay no deja ver qué falta, que es para lo que se mira |

### CP-003 · El estado dice cuántas fases hay y en qué estación

| Campo | Valor |
|---|---|
| **Qué comprueba** | La segunda mitad de `CA-01` |
| **Cómo se corre** | Se trae un proyecto con fases en estaciones distintas, incluida una cerrada |
| **Resultado esperado** | Dice cuántas hay en total y cuántas siguen abiertas |
| **Si falla** | Se revisa si se está leyendo la estación o suponiéndola |

### CP-004 · Una estación que no se deja leer se dice, no se supone

| Campo | Valor |
|---|---|
| **Qué comprueba** | `04·R4` sobre un caso real: 5 de los 125 estados del repositorio no se dejan leer |
| **Cómo se corre** | Se trae un proyecto con un `estado-fase.md` cuya línea de estación está escrita de otra forma |
| **Resultado esperado** | El estado dice **cuántas no se pudieron leer, y cuáles**, con su ruta |
| **Si falla** | Si la cuenta como cerrada o la deja fuera, el estado está afirmando algo que no leyó |

**Es el caso que más protege.** Doce formas distintas de escribir la misma línea, y va a haber una trece.

### CP-005 · Lo aprobado se distingue, y se dice con palabras

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-03` |
| **Cómo se corre** | Se trae un proyecto con documentos aprobados y sin aprobar, y se mira la pantalla |
| **Resultado esperado** | Dice cuántos están aprobados **con palabras**, no solo con color |
| **Si falla** | Un color no se lee en voz alta, ni lo distingue quien no ve los colores |

### CP-006 · Un proyecto sin nada dice qué haría falta

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-02` |
| **Cómo se corre** | Se conecta un proyecto y se pide su estado **sin traer nada** |
| **Resultado esperado** | Dice `sin empezar` **y qué haría falta para arrancar**. No una pantalla vacía |
| **Si falla** | Una pantalla vacía se lee como un error de la plataforma |

### CP-007 · Con la ruta perdida, el estado se ve igual

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el estado salga de lo traído, no del proyecto |
| **Cómo se corre** | Se trae un proyecto, **se borra su carpeta**, y se pide el estado |
| **Resultado esperado** | El estado sale completo, con el aviso de la ruta perdida al lado |
| **Si falla** | El estado se está calculando leyendo la carpeta, y `CA-01` dice lo contrario |

### CP-008 · Cincuenta proyectos con estado listan bajo un segundo

| Campo | Valor |
|---|---|
| **Qué comprueba** | `RNF-02` con el estado calculado, que es más caro que sin él |
| **Cómo se corre** | Se conectan cincuenta proyectos con documentación traída y se pide la lista, midiendo |
| **Resultado esperado** | Menos de un segundo, **con el número escrito** |
| **Si falla** | Se decide antes de cerrar: calcular menos, o calcular solo al entrar a un proyecto |

### CP-009 · Que NO pase: que calcular el estado lea la carpeta del proyecto

| Campo | Valor |
|---|---|
| **Qué comprueba** | `CA-01`: «y no hace falta abrir su carpeta para saberlo» |
| **Cómo se corre** | Se trae un proyecto, se borra su carpeta entera, y se pide el estado |
| **Resultado esperado** | El estado sale **idéntico** al de antes de borrarla |
| **Si falla** | La plataforma depende de que el proyecto esté ahí, y entonces no sirve para un proyecto archivado o entregado |

**Es la forma más dura de probarlo:** si el estado cambia al borrar la carpeta, se estaba leyendo.

## 6. Lo que este plan NO puede probar

- **Que el estado sea útil.** Se prueba que diga lo que la historia pide, no que ayude a decidir. Eso lo dice el usuario al usarlo.
- **Que las doce formas de escribir la estación sean todas.** Se prueba que lo ilegible se diga, no que se conozcan todos los casos.

## 7. Criterios de salida

- Los nueve casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- El número de la medición escrito, aunque cumpla.
- Las pruebas validadas con sabotaje, restaurando con copia y limpiando rastros.
- El defecto de la fase E anotado en su documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
