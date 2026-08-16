# HU-015 — Derogación sin adoptar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-015 |
| **Épica / Feature** | [EP-004 Comprobación automática](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Construida sin fase — pendiente de retrodocumentar |

---

## 2. Narrativa

- **Como** dueño de un proyecto que hereda el estándar
- **Quiero** que la comprobación falle sola cuando entre mi versión y la vigente hay una regla derogada que no adopté
- **Para** no descubrir el atraso leyendo el `CHANGELOG.md` a mano

---

## 3. Contexto y descripción

El estándar vive en una carpeta central, así que al derogar una regla todo proyecto deja de leerla ese mismo día. Pero ningún proyecto se pone al día solo: declara su versión en su `CLAUDE.md` y ahí se queda. Antes de la 19.0.0 ese atraso salía como aviso, sin límite escrito, y un proyecto podía quedarse tres versiones atrás para siempre.

[`02·F22`](../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) puso el límite: con una derogación sin adoptar no se abre ni se cierra fase, y lo único que se abre es la fase que la adopta. Esta historia es la parte que lo comprueba sola.

**El código ya está escrito** —se hizo el 2026-08-16 en la misma sesión que la regla, sin pasar por la cadena de [`02·F0`](../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)—. Esta historia existe para retrodocumentarlo: darle su fase, su plan y su cierre. Está en [`validadores/version.py`](../../../../validadores/version.py) (`derogaciones`, `sin_adoptar`, `validar_fase`) y lo llama [`validadores/flujo.py`](../../../../validadores/flujo.py).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Las reglas jubiladas se leen de la marca `[DEROGADA en X.Y.Z → ver ID]` del título de cada regla, no del `CHANGELOG.md`: el changelog es prosa y nombrar ahí la palabra no jubila nada |
| RN-02 | Cuenta la derogación publicada **después** de la versión que el proyecto declara y hasta la vigente |
| RN-03 | Un proyecto que no declara versión no produce este hallazgo: de eso ya avisa la comprobación de desfase |
| RN-04 | Se cobra donde hay fases. Sin fases, el desfase sigue siendo aviso |
| RN-05 | Es **falla**, no aviso: es lo que distingue esta comprobación del desfase de número |
| RN-06 | El programa no adopta nada ni toca el `CLAUDE.md`: avisa |

### 3.2 Supuestos

- Toda regla derogada lleva su marca en el título, que es lo que exige [`20·M11`](../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md).

### 3.3 Fuera de alcance

- Distinguir si la regla derogada era una `*opt-in*` que el proyecto nunca encendió. Hoy igual se le cuenta; queda anotado en [`validadores/reglas-validables.md`](../../../../validadores/reglas-validables.md).
- Reconocer cuál de las fases abiertas es la que adopta la derogación, para dejarla pasar.
- Detener el trabajo cuando aparece el hallazgo: eso es [EP-005 · HU-003](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).

---

## 4. Criterios de aceptación

### CA-01 — Falla el proyecto con una derogación sin adoptar

```gherkin
Dado un proyecto que declara una versión anterior a la que jubiló una regla
Cuando se comprueba un proyecto que tiene fases
Entonces sale una falla que nombra cada regla jubilada y cuál la reemplazó
```

**Cómo validarlo:**

1. Armar un proyecto con `CLAUDE.md` declarando `3.0.0` y una fase. Correr. Resultado esperado: la falla nombra las reglas jubiladas desde la 3.1.0.
2. Subir la versión declarada a la vigente. Correr. Resultado esperado: ningún hallazgo.
- **Aprobado cuando:** el atraso con derogación no pasa como aviso.

### CA-02 — No cuenta lo que ya está adoptado

```gherkin
Dado un proyecto que declara una versión posterior a una derogación
Cuando se comprueba
Entonces esa derogación no aparece en el hallazgo
```

**Cómo validarlo:**

1. Declarar una versión intermedia y correr. Resultado esperado: solo salen las jubiladas después de esa versión.
- **Aprobado cuando:** el hallazgo dice lo que falta, no la historia entera.

### CA-03 — Sin fases no se cobra

```gherkin
Dado un proyecto atrasado que no tiene ninguna fase
Cuando se comprueba
Entonces no sale la falla, solo el aviso de desfase
```

**Cómo validarlo:**

1. Quitar las fases del proyecto de prueba y correr. Resultado esperado: ninguna falla.
- **Aprobado cuando:** el trabajo que `02·F0` exceptúa no queda bloqueado.

### Criterios de aceptación transversales

- [ ] **Inocuidad** — no modifica ningún archivo del proyecto.
- [ ] **Límites** — sin `CLAUDE.md`, sin versión declarada o sin `VERSION` del estándar, no produce hallazgos de este tipo.
- [ ] **Errores** — un archivo que no se puede leer se salta, no rompe la ejecución.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Precisión** | Cero falsos positivos: los ejemplos del molde y las tablas de los índices repiten la marca sin ser reglas, y no se cuentan |
| RNF-02 | **Rendimiento** | Recorre `base/` una vez por corrida |

---

## 6. Diseño y referencias

- **Documento funcional:** los hallazgos H-2 y H-3 del [2026-08-16 · sesión](../../../../historico-chat/resumenes/2026-08-16/sesion.md).
- **Regla que la origina:** [`02·F22`](../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md).
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Leer las reglas jubiladas de la marca del título (`derogaciones`).
- [x] Quedarse con las que caen dentro del atraso (`sin_adoptar`).
- [x] Emitir la falla que las nombra (`validar_fase`).
- [x] Llamarla desde el recorrido de fases (`flujo.py`).
- [ ] Retrodocumentar todo lo anterior como fase, con su plan y su cierre.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| «…» | CA-01, CA-02, CA-03 | Sin abrir — el código existe y la fase no |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [`20·M11`](../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md): si una regla se jubila sin su marca, esta comprobación no la ve | Alto |
| Riesgo | Que el proyecto no declare su versión y la comprobación quede muda | Ya lo cubre el aviso de desfase, que pide fijarla |
| Riesgo | Que la fase que adopta la derogación quede bloqueada por la misma comprobación | Está fuera de alcance reconocerla; hoy se resuelve subiendo la versión al cerrar |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [x] Falla el proyecto con una derogación sin adoptar
- [x] No cuenta lo que ya está adoptado
- [x] Sin fases no se cobra
- [ ] La fase que lo implementa, escrita y cerrada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Solo necesita el `CLAUDE.md` del proyecto y el `base/` del estándar |
| **N**egociable | Sí | El filtro de las `*opt-in*` se puede dejar para después, y así quedó |
| **V**aliosa | Sí | Sin ella, `02·F22` depende de que alguien se acuerde |
| **E**stimable | Sí | Tres funciones y un enganche |
| **S**mall (pequeña) | Sí | Cabe en una fase |
| **T**esteable | Sí | Se arma un proyecto de prueba con la versión atrasada |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde los hallazgos H-2 y H-3 del 2026-08-16, para retrodocumentar el código que ya se escribió |
