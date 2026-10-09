# Análisis 4: en un proyecto con dos programas, Cimiento revisa solo el primero que encuentra

> **Aprobado** por el usuario el 2026-10-08, en el turno 41, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisaron todos los proyectos registrados buscando más de un programa: el estándar (`interfaz/` y Cimiento) y RNI (`rni-front` y `rni-back`) |
| R-2 | Se buscó todo lo que nombra `interfaz/` |
| R-15 | No se dio clic en «Revisar» en ningún proyecto |
| R-19 | Lo que pida cada cambio se lista antes de escribir los planes |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-7 · En un proyecto con dos programas, Cimiento revisa solo el primero que encuentra

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, al volver a instalar Cimiento en todos los proyectos, el repositorio del estándar se reconoció como Django por `interfaz/manage.py`, que está antes que `proyectos/cimiento/manage.py`. coverage.py quedó instalado en el Python de `interfaz/`, y Cimiento mismo no se revisaría. La EP-029 supuso un programa por proyecto |
| Por qué importa | Un proyecto con varios programas (un visor y una aplicación, un frente y un servidor) queda revisado a medias, y la página dice que está al día |
| Pendiente | El mismo pendiente 141: se trata en su análisis 4 |

## Pendiente

La V4, según el análisis 3: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 39 · Usuario, 2026-10-08 23:00:53
> Analicemos: el pendiente 141

**Agente**, 2026-10-08 23:02:02
<!-- agente: 59c58166-c1dd-4443-96e1-a58df8c54cce -->

Abrí el análisis 4: [analisis-4.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md).

Al revisar todos los proyectos encontré que RNI tiene el mismo problema: tiene un frente en Angular y un servidor en Python, y Cimiento revisa solo el frente.

Necesito dos respuestas, cada una con SÍ o NO:

1. **¿Se borra `interfaz/`?** Se borrarían la carpeta y su Python. También se quitarían sus menciones en el permiso de `.claude/settings.json` y en las dos guías de `anatomia/`. Los documentos de fases viejas que la nombran se dejan como están, porque son historia. Si algún día hace falta, se recupera desde git. Recomiendo SÍ.
2. **¿Se revisa cada programa por separado?** Cimiento encontraría todos los programas de un proyecto y revisaría cada uno con su herramienta. La página mostraría una fila por proyecto con el programa que tenga menos pruebas, y el detalle mostraría cada programa. Recomiendo SÍ.

### 40 · Usuario, 2026-10-08 23:04:04
> Respondo:
> 1. si
> 2. si

**Agente**, 2026-10-08 23:05:48
<!-- agente: 71ad2896-ade4-4699-8e19-e9f667078580 -->

El freno volvió a cobrarme `core/comun/enganches.py`, que cambió otra sesión. Es el mismo defecto del pendiente 123. Lo reporto aquí porque hay un análisis abierto, y sigo.

Los dos acuerdos quedaron anotados en el análisis 4. De ahí salen dos HU nuevas en la EP-029:

- **HU-006:** borrar `interfaz/` y quitar sus menciones.
- **HU-007:** revisar cada programa de un proyecto.

El pendiente y el hallazgo ya quedaron actualizados.

El análisis no tiene preguntas abiertas. Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 41 · Usuario, 2026-10-08 23:08:31
> Apruebo el análisis

**Agente**, 2026-10-08 23:16:37
<!-- agente: dee6f158-7c7a-4fce-863b-e442a39a3ba3 -->

El análisis 4 quedó aprobado. Sigo con la HU-006, que borra `interfaz/`. Antes reviso cómo compara el freno las rutas, para saber si acepta una carpeta entera en el plan.

El freno deja borrar la carpeta si el plan nombra sus archivos. Armo la HU-006 con la lista exacta que guarda git.

Escribo los documentos de la HU-006. La tabla de archivos del plan la armo desde git.

Otra vez la consola no acepta el texto largo. Uso el camino que pide la regla `04·S18`: guardo el guion de apoyo en `historico-chat/scripts/2026-10-08/` y lo corro desde ahí.

Mejor escribo los documentos de la HU-006 directamente con el editor. Primero saco de git la lista de archivos.

Borro `interfaz/`: primero lo que guarda git y después lo que queda suelto, como su Python.

Carpeta borrada: 50 archivos de git y el resto. Ahora quito sus menciones en `.claude/settings.json` y en `anatomia/`.

La HU-006 pasa: 3 de 3 pruebas. Escribo su cierre.

El hallazgo quedó anotado como H-8. La HU-006 está hecha, salvo esos enlaces rotos; la HU-007 todavía no empieza.

Para el análisis 5 propongo esto: en esos seis archivos, convertir el enlace roto en texto normal. El nombre `interfaz/` sigue ahí como historia, pero ya no apunta a nada. Así no se reescribe la historia y el control de enlaces pasa.

