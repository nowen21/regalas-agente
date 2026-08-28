# La orden se resuelve de una, no se vuelve pendiente

**Qué se pide.** Cuando el usuario da una orden de trabajo, se ejecuta de una: no se convierte en un pendiente del backlog. Si al ejecutar aparece un impedimento real, se **muestra** con la evidencia para analizarlo juntos, y no se toman determinaciones unilaterales (ni abrir el pendiente, ni elegir la salida por él).

**Por qué.** El 2026-08-21 el usuario ordenó crear `plantillas/ciclo-vida-proyectos/` con sus moldes, y el agente, al encontrar que las rutas estaban amarradas al código, creó un pendiente con las opciones en vez de resolver. El usuario corrigió: «no hay que crear pendiente de pendientes, hay que dar solución de una y si hay algún pendiente mostrarlo para analizar el caso pero no tomar determinaciones de una». El backlog es para lo que **no** se ordenó todavía; lo ordenado se hace.

**Cómo se aplica.** Ante una orden: ejecutar. Ante un impedimento a mitad de la orden: parar, mostrar el impedimento con lo verificado y las salidas posibles, y esperar la decisión en el chat — sin abrir pendientes ni elegir por cuenta propia. El pendiente queda solo para lo que el usuario explícitamente difiera.

**Y el 2026-08-27 el usuario lo dijo de la forma más corta:** ante un defecto de una línea encontrado a mitad de una fase, el agente propuso arreglarlo **y además** abrir un pendiente por el patrón de fondo. El usuario cortó: *«para qué dejar pendientes si se puede solucionar?»*. **Un pendiente no es un lugar donde guardar lo que ya se puede hacer**: es para lo que de verdad no se puede resolver ahora. Anotar en vez de arreglar convierte el backlog en el sustituto de trabajar.

**Ya pasó, el mismo día.** Minutos después de esta corrección, el agente la leyó como «ejecute ya» y **eligió él la salida** (mover los moldes) cuando el usuario no había escogido entre las dos opciones mostradas. El usuario paró el trabajo: «esa era la corrección que le estaba haciendo e hizo todo lo contrario». Las dos mitades valen juntas: resolver de una **lo ordenado**, y no decidir **lo abierto** — que el usuario pida velocidad no convierte una decisión suya en decisión del agente.
