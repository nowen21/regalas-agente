# Pendiente · Una sesión publica en su commit el trabajo a medio hacer de otra

**Estado:** cerrado el 2026-08-22, en la fase [`A-EP-005-HU-017`](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-017-el-commit-no-se-lleva-lo-ajeno/A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones/funcionalidad_implementada.md) (v31.14.0) · anotado ese mismo día.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-017 — El commit no se lleva el trabajo de otra sesión](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-017-el-commit-no-se-lleva-lo-ajeno/HU-017-el-commit-no-se-lleva-lo-ajeno.md), escrita para este pendiente. Es un automatismo que faltaba, no una regla nueva: la de no commitear sin aprobación ya existe |
| **De dónde sale** | Hallazgo H-6 del resumen [2026-08-22 · sesión 2](../../historico-chat/resumenes/2026-08-22/sesion-2.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

El 2026-08-22, dos sesiones trabajaron a la vez sobre este repositorio. Una de ellas hizo `git add` de todo el árbol y commiteó. Los commits `7eaade3` (12:02) y `0e7e307` (12:10) se llevaron el trabajo que la otra sesión tenía a medio construir:

- Un archivo de pruebas sin sus dos últimos casos.
- `validadores/plantillas.py` **con un criterio que reprobaba documentos correctos**, y sin la corrección que evitaba 110 falsos positivos.
- Tres carpetas de fase con los moldes del andamio sin llenar.
- La subida de `VERSION` de `31.9.0` a `31.11.0`, que dejó viejo el número que declaraban los planes de las otras fases.

## Por qué importa

Durante ocho minutos, lo publicado fue la versión del validador que reprobaba lo que estaba bien. Un validador así es el caso borde que el [planteamiento](../../prompts/cimiento-planteamiento.md) nombra en §8: enseña a ignorar todos los veredictos, y desde ahí ninguno sirve.

Y hay una regla escrita que se incumplió sin que nadie pudiera notarlo: no hay commit hasta que el usuario lea el cambio y lo apruebe. El usuario aprobó **un** cambio, y en el commit viajó **otro** que ni siquiera estaba terminado.

El riesgo ya estaba listado como caso borde. Esta es la primera vez que se documenta ocurriendo con daño concreto.

## Qué falta

Que un commit no arrastre archivos que otra sesión tiene abiertos. Dos salidas:

1. **Que cada sesión declare lo que está tocando**, en un archivo de la carpeta de trabajo, y que el enganche de `pre-commit` rechace el commit que incluya un archivo declarado por otra sesión viva. Es lo que de verdad lo impide, y cuesta más.
2. **Que el enganche avise** cuando entran archivos que la sesión que commitea no tocó, comparándolos con la traza de la sesión, que ya se guarda. Más barato, y no detiene: informa.

Conviene la segunda primero. La primera exige saber qué sesión está viva, y eso hoy no se sabe.

## El límite

No cubre dos personas en máquinas distintas: eso lo resuelve el control de versiones remoto, y acá todo corre en una sola máquina.

No cubre el caso de que la misma sesión commitee de más por descuido.

## Cómo se sabrá que cerró

Se abren dos sesiones, la primera deja un archivo modificado sin terminar, la segunda hace `git add -A` y commitea, y el enganche nombra ese archivo y dice de qué otra sesión es.

---

## Cómo se cerró — 2026-08-22

**Se tomó la segunda salida, la de avisar.** El enganche anota qué archivo toca cada sesión, y el `pre-commit` avisa cuando lo que entra al commit lo tocaron dos. No rechaza: retomar lo que otra dejó a medias es legítimo, y un enganche que rechaza siempre se apaga en una tarde.

**Y la primera salida resultó innecesaria.** Se había planteado que cada sesión declarara lo que está tocando para poder saber cuál está viva. No hace falta: la pregunta se dio vuelta. No se comprueba **de quién es el commit**, que `git` no sabe, sino si **mezcla dos sesiones**, que se ve desde los archivos. Un commit legítimo sale de una sola conversación.

Diez casos, cinco de ellos de lo que **no** debe avisar, que es lo que decide si esto sobrevive al primer mes.
