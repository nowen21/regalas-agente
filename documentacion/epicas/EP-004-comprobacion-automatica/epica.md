# EP-004 — Comprobación automática de lo que no admite discusión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-004 |
| **Brief de origen** | [planteamiento.md](../../../planteamiento.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | L |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Una regla escrita se cumple cuando alguien se acuerda de cumplirla. Eso no alcanza. Buena parte de lo que exigen las reglas se responde con un sí o un no, sin opinión: el documento tiene la sección o no la tiene, el enlace apunta a algo que existe o no, el mensaje del commit tiene la forma acordada o no.

Esta épica construye los programas que responden esas preguntas. Corren sin IA, sin internet y dan el mismo resultado siempre. Lo que requiere leer y juzgar sigue siendo trabajo de la IA y no se intenta automatizar.

Estos programas reportan y no corrigen. Corregir es una decisión, y quien la toma es la persona.

## 3. Problema y oportunidad

### 3.1 Situación actual

El cumplimiento se revisa leyendo. Cuando el trabajo crece, nadie relee todo, así que las fallas de forma pasan y se descubren meses después, cuando ya cuesta arreglarlas.

### 3.2 Impacto de no hacerlo

Las reglas quedan sin piso: se puede incumplir una durante meses sin que nada lo note. Y la IA se vuelve el único control, cuando es justamente la que puede equivocarse.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Revisiones a mano de trabajo ya entregado | Aparecen fallas de forma que estaban desde el principio: enlaces rotos, secciones faltantes, nombres fuera de convención |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que todo lo que se responde con un sí o un no lo compruebe un programa, y que su resultado sea el mismo siempre, sin importar quién ni cuándo lo corra.

**Hipótesis de valor.** Si la comprobación es mecánica, el incumplimiento se ve el mismo día y no seis meses después. Se sabrá cuando una falla de forma deje de aparecer en las revisiones a mano, porque el programa ya la atajó antes.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| La persona | Deja de revisar a mano lo que una máquina revisa mejor | Cualitativo |
| El proyecto | El incumplimiento se ve el mismo día | Cualitativo |
| Las reglas | Se sabe cuáles se incumplen siempre, que es señal de que están mal escritas | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un programa por familia de comprobación, que reporte los hallazgos con su regla y su ubicación.
- El criterio escrito de qué entra: si dos personas pueden discutir si se cumplió, no entra.
- La marca, en cada regla, de si es comprobable o no.
- Una forma de correr todas las comprobaciones de una sola vez.
- Que la salida diga qué falló, dónde y qué regla es, para poder arreglarlo sin adivinar.

### 5.2 Fuera del alcance

- Corregir lo que se encuentra. Estos programas reportan.
- Juzgar si algo está bien escrito o bien diseñado. Eso es criterio.
- Dispararse solos en el momento de trabajar. Eso es EP-005.

### 5.3 Diferido

- Comprobaciones que necesiten que el proyecto declare sus convenciones propias, como dónde viven sus módulos. **Retomado el 2026-08-14 en [HU-010](HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md)**, que empieza por definir esa declaración y después compara contra ella.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Comprobar sin opinión lo que las reglas exigen y se puede responder con un sí o un no |
| 2 | Actores | La persona que corre las comprobaciones, la IA que las corre antes de entregar, el programa que las dispara |
| 3 | Información | Cada hallazgo dice qué regla, en qué archivo, en qué línea y qué se esperaba |
| 4 | Campos | Un hallazgo tiene campos definidos: regla, ubicación, severidad, qué se encontró y qué se esperaba. El detalle baja a la historia de usuario |
| 5 | Validaciones | Un hallazgo sin regla asociada no sirve; una comprobación sin salida clara tampoco |
| 6 | Reglas de negocio | Lo que reporta no corrige; lo discutible no entra; el mismo insumo da siempre el mismo resultado |
| 7 | Estados y transiciones | Un hallazgo es falla, que detiene, o aviso, que informa. Una regla está marcada como comprobable o no |
| 8 | Operaciones | Correr una comprobación, correr todas, ver el resultado, marcar una regla como comprobable |
| 9 | Restricciones | Ninguna comprobación modifica archivos; ninguna necesita internet; ninguna necesita IA |
| 10 | Relaciones | Cada comprobación se apoya en una o varias reglas y las cita por su identificador |
| 11 | Consultas | Ver los hallazgos de una corrida, filtrarlos por regla y por severidad |
| 12 | Mensajes | La salida dice qué falló y cómo se arregla. Cuando detiene el trabajo, dice también cómo saltarse el control y cuándo es válido hacerlo |
| 13 | Errores | Archivo que no existe, formato que no se puede leer, regla citada que fue derogada |
| 14 | Permisos | No aplica porque corre en la máquina de quien trabaja |
| 15 | Auditoría | Cada corrida puede dejar registro de cuántos hallazgos hubo por regla |
| 16 | Resultado final | La épica está completa cuando lo comprobable de las reglas lo comprueba un programa, y la salida alcanza para arreglar sin adivinar |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 21 | Indicadores | Cuántos hallazgos por regla, para descubrir la regla que se incumple siempre |
| 23 | Volumen | Cientos de archivos por proyecto. La corrida completa tiene que ser rápida o nadie la usa |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La persona | Corre las comprobaciones antes de aprobar | Un resultado claro, sin falsos positivos |
| La IA | Las corre antes de entregar | Saber qué arreglar y dónde |

**Volumetría estimada.** Cientos de archivos por proyecto, varias decenas de comprobaciones.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Existe el criterio escrito de qué se comprueba con un programa y qué queda como criterio.
- [ ] **CAE-02** Cada regla está marcada como comprobable o no.
- [ ] **CAE-03** Las comprobaciones corren sin IA, sin internet y dan el mismo resultado siempre.
- [ ] **CAE-04** Ninguna comprobación modifica archivos.
- [ ] **CAE-05** La salida de un hallazgo alcanza para arreglarlo sin abrir el código de la comprobación.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Reglas comprobables que ningún programa revisa | Todas, hoy | Ninguna | Al terminar la épica | Marca de comprobable en cada regla |
| Fallas de forma encontradas a mano después de entregar | Sin medir | Que bajen | Después de tres trabajos | Revisiones |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| [HU-001](HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md) | Fijar el criterio de qué se comprueba con un programa | Must | S |
| [HU-002](HU-002-marca-de-comprobable-en-cada-regla/HU-002-marca-de-comprobable-en-cada-regla.md) | Marcar en cada regla si es comprobable | Must | M |
| [HU-003](HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md) | Definir el formato de un hallazgo y su severidad | Must | S |
| [HU-004](HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md) | Comprobar la forma de los documentos y sus espacios sin llenar | Must | M |
| [HU-005](HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) | Comprobar los enlaces y las citas a reglas | Must | M |
| [HU-006](HU-006-nomenclatura-y-estructura/HU-006-nomenclatura-y-estructura.md) | Comprobar la nomenclatura y la estructura de carpetas del trabajo | Must | M |
| [HU-007](HU-007-claves-y-datos-sensibles/HU-007-claves-y-datos-sensibles.md) | Comprobar que no salgan claves ni datos sensibles | Must | M |
| [HU-008](HU-008-corrida-completa/HU-008-corrida-completa.md) | Correr todas las comprobaciones de una sola vez | Must | S |
| [HU-009](HU-009-conteo-por-regla/HU-009-conteo-por-regla.md) | Registrar cuántos hallazgos hubo por regla | Should | S |
| [HU-010](HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) | Comprobar el código contra la convención que el proyecto declara | Must | L |
| [HU-011](HU-011-molde-de-las-reglas/HU-011-molde-de-las-reglas.md) | Comprobar que cada regla del estándar cumple su propio molde | Must | M |
| [HU-012](HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md) | Comprobar las marcas de generación automática en lo que se entrega | Should | S |
| [HU-013](HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) | Comparar el plan aprobado con lo que se hizo | Must | M |
| [HU-014](HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) | Que el veredicto de una fase no diga dos cosas distintas | Must | S |
| [HU-015](HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md) | Comprobar que no haya una regla derogada sin adoptar antes de avanzar de fase | Must | S |
| [HU-016](HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) | Comprobar que un pendiente marcado hecho nombre la historia y la fase donde se construyó | Should | S |
| [HU-017](HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) | Decir cuántas HU quedan sin su fase completa | Should | S |
| [HU-018](HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md) | Avisar cuando dos pendientes se disputan el mismo número | Should | S |
| [HU-019](HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md) | Que el inventario de historias deje de mantenerse a mano | Should | S |
| [HU-020](HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano/HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md) | Que el inventario que heredan los proyectos tampoco se mantenga a mano | Should | S |
| [HU-021](HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) | Que la cuenta distinga lo terminado de lo cumplido | Must | M |
| [HU-022](HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md) | Que un documento que sigue siendo el molde no cuente como escrito | Must | S |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Programas de comprobación | Nuevo | |
| Cuerpo de reglas | Modificado | Cada regla gana la marca de comprobable |

### 10.2 Decisiones de arquitectura

- Los programas reportan y no corrigen. Lo que corrige va aparte y se corre a propósito, porque romper eso vuelve impredecible todo lo demás.
- Se escriben con la biblioteca estándar del lenguaje, sin dependencias, para que corran en cualquier máquina sin instalar nada.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Determinismo | El mismo insumo da el mismo resultado |
| Rendimiento | La corrida completa no puede demorar tanto que la gente la evite |
| Autonomía | Sin internet y sin IA |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-001, porque se comprueba contra reglas escritas | Interna | Bloqueante |
| DEP-02 | EP-003, porque buena parte de lo comprobable es la forma de los documentos modelo | Interna | Bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Falsos positivos que hagan perder la confianza | Alta | Alto | Lo dudoso sale como aviso, nunca como falla |
| R-02 | Que se intente comprobar lo que es criterio | Media | Alto | El criterio de qué entra se escribe primero, en HU-001 |
| R-03 | Que la salida no alcance para arreglar y toque abrir el código | Media | Medio | El formato del hallazgo se define antes de escribir las comprobaciones |

## 13. Supuestos y restricciones

**Supuestos**

- La mayoría de las fallas repetidas son de forma, no de fondo.

**Restricciones**

- Sin dependencias externas, sin red, y tiene que correr en Windows con rutas que llevan espacios y tildes.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Criterio, marca y formato del hallazgo | HU-001, HU-002, HU-003 |
| Fase 2 | Comprobaciones de documentos y enlaces | HU-004, HU-005 |
| Fase 3 | Comprobaciones de estructura y de datos sensibles | HU-006, HU-007 |
| Fase 4 | Corrida completa y conteo por regla | HU-008, HU-009 |
| Fase 5 | El estándar comprobándose a sí mismo, y el proyecto contra lo que declara | HU-010, HU-011, HU-012 |
| Fase 6 | Un documento contra otro: el plan contra lo hecho, y el veredicto contra sí mismo | HU-013, HU-014 |
| Fase 7 | Retrodocumentar la comprobación de la derogación sin adoptar, que se construyó antes de tener su fase | HU-015 |
| Fase 8 | Que el backlog no se construya saltándose la cadena: el pendiente cerrado nombra su fase | HU-016 |
| Fase 9 | Contar lo que falta sin recorrerlo a mano: HU sin fase y números de pendiente disputados | HU-017, HU-018 |
| Fase 10 | Que la cuenta no exista dos veces: el inventario enlaza lo que el árbol sabe en vez de copiarlo | HU-019 |
| Fase 11 | Que lo mismo llegue a quien hereda el estándar: la plantilla y la comprobación | HU-020 |
| Fase 12 | Que el número que dice cuánto falta no cuente como hecha una fase que no cumplió | HU-021 |
| Fase 13 | Que una fase recién abierta no cuente como terminada: el molde sin llenar no es un documento | HU-022 |

## 15. Definition of Ready

- [ ] Criterio de qué se comprueba acordado
- [ ] Formato del hallazgo definido

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Ninguna comprobación modifica archivos
- [ ] Ninguna comprobación necesita red ni IA
- [ ] Cada regla marcada como comprobable tiene su programa

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
