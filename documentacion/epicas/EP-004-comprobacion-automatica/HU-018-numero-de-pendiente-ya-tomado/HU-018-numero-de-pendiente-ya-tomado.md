# HU-018 — Avisar cuando dos pendientes se disputan el mismo número

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-018 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien abre un pendiente
- **Quiero** que un programa diga cuál es el número libre y avise si el que voy a usar ya está tomado
- **Para** que dos sesiones abiertas a la vez no escriban dos pendientes distintos con el mismo número

---

## 3. Contexto y descripción

El backlog de [`pendientes/`](«RUTA-ESTANDAR»/pendientes/) se numera a mano, leyendo el índice. El índice puede estar más viejo que la carpeta, así que el número se elige contra una foto que ya no es.

El 2026-08-16 pasó: dos sesiones trabajaban el mismo repositorio, una tomó el `52` y la otra iba a tomarlo también. Se vio de casualidad, al listar la carpeta antes de escribir y encontrar el archivo ya ahí. Si el orden hubiera sido el otro, el segundo archivo habría pisado al primero sin que nadie se enterara.

No es un caso nuevo: el pendiente [22](«RUTA-ESTANDAR»/pendientes/22-dos-sesiones-versionando-a-la-vez.md) plantea lo mismo un piso más arriba, con dos sesiones subiendo `VERSION` a la vez, y tiene tres opciones sin decidir. Esta historia **no decide eso**: comprueba lo que ya se puede comprobar sin acuerdo previo — que el número esté libre y que el índice y la carpeta digan lo mismo.

El número importa porque los pendientes se citan entre sí por número, y [su README](«RUTA-ESTANDAR»/pendientes/README.md) dice que no se renumera nunca: renumerar rompe los enlaces. Un número duplicado no se arregla después.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Dos archivos de `pendientes/` no pueden empezar con el mismo número |
| RN-02 | El número tomado por un pendiente cerrado en `hecho/` tampoco se reutiliza |
| RN-03 | Todo archivo de la carpeta tiene su línea en el índice, y toda línea del índice tiene su archivo |
| RN-04 | El programa dice cuál es el próximo número libre |
| RN-05 | El programa reporta y no renumera: renumerar rompe las citas entre pendientes |

### 3.2 Supuestos

- El backlog seguirá siendo archivos numerados en una carpeta, con su índice.

### 3.3 Fuera de alcance

- Decidir cómo se coordinan dos sesiones abiertas. Esa decisión es del pendiente [22](«RUTA-ESTANDAR»/pendientes/22-dos-sesiones-versionando-a-la-vez.md) y no la toma un programa.
- Bloquear la escritura. El programa avisa; quien escribe decide.
- Los huecos de numeración: son historia y no se rellenan.

---

## 4. Criterios de aceptación

### CA-01 — Dice cuál es el próximo número libre

```gherkin
Dado el backlog con sus archivos numerados
Cuando se pregunta por el próximo número
Entonces devuelve el primero que no esté usado ni en la carpeta ni en `hecho/`
```

**Cómo validarlo:**

1. Correr la comprobación sobre `pendientes/`.
2. Leer el número que propone y comprobar que no exista ningún archivo que empiece con él, ni en `pendientes/` ni en `pendientes/hecho/`. Resultado esperado: no existe.
3. Crear un archivo con ese número y volver a correr. Resultado esperado: propone el siguiente.
- **Aprobado cuando:** el número propuesto nunca es uno ya usado.

### CA-02 — Avisa del número repetido

```gherkin
Dado dos archivos que empiezan con el mismo número
Cuando se corre la comprobación
Entonces los nombra a los dos
Y sale como falla, no como aviso
```

**Cómo validarlo:**

1. Crear a propósito dos archivos con el mismo número en `pendientes/`.
2. Correr la comprobación. Resultado esperado: los nombra a los dos y el resultado es falla.
3. Borrar uno y volver a correr. Resultado esperado: la falla desaparece.
- **Aprobado cuando:** ningún número duplicado pasa en silencio.

### CA-03 — Cruza la carpeta con el índice

```gherkin
Dado un archivo de la carpeta que el índice no menciona
Cuando se corre la comprobación
Entonces lo reporta
Y también reporta la línea del índice cuyo archivo no existe
```

**Cómo validarlo:**

1. Correr la comprobación sobre el backlog tal como está hoy.
2. Comparar con lo que ya reporta `validar.py estandar`, que detecta parte de esto. Resultado esperado: los mismos archivos, más los que el otro no mira.
3. Agregar la línea faltante al índice y volver a correr. Resultado esperado: ese archivo desaparece de la salida.
- **Aprobado cuando:** carpeta e índice quedan dichos el uno contra el otro, en los dos sentidos.

### Criterios de aceptación transversales

- [ ] **Límites** — carpeta vacía, archivo sin número y número con ceros a la izquierda tienen comportamiento definido (`08`).
- [ ] **Errores** — un nombre que no se puede interpretar se reporta y no detiene la corrida (`05`).
- [ ] **No regresión** — lo que ya comprueba `validar.py estandar` sigue dando lo mismo (`08`).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Determinismo** | La misma carpeta da la misma salida siempre |
| RNF-02 | **Autonomía** | Sin internet, sin IA y sin dependencias fuera de la biblioteca estándar |
| RNF-03 | **Rendimiento** | Instantáneo: es listar una carpeta |
| RNF-04 | **Compatibilidad** | Corre en Windows, con rutas que llevan espacios y tildes |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [epica.md](../epica.md).
- **Contrato de API:** no aplica; se corre por línea de comandos.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Leer los números de `pendientes/` y de `pendientes/hecho/`.
- [ ] Detectar repetidos y proponer el próximo libre.
- [ ] Cruzar carpeta contra índice en los dos sentidos.
- [ ] Sumarla a la corrida completa.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-018-el-numero-de-pendiente-libre](A-EP-004-HU-018-el-numero-de-pendiente-libre/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase construye.** El número se elige a ojo leyendo un índice que puede estar más viejo que la carpeta: el 2026-08-16 dos sesiones tomaron el 52. La fase avisa; repartir turnos es la decisión del pendiente 22.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Pendiente [22](«RUTA-ESTANDAR»/pendientes/22-dos-sesiones-versionando-a-la-vez.md), que decide cómo se coordinan dos sesiones. Esta HU no lo espera: comprueba lo que ya es cierto sin esa decisión | Bajo |
| Dependencia | HU-003, porque la salida usa el formato de hallazgo ya definido | Medio |
| Riesgo | Que avise cuando el número ya se escribió y sea tarde | Mitiga a medias: avisa, no bloquea. Bloquear es la decisión del 22 |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Propone el próximo número libre
- [ ] Reporta los números repetidos como falla
- [ ] Cruza carpeta e índice en los dos sentidos
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Solo lee una carpeta y su índice |
| **N**egociable | Sí | Si avisa o además propone, se puede discutir |
| **V**aliosa | Sí | Un número duplicado no se arregla después: renumerar rompe las citas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Se prueba creando dos archivos con el mismo número |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, desde el hallazgo H-2 de la sesión «las HU sin su fase» |
