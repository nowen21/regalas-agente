# HU-020 — Que el inventario que heredan los proyectos tampoco se mantenga a mano

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-020 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada. Los cuatro criterios y su transversal, verificados el 2026-08-26 |
---

## 2. Narrativa

- **Como** quien recibe el estándar en su proyecto
- **Quiero** que el inventario de historias que me llega no me pida mantener una cuenta a mano
- **Para** no repetir el desfase que el estándar ya sufrió tres veces y acaba de quitarse

---

## 3. Contexto y descripción

La [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md) le quitó al estándar la cuenta escrita a mano. **Quedó a medias hacia afuera**, y en dos sitios distintos.

**La plantilla sigue enseñando lo que se acaba de quitar.** [`plantillas/inventario-hu.md`](../../../../plantillas/inventario-hu.md) trae los tres campos —`Total de HU`, `Completas`, `Incompletas`— con su `«N»` por llenar, una tabla de una fila por historia con seis casillas, y una sección de seis pasos titulada «Cómo se llena la tabla», donde el paso 6 dice que **la casilla la marca quien escribió el archivo**. Un proyecto que instale el estándar arma su inventario exactamente como el estándar lo armaba, con el defecto por el que se le desfasó tres veces.

**Y la comprobación que impide que vuelva mira una sola ruta.** `cuenta_escrita_a_mano` en `validadores/fases.py` busca en `pendientes/48-inventario-hu.md`, escrito fijo. La propia plantilla dice que en un proyecto el inventario vive en `documentacion/`, así que **la comprobación nunca lo ve**. Protege al estándar y a nadie más.

**Los proyectos sí pueden preguntar la cuenta.** Se verificó corriendo `validar.py fases --raiz <proyecto>` sobre un árbol de prueba: da la lista de lo que falta a cada historia **y** la línea con el total, las completas y las incompletas. Los validadores no se copian a los proyectos — los enganches los llaman en su sitio —, así que no hay nada que instalar para que esto funcione.

**Es la misma asimetría contada dos veces:** lo que el estándar arregló para sí mismo no llegó a quien lo hereda. Y en un estándar eso importa más que en un proyecto, porque **lo que reparte se multiplica**.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | La plantilla del inventario no trae campos de cuenta por llenar | Hallazgo H-31 del 2026-08-26 |
| RN-02 | Tampoco trae la tabla de una fila por historia, ni los pasos para llenarla a mano | El mismo |
| RN-03 | La plantilla dice con qué comando se obtiene la cuenta **desde un proyecto**, con su `--raiz` | Se verificó que funciona antes de escribirlo |
| RN-04 | La comprobación encuentra el inventario **donde el proyecto lo tenga**, no en una ruta fija | `cuenta_escrita_a_mano` hoy solo mira `pendientes/48-inventario-hu.md` |
| RN-05 | Lo que la plantilla enseña y no es derivable del árbol se conserva | La guía de en qué orden se escriben los documentos, y la distinción entre construir y retrodocumentar |
| RN-06 | El cambio de `plantillas/` suma entrada en el `CHANGELOG` y sube `VERSION` | `20·M10` |

### 3.2 Supuestos

- Los proyectos que heredan el estándar lo hacen con `instalar.py`, que deja los enganches llamando a los validadores en su sitio.
- El inventario de un proyecto se reconoce por traer los campos de la cuenta, no por su nombre de archivo.

### 3.3 Fuera de alcance

- **Cambiar los inventarios ya escritos en proyectos existentes.** La plantilla rige lo nuevo; lo viejo lo avisa la comprobación y lo arregla quien quiera.
- **Cambiar cómo se cuenta.** Sigue siendo de la `HU-017`.
- **Las demás plantillas.** Si otra enseña a mantener a mano algo derivable, sale de un barrido aparte.
- **Que un programa escriba el inventario de un proyecto.** Sigue prohibido por `EP-004 §10.2`.

---

## 4. Criterios de aceptación

