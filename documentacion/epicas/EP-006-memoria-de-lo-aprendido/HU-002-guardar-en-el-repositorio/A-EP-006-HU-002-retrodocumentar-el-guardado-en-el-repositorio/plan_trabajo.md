# Plan de Trabajo — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-guardar-en-el-repositorio.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-002 Guardar lo aprendido en el repositorio](../HU-002-guardar-en-el-repositorio.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-002](../HU-002-guardar-en-el-repositorio.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que existe: las preferencias del usuario viven en [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md), un archivo por recuerdo y con su índice, y eso sí está en el repositorio y se ve en el historial. ✨ Y destapa lo que falta: las **señales** viven en [`memoria/senales.db`](../../../../../memoria/esquema.sql), que es una base binaria — está en el repositorio, y en el historial no se puede leer qué cambió. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-guardar-en-el-repositorio.md#ca-01--lo-guardado-vive-en-el-repositorio-y-se-ve-en-el-historial) | Lo guardado vive en el repositorio y se ve en el historial | **A medias.** Los recuerdos son archivos de texto y se ven; las señales están en una base binaria y su cambio no se puede leer |
| [CA-02](../HU-002-guardar-en-el-repositorio.md#ca-02--hay-un-índice-que-dice-de-qué-trata-cada-cosa) | Hay un índice que dice de qué trata cada cosa | Cumplido para los recuerdos: el índice existe y dice de qué trata cada uno, con la advertencia de que el índice no reemplaza leer el archivo. Para las señales, el índice es la búsqueda |

**Por qué una sola fase.** Los dos CA son la misma pregunta —dónde vive y cómo se encuentra— sobre las dos formas de memoria que hay (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar dicho qué parte de la memoria se puede leer del historial y qué parte no, y probar que el índice de los recuerdos está al día.

**Fuera de alcance:**

- **Cambiar dónde viven las señales.** Se mide y se propone: mover la memoria es una decisión de fondo.
- **Sacar del almacén local,** que es [HU-006](../../HU-006-sacar-del-almacen-local/HU-006-sacar-del-almacen-local.md).
- **Buscar,** que son HU-003 y HU-004.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: la carpeta de recuerdos tiene 19 archivos y su índice; la base de señales es un archivo binario.

**Lo que ya existe:** la carpeta de recuerdos con un archivo por recuerdo y su índice, con la forma fija de qué se pide, por qué y cómo se aplica; la razón escrita de por qué van ahí y no en el almacén local —lo local no se ve en git, no se puede revisar, no se versiona y no viaja—; y la base de señales, con su búsqueda como forma de índice.

**Lo que no existe:**

1. **La lectura del historial de las señales.** La base es binaria: se puede ver que cambió, no qué cambió.
2. **La prueba del índice de recuerdos** en los dos sentidos.
3. **La decisión sobre el límite.** Si se acepta que las señales no se lean del historial, hay que decirlo; si no, hay que exportarlas.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | La prueba del índice de recuerdos en los dos sentidos |
| `…/A-EP-006-HU-002-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos, la medición y la propuesta |
| `HU-002-guardar-en-el-repositorio.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni la base ni la carpeta de recuerdos se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agrega una prueba y se mide.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

Los recuerdos se leen abriendo el archivo, y llegan puestos al abrir la sesión. Las señales se leen con `memoria.py search`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El límite de la base binaria se mide y se propone | Exportar las señales a texto en esta fase | Cambiar dónde vive la memoria es una decisión de fondo, y decidir por cuenta propia dónde vive lo aprendido es peor que el límite |
| La prueba del índice va en los dos sentidos | Comprobar solo que el archivo tenga su línea | Una línea sin archivo es un índice que miente, y es lo que ya pasó con otros índices del repositorio |
| La forma de los recuerdos no se cambia | Unificarla con la de las señales | Son dos cosas distintas, y unirlas es justo lo que HU-005 dice que no se debe hacer |

### 2.7 Dudas por resolver antes de escribir

Ninguna para lo que la fase hace: la decisión que aparece se propone, no se toma.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo guardado vive en el repositorio y se ve en el historial

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: un recuerdo nuevo se ve en el historial como texto | `plan_pruebas.md` | 1,5 |
| T-02 | Levantar qué se puede y qué no se puede leer del historial de la base de señales | `resultado_pruebas.md` | 2,0 |
| T-03 | Proponer la salida —exportar las señales a texto junto a la base, o dejarlo declarado como límite— sin decidirla | `resultado_pruebas.md` | 1,5 |

### CA-02 — Hay un índice que dice de qué trata cada cosa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Prueba: todo archivo de la carpeta de recuerdos tiene su línea en el índice, y toda línea su archivo | `validadores/pruebas.py` | 2,0 |
| T-05 | Caso de prueba: por el índice se llega al recuerdo que se busca sin abrir los otros | `plan_pruebas.md` | 1,5 |

### RNF — Que lo aprendido se pueda revisar

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-04 primero, que es la prueba. T-01 → T-05 después. T-02 → T-03 al final, y T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Recuerdo visible en el historial, y la medición de la base binaria | T-01, T-02, T-03 |
| CA-02 | Índice completo en los dos sentidos, y una búsqueda por él | T-04, T-05 |

---

## 6. Datos y ambiente de prueba

Bases de datos temporales para los casos, y este repositorio. Ningún dato real de cliente y ninguna clave: el contenido de las señales no sale de la máquina.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. La base de prueba se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no se cambia nada de lo que corre. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`01·C19`](../../../../../base/01-conducta.md), [`09`](../../../../../base/09-git.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba del índice falle con los 19 recuerdos que hay | Se destapa deuda | Se anota y se corrige el índice, que es un archivo del repositorio y no rompe nada |
| R-02 | Que la propuesta de exportar las señales se lea como decidida | Se movería la memoria sin aprobación | Se escribe como propuesta, con lo que deja cada salida |
| R-03 | Que la base de señales cambie durante la medición | Medición inconsistente | Se mide sobre una copia |

---

## 11. Definition of Done

- [ ] Está probado que un recuerdo nuevo se ve en el historial como texto.
- [ ] Está escrito qué se puede y qué no se puede leer del historial de la base de señales.
- [ ] La salida para ese límite quedó propuesta, sin decidirla.
- [ ] El índice de recuerdos está probado en los dos sentidos.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
