# Plan de Trabajo — Fase `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara` (módulo Enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-001](../HU-001-transcripcion-de-la-sesion.md) — **una sola** (`F12.1`) |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Cierra un rojo que dejó de ser cierto.** La fase [`A`](../A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md) cerró con «No cumple» el 2026-08-22 por su exigencia transversal de privacidad — *«Nada enmascara»*. **Era cierto entonces.** El enmascarado lo construyó después la [`HU-002`](../../HU-002-enmascarar-claves/) de esta misma épica, que la fase `A` ya nombraba como su destino.

**Por qué hace falta una fase y no basta con anotarlo:** el veredicto de la `A` no se toca —reescribirlo borraría el rastro—, y **nadie vuelve a mirar un rojo por su cuenta**. Sin una fase que lo declare, la historia arrastra un «no cumple» que ya no existe. Es `S-061`.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** comprobar que **la exigencia transversal de privacidad hoy se cumple**, y dejarlo declarado donde se lee.

**Fuera de alcance:**

- **Construir enmascarado.** Ya está: `enmascarar.py`, y su fase `B` para la clave sin comillas.
- **Ampliar qué se tapa.** La clave dicha enteramente en prosa sigue sin taparse, y está declarado en la `HU-002` con su motivo: el riesgo de tapar de más.
- **Tocar la fase `A`.** Su veredicto fue cierto el día que se escribió.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase**, porque abrirla mueve el número.

### 2.0 La línea base

```
119 en total · 32 sin terminar · 87 terminadas,
de las cuales 66 cumplen, 16 no cumplen y 5 no dicen si cumplen
```

### 2.1 Lo que dice la exigencia, y lo que hay hoy

**La exigencia, palabra por palabra:** *«Privacidad — lo que se enmascara no queda escrito en claro en la transcripción.»*

| Pieza | Estado | Cómo se comprobó |
|---|---|---|
| Existe quien enmascare | **Sí** | `validadores/enmascarar.py` |
| **Está conectado al enganche** | **Sí** | `historico.py` lo llama en las dos rutas: el mensaje del usuario y la respuesta del agente |
| El enganche usa ese módulo | **Sí** | `hook_historico.py` llama a `historico.anotar_usuario` y `anotar_agente` |
| **Tapa de verdad** | **Sí** | Corrido: `API_KEY=supersecreto123456` sale `API_KEY=«enmascarado»` |
| **No tapa de más** | **Sí** | Corrido: `la clave del asunto es que sirva` sale intacto |

**Las dos últimas se ejecutaron, no se leyeron.** Es lo que faltó tres veces hoy.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |
| `HU-001-transcripcion-de-la-sesion.md` | Modificar | Documentación | Su `Estado` dice «el transversal de privacidad, no», y su casilla sigue vacía |

**No se toca código.** Lo que esta fase hace es **comprobar y declarar**.

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| La historia | Su `Estado` y una casilla | `fases.py`, que lee el estado contra el glosario | No rompe si la palabra sale del glosario |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

Ninguno nuevo.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Una fase que **declara**, sin tocar la `A` | Reescribir el veredicto de la `A` | Aquel fue cierto el día que se escribió. Reescribirlo borra el rastro de que la exigencia estuvo en rojo tres días |
| Se comprueba **ejecutando el enmascarado**, no leyendo el código | Mirar que el módulo exista y esté importado | Existir e importarse no es tapar. Hoy mismo se afirmó tres veces sobre lo que no se ejecutó |
| Se comprueba **también que no tape de más** | Solo que tape | Un enmascarador que tapa de más se apaga, y entonces no queda nada tapado |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. Las dos mitades se corrieron antes de escribir esto | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comprobar que enmascara, ejecutándolo | Calidad | 0,5 h | — | EV-01 |
| T-02 | Comprobar que **no** enmascara de más | Calidad | 0,5 h | — | EV-02 |
| T-03 | Comprobar que está conectado al enganche que escribe | Calidad | 0,5 h | — | EV-03 |
| T-04 | Poner al día el `Estado` y la casilla de la historia | Documentación | 0,5 h | T-01 a T-03 | EV-04 |
| T-05 | Declarar el veredicto en el cierre de esta fase | Documentación | 0,5 h | T-04 | EV-04 |

**Total estimado:** 2,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`, y no se agrega funcionalidad. `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-03 → T-01 → T-02 → T-04

**La `T-03` va primero.** Que el módulo exista y tape no sirve de nada si el enganche que escribe la transcripción no lo llama — **la exigencia habla de lo que queda escrito, no de lo que el módulo sabe hacer**. Es el mismo defecto de `EP-002·HU-004`: construido y no llamado.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| Transversal · Privacidad | Ejecutar el enmascarado por las dos mitades, y seguir la cadena hasta el enganche | EV-01, EV-02, EV-03 | | ☐ |

---

## 6. Datos y ambiente de prueba

**Ninguna prueba usa credenciales** (`00·N6`): los valores son cadenas evidentemente falsas, y lo que se comprueba es justamente que **no queden escritas**.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. No hay estado ni versión que deshacer.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que ya no existe.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `00·N6` — una credencial no se escribe, no se registra y no se guarda. Es la exigencia que esta fase verifica.
- `02·F17` — la línea base, medida antes de crear la carpeta.
- `04·R4` — se ejecuta en vez de afirmar sobre lo leído.
- `13·DOC5` — lo decidido se registra como señal.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se dé por cumplido leyendo el código en vez de corriéndolo | Sería el defecto del día, otra vez | `T-01` a `T-03` ejecutan | Abierto |
| B-02 | Que se declare cumplido y el enmascarado tape de más | Se apagaría, y entonces no tapa nada | `T-02`, con la frase normal | Abierto |
| B-03 | Que abrir esta fase mueva la medición | `S-053` | La línea base está anotada en el §2.0 | Abierto |

---

## 11. Definition of Done

- [ ] Las tres comprobaciones, **ejecutadas**
- [ ] El `Estado` y la casilla de la historia, al día
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
