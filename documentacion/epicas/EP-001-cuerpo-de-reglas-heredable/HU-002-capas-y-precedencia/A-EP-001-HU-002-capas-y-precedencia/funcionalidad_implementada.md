# Funcionalidad implementada — Fase A-EP-001-HU-002-capas-y-precedencia

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta el archivo donde vive cada cosa. Lo probado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué quedó, en una frase

**Está escrito en cuántas capas se reparten las reglas, qué va en cada una, cómo se ve la capa al abrir el capítulo y cuál gana cuando dos se contradicen.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Cuántas capas hay y qué va en cada una | regla | [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y la tabla de [`base/README.md`](../../../../../base/README.md) | ✅ | cuatro niveles, con qué puede tocar un proyecto en cada uno |
| El orden de desempate completo | regla | [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) y su [anexo](../../../../../base/20-meta-reglas/desempate.md) | ✅ | seis pasos numerados, que se recorren de arriba abajo |
| La capa se ve al abrir el capítulo | doc | la cabecera de cada capítulo | ✅ | 23 de 23 con su marca en la primera línea |
| Lo opcional está marcado como tal | doc | los capítulos opt-in | ✅ | siete con `[CAPA 2 · opt-in]` |
| El preámbulo queda fuera del orden | doc | `00-identidad-y-rol` y `20-meta-reglas` | ✅ | marca `[PREÁMBULO]`, y el `20` declara que sus reglas son de procedimiento y no de fondo |
| La capa protegida no se puede aflojar | prueba | `validar.py metareglas` | ✅ | ninguna `[BLINDADA]` vive fuera del núcleo |
| El proyecto declara su capa | doc | `.agente/reglas-proyecto.md` y el paso 4 del `CLAUDE.md` instalado | ✅ | con `20·M16`, que obliga a nombrar la regla de base que ajusta |

## 2. Lo que cambia para un proyecto que hereda

**Nada nuevo.** Las cuatro capas y su orden ya regían; esta fase los deja comprobados y escritos como tales.

## 3. Lo que queda abierto

**Que un programa vea si el proyecto declaró su ajuste con una marca fija.** Se evaluó al cerrar el [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md) y **se decidió no agregarlo**: obligaría a todos los proyectos instalados a escribir algo que hoy no escriben, a cambio de comprobar lo que `20·M16` ya exige por otro lado.

**Y lo que ningún caso prueba:** que la IA respete el orden en cada respuesta. Se comprobó lo comprobable —que el orden esté escrito, sea seguible y esté vigilado donde un programa alcanza—, y queda dicho para que nadie lea este cierre como si probara la conducta.
