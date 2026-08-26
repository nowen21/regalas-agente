# Funcionalidad implementada — Fase A-EP-003-HU-010-glosario-de-la-terminologia

**Para qué sirve este documento.** Es el cierre de la fase: qué quedó hecho de cada tarea, qué se probó, qué se decidió y qué deuda quedó, comparado contra lo que el [plan_trabajo.md](plan_trabajo.md) prometió. El plan no se toca; acá se dice qué pasó de verdad.

> **Estado al 2026-08-16: la fase cumple.** El ciclo 3 ejecutó CP-006 con lector de fuera y cerró RNF-01. Lo que la prueba destapó cambió el glosario entero y hasta el nombre de un término: `brief` pasó a **planteamiento**.

## 1. Qué quedó hecho

El estándar tiene glosario. Un lector que se atraviesa con una palabra —especificación, señal, fase, puerta, enganche— la busca en [base/glosario.md](../../../../../base/glosario.md) y la encuentra explicada en una línea, con quién la escribe, dónde vive y qué regla la manda. Antes había que leer el capítulo entero.

Y quedó el inventario de lo que sigue en inglés: 12 términos con traducción usada que todavía no se cambiaron, cada uno con el archivo donde vive. Eso es lo que le faltaba al hallazgo H-8.

## 2. Trazabilidad

### 2.1 Criterio de aceptación contra lo construido

| CA | Qué exigía | Dónde quedó | Cómo se verificó | Veredicto |
|---|---|---|---|---|
| CA-01 | Cada término definido en una línea | Los cuatro grupos de [base/glosario.md](../../../../../base/glosario.md) | CP-001 y CP-002 del [resultado_pruebas.md](resultado_pruebas.md) | Cumple |
| CA-02 | Cada entrada dice dónde vive y qué regla lo manda | Las columnas **Dónde vive** y **Regla** de cada tabla | CP-004 y CP-005 | Cumple |
| CA-03 | Se ve qué quedó en otro idioma | La sección de cierre del glosario, con sus dos tablas | CP-008 | Cumple |
| RNF-01 | Se entiende sin saber del tema | Todo el glosario | CP-006, ciclo 3. El lector de fuera preguntó tres veces y las tres eran defectos, corregidos | Cumple, probado sobre una entrada de cinco |
| RNF-02 | Enlaza a la regla dueña, no copia su texto | Todas las entradas | CP-007 | Cumple |

### 2.2 Tarea por tarea

| Tarea | Qué prometía | Qué pasó |
|---|---|---|
| T-01 | Listar los términos por grupo | Hecho, recorriendo `base/`, `plantillas/` y `skills/` |
| T-02 | Descartar lo que no es del estándar | Hecho. CP-003 lo comprobó con tres palabras del oficio que el estándar no usa |
| T-03 | Definir cada término en una línea | Hecho: 72 definiciones. Eran 67 hasta que el ciclo 2 destapó cinco que faltaban |
| T-04 | Armar el documento con sus cuatro grupos | Hecho, con orden alfabético dentro de cada grupo |
| T-05 | Agregar quién lo escribe, dónde vive y qué regla lo manda | Hecho, con el enlace resuelto en cada cita |
| T-06 | Enlazarlo desde las tres puertas de entrada | Hecho en [README.md](../../../../../README.md), [base/README.md](../../../../../base/README.md) y [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) |
| T-07 | Seguir los enlaces uno por uno | Hecho con `validadores/enlaces.py`. Destapó el defecto D-02 |
| T-08 | Marcar lo que sigue en otro idioma | Hecho: 10 términos se quedan, con su motivo |
| T-09 | Cerrar con la tabla de lo que falta traducir | Hecho: 12 términos, con el archivo de cada uno |
| T-10 | Releer contra `00·ID7` y `00·ID8` | Hecho por el agente. La lectura por alguien de fuera queda pendiente (CP-006) |
| T-11 | Comprobar que ninguna entrada copia su regla | Hecho dos veces. El ciclo 1 destapó D-03, corregido; el ciclo 2 lo rehízo contra la regla que cada entrada nombra y dio cero |
| T-12 | Sumarle el incremento a la especificación del módulo | Hecho en [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md) |
| T-13 | Registro de cambios y `VERSION` | Hecho: entrada 15.3.0 y `VERSION` de 15.2.0 a 15.3.0 |
| T-14 | HU, su índice, el mapa del sitio y este cierre | Hecho |
| T-15 | Cerrar el pendiente 21 en su parte del glosario | Hecho: queda abierto solo en la parte de los roles |

