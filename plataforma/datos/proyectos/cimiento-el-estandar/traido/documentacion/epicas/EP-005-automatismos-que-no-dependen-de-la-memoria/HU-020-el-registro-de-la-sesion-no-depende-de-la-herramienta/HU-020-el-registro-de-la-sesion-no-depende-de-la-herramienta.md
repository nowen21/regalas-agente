# HU-020 — Que el registro de la sesión no dependa de con qué herramienta se escribió

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-020 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Enganches |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien va a guardar el trabajo de una conversación
- **Quiero** que quede registrado lo que la sesión tocó, sin importar cómo lo escribió
- **Para** que la comprobación que evita llevarse trabajo ajeno tenga con qué compararlo

---

## 3. Contexto y descripción

**Un commit se llevó 712 líneas de trabajo ajeno**, barridas por un `git add -A`. La comprobación que existe para eso —*«el commit no se lleva lo ajeno»*— **corrió y dijo OK**.

Pregunta si lo que entra al commit **lo tocaron dos sesiones registradas**. A esos archivos **no los había registrado ninguna**, así que no había colisión que ver. Es `S-071`.

### Por qué no basta con afinar la comprobación

Se propuso avisar de los archivos **sin registro** cuando al menos uno de los que entran sí lo tuviera. **Medido sobre los últimos doce commits: avisaría en siete, con hasta 31 archivos de una vez.**

| Commit | Archivos | Sin registro |
|---|---|---|
| `6abffdc` | 55 | **31** |
| `b3df9f1` | 34 | **13** |
| `ef22e79` | 34 | **11** |

**Porque el registro se llena solo desde las herramientas de escritura**, y la mayoría de los archivos los escriben guiones que se corren en la terminal. Así que *«sin registro»* no significa *«de otro»*: significa *«escrito como se escribe casi todo»*.

**El hueco por el que entró lo ajeno es el mismo por el que pasa casi todo lo propio.** Con ese registro no hay forma de separarlos, y afinar la comprobación sería afinar un instrumento que mide otra cosa. Es `S-072`.

### Lo que sí lo separa

**Que el registro anote lo que cambió, mire quien lo mire.** Al terminar cada turno, la sesión anota **los archivos cuya última modificación cae dentro de ese turno**.

Con eso, el caso del daño se detecta solo:

| Quién escribió | Quién lo anota | Qué pasa |
|---|---|---|
| Solo esta sesión | Solo esta | Sin colisión. Correcto |
| **Otra sesión, mientras esta trabajaba** | **Las dos** | **Colisión: la comprobación de hoy la ve** |
| Nadie durante el turno | Ninguna | No se reclama lo que no se tocó |

**No hace falta una comprobación nueva.** La que existe empieza a funcionar cuando su registro deja de tener el hueco.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | El registro anota **lo que cambió en el turno**, sin mirar qué herramienta lo escribió | `S-072` |
| RN-02 | Solo se anota lo modificado **dentro de la ventana del turno** | Reclamar lo de antes atribuiría trabajo viejo a quien pasaba por ahí |
| RN-03 | **Anotar de más se prefiere a anotar de menos**, y es lo que hace que la colisión se vea | Si dos sesiones anotan el mismo archivo, la comprobación lo dice |
| RN-04 | Lo que ya anotaba el enganche de escritura **se conserva** | No se reemplaza lo que funciona: se le suma lo que le falta |
| RN-05 | El registro **no se versiona**, y sigue caducando a las doce horas | Ya es así, y versionarlo lo volvería el próximo archivo que dos sesiones se pisan |
| RN-06 | Si el enganche falla, **el turno termina igual** | Un automatismo que rompe la conversación se desinstala el mismo día |

### 3.2 Supuestos

- El enganche de fin de turno recibe el identificador de la sesión y la carpeta del proyecto. **Comprobado leyendo `hook_historico.py`**, que ya los usa.

### 3.3 Fuera de alcance

- **Cambiar la comprobación de sesiones.** Empieza a funcionar sola cuando el registro se completa.
- **Identificar quién escribió cada archivo.** No se puede y no hace falta: basta ver que dos sesiones lo tocaron.
- **Los archivos que ninguna sesión toca en su turno.** Siguen sin registro, y eso es correcto.

---

## 4. Criterios de aceptación

### CA-01 — Lo escrito fuera de las herramientas queda registrado

```gherkin
Dado que un guion escribe un archivo del proyecto durante el turno
Cuando el turno termina
Entonces ese archivo queda en el registro de la sesión
```

**Cómo validarlo:**
1. En un proyecto de prueba, escribir un archivo **sin usar las herramientas de escritura**.
2. Correr el enganche de fin de turno.
3. Leer el registro de la sesión. Resultado esperado: el archivo está.
- **Aprobado cuando:** el registro no depende de cómo se escribió.

### CA-02 — No se reclama lo que no se tocó en el turno

```gherkin
Dado un archivo modificado antes de que el turno empezara
Cuando el turno termina
Entonces ese archivo no entra al registro
```

