# Resultado de Pruebas — Fase `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la exigencia transversal de privacidad **se cumple hoy**, comprobado ejecutando el enmascarado por sus dos mitades y siguiendo la cadena hasta quien escribe. Lo que la fase `A` declaró en rojo el 2026-08-22 **era cierto entonces**, y lo construyó después la `HU-002` de esta misma épica, que aquella ya nombraba como su destino.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 3 de 3 | 3 de 3 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |
| Prosa normal que se tapa | 0 | **0 de 5** |
| Rutas de escritura sin enmascarar | 0 de 2 | **0 de 2** |

---

## 3. Resultado por caso

### CP-001 — Enmascara

| Qué entró | Qué salió |
|---|---|
| `API_KEY=supersecreto123456` | `API_KEY=«enmascarado»` |
| `password: MiClave123456` | `password: «enmascarado»` |
| `la contraseña: Patito2026` | `la contraseña: «enmascarado»` |

**El nombre de la variable se conserva**, y la marca es `«enmascarado»` — la que el estándar ya usa, no una inventada.

### CP-002 — No enmascara de más

| Qué entró | Qué salió |
|---|---|
| `la clave del asunto es que el proceso sirva` | **Intacto** |
| `clave = h.regla or algo` | **Intacto** |
| `token: xyz` | **Intacto** |
| `API_KEY=os.environ['X']` | **Intacto** |
| `password: changeme` | **Intacto** |

**Cinco de cinco intactos.** El cuarto es el que más importaría tapar mal: es exactamente lo que se quiere que la gente haga.

### CP-003 — Está conectado a quien escribe

| Eslabón | Resultado |
|---|---|
| `hook_historico.py` llama a `historico.anotar_usuario` | Sí |
| `hook_historico.py` llama a `historico.anotar_agente` | Sí |
| `historico.py` llama al enmascarado | **Dos veces**: una por ruta |
| El enmascarado ocurre **antes** de escribir | Sí, en las dos |

**Las dos rutas importan por separado:** si solo se enmascarara el mensaje del usuario, una clave que el agente repita en su respuesta quedaría en claro.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Un falso hallazgo, cazado antes de reportarlo

En la primera corrida, `la contrasena: Patito2026` salió **sin tapar**, y estuvo a punto de reportarse como defecto.

**No era del código: la palabra estaba mal escrita**, sin la ñ. Con `contraseña` se tapa. **Se comprobó antes de escribirlo**, que es la diferencia entre un defecto y un susto.

Vale dejarlo dicho porque es el patrón del día al revés: casi se afirma un defecto sin ejecutar el caso bueno.

### 4.2 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A` **no se toca**: fue cierto el día que se escribió, y reescribirlo borraría el rastro de que la exigencia estuvo en rojo.

Pero **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). Sin una fase que lo declare, la historia arrastra un «no cumple» que ya no existe, y quien lo lea después va a buscar un trabajo que ya está hecho.

### 4.3 Rastros

Ninguno. No se escribió en la transcripción real, ni se editó ningún documento para probar.

### 4.4 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`): los valores son cadenas evidentemente falsas. **Es la regla que esta fase verifica** — no se puede comprobar que algo no queda escrito escribiéndolo.

---

## 5. Defectos encontrados

**Ninguno.** El único candidato fue un error de la propia prueba, contado en el §4.1.

---

## 6. Evidencias

- El guion que lo midió, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
- `validadores/enmascarar.py` y su fase `B` en la [HU-002](../../HU-002-enmascarar-claves/)
- La cadena `hook_historico.py` → `historico.anotar_*` → `enmascarar`
