# HU-003 — Declarar en el proyecto la versión adoptada y la fecha

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — el CA-02 se volvió a medir y hoy cumple, en la fase `C` |
---

## 2. Narrativa

- **Como** quien trabaja en un proyecto que hereda las reglas
- **Quiero** que el proyecto declare qué versión sigue y desde cuándo
- **Para** poder demostrar contra qué reglas se hizo el trabajo, sin depender de la memoria de nadie

---

## 3. Contexto y descripción

Un proyecto que no declara su versión no se puede comparar con nada: no se sabe si está al día, y tampoco se puede defender lo que ya hizo, porque no hay contra qué medirlo.

La declaración es del proyecto, no del estándar. Y lleva fecha, porque lo que importa no es solo qué versión sigue, sino desde cuándo: eso es lo que permite decir que una fase cerrada antes se cerró bajo otras reglas.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada proyecto declara la versión del estándar que adoptó y la fecha |
| RN-02 | La versión declarada tiene que existir en el registro de cambios |
| RN-03 | La declaración vive en el proyecto, en un archivo que se versiona con él |
| RN-04 | Adoptar una versión nueva es una decisión de la persona, no algo que pase solo |
| RN-05 | Queda el historial de las adopciones, no solo la última |

### 3.2 Supuestos

- Un proyecto adopta versiones cada tanto, no en cada cambio del estándar.

### 3.3 Fuera de alcance

- El aviso de que quedó atrás. Eso es HU-004.
- Actualizar los archivos que el proyecto heredó. Eso es EP-007.

---

## 4. Criterios de aceptación

### CA-01 — El proyecto declara su versión y su fecha

```gherkin
Dado que un proyecto usa el estándar
Cuando se abre su declaración
Entonces dice qué versión adoptó y en qué fecha
```

**Cómo validarlo:**

1. Abrir un proyecto de prueba que ya use el estándar.
2. Buscar el archivo donde declara la versión. Resultado esperado: existe y trae número y fecha.
3. Comparar ese número con el registro de cambios del estándar. Resultado esperado: esa versión existe.
- **Aprobado cuando:** el dato está y corresponde a una versión real.

### CA-02 — Una versión que no existe se detecta

```gherkin
Dado que un proyecto declara una versión inventada
Cuando se comprueba su declaración
Entonces se reporta que esa versión no existe en el registro
```

**Cómo validarlo:**

1. Escribir en el proyecto de prueba una versión que no está en el registro.
2. Correr la comprobación. Resultado esperado: reporta que no existe.
3. Corregirla y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el número inventado no pasa.

### CA-03 — Queda el historial de adopciones

```gherkin
Dado que un proyecto adopta una versión nueva
Cuando se mira su historial
Entonces se ve desde cuándo usó cada versión
```

**Cómo validarlo:**

1. En el proyecto de prueba, adoptar una versión nueva.
2. Abrir el historial de adopciones. Resultado esperado: aparece la anterior con sus fechas y la nueva.
3. Adoptar otra más y volver a mirar. Resultado esperado: las tres quedan, en orden.
- **Aprobado cuando:** el historial permite decir qué versión regía en una fecha dada.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto recién instalado declara la versión con que se instaló, no queda en blanco.
- [ ] **No regresión** — adoptar una versión no borra el historial anterior.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Trazabilidad** | Se puede decir qué versión regía en cualquier fecha pasada |
| **Portabilidad** | La declaración viaja con el repositorio del proyecto |
| **Autonomía** | Se puede leer sin conexión al estándar |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un archivo de texto.
- **Documento funcional:** [documentacion/epicas/EP-002-versionado-y-adopcion/epica.md](../epica.md), criterio CAE-03.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir dónde declara el proyecto su versión y con qué formato.
- [ ] Definir dónde queda el historial de adopciones.
- [ ] Comprobar que la versión declarada existe en el registro.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir](C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir/estado-fase.md) | CA-02, otra vez | **Ejecutada el 2026-08-29.** Veredicto: [**Cumple**](C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir/resultado_pruebas.md#2-veredicto-de-la-fase) — el CA-02 se ejecutó de nuevo y hoy se cumple: la versión inventada sale como falla. Declara reemplazar el veredicto de la fase `A` |
**Ejecutada el 2026-08-22.** Veredicto: [**No cumple**](A-EP-002-HU-003-retrodocumentar-la-version-adoptada/resultado_pruebas.md#5-veredicto-de-la-fase) — el CA-01 y el CA-03 sí; el CA-02 no: una versión inventada pasa y apaga el aviso. Probada sobre **shopnest-mesa** |

**La fase retro-documenta y mide sin corregir.** La declaración se lee y el historial de adopciones existe. Lo que falta: que la versión declarada **exista de verdad** no lo comprueba nadie, y el registro arrastra los pendientes 44 y 46.

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
| Dependencia | HU-002, porque la versión declarada se comprueba contra el registro | Alto |
| Riesgo | Que la declaración quede en un archivo local que no viaja | Vive en el repositorio del proyecto, no en la máquina |
| Riesgo | Que se actualice sola y nadie decida | Adoptar es decisión de la persona, escrito como regla |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El proyecto declara versión y fecha
- [ ] La versión declarada se comprueba contra el registro
- [ ] Queda historial de adopciones
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el registro de HU-002 |
| **N**egociable | Sí | Dónde vive la declaración se puede discutir |
| **V**aliosa | Sí | Permite demostrar contra qué reglas se trabajó |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un archivo y su historial |
| **T**esteable | Sí | Se prueba con un proyecto de prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
