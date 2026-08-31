# Funcionalidad implementada — Fase `A-EP-003-HU-012-una-sola-palabra-por-estado` (módulo Documentos modelo)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-012-una-sola-palabra-por-estado` |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-26 |
| **HU / CA cubiertas** | [HU-012](../HU-012-una-sola-palabra-para-cada-estado.md): `CA-01`, `CA-02`, `CA-03`, `CA-04` y sus dos transversales |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.0.0` |
| **Commit** | `a14f5ed` |

---

## 1. Qué se implementó — resumen

**«Terminado» se escribe de una sola forma.** Era `Completada` en el molde de la épica, `Done` en el de la historia y `Hecha` en el de la tarea. Ahora es **`Terminada`** en los tres.

**Y se define en un solo sitio.** El glosario gana su sección 5 con los nueve estados y los tres conjuntos; los cuatro moldes la citan en vez de llevar cada uno su lista. **La de la épica estaba escrita dos veces sin coincidir**, y ahora está una.

**El vocabulario pasó al español**, que es lo que `01·C20` pide y lo que el propio glosario exige llevar en cuenta.

**115 de 115 historias lo usan**, y **ninguna cambió de sentido**: 36 cerradas antes, 36 después.

**Y queda una comprobación que lee el vocabulario del glosario**, no de una lista en el código — que es lo único que impide que vuelvan las cuatro listas.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` el glosario define, y es el único sitio | documento | [base/glosario.md](../../../../../base/glosario.md) §5 | ✅ | CP-001 |
| `RN-02` los moldes citan en vez de listar | documento | Los cuatro de [plantillas/ciclo-vida-proyectos/](../../../../../plantillas/ciclo-vida-proyectos/) | ✅ | CP-001 |
| `RN-03` un estado por concepto | documento | La tabla de nueve estados | ✅ | CP-001 paso 2 |
| `RN-04` `En implementación` pasa a `En curso` | documento | 19 historias | ✅ | CP-002 |
| `RN-05` se normalizan los existentes | documento | 111 de 115 | ✅ | CP-002 |
| `RN-06` un programa comprueba, y **avisa** | servicio | `estado_fuera_del_vocabulario` en [fases.py](../../../../../validadores/fases.py) | ✅ | CP-004, CP-005 |
| `RN-07` conjuntos distintos, palabra compartida única | documento | Los tres conjuntos del glosario | ✅ | CP-001 paso 3 |
| `RN-08` el vocabulario en español | documento | Los nueve estados | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · el glosario define los tres conjuntos en español | ✅ | §5 del glosario |
| T-02 · unificar la palabra de «terminado» | ✅ | CP-001 paso 3 |
| T-03 · los cuatro moldes citan | ✅ | CP-001 paso 4 |
| T-04 · guardar la foto de las 115 | ✅ | Antes de tocar nada |
| T-05 · normalizar | ✅ | 111 cambiadas, 4 ya estaban |
| T-06 · comparar par por par | ✅ | 0 fuera del mapa |
| T-07 · contar completas antes y después | ✅ | 72 y 72 |
| T-08 · comprobar contra el vocabulario | ✅ | `estado_fuera_del_vocabulario` |
| T-09 · que el aviso diga cuáles valen | ✅ | CP-004 |
| T-10 · casos del vocabulario y los bordes | ✅ | 15 pruebas |
| T-11 · una prueba que lo busque por `validar` | ✅ | `test_el_aviso_sale_en_la_corrida_de_fases` |
| T-12 · subir `VERSION` y el `CHANGELOG` | ✅ | 35.0.0 |
| T-13 · correr `validar.py versionado` | ✅ | Sin incumplimientos |
| T-14 · sabotear | ✅ | Siete, siete cazados |

**Correspondencia:** 14 tareas en el plan, 14 acá. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Una cosa se hizo distinto a lo que el plan decía, y se declara.** El plan pedía reportar las historias **sin campo de estado**. Se construyó así y dejó **siete pruebas de otra clase en rojo**. Se sacó, con su porqué escrito en el código. Ver §6.

### 2.3 El vocabulario acordado