**Hechas: 15 de 15.**

## 3. Qué se probó

Tres ciclos. Ocho casos diseñados, siete ejecutados, siete aprobados, cero fallidos. El ciclo 2 corrió los 12 pasos que el ciclo 1 había dejado sin registro y rehízo los 3 que se habían hecho distinto; ahí salió D-05, que faltaban cinco términos, ya agregados. El detalle está en el [resultado_pruebas.md](resultado_pruebas.md). El ciclo 3 corrió CP-006: el usuario leyó el glosario, no entendió la entrada de `brief` y preguntó tres veces. De esas tres preguntas salieron la reescritura de las 72 definiciones y el cambio a **planteamiento**.

Cinco defectos aparecieron y tres se corrigieron dentro de la fase: enlaces que no cumplían `13·DOC14` y tres definiciones que copiaban el texto de su fuente. Dos se aceptaron: que el glosario tenga 72 entradas donde la historia suponía unas treinta, y que cinco definiciones cierren repitiendo lo que exige su regla sin llegar a copiarla.

## 4. Qué no se hizo, y por qué

- **Renombrar los roles.** Estaba declarado fuera de alcance desde el plan. Toca diez archivos y rompe las citas que los nombran, así que necesita su propia historia de usuario. El glosario deja el inventario listo para esa fase.
- **Reescribir las reglas** para que usen el término del glosario. Acá se definió, no se corrigió lo escrito.

## 5. Qué se decidió

| Decisión | Por qué |
|---|---|
| El glosario vive en `base/`, no en `documentacion/` | `base/` es lo que heredan los proyectos. Recibir las reglas sin la explicación de sus palabras es recibir media cosa |
| Sin número de capítulo y sin checklist del estándar | No es una regla: no exige nada. Numerarlo lo cargaría en cada sesión sin motivo |
| Cuatro grupos temáticos, con orden alfabético dentro de cada uno | El orden alfabético puro sirve para buscar lo que ya se sabe cómo se llama; los grupos sirven para entrar sin saber nada, que es el lector de la historia |
| La entrada define y enlaza; nunca copia | Dos copias de la misma norma se desincronizan, y manda la que nadie relee |
| Los enlaces a la misma carpeta se dejan con nombre corto | Es la excepción escrita en la propia `13·DOC14`. La ruta completa dentro de una frase vuelve el documento ilegible, y ahí manda `00·ID7` |

## 6. Deuda que queda

| Qué | De dónde sale | Dónde queda anotada |
|---|---|---|
| Los 12 términos que faltan traducir, empezando por los roles | CA-03 de esta fase | El cierre de [base/glosario.md](../../../../../base/glosario.md) y el [pendiente 21](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md) |
| Probar las otras cuatro entradas con lector de fuera. Solo se probó una | Salvedad 1 del veredicto | §6 del [resultado_pruebas.md](resultado_pruebas.md) |
| El validador de enlaces marca como aviso los enlaces a la misma carpeta, que `13·DOC14` exime | Se vio al correr CP-005 | Hallazgo de la sesión del 2026-08-14 |
| El encabezado de [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) dice v1.4.0 del 2026-08-07, con el estándar en 18.0.0 | Se vio al tocar el árbol en T-06 | Hallazgo de la sesión del 2026-08-14 |

Las dos últimas se vieron trabajando y no se tocaron: están fuera de los archivos que el plan declara (`02·F8`).