### CA-01 — La plantilla ya no pide mantener una cuenta

```gherkin
Dado que un proyecto va a armar su inventario desde la plantilla
Cuando la abre
Entonces no encuentra campos de cuenta por llenar ni tabla de filas por historia
Y encuentra el comando que le da las dos cosas, con su «--raiz»
```

**Cómo validarlo:**
1. Abrir [plantillas/inventario-hu.md](../../../../plantillas/inventario-hu.md).
2. Buscar los rótulos «Total de HU», «Completas» e «Incompletas» como campo de tabla con un valor al lado. Resultado esperado: no aparecen.
3. Buscar la tabla con columnas `Épica`, `HU`, `Fase` y los cinco documentos. Resultado esperado: no aparece.
4. Buscar el comando. Resultado esperado: está escrito con `--raiz`, de forma que un proyecto lo pueda copiar y correr desde su propia carpeta.
5. Copiar ese comando y correrlo contra una carpeta de proyecto de prueba con al menos una historia. Resultado esperado: lista qué le falta a esa historia y termina con la cuenta.
- **Aprobado cuando:** ninguno de los tres rótulos aparece como campo, la tabla no está, y el comando que la plantilla nombra funciona al copiarlo.

### CA-02 — La comprobación encuentra el inventario donde el proyecto lo tenga

```gherkin
Dado un proyecto cuyo inventario vive en «documentacion/», no en «pendientes/»
Cuando ese inventario guarda un total escrito a mano
Entonces la comprobación lo reporta, nombrando el archivo
Y lo reporta igual si vive en cualquier otra carpeta del proyecto
```

**Cómo validarlo:**
1. Armar una carpeta de proyecto de prueba con `documentacion/epicas/` y una historia con su fase.
2. Escribir en `documentacion/inventario-hu.md` una fila `| **Total de HU** | 99 |`.
3. Correr `validar.py fases --raiz <proyecto de prueba>`. Resultado esperado: reporta ese archivo, con su ruta, diciendo que la cuenta sale del árbol.
4. Mover el archivo a otra carpeta del proyecto y volver a correr. Resultado esperado: lo reporta en la ruta nueva.
5. Quitarle la fila y correr otra vez. Resultado esperado: no reporta nada sobre ese archivo.
- **Aprobado cuando:** el reporte aparece en las dos ubicaciones y desaparece al quitar la fila.

### CA-03 — Lo que la plantilla enseña y no es derivable se conserva

```gherkin
Dado que la plantilla explica en qué orden se escriben los cinco documentos,
  y la diferencia entre construir y retrodocumentar
Cuando se le quitan la cuenta y la tabla
Entonces esas dos explicaciones siguen estando
Y sigue diciendo dónde vive el inventario y cuándo se da por cerrado
```

**Cómo validarlo:**
1. Antes de cambiar nada, listar las secciones de la plantilla y guardar la lista.
2. Aplicar el cambio.
3. Listar otra vez. Resultado esperado: siguen las secciones «Qué clase de trabajo es» y «Cómo se sabe que cerró», y sigue la guía del orden de los documentos.
4. Buscar dónde dice que el inventario vive donde el proyecto lleve su backlog. Resultado esperado: sigue diciéndolo.
- **Aprobado cuando:** ninguna explicación no derivable se perdió.

### CA-04 — La versión del estándar sube, porque cambió una plantilla

```gherkin
Dado que «20·M10» exige versionar todo cambio de «plantillas/»
Cuando la plantilla del inventario cambia
Entonces «VERSION» sube y el «CHANGELOG» gana su entrada
Y la entrada dice qué cambia para un proyecto que ya tenía el estándar
```

