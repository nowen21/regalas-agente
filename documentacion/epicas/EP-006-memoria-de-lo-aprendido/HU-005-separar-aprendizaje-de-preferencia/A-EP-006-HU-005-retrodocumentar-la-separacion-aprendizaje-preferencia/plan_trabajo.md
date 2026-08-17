# Plan de Trabajo — Fase A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-005 Separar lo que el proyecto aprendió de cómo el usuario quiere trabajar](../HU-005-separar-aprendizaje-de-preferencia.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). La separación existe y se usa: lo que el proyecto aprendió va como señal a [`memoria/senales.db`](../../../../../memoria/esquema.sql), y cómo el usuario quiere trabajar va a [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md), con su forma fija —qué se pide, por qué y cómo se aplica—. Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-005-separar-aprendizaje-de-preferencia.md#ca-01--las-dos-cosas-se-guardan-por-separado) | Las dos cosas se guardan por separado | Cumplido: dos sitios distintos, con formas distintas. Sin prueba, y **sin el criterio escrito de cuál va dónde** |
| [CA-02](../HU-005-separar-aprendizaje-de-preferencia.md#ca-02--la-preferencia-dice-por-qué-se-pidió) | La preferencia dice por qué se pidió | Cumplido: los 19 recuerdos traen su porqué, y varios traen además las veces que el usuario tuvo que repetirlo. Sin prueba |

**Por qué una sola fase.** Los dos CA se comprueban sobre los mismos dos sitios (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que quede escrito cuál de las dos memorias recibe cada cosa, y probado que la preferencia siempre dice por qué se pidió.

**Fuera de alcance:**

- **Mover nada de sitio.** Si al clasificar aparece algo en el sitio equivocado, se anota.
- **Sacar del almacén local,** que es [HU-006](../../HU-006-sacar-del-almacen-local/HU-006-sacar-del-almacen-local.md).
- **La regla que obliga a que la memoria viva en el repositorio,** que es `01·C19` y es de EP-001.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: la carpeta de recuerdos tiene 19 archivos con su forma fija, y la base de señales guarda tipos y alcances distintos.

**Lo que ya existe:** los dos sitios; la forma fija de los recuerdos, con su porqué; los diez tipos de señal; la razón escrita de por qué la preferencia no va a `base/` —lo que obliga a guardarla ahí es norma del estándar, y lo que dice cada recuerdo es preferencia sobre cómo trabajar—; y varios recuerdos que llevan la cuenta de las veces que el usuario tuvo que repetir lo mismo.

**Lo que no existe:**

1. **El criterio escrito de cuál va dónde.** Hoy se decide bien por costumbre, y el caso de borde —una preferencia que en realidad es una regla para cualquier proyecto— no está resuelto por escrito.
2. **La prueba de las tres partes** del recuerdo.
3. **La revisión de si algo quedó en el sitio equivocado.**

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `historico-chat/memory/memory.md` | Modificar | Le entra el criterio de cuál va dónde, con el caso de borde |
| `validadores/pruebas.py` | Modificar | La prueba de las tres partes del recuerdo |
| `…/A-EP-006-HU-005-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-005-separar-aprendizaje-de-preferencia.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ningún recuerdo ni ninguna señal se mueve de sitio.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agrega una prueba y se escribe el criterio en el índice que ya existe.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

Los recuerdos llegan puestos al abrir la sesión; las señales se consultan con la búsqueda.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El criterio se escribe en el índice de la memoria, no en `base/` | Hacerlo regla del estándar | El criterio de qué es preferencia del usuario es de este repositorio; si aplicara a cualquier proyecto, sería regla — y eso es justo el caso de borde que hay que escribir |
| Lo que esté en el sitio equivocado se anota | Moverlo de paso | Mover un recuerdo cambia lo que rige la sesión: se propone |
| La prueba mira las tres partes, no la redacción | Juzgar si el porqué es bueno | Que las tres partes estén es sí o no; si el porqué convence es criterio |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los dos sitios existen y su contenido se puede leer.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Las dos cosas se guardan por separado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el criterio: qué es aprendizaje del proyecto y qué es preferencia del usuario, con el caso de borde | `historico-chat/memory/memory.md` | 2,0 |
| T-02 | Caso de prueba: clasificar cinco cosas guardadas y comprobar que están donde el criterio dice | `plan_pruebas.md` | 2,0 |

### CA-02 — La preferencia dice por qué se pidió

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: todo recuerdo trae sus tres partes — qué se pide, por qué y cómo se aplica | `validadores/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: un recuerdo sin el porqué se detecta | `plan_pruebas.md` | 1,5 |

### RNF — Que no se confunda lo aprendido con lo pedido

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 9,0 horas.**

---

## 4. Secuencia de ejecución

T-03 primero, que es la prueba. T-01 después. T-02 y T-04 con el criterio escrito, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Cinco cosas guardadas, clasificadas con el criterio | T-01, T-02 |
| CA-02 | Prueba de las tres partes, y el recuerdo sin porqué | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Bases de datos temporales para los casos, y este repositorio. Ningún dato real de cliente y ninguna clave: el contenido de las señales no sale de la máquina.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. La base de prueba se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no se toca `base/` ni `plantillas/`. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`01·C19`](../../../../../base/01-conducta.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que al escribir el criterio aparezca que varios recuerdos deberían ser reglas | Se destapa trabajo sobre `base/` | Se anotan y se proponen: subir un recuerdo a regla es decisión del usuario, como ya pasó con dos en EP-001 · HU-004 |
| R-02 | Que la prueba falle con recuerdos viejos | Suite roja por deuda | Se anotan y se completan, que es un cambio de texto sin riesgo |
| R-03 | Que el criterio quede tan general que no decida | Vuelve a decidirse a ojo | El caso de borde es la prueba: si con el criterio no se resuelve, falta texto |

---

## 11. Definition of Done

- [ ] El criterio de cuál va dónde está escrito, con su caso de borde.
- [ ] Cinco cosas guardadas quedaron clasificadas con él.
- [ ] Hay prueba de que todo recuerdo trae sus tres partes.
- [ ] Lo que esté en el sitio equivocado quedó anotado, sin moverlo.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
