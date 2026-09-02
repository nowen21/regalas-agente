# Especificación del módulo Seguridad  ·  `[CAPA 3]`

- **Slug del módulo:** `seguridad`
- **Estado:** aprobada, el 2026-09-01 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 3, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Que ninguna credencial quede escrita por la plataforma, y que lo que no se tapa se diga.

- **Dentro de alcance:** tapar en los caminos que escriben lo que alguien acaba de teclear (`F-031`), y contar sin alterar lo que ya existía.
- **Fuera de alcance:** reconocer las formas de credencial, que vive en el estándar; alterar lo importado; y quitar del historial de versiones una clave ya escrita.

## 2. Contexto — qué hay hoy

**El módulo ya existía sin especificación.** Nació dentro de la fase de auditoría como un puente de tres líneas hacia `validadores/enmascarar.py`, que conoce ocho formas de secreto de proveedor, la clave entre comillas y la pegada sin ellas, y sabe **no** tapar los moldes ni la línea que lee del entorno.

**Lo medido el 2026-09-01:**

| Qué se midió | Resultado |
|---|---|
| Caminos que escriben | 6 |
| Caminos que tapan | **1**, la auditoría |
| Documentos guardados | 1 002 |
| Documentos que el tapador cambiaría | **7**, con 21 fragmentos |
| De esos 21, cuántos son claves de verdad | **Ninguna.** Son ejemplos escritos en los documentos de las fases que construyeron el tapador |

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que el enmascarador del estándar está disponible. Si no está, **se revienta en vez de escribir sin tapar**.
- **Dependencias:** el estándar, por el puente; Auditoría y Ciclo de vida, que son los caminos que tapan.
- **Preguntas abiertas:** qué pasa el día que la plataforma y el estándar vivan en repositorios distintos. El puente es lo primero que habría que mover, y está dicho en su propio archivo.

## 4. Reglas de negocio

1. **Se tapa lo que una persona acaba de escribir**, no el texto que ya existía en un archivo.
2. **El nombre de la variable queda intacto.** Taparlo haría el documento ilegible sin proteger nada.
3. **Lo importado no se altera.** Lo que parezca traer credenciales se dice con su número y su nombre.
4. **Sin enmascarador no se escribe.** Baja de [`00·N6`](../../base/00-nucleo-blindado.md), que es blindada.
5. **El reconocimiento no se duplica.** Dos listas de secretos se separan, y la vieja deja pasar una clave.
6. **Todo camino que escribe declara si tapa**, acá, en la §5.1. Un camino que nace sin declararse es el que va a dejar pasar la próxima.

## 5. Modelo de datos

- **Entidades:** ninguna. El módulo transforma texto y no guarda nada.
- **Valores configurables:** dónde vive `validadores/`, que ya lo declara la configuración de la plataforma.
- **Migración:** no aplica.

### 5.1 Qué camino tapa, y cuál no

Es lo que la `RN-6` pide declarar. **Se tapa lo que se teclea; no lo que se copia.**

| Camino | ¿Tapa? | Por qué |
|---|---|---|
| **Auditoría**, al registrar una acción | **Sí** | Es lo que el agente escribe ahora, y una acción puede traer el texto que el usuario acaba de pegar |
| **Ciclo de vida**, al llenar un espacio | **Sí** | Es lo que una persona acaba de teclear. Es el caso que la ficha de `F-031` describe |
| **Importación**, al traer documentos | **No, y avisa** | Copia texto que ya existe. Taparlo lo alteraría sin vuelta atrás, y hoy alteraría 7 documentos que solo hablan del tapador |
| **Almacén**, al guardar | No | Solo escribe lo que otro camino ya le entregó, y esos ya taparon |
| **Expediente**, al generar | No | Se arma con documentos importados, que entran como están. Tapar acá cambiaría el entregable respecto del proyecto |
| **Medición**, al indexar | No | Guarda índice, no contenido. Lo indexado se lee del archivo cada vez |

**Por qué la importación avisa en vez de tapar.** Un documento que **habla de** una credencial parece contenerla. Los 7 que el tapador tocaría son los documentos de las fases que lo construyeron, con sus casos de prueba escritos. Alterarlos sería corromper la documentación del propio tapador, en silencio y sin vuelta atrás. Decir cuántos son deja la decisión donde corresponde.

## 6. Comportamiento y flujos

**Tapar.** Se recibe el texto que se va a escribir y se devuelve el texto tapado **y cuántas se taparon**. El número importa: tapar en silencio deja al usuario creyendo que escribió otra cosa.

- El nombre de la variable no se toca.
- Un texto sin claves sale idéntico.
- Si el enmascarador no está, se levanta un error y **no se escribe nada**.

**Contar sin alterar.** Se recorre lo que un proyecto tiene guardado y se dice **cuántos documentos parecen traer credenciales, y cuáles**. Ninguno se toca.

## 7. Interfaz

Sin pantalla. El aviso sale por la orden de consola, como el resto de los módulos de esta etapa.

## 8. Permisos y autorización

Un solo usuario, sin credenciales propias. **Y esa es la razón de ser del módulo:** la plataforma no guarda credenciales de nadie, ni las suyas ni las que se le escapen a quien escribe.

## 9. Marco normativo

**Es el módulo del marco normativo.** [`00·N6`](../../base/00-nucleo-blindado.md) es blindada y dice que una credencial no se escribe, no se registra y no se guarda. Todo lo de acá baja de ahí.

Lo que **no** cubre, y hay que decirlo: una clave ya escrita en el historial de versiones no se saca desde la plataforma.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Tapar al teclear | Clave entre comillas · sin comillas · dos en el mismo texto |
| El nombre de la variable | Que quede intacto |
| Que NO pase | Que se altere un documento importado · que se escriba sin enmascarador |
| El texto limpio | Que salga idéntico |
| El aviso | Sobre los 1 002 documentos reales |

## 11. Criterios de aceptación

- `CA-1` Una clave tecleada al llenar un espacio queda tapada.
- `CA-2` Se dice cuántas se taparon.
- `CA-3` Lo importado no se altera.
- `CA-4` Lo que no se tapa se dice, con su nombre.
- `CA-5` Sin enmascarador no se escribe.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **Se tapa lo que se teclea, no lo que se copia** | Tapar en los seis caminos | Medido: alteraría 7 documentos reales sin vuelta atrás, y los 21 fragmentos son ejemplos escritos |
| **La importación avisa en vez de tapar** | Callarse | Perder en silencio es perder igual |
| **El reconocimiento se usa por un puente** | Copiarlo dentro de la plataforma | Dos listas de secretos se separan, y la vieja deja pasar una clave |
| **Sin enmascarador se revienta** | Escribir el texto tal cual | Escribir sin tapar es el daño que esto viene a evitar |
| **Se devuelve cuántas se taparon** | Tapar en silencio | El usuario tiene que saber que lo que escribió no quedó igual |
| **Cada camino se declara acá** | Dejarlo implícito en el código | El camino que nace sin declararse es el que va a dejar pasar la próxima |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-031 | RF-31 | [HU-001 Tapar la clave al escribirla](../epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/HU-001-tapar-la-clave-al-escribirla.md) | [C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia](../epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia/estado-fase.md), cerrada el 2026-09-01 |

## 14. Cruces con otros módulos

- **Auditoría:** fue el primer camino que tapó, y de ahí nació el puente.
- **Ciclo de vida:** es el camino que teclea, y el que esta especificación agrega.
- **Importación:** no tapa, y avisa. Es la decisión que más se discutió.
- **El estándar:** aporta el reconocimiento. Este módulo **no sabe** qué es una credencial.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| — | — | — | — |
