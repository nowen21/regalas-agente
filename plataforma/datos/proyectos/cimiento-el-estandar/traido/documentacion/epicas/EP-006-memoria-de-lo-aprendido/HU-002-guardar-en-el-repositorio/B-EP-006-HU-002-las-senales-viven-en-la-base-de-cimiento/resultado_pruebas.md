# Resultado de Pruebas — Fase `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la decisión del usuario está aplicada y comprobada. Lo que la fase `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` declaró en rojo el 2026-08-17 era cierto entonces, y siguió siéndolo hasta que hubo decisión: no era trabajo pendiente, era una pregunta sin responder.

| Métrica | Real |
|---|---|
| Señales en la base de Cimiento | 268 |
| De ellas, de otros proyectos | 186 |
| Señales de este repositorio, versionadas en texto | 85 |
| Recuerdos versionados, con su índice | 23 |

---

## 3. Resultado por caso

### CP-001 — Qué hay en cada sitio, contado

Contado sobre la base y sobre el árbol:

| Sitio | Qué guarda | Cuánto | Versionado acá |
|---|---|---|---|
| `historico-chat/memory/` | recuerdos de este repositorio | 23 | Sí |
| `documentacion/senales.md` | señales de este repositorio | 85 | Sí |
| `memoria/senales.db` | señales de Cimiento, de todos los proyectos | 268 | No, y es lo decidido |

**Resultado: pasa.** Lo de este repositorio está versionado; lo que es de todos los proyectos vive donde sirve a todos.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué este rojo no se cerraba midiendo

Es de los que pedían una decisión, no trabajo. Medirlo otra vez habría dado el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él. Está en `S-085`.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- La decisión del usuario, en la transcripción del 2026-08-30
- Las cuentas del §3, tomadas sobre el árbol y la base