Para abrirlo, escriba:

```
Analicemos: el pendiente 141
```

> acá termina la conversación

---

## Lo acordado

1. `interfaz/`: se borra, con su Python, y se quitan sus menciones en `.claude/settings.json` y en `anatomia/`; los documentos de fases cerradas que la nombran se dejan como historia (turno 40).
2. Proyectos con varios programas: Cimiento encuentra todos los programas de un proyecto y revisa cada uno con su herramienta; la fila del proyecto muestra el programa con menos pruebas y el detalle muestra cada uno (turno 40).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F0` (lo que se construya recorre la cadena), `02·F30` (borrar `interfaz/` es una acción; su contraria es recuperarla de git) y `20·M11` (las fases cerradas que nombran `interfaz/` no se reescriben). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `interfaz/` | El visor viejo del estándar, que reemplazó Cimiento. 72 MB, 50 archivos en git, sin cambios desde el 2026-08-22. Tiene su `.venv`, donde la instalación del 2026-10-08 puso coverage.py |
| Lo que nombra `interfaz/` | `.claude/settings.json` (un permiso: `python interfaz/manage.py check`), `anatomia/componentes-del-agente.md`, `anatomia/mapa-del-sitio.md`, `cvds/cumplimiento.md`, `CHANGELOG.md`, `documentacion/senales.md` y documentos de fases cerradas de EP-008, EP-009 y EP-025 |
| RNI | `proyectos/rni-front` (Angular) y `proyectos/rni-back` (Python): Cimiento reconoce solo el frente y deja el servidor sin revisar |
| `reconocer` (`core/pruebas/lenguaje.py`) | Devuelve un solo lenguaje y una sola carpeta |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 del pendiente 141, acuerdo 1 | Cimiento reconoce el lenguaje por los archivos; no dijo qué pasa cuando hay más de uno |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): la revisión cubre más; nadie tiene que hacer nada nuevo |
| Normas y leyes | Ninguna |
| Herramientas | Cada programa necesita su herramienta y su Python o su Node |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| El estándar | `interfaz/` y Cimiento | Cimiento no se revisa | Acuerdo 1 |
| RNI | `rni-front` y `rni-back` | El servidor no se revisa | Acuerdo 2 |
| Cualquier proyecto con frente y servidor | Proyectos futuros | Lo mismo | Acuerdo 2 |

---

## Propuesta final: hallazgo y pendiente V5, épica y HU

### Hallazgo V2. En un proyecto con varios programas, Cimiento revisa solo el primero que encuentra

| Campo | Valor |
|---|---|
| Qué pasó | Cimiento reconoce un solo programa por proyecto. En el estándar tomó `interfaz/`, el visor viejo, y dejó a Cimiento sin revisar; en RNI tomó el frente y dejó el servidor |
| Por qué importa | Un proyecto con varios programas queda revisado a medias, y la página dice que está al día |

### Pendiente V5. Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos V2 de H-1, H-2 y H-3, según los análisis 1 a 3, y el hallazgo V2 de H-7: en un proyecto con varios programas, Cimiento revisa solo el primero que encuentra |
| El problema | El de la V4. Además, Cimiento revisa un solo programa por proyecto, y el estándar guarda `interfaz/`, un visor que ya no se usa |
| Por qué importa | El de la V4, y que ningún programa de un proyecto quede sin revisar |

### Épica y HU que salen del análisis

Las HU se suman a la EP-029.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-029·HU-006 | El visor viejo `interfaz/` sale del estándar | El estándar guarda un visor que ya no se usa | Ninguna | Sin él, el estándar tiene un solo programa | 2 |
| 2 | EP-029·HU-007 | Cimiento revisa cada programa de un proyecto | Se revisa un solo programa por proyecto | EP-029·HU-006 | Con `interfaz/` fuera, la prueba sobre el estándar ve solo a Cimiento | 3 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Al reconocer el lenguaje de un proyecto se buscan todos sus programas, no el primero | Falló | S-357 | Complementa R-1 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo H-7 a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md` y `historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md`, hecho el 2026-10-08 |
| 2 | Borrar `interfaz/` con su Python, y quitar sus menciones en `.claude/settings.json`, `anatomia/componentes-del-agente.md` y `anatomia/mapa-del-sitio.md`; las fases cerradas, `CHANGELOG.md`, `cvds/` y `documentacion/senales.md` quedan como historia | 1 | EP-029·HU-006 |
| 3 | Reconocer todos los programas de un proyecto, revisar cada uno con su herramienta y mostrar en la fila el que tiene menos pruebas y en el detalle cada uno | 2 | EP-029·HU-007 |
| 4 | Sumar la lección 1 al origen de R-1 | Análisis 2, acuerdo 3 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-08 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** cuando un proyecto tiene varios programas, Cimiento revisa cada uno con su herramienta, y el estándar deja atrás su visor viejo.
