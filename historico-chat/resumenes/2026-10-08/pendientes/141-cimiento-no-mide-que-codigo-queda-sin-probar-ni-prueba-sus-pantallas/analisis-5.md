# Análisis 5: borrar `interfaz/` dejó enlaces rotos en archivos que el plan no nombra

> **Aprobado** por el usuario el 2026-10-08, en el turno 44, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
| R-1 | Se buscaron todos los enlaces rotos con el control de enlaces del estándar, no con una búsqueda recortada: son 6 |
| R-19 | El plan de la HU-006 debió listar los archivos que enlazan la carpeta borrada |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-8 · Borrar `interfaz/` dejó enlaces rotos en archivos que el plan no nombra

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, en la fase `A-EP-029-HU-006-sin-interfaz`, al borrar `interfaz/` quedaron enlaces rotos en `README.md`, `metricas/README.md`, `cvds/cumplimiento.md` (dos) y `pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md` y `pendientes/hecho/metricas-del-proceso.md`. La búsqueda de quién nombraba la carpeta se cortó en las primeras 15 líneas y no los mostró; el análisis 4 dejó `cvds/` como historia sin ver que un enlace roto no pasa el control de enlaces |
| Por qué importa | Lo que el plan no declara no se escribe, y los enlaces rotos detienen la publicación |
| Pendiente | El mismo pendiente 141: se trata en su análisis 5 |

## Pendiente

La V5, según el análisis 4: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 42 · Usuario, 2026-10-08 23:19:03
> Analicemos: el pendiente 141

**Agente**, 2026-10-08 23:21:13
<!-- agente: bc858f06-2055-4fca-8c0d-548d8a0d4015 -->

Primero busco todos los enlaces que apuntan a `interfaz/`, esta vez sin cortar la búsqueda.

El control de enlaces confirma que son exactamente esos 6 y ningún otro. Lleno el análisis 5.

El análisis 5 está abierto: [analisis-5.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-5.md). El control de enlaces confirma que los enlaces rotos son exactamente 6.

Necesito dos respuestas, cada una con SÍ o NO:

1. **¿Los 6 enlaces se vuelven texto normal?** El nombre `interfaz/` queda escrito como historia, pero ya no apunta a nada. Recomiendo SÍ.
2. **¿Se amplía la R-19 para que no se repita?** Antes de borrar una carpeta, se corre el control de enlaces para ver quién la enlaza, y esos archivos entran al plan. Recomiendo SÍ.

### 43 · Usuario, 2026-10-08 23:25:25
> apruebo si a las dos

**Agente**, 2026-10-08 23:26:45
<!-- agente: c97c591c-468b-4830-8282-c7ba8c745a66 -->

Los dos acuerdos quedaron anotados. Ya hice lo que se hace de una vez: el pendiente pasó a su V6, el hallazgo H-8 a su V2 y amplié la R-19. El análisis 5 no tiene preguntas abiertas.

Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 44 · Usuario, 2026-10-08 23:30:22
> Apruebo el análisis

**Agente**, 2026-10-08 23:49:58
<!-- agente: 19f54777-0b8e-4f64-9ced-57980eff70d0 -->

El análisis 5 quedó aprobado. Sumo los 6 archivos al plan de la HU-006 y convierto sus enlaces en texto normal.

Ya no queda ningún enlace roto a `interfaz/`. Anoto en el resultado de la HU-006 que hubo un segundo ciclo.

Paso a la HU-007, que revisa cada programa de un proyecto. Siguiendo la R-19, primero agrego al modelo el dato «programa» y le pregunto a Django qué migración pide.

Escribo la HU-007 y su plan, que declara todos los archivos que toca.

Ahora el código. Primero la migración declarada y `reconocer_todos`.

Ahora `revisar.py`: una revisión por programa.

Ahora `parte.py`: pone y quita la herramienta en cada programa.