**Cómo validarlo:**
1. Anotar el contenido de [VERSION](../../../../VERSION) antes del cambio.
2. Aplicar el cambio.
3. Leer `VERSION`. Resultado esperado: subió el número **menor**, porque es aditivo: ningún proyecto al día queda obligado a hacer algo nuevo, y lo que aparece es un aviso.
4. Leer la primera entrada del [CHANGELOG](../../../../CHANGELOG.md). Resultado esperado: nombra la plantilla y la comprobación, y dice qué verá un proyecto que ya tenía el estándar.
5. Correr `validar.py versionado`. Resultado esperado: sin incumplimientos.
- **Aprobado cuando:** `VERSION` subió en su parte menor, el `CHANGELOG` tiene la entrada, y el validador de versionado pasa.

### Criterios de aceptación transversales

- [x] **No regresión** — lo existente sigue funcionando; la suite relacionada queda verde (`08`, `02·F5`). En particular, **las siete pruebas de la `HU-019` siguen pasando** con la comprobación generalizada.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Buscar el inventario no puede recorrer el proyecto entero en cada corrida: se limita a las carpetas donde el estándar dice que vive |
| RNF-02 | **Compatibilidad** | Un proyecto cuyo inventario esté en `pendientes/`, como el estándar, sigue funcionando igual |

---

## 6. Diseño y referencias

- **Lo que se cambia:** [plantillas/inventario-hu.md](../../../../plantillas/inventario-hu.md) y `cuenta_escrita_a_mano` en `validadores/fases.py`.
- **De dónde viene:** la [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md), que lo resolvió puertas adentro.
- **Lo que hay que respetar:** `EP-004 §10.2` y `DA-06` — el programa reporta y no corrige. `20·M10` — versionar.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] «Documentación» Quitar de la plantilla los campos de cuenta, la tabla y los pasos para llenarla.
- [ ] «Documentación» Escribir el comando con `--raiz`, verificado corriéndolo.
- [ ] «Backend» Que la comprobación encuentre el inventario donde el proyecto lo tenga.
- [ ] «Pruebas» Casos para el inventario fuera de `pendientes/`.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano`](A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/) | CA-01, CA-02, CA-03, CA-04 | (vacío) | [plan_trabajo](A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/plan_trabajo.md) | [plan_pruebas](A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/plan_pruebas.md) | [resultado](A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/resultado_pruebas.md) · cumple | Cerrada |

Los cuatro van juntos porque **cambiar la plantilla sin generalizar la comprobación deja el agujero al revés**: los proyectos nuevos harían lo correcto y nadie se lo estaría comprobando. Y `CA-04` no es separable: es la condición para que el cambio de plantilla exista según `20·M10`.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md), cerrada el 2026-08-26 | Bajo |
| Riesgo | Que buscar el inventario en un proyecto grande sea lento | Se busca solo en las carpetas donde el estándar dice que vive, no en todo el árbol (`RNF-01`) |
| Riesgo | Que la comprobación reporte archivos que no son inventarios pero traen esos rótulos | El reconocimiento pide el rótulo **como campo de tabla con un número**, que es la forma exacta que tenía el defecto |
| Riesgo | Que quitar la tabla se lleve la guía de proceso que sí sirve | `CA-03` existe para eso, y se comprueba listando secciones antes y después |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible — no aplica: no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [x] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [x] Código implementado y en rama principal
- [x] Pruebas unitarias e integración pasando — 381 de 381
- [ ] Code review aprobado — lo hace el usuario al aprobar la fase
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [x] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica: son programas que se corren a mano
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | Depende de la HU-019, que ya cerró |
| **N**egociable | ☑ | Qué se conserva de la plantilla se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Es lo que el estándar reparte, y lo que reparte se multiplica |
| **E**stimable | ☑ | Una plantilla, una función y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cuatro criterios se comprueban leyendo archivos y corriendo comandos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del hallazgo H-31, y de verificar que la comprobación de la HU-019 mira una ruta fija |
| 2026-08-26 | Agente | Cerrada la fase `A`. Los cuatro criterios cumplidos; tres defectos encontrados, dos corregidos y uno reportado por estar fuera de lo declarado (`S-045`, `S-046`, `S-047`) |