**Cómo validarlo:**
1. Un archivo con fecha de modificación anterior al turno.
2. Correr el enganche.
3. Resultado esperado: **no está** en el registro.
- **Aprobado cuando:** un archivo viejo no se atribuye a quien pasaba por ahí.

**Este es el criterio que decide si sirve.** Sin él, la primera sesión del día reclamaría el árbol entero, y la comprobación pasaría de callar siempre a hablar siempre.

### CA-03 — Dos sesiones que tocan lo mismo producen colisión

```gherkin
Dado que dos sesiones registran el mismo archivo
Cuando ese archivo entra a un commit
Entonces la comprobación de sesiones avisa
```

**Cómo validarlo:**
1. Dos registros de sesión distintos, los dos con el mismo archivo.
2. Preparar ese archivo para el commit.
3. Correr la comprobación. Resultado esperado: **avisa**, y nombra el archivo.
- **Aprobado cuando:** el caso que causó el daño se detecta.

### CA-04 — Lo que ya se registraba se sigue registrando

```gherkin
Dado un archivo escrito con las herramientas de siempre
Cuando el turno termina
Entonces sigue estando en el registro, una sola vez
```

**Cómo validarlo:**
1. Escribir con la herramienta, y además correr el enganche de fin de turno.
2. Leer el registro. Resultado esperado: el archivo aparece **una sola vez**.
- **Aprobado cuando:** no se duplica ni se pierde nada de lo que ya funcionaba.

### CA-05 — Un fallo del enganche no rompe el turno

```gherkin
Dado que el enganche revienta por cualquier motivo
Cuando termina el turno
Entonces la conversación sigue
```

**Cómo validarlo:**
1. Romper el enganche a propósito.
2. Correrlo. Resultado esperado: termina en cero y sin decir nada.
3. Sin git, o sin carpeta de proyecto. Resultado esperado: lo mismo.
- **Aprobado cuando:** ninguna entrada mala detiene nada.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Corre al final de cada turno: se apoya en lo que git ya sabe, sin recorrer el árbol entero |
| RNF-02 | **No estorbar** | Un fallo no detiene la conversación ni escribe ruido |

---

## 6. Diseño y referencias

- **Dónde vive la lógica:** `validadores/sesiones.py`, que ya tiene `anotar` y el registro.
- **Dónde se dispara:** un enganche de fin de turno, junto a los dos que ya corren ahí.
- **La comprobación que se beneficia:** `validar_preparados`, **que no se toca**.
- **La medición que descartó el otro diseño:** [historico-chat/scripts/2026-08-28/](../../../../historico-chat/scripts/2026-08-28/).

---

## 7. Tareas técnicas derivadas

- [x] «Backend» Saber qué archivos cambiaron dentro de la ventana del turno.
- [x] «Backend» Anotarlos en el registro de la sesión, sin duplicar.
- [x] «Adaptador» El enganche de fin de turno, que nunca rompe nada.
- [x] «Documentación» Que el instalador lo cuelgue.
- [x] «Pruebas» Los cinco criterios, con el caso del archivo viejo.
- [x] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [A-EP-005-HU-020-el-turno-anota-lo-que-cambio](A-EP-005-HU-020-el-turno-anota-lo-que-cambio/) | CA-01 a CA-05 | (vacío) | [plan_trabajo](A-EP-005-HU-020-el-turno-anota-lo-que-cambio/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-020-el-turno-anota-lo-que-cambio/plan_pruebas.md) | [resultado](A-EP-005-HU-020-el-turno-anota-lo-que-cambio/resultado_pruebas.md) — **Cumple** | Terminada |

**La línea base, medida antes de abrir la carpeta:** `121 en total · 32 sin terminar · 89 terminadas, de las cuales 71 cumplen, 13 no cumplen y 5 no dicen si cumplen`.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que reclame archivos viejos y la comprobación pase a hablar siempre | `CA-02`, y es el criterio que decide |
| Riesgo | Que duplique lo que el enganche de escritura ya anota | `CA-04` |
| Riesgo | Que un fallo detenga el turno | `CA-05` y `RNF-02` |
| Riesgo | Que anotar de más produzca colisiones falsas | **Es deliberado.** Dos sesiones que tocan el mismo archivo **es** lo que hay que ver, aunque una solo lo haya leído en disco |
| Dependencia | Hace falta un enganche que hoy no se instala | Se agrega, como los diez que ya hay |

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

- [ ] Código implementado y revisado
- [ ] Pruebas unitarias escritas y en verde
- [ ] Criterios de aceptación validados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | El registro y la comprobación ya existen |
| **N**egociable | ☑ | Cómo se calcula la ventana se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Es la única comprobación que dejó pasar daño real medido: 712 líneas |
| **E**stimable | ☑ | Una función, un enganche y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios, con proyectos de prueba y fechas controladas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-28 | Agente, con el usuario | Creación de la HU. Sale de `S-071` y `S-072`. **La medición descartó el diseño obvio** —avisar de los archivos sin registro habría hablado en 7 de 12 commits— y llevó a arreglar el registro en vez de la comprobación |
