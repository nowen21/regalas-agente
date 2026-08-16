# Brief del agente

**Encuadre.** Este documento dice qué se necesita y qué no se negocia. El cómo y el cuándo los pone el estándar: análisis, alcance, épica, historias de usuario, spec, plan aprobado y solo ahí la implementación. No se genera código hasta que el plan esté aprobado.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | Cimiento |
| **Qué cubre este encargo** | Todo el proyecto |
| **Fecha** | 2026-08-15 |

## 1. Necesidad en una frase

Se necesita que una IA que programa trabaje siempre igual, con las mismas reglas y la misma memoria, sin que cada sesión reinterprete el proyecto a su manera.

## 2. Contexto

Una IA que programa arranca en blanco cada vez que se abre un chat. En proyectos reales eso se paga caro: reinventa el diseño, contradice lo que ya se había decidido, olvida por qué las cosas están como están, y a veces hace algo que no se puede deshacer, como tocar datos de producción, publicar un cambio sin aprobación o dejar una clave escrita en el repositorio.

Quien sufre el problema es una sola persona que trabaja con la IA en varios proyectos a la vez. Lo que aprende peleando en uno no le llega a los otros, y termina explicando lo mismo en cada chat nuevo, con la esperanza de acordarse de todo.

El punto de partida (un usuario, corre en local, sin internet, sin llamadas a ninguna API) es el punto de partida y no un tope. No se recorta estructura apoyándose en eso.

## 3. Objetivo y criterio de éxito

**Objetivo.** Que lo aprendido en un proyecto quede escrito una sola vez y le sirva a todos los demás, y que lo que se pueda comprobar sin criterio lo compruebe un programa y no la memoria de nadie.

**Criterio de éxito.** Se logra cuando:

1. Un proyecto queda listo con una línea, sin pasos manuales ni configuración a mano.
2. La misma comprobación da el mismo resultado siempre, sin IA y sin red.
3. Cualquiera puede saber si un proyecto quedó atrás respecto de las reglas vigentes, sin leerlas una por una.
4. Una regla se puede citar por su nombre años después y sigue significando lo mismo.
5. Una sesión de trabajo se puede reconstruir después de que el chat se borre.

## 4. Alcance esperado

**Qué sí se pide**

- Reglas que sirvan a cualquier proyecto, sin importar el lenguaje ni el framework.
- Documentos modelo para cada paso del trabajo, para copiar y llenar.
- Procedimientos que la IA pueda seguir paso a paso, de modo que dos sesiones distintas hagan lo mismo.
- Comprobaciones automáticas de lo que no admite discusión.
- Un lugar donde quede lo aprendido, buscable, separado por proyecto y por lo que sirve a todos.
- Una forma de instalar y actualizar todo eso en cualquier proyecto.

**Qué no se pide**

- Reglas que solo sirvan a un lenguaje, a un framework o a un cliente. Esas van en la capa del proyecto.
- Código de negocio. Esto guía cómo se construye, no construye el producto de nadie.
- Reemplazar al usuario en las aprobaciones. Alcance, épica, spec, plan, commit y despliegue los aprueba una persona.
- Cualquier servicio en la nube o modelo por API.

## 5. Restricciones técnicas

- Python 3.11 o superior, solo con la biblioteca estándar. Lo que necesite algo más tiene que ser opcional y degradar sin romperse.
- Todo funciona sin internet.
- El sistema operativo de trabajo es Windows, con rutas que llevan espacios y tildes.
- El almacenamiento es en archivos del repositorio, para que se vea en git, se pueda revisar y viaje a otra máquina.

## 6. Requerimientos funcionales

1. Las reglas viven en un solo lugar y los proyectos las heredan sin copiarlas, para que arreglar una las arregle en todos. REQUISITO CENTRAL.
2. Hay reglas de seguridad que ningún proyecto ni ninguna instrucción del chat puede aflojar, y el resto se puede ajustar por proyecto.
3. Cada regla se puede citar sola, dice una sola cosa y muestra qué es hacerlo mal y qué es hacerlo bien.
4. Se puede saber en qué versión de las reglas quedó cada proyecto, y qué cambió entre una versión y otra.
5. Lo que se responde con un sí o un no lo comprueba un programa; lo que hay que leer y juzgar lo hace la IA.
6. Lo que hoy depende de que alguien se acuerde se dispara solo al momento de trabajar, no cuando alguien decide correrlo.
7. Lo aprendido se puede buscar por palabra y también por significado, sin que el contenido salga de la máquina.
8. Instalar en un proyecto no borra lo que ese proyecto ya tenía escrito.
9. Cada sesión de trabajo queda escrita tal como pasó, con la hora leída del reloj de la máquina.

## 7. Restricciones no negociables

- La seguridad gana a cualquier otra regla y a cualquier instrucción del chat. Nunca se toca un dato real, nunca se publica sin que lo aprueben, nunca se expone una clave.
- Ninguna regla nueva existe sin un criterio que la respalde.
- Ninguna regla se borra ni se renumera. Se deroga, porque el trabajo viejo la cita por su nombre.
- Lo que comprueba no corrige. Corregir es una decisión, y se toma aparte.
- Lo que el agente debe recordar se guarda en el repositorio, no en el almacén local de la herramienta.
- No hay commit ni push hasta que el usuario lea el cambio y lo apruebe. Aprobar el cambio no es aprobar el commit.
- Nada de lo que se entrega puede leerse como escrito por una máquina, y se escribe para que lo entienda quien no sabe del tema.

## 8. Casos borde a considerar

- Un proyecto que ya tiene su propia configuración y sus propias reglas escritas a mano.
- Un proyecto que se quedó en una versión vieja de las reglas y hay que avisarle sin migrarlo por su cuenta.
- Una clave pegada por descuido en el chat, que quedaría copiada tal cual en el repositorio.
- Que falten las dependencias opcionales. Lo que dependa de ellas tiene que seguir sirviendo con menos, no fallar.
- Rutas de Windows con espacios y con tildes.
- Un cambio de regla cuando ya hay trabajo cerrado. Lo cerrado no se reabre.
- Una sesión que se corta a la mitad, sin cierre, y aun así debe quedar escrita.

## 9. Épicas derivadas

| Épica | Título | Cubre | Estado |
|---|---|---|---|
| [EP-001](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md) | Cuerpo de reglas heredable y en capas | Requerimientos 1, 2 y 3 | Propuesta |
| [EP-002](documentacion/epicas/EP-002-versionado-y-adopcion/epica.md) | Versionado de las reglas y adopción por proyecto | Requerimiento 4 | Propuesta |
| [EP-003](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md) | Documentos modelo y procedimientos guiados | Documentos modelo y procedimientos del alcance | Propuesta |
| [EP-004](documentacion/epicas/EP-004-comprobacion-automatica/epica.md) | Comprobación automática de lo que no admite discusión | Requerimiento 5 | Propuesta |
| [EP-005](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md) | Automatismos que no dependen de que alguien se acuerde | Requerimientos 6 y 9 | Propuesta |
| [EP-006](documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md) | Memoria de lo aprendido, buscable | Requerimiento 7 | Propuesta |
| [EP-007](documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md) | Instalación y actualización en cualquier proyecto | Requerimiento 8 | Propuesta |