Ahora la vista y el detalle: la fila muestra el programa con menos pruebas y el detalle muestra cada uno.

Escribo las pruebas de la HU-007.

La página funciona bien: muestra «30,0%» con coma, como se escribe en Colombia. La que estaba mal era la prueba, que esperaba el punto. La corrijo.

La regresión tarda más de diez minutos y siguió corriendo aparte. Espero a que termine para escribir el resultado.

> acá termina la conversación

---

## Lo acordado

1. Los 6 enlaces rotos: se vuelven texto normal; el nombre `interfaz/` queda escrito como historia sin apuntar a nada (turno 43).
2. La R-19 se amplía: antes de borrar una carpeta se corre el control de enlaces para ver quién la enlaza, y esos archivos entran al plan (turno 43).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` y `20·M11`. Choca el acuerdo 1 del análisis 4 (dejar `cvds/` y los pendientes cerrados como historia) con el control de enlaces, que no deja publicar un enlace roto; se resuelve en este análisis.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Los enlaces rotos | 6, según `validar.py estandar`: `README.md:103`, `metricas/README.md:31`, `cvds/cumplimiento.md:109` y `:127`, `pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md:32`, `pendientes/hecho/metricas-del-proceso.md:17` |
| La fase A de la HU-006 | La carpeta y sus menciones en `.claude/settings.json` y `anatomia/` ya salieron; su prueba pasa |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 4 del pendiente 141, acuerdo 1 | Dejó la historia como estaba; este análisis precisa qué se hace con sus enlaces |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno |
| Normas y leyes | Ninguna |
| Herramientas | El control de enlaces de `validar.py estandar`, que corre antes de publicar |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Los 6 enlaces | Los archivos de arriba | No se puede publicar | Acuerdo 1 |
| Borrar cualquier carpeta en el futuro | Toda fase que borre | Lo mismo | Acuerdo 2 |

---

## Propuesta final: hallazgo y pendiente V6, épica y HU

### Hallazgo V2. Borrar `interfaz/` dejó enlaces rotos en archivos que el plan no nombra

| Campo | Valor |
|---|---|
| Qué pasó | Al borrar `interfaz/` quedaron 6 enlaces rotos en archivos que el plan de la HU-006 no nombraba. La búsqueda de quién enlazaba la carpeta se recortó y no los mostró |
| Por qué importa | Los enlaces rotos detienen la publicación, y le puede pasar a cualquier fase que borre algo |

### Pendiente V6. Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos V2 de H-1, H-2, H-3 y H-7, según los análisis 1 a 4, y el hallazgo V2 de H-8: borrar `interfaz/` dejó enlaces rotos en archivos que el plan no nombra |
| El problema | El de la V5. Además, quedan 6 enlaces rotos a `interfaz/`, y los planes que borran no buscan antes quién enlaza lo que borran |
| Por qué importa | El de la V5, y que el estándar se pueda publicar |

### Épica y HU que salen del análisis

Las mismas de la EP-029: este análisis no crea HU, completa el plan de la HU-006.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-029·HU-006 | El visor viejo `interfaz/` sale del estándar | Los enlaces rotos | Ninguna | Es la que los dejó | 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Para saber quién enlaza una carpeta antes de borrarla se corre el control de enlaces, no una búsqueda recortada | Falló | S-358 | Complementa R-19 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo H-8 a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md` y `historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md`, hecho el 2026-10-08 |
| 2 | Volver texto normal los 6 enlaces a `interfaz/` de `README.md`, `metricas/README.md`, `cvds/cumplimiento.md` y los dos pendientes de `pendientes/hecho/`, sumándolos al plan de la HU-006 | 1 | EP-029·HU-006 |
| 3 | Ampliar la R-19 con el control de enlaces antes de borrar, y sumarle el origen de la lección 1 | 2 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-08 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** antes de borrar una carpeta, se corre el control de enlaces para ver quién la enlaza, y esos archivos entran al plan.
