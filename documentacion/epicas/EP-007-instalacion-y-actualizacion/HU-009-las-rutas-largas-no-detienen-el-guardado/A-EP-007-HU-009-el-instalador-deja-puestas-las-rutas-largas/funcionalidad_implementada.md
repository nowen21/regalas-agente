# Funcionalidad implementada — Fase `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` (módulo Instalador)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` |
| **Módulo** | Instalador |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-26 |
| **HU / CA cubiertas** | [HU-009](../HU-009-las-rutas-largas-no-detienen-el-guardado.md): `CA-01`, `CA-02`, `CA-03` y sus dos transversales |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

---

## 1. Qué se implementó — resumen

**El instalador deja puesto `core.longpaths`.** En Windows, guardar una ruta de más de 260 caracteres falla con `Filename too long`; le pasó a este repositorio y detuvo un commit dos veces.

**Sin pisar lo que alguien haya decidido:** si el ajuste está en `false`, lo dice y no lo toca.

**Y sin salirse del repositorio.** La configuración de la máquina no se toca. Existe la forma que valdría para todos los clones futuros, y **queda escrita para quien la quiera**: es un cambio fuera del proyecto, y esa decisión no la toma el instalador (`00·N1`).

**Queda escrito qué hacer si aparece igual**, porque **la configuración de git no viaja al clonar** — y esa es la mitad de los casos que el instalador no alcanza.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` el instalador deja el ajuste puesto | servicio | `_rutas_largas` en [validadores/instalar.py](../../../../../validadores/instalar.py) | ✅ | CP-001 |
| `RN-02` un `false` no se pisa | servicio | La misma función | ✅ | CP-002 |
| `RN-03` se pone en cualquier sistema | servicio | Sin detección de sistema, con su porqué | ✅ | CP-001 |
| `RN-04` no se toca la configuración global | servicio | `git config` sin `--global` | ✅ | CP-003 |
| `RN-05` queda escrito qué hacer al clonar | documento | [cvds/despliegue/README.md](../../../../../cvds/despliegue/README.md) §3.1 | ✅ | CP-006 |
| `RNF-01` nada fuera del repositorio | servicio | El valor **local**, comprobado | ✅ | CP-003 |
| `RNF-02` sus pasos lo dicen | servicio | El paso entre los demás | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · leer el valor actual sin escribir | ✅ | `_rutas_largas` |
| T-02 · ponerlo si no está, y decirlo | ✅ | CP-001 |
| T-03 · si está en `false`, no pisarlo | ✅ | CP-002 |
| T-04 · el modo que muestra no escribe | ✅ | CP-003 |
| T-05 · casos de los cuatro escenarios | ✅ | 6 pruebas |
| T-06 · las clases de EP-007 siguen pasando | ✅ | CP-005 |
| T-07 · el texto de despliegue | ✅ | §3.1 |
| T-08 · los dos comandos, y cuál es opcional | ✅ | CP-006 |
| T-09 · que se entienda sin conocer el proyecto | ✅ | CP-006 paso 2 |
| T-10 · `VERSION` y el `CHANGELOG` | ✅ | 35.1.0 |
| T-11 · sabotear | ✅ | Siete, siete cazados |

**Correspondencia:** 11 tareas en el plan, 11 acá. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Un paso que el plan no traía, y lo pidió un sabotaje:** la prueba de la configuración global pregunta ahora por el valor **local** del repositorio. Ver §5.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python validadores/pruebas.py`: **402 de 402 verdes** |
| **Defectos** | `DEF-01` y `DEF-02`, los dos corregidos |

**Los dos defectos eran de la forma de probar, no del instalador.** El código quedó bien al primer intento; lo que estaba mal era cómo se comprobaba.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Con el instalador de siempre:

```
python validadores/instalar.py <ruta-al-proyecto> --aplicar
```

Entre sus pasos aparece `git config core.longpaths true`, o `ya estaba puesto`, o un `OMITIDO` si alguien lo dejó en `false`.

**Si el error aparece de todas formas** —porque el repositorio se clonó y no se instaló nada en él— el documento de [despliegue](../../../../../cvds/despliegue/README.md) §3.1 dice qué correr y por qué.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| `core.longpaths` en vez de acortar nombres | Medido: la holgura del peor caso son **8 caracteres** y anidar necesita **55**. Acortar la convención ahorra 14. Ninguna combinación crea los 55 | `S-042` |
| Se pone en cualquier sistema | Fuera de Windows es inerte, y detectar el sistema sería peor: la copia puede terminar en otra máquina | `RN-03` |
| Un `false` a mano no se pisa | Es la misma cortesía que el instalador ya tiene con `core.hooksPath`. Pisar una decisión ajena sin decirlo es peor que no hacer nada | `CP-002` |
| **No** se toca la configuración global | Es fuera del proyecto, y `00·N1` pide aprobación. Se dice el comando y decide quien lee | `RN-04` |
| El texto va en el documento de despliegue, no solo en el registro | El registro se lee al actualizar; quien clona de cero no pasa por ahí | `CA-03` |
| La prueba pregunta por el valor **local**, no compara el global consigo mismo | Comparar antes y después pasa si otra prueba ya lo cambió. Preguntar por el local no depende del orden | `S-051` |
| El guion limpia el rastro **tras cada sabotaje**, no al final | El rastro cae fuera del repositorio, donde ningún `git status` lo muestra, y contamina los siguientes | `S-051` |
| Ninguna prueba fabrica rutas largas | Que el ajuste sirva está comprobado en la realidad. Fabricar el caso probaría a git, no al instalador | El plan de pruebas §7.4 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **Quien clone y no instale sigue tropezando.** La configuración de git no viaja | Limitación declarada desde la historia | No hay forma de alcanzarlo desde el repositorio. Lo que hay es el texto de despliegue. **Si algún día molesta, la salida es el ajuste global, y es decisión del usuario** |
| `_ProyectoDePrueba` deja un `ResourceWarning`: abre el registro de proyectos sin cerrarlo | **Anterior a esta fase**, en su línea 2640 | No se tocó: es código compartido y el plan no lo declara. Es una línea |
| El instalador no comprueba si el repositorio **ya tiene** rutas cerca del tope | No previsto | Hoy no hace falta: el ajuste se pone siempre. Serviría para avisar antes de que duela |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-007](../../epica.md): la `HU-009` en su tabla de historias.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] El documento de [despliegue](../../../../../cvds/despliegue/README.md), con su §3.1.
- [x] La señal `S-051`.
- [x] `VERSION` y `CHANGELOG.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** al volver a instalar, el ajuste queda puesto. **Quien no vuelva a instalar, sigue como estaba** — y por eso la versión es MENOR: nadie queda obligado a nada.
- **Reversión:** se descarta el commit. El ajuste ya puesto en un repositorio no se deshace solo, y no hace falta: es inerte donde no aplica. Quitarlo es `git config --unset core.longpaths`.
