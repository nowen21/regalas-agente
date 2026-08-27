# Funcionalidad implementada — Fase `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa` (módulo Automatismos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa` |
| **Módulo** | Automatismos que no dependen de la memoria |
| **Especificación del módulo** | La propia [HU-002](../HU-002-enmascarar-claves.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), abierto el 2026-08-22 |
| **HU / CA cubiertas** | [HU-002](../HU-002-enmascarar-claves.md): las formas de clave que el enmascarador no tapaba |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

> **Se ejecutó el 2026-08-22 y este documento se escribió el 2026-08-27.** Hasta entonces **era el molde sin llenar**. El trabajo estaba hecho y probado; lo que faltaba era decir qué quedó.

---

## 1. Qué se implementó — resumen

**Una clave pegada sin comillas ya no queda escrita en claro.** El enmascarador tapaba las que venían entrecomilladas y dejaba pasar `API_KEY=supersecreto123456`, que es como se pega una clave de verdad en un chat.

**Y sigue sin tapar lo que no es una clave**, que es la mitad del trabajo: código pegado, valores cortos, lecturas del entorno, moldes con `changeme`, y frases normales donde aparece la palabra «clave».

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Estado | Evidencia |
|---|---|---|---|
| Asignación sin comillas | servicio | ✅ | `API_KEY=supersecreto123456`: **se tapa el valor, no la variable** |
| Con dos puntos | servicio | ✅ | `password: MiClave123456`: se tapa |
| La palabra en español | servicio | ✅ | `la contraseña: Patito2026`: se tapa |
| Valor largo sin números | servicio | ✅ | `secret=abcdefghijklmnop`: se tapa |

**Que se tape el valor y no el nombre de la variable importa:** un registro donde no se sabe ni qué variable era no sirve para nada.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho, **medido antes de dejarlo** como pide `20·M19` |
| Defectos propios | **Ninguno** |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días con su cierre en blanco.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |
| **Suites** | `test_la_clave_sin_comillas_se_enmascara` (12), `test_la_clave_no_llega_al_historico` (11), `test_el_historico_se_busca_por_tema` (7) |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Nueve casos, y cinco son de lo que NO debe tapar:**

| Caso | Qué sale |
|---|---|
| Código pegado en el chat: `clave = h.regla or algo` | **No** se tapa |
| Valor corto y sin números: `token: xyz` | **No** se tapa |
| Lee del entorno: `API_KEY=os.environ[...]` | **No** se tapa |
| Un molde: `password: changeme` | **No** se tapa |
| Una frase normal: «La clave del asunto es que el proceso sirva» | **No** se toca |

**Los cinco de «no tapar» son los que sostienen el veredicto**, y en un enmascarador más que en cualquier otra comprobación: uno que tapa de más vuelve ilegible el histórico, y un histórico ilegible se deja de leer. **Entonces la clave estaría tapada en un archivo que nadie abre**, que no es lo mismo que estar a salvo.

**Y el caso del molde es el más fino:** `changeme` tiene forma de clave y no lo es. Taparlo escondería justamente lo que hay que ver — que alguien dejó el valor de ejemplo puesto.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**No se usa: corre solo.** El enganche del histórico enmascara antes de escribir, así que una clave pegada en el chat no llega al archivo.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se tapa **el valor**, no el nombre de la variable | Un registro donde no se sabe qué variable era no sirve |
| Un valor **corto y sin números** no se tapa | Se parece más a una palabra que a una clave, y tapar de más cuesta más que dejar pasar un `xyz` |
| Una lectura del entorno **no se tapa** | `os.environ[...]` no es una clave: es la forma correcta de no tenerla escrita |
| Un molde con `changeme` **no se tapa** | Taparlo escondería que alguien dejó el ejemplo puesto |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| La fase quedó con su **cierre en blanco cinco días**, contada como completa | **Corregido acá.** Es uno de los cuatro casos que destaparon `S-052` |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-002](../HU-002-enmascarar-claves.md): su §8 nombra esta fase.
- [x] El pendiente que la originó, en `pendientes/hecho/`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** el enmascarador tapa más formas de clave. **Lo ya escrito en el histórico no se toca**: el enmascarado ocurre al escribir, y reescribir el histórico sería borrar el rastro.
- **Reversión:** se descarta el commit.
