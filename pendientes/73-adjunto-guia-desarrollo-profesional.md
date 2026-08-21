# Guía: el paso a paso lógico del desarrollo de software

> **Adjunto del [pendiente 73](73-la-guia-del-desarrollo-profesional-es-doctrina-del-estandar-no-de-un-proyecto.md).** Copia literal de `documentacion/guia-desarrollo-profesional.md` del proyecto **matematica** (2026-08-21), traída acá para que quien resuelva el pendiente tenga el material de partida sin salir de este repositorio. Los enlaces relativos internos apuntan a rutas de aquel proyecto y acá no resuelven. Este adjunto se borra al cerrar el pendiente.

**Para qué sirve este documento.** Resume, en lenguaje llano, el ciclo que sigue cualquier desarrollo de software profesional (no importa el proyecto ni la tecnología) y las cualidades que un producto debe tener para poder ponerse en producción. Salió de la sesión del 2026-08-21, respondiendo dos preguntas del usuario; queda acá porque aplica a todo lo que se construya en este repositorio.

---

## Primera parte: los 10 pasos del proceso

El orden es el mismo para cualquier software, del más chico al más grande. Cambia la formalidad, no el orden.

1. **Entender la necesidad.** Qué problema hay que resolver y para quién, en lenguaje de negocio, sin hablar todavía de tecnología. Si esto está mal, todo lo demás queda bien construido sobre el problema equivocado.

2. **Analizar el contexto.** Qué existe hoy (sistemas, procesos, datos), qué restricciones hay (presupuesto, normas, stack obligatorio) y qué es éxito medible. Aquí nace la decisión de tecnología, no antes: la tecnología es consecuencia del problema.

3. **Delimitar el alcance.** Qué entra, qué no entra, y qué se deja explícitamente para después. El "qué no" es tan importante como el "qué sí": los proyectos no mueren por lo que hacen sino por lo que se les fue sumando.

4. **Descomponer en unidades.** El alcance se parte en piezas con valor propio (épicas, y estas en historias de usuario), cada una con **criterios de aceptación**: la definición verificable de "esto quedó bien". Sin criterio de aceptación no hay forma objetiva de decir "terminé".

5. **Especificar y planificar cada unidad.** Antes de codificar: qué archivos se tocan, qué cambia técnicamente, cómo se prueba, cómo se revierte si sale mal, y quién lo aprueba. El plan se aprueba primero y se ejecuta después; no se renegocia a mitad de camino.

6. **Implementar.** Escribir el código siguiendo el plan. Si aparece algo no previsto, se para y se replanifica; no se improvisa en silencio.

7. **Probar contra los criterios.** No "ver si funciona": ejecutar los casos diseñados en el plan de pruebas y registrar qué dio cada uno. Un criterio sin prueba ejecutada no está cumplido, aunque "se haya visto andar".

8. **Documentar y cerrar.** Qué quedó hecho, qué decisiones se tomaron y por qué, qué deuda quedó declarada. Es lo que permite que otra persona (o uno mismo en seis meses) retome sin arqueología.

9. **Entregar y desplegar.** Poner la unidad en manos del usuario real, con migración de datos y plan de reversión si aplica.

10. **Mantener y evolucionar.** Lo entregado genera aprendizaje y pedidos nuevos, que vuelven a entrar por el paso 1. El desarrollo no es una línea: es este ciclo repetido por cada unidad.

### Cómo se vivió en este proyecto

| Paso | Dónde quedó en este repositorio |
|---|---|
| 1. Necesidad | [prompts/matematica-planteamiento.md](../prompts/matematica-planteamiento.md) |
| 2. Análisis y stack | [analisis/analisis-del-proyecto.md](../analisis/analisis-del-proyecto.md) |
| 3. Alcance | [epicas/EP-001.../epica.md](epicas/EP-001-metodos-numericos-en-python/epica.md) secciones 5.1 a 5.4 |
| 4. Unidades con criterios | [HU-001](epicas/EP-001-metodos-numericos-en-python/HU-001-esqueleto-del-proyecto-python/HU-001-esqueleto-del-proyecto-python.md) con sus 5 CA |
| 5. Planes aprobados | `plan_trabajo.md` y `plan_pruebas.md` de la fase A |
| 6. Implementación | `proyectos/matematica-python/` |
| 7. Pruebas contra criterios | `resultado_pruebas.md` de la fase (6 de 6 casos) |
| 8. Cierre | `funcionalidad_implementada.md` y los commits |
| 9 y 10 | Llegarán cuando haya algo que entregar |

La trampa clásica es saltar del paso 1 al 6: "ya sé qué quiero, empecemos a programar". Funciona los primeros días y se paga después con alcance sin control, código sin pruebas y decisiones que nadie recuerda. El estándar instalado en este proyecto existe para hacer ese salto imposible.

---

## Segunda parte: las cualidades del producto

Los 10 pasos son la **disciplina del proceso**: garantizan que nada se salte y que todo sea verificable y rastreable. Pero "listo para producción" exige además que el **producto** tenga cualidades técnicas propias. El proceso obliga a preguntarse por ellas en el momento correcto; el trabajo de dárselas es aparte.

1. **Seguridad.** Entradas validadas, contraseñas y secretos fuera del código, permisos por rol, protección contra inyección SQL, XSS y CSRF. En este proyecto ya apareció: las credenciales de MySQL van por variables de entorno, y la `SECRET_KEY` de desarrollo quedó declarada como deuda que debe salir del código antes de cualquier despliegue.

2. **Manejo de errores.** El sistema falla con mensajes útiles para el usuario y registros útiles para quien mantiene, sin exponer detalles internos y sin dejar datos a medias (operaciones todo o nada).

3. **Datos protegidos.** Respaldos automáticos y **probados** (un respaldo que nunca se restauró es una esperanza, no un respaldo), migraciones reversibles, datos personales tratados según la norma que aplique.

4. **Pruebas automatizadas.** Una suite que cualquiera corre en un comando y que detecta regresiones cuando el cambio de hoy rompe lo de hace tres meses.

5. **Reproducibilidad.** El entorno se levanta desde cero con instrucciones escritas (acá: `uv sync`); nada depende de "la máquina donde funciona".

6. **Observabilidad.** Logs, y enterarse de que el sistema se cayó antes de que lo llame el usuario. En producción real: monitoreo y alertas.

7. **Rendimiento bajo carga real.** No el dato de prueba de 10 filas, sino el volumen que habrá en un año.

8. **Despliegue repetible y reversible.** Publicar una versión nueva es un procedimiento aburrido y documentado, no una operación heroica; y si sale mal, se vuelve atrás en minutos.

9. **Documentación de operación.** Cómo instalar, configurar, respaldar y recuperar, escrita para quien no estuvo en el desarrollo.

### Cómo lo modela el estándar de este proyecto

Los 10 pasos viven en las reglas de flujo de trabajo del estándar (siempre obligatorias). Varias cualidades del producto son los **patrones opt-in** del `CLAUDE.md`: registros inmutables (`15`), despliegue e infraestructura (`18`), observabilidad y operación (`19`). Hoy están en "no" porque un proyecto local personal no los exige; el día que esto se publique para estudiantes reales, encenderlos es parte del paso 9.

---

## La frase que lo resume

**El proceso hace que el desarrollo sea confiable; las cualidades hacen que el producto lo sea.** Un equipo con proceso perfecto puede producir software frágil si nunca prueba un respaldo, y un producto técnicamente sólido construido sin proceso es imposible de mantener porque nadie sabe por qué es como es. Profesional es tener las dos cosas.
