# Resultado de Pruebas — Fase `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la decisión está aplicada y comprobada ejecutando. Lo que la
fase `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` declaró en rojo el 2026-08-22 era cierto entonces y siguió
siéndolo hasta que hubo decisión: no era trabajo pendiente, era una pregunta sin
responder.

| Métrica | Real |
|---|---|
| Formas con la clave pegada a su nombre, tapadas | 3 de 3 |
| Frases corrientes que se tapan de más | 0 de 5 |
| Formas dentro de una frase, tapadas | 0 de 3, y es lo decidido |

---

## 3. Resultado por caso

### CP-001 — Qué tapa y qué no, ejecutado

Corrido sobre las seis formas:

| Lo que entra | Sale |
|---|---|
| `API_KEY=supersecreto123456` | tapado |
| `password: MiClave123456` | tapado |
| `la contraseña: Patito2026` | tapado |
| `mi clave es Patito2026` | **intacto**, y es lo decidido |
| `el token es abc123xyz789` | **intacto**, y es lo decidido |
| `usa la contraseña Patito2026 para entrar` | **intacto**, y es lo decidido |

Y la contraprueba, que es la que sostiene la decisión: cinco frases corrientes
—entre ellas `la clave del asunto es que el proceso sirva` y
`API_KEY=os.environ['X']`— salen **intactas**. Ninguna se tapa de más.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Lo que este criterio no cubre, dicho acá y no escondido

La clave dicha dentro de una frase queda en claro. Abierta y declarada, con su motivo. La defensa ahí es `00·N6`, no el programa

### 4.2 Por qué este rojo no se cerraba midiendo

Medirlo otra vez daba el mismo resultado todos los días. El dato no cambiaba;
faltaba saber qué se quería hacer con él. Está en `S-085`.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- La decisión del usuario, en la transcripción del 2026-08-30
- La corrida del §3