| Estado | Qué quiere decir | Lo usan |
|---|---|---|
| **Pendiente** | Existe y no empezó | Historia · tarea |
| **Propuesta** | Escrita, sin aprobar | Épica |
| **Aprobada** | Aprobada, y no empezó | Épica |
| **Lista** | Lista para construirse | Historia |
| **En curso** | Se está construyendo | Épica · historia · tarea |
| **En prueba** | Construida, probándose | Historia |
| **Terminada** | Se terminó | Épica · historia · tarea |
| **Bloqueada** | Detenida por algo de afuera | Tarea |
| **Cancelada** | Se decidió no hacerla | Épica |

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python validadores/pruebas.py`: **396 de 396 verdes** |
| **Defectos** | `DEF-01`, `DEF-02` y `DEF-03`, los tres corregidos |

**Los dos primeros los cazó el ensayo en seco, no una prueba**: el guion de normalización perdía un punto en 19 documentos y dejaba un `**` suelto en 2. Aplicar directo habría dañado el texto de forma difícil de ver, porque **se lee casi bien**.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**Para saber qué estado poner:** [base/glosario.md](../../../../../base/glosario.md), sección 5. Los moldes remiten ahí.

**Para comprobar un proyecto:**

```
python "<ruta-al-estandar>/validadores/validar.py" fases --raiz .
```

- **Desde el código:** `fases.vocabulario_de_estados()` da los tres conjuntos; `fases.estado_fuera_del_vocabulario(proyecto)` da los avisos.
- **De dónde sale el vocabulario:** del glosario **del estándar**, no del proyecto que se valida. Un proyecto hereda las reglas, no las redefine.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| El diagnóstico fue «el molde lo enseñó», no «hubo descuido» | Con el segundo, el arreglo habría sido corregir 111 documentos y pedir cuidado — y en seis meses estarían repartidos otra vez | `S-049` |
| El vocabulario se lee **del glosario** en tiempo de corrida | Una lista en el código sería la quinta copia, y el problema entero eran las copias. Hay una prueba que quita `Terminada` del glosario y exige que cambie qué acepta | `CP-005` paso 5 |
| **`Terminada`**, no `Cerrada` | `cerrada` ya significa otra cosa: es como se marca una **estación** de fase | El glosario, con su porqué |
| Los tres conjuntos siguen siendo distintos | Una épica se cancela y una tarea se bloquea. Un conjunto único obligaría a estados que no aplican | `RN-07` |
| Traducir, en vez de agregar tres excepciones | El glosario es el documento que lleva la lista de lo que se queda en otro idioma **y por qué**. Escribir `Backlog` ahí sin razón sería incumplir donde más se nota | `RN-08` |
| **MAYOR**, no menor | El precedente del registro es claro, y un aviso permanente **es trabajo pendiente, no información** | La entrada del `CHANGELOG` |
| Se normaliza la palabra, no la frase | 43 traen texto útil detrás: la fecha, los criterios verificados | `CP-002` paso 5 |
| La caja cuenta: `terminada` se reporta | Aceptarla abriría la puerta a que vuelvan las variantes, que es lo que se vino a cerrar | `test_limites_la_caja_si_cuenta` |
| La comprobación **no** reporta el campo faltante | Salía de su tema y ensuciaba pruebas ajenas | `S-050` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **Nadie reporta que a una historia le falte el campo `Estado`** | Se sacó de esta comprobación en `DEF-03` | No es taparlo: pasa a quien comprueba que un documento traiga sus campos, que es otra cosa. **Hoy no existe esa comprobación.** Se decide con el usuario |
| **Solo se comprueban las historias.** Épicas y planes tienen conjunto y molde, pero no guardia | Fuera de alcance declarado | Es la continuación natural, y ahora es barata: el vocabulario ya está en un sitio |
| Los documentos de proyectos que heredan el estándar | Declarado en el `CHANGELOG` | Se avisan al correr `validar.py fases`; migrar es decisión de cada proyecto |
| La comprobación de rastros del guion de sabotaje no distingue trabajo sin guardar de daño | No previsto, apareció en §4.3 del resultado | Con el árbol limpio funciona. Si estorba, se le enseña a comparar contra el `diff` |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-003](../../epica.md): la `HU-012` en su tabla de historias y en la de fases.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] El [glosario](../../../../../base/glosario.md), con su sección 5.
- [x] Las señales `S-049` y `S-050`.
- [x] `VERSION` y `CHANGELOG.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna en base de datos. **Sí hay migración de documentos**, y por eso la versión es MAYOR: quien tenga documentos escritos cambia la palabra de su campo `Estado`. La tabla de qué pasa a qué está en el `CHANGELOG`.
- **Qué cambia para quien ya tenía el estándar:** los moldes citando el glosario, y un aviso por cada documento con un estado del vocabulario viejo.
- **Reversión:** se descarta el commit. **Con la salvedad de siempre:** si la versión ya se publicó, bajarla no deshace que un proyecto la haya visto.
