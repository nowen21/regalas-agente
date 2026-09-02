# HU-014 — Un solo veredicto por fase

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-014 |
| **Épica / Feature** | [EP-004 Comprobación automática](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada el 2026-08-16, con su fase cerrada en «Cumple» |
---

## 2. Narrativa

- **Como** quien revisa una fase
- **Quiero** que el concepto del `resultado_pruebas` y el del `estado-fase` no puedan decir cosas distintas
- **Para** no pasar una puerta de verificación con un veredicto viejo

---

## 3. Contexto y descripción

El veredicto de una fase se escribe dos veces a mano: en la sección 6 del `resultado_pruebas.md` y en el `estado-fase.md`. Nada comprueba que coincidan.

El 2026-08-15 dejaron de coincidir. Al reescribir el resultado de la [fase A de EP-003 · HU-010](../../EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) con la forma nueva de la plantilla, el veredicto pasó a **No cumple** y el `estado-fase` se quedó diciendo «aprobada con una prueba pendiente».

**Lo que hace grave la divergencia:** el `estado-fase` es lo que se lee para pasar la puerta de verificación. Cuando los dos difieren, el que manda termina siendo el que nadie actualizó.

No hace falta criterio para verlo. Son dos valores que tienen que ser el mismo:

| Del `resultado_pruebas` | Del `estado-fase` |
|---|---|
| El concepto de la sección 6 | El veredicto de la fase |
| El conteo de la sección 1 —diseñados, ejecutados, aprobados, fallidos, no ejecutados— | El conteo que repite |
| Los criterios en «Sí» de la sección 5 | Los criterios que da por cumplidos |

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El `resultado_pruebas` es la fuente. Si difieren, el hallazgo señala el `estado-fase` |
| RN-02 | Un `estado-fase` que da la fase por cumplida con un criterio en «No» en el resultado es un hallazgo |
| RN-03 | Un conteo que no cuadra entre los dos documentos es un hallazgo |
| RN-04 | El programa **no corrige** ninguno de los dos: avisa |
| RN-05 | El hallazgo dice qué documento, qué campo y qué se esperaba, como cualquier otro ([HU-003](../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md)) |
| RN-06 | Una fase sin `resultado_pruebas` todavía no produce hallazgos de este tipo |

### 3.2 Supuestos

- Los dos documentos se escriben con las plantillas centrales, así que el veredicto y el conteo tienen un sitio fijo donde buscar.

### 3.3 Fuera de alcance

- Decidir si el veredicto es correcto. Eso sale de la sección 5 del resultado, y comprobarlo es [HU-013](../HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md).
- Quitar la copia cambiando el molde del `estado-fase` para que enlace en vez de repetir. Es la otra salida del [pendiente 28](../../../../pendientes/hecho/un-solo-veredicto-por-fase.md) y se decide aparte.
- Detener el trabajo cuando aparece el hallazgo: eso es [EP-005 · HU-003](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).

---

## 4. Criterios de aceptación

### CA-01 — Avisa cuando los dos veredictos difieren

```gherkin
Dado un resultado_pruebas cuyo concepto es "No cumple"
Cuando el estado-fase de esa misma fase dice que la fase está aprobada
Entonces sale un hallazgo que nombra los dos documentos y los dos valores
```

**Cómo validarlo:**

1. Tomar una fase con los dos documentos y dejar el veredicto igual en ambos. Correr la comprobación. Resultado esperado: ningún hallazgo.
2. Cambiar el concepto del `resultado_pruebas` a «No cumple» sin tocar el `estado-fase`. Correr. Resultado esperado: un hallazgo que dice los dos valores.
3. Copiar el veredicto al `estado-fase` y volver a correr. Resultado esperado: ya no sale.
- **Aprobado cuando:** un `estado-fase` desactualizado no puede pasar por veredicto.

### CA-02 — Avisa la fase dada por cumplida con un criterio en «No»

```gherkin
Dado un resultado_pruebas con un criterio de aceptación o un requisito no funcional en "No"
Cuando el estado-fase da la fase por cumplida
Entonces sale un hallazgo que nombra ese criterio
```

**Cómo validarlo:**

1. Marcar un `RNF` en «No» en la sección 5 del resultado y dejar el `estado-fase` en cumplida.
2. Correr la comprobación. Resultado esperado: el hallazgo nombra el requisito.
- **Aprobado cuando:** la puerta de verificación no se pasa con una exigencia en «No».

### CA-03 — Avisa el conteo que no cuadra

```gherkin
Dado el conteo de la sección 1 del resultado_pruebas
Cuando el estado-fase repite un número distinto
Entonces sale un hallazgo por cada número que no cuadra
```

**Cómo validarlo:**

1. Cambiar el número de casos ejecutados en el `estado-fase`. Correr. Resultado esperado: hallazgo que dice los dos números.
2. Dejarlos iguales. Resultado esperado: ninguno.
- **Aprobado cuando:** los dos documentos no pueden contar cosas distintas.

### Criterios de aceptación transversales

- [ ] **Inocuidad** — no modifica ningún documento.
- [ ] **Límites** — una fase sin `resultado_pruebas`, o sin `estado-fase`, no produce hallazgos de este tipo.
- [ ] **Errores** — un documento que no se puede leer se reporta, no rompe la ejecución.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Precisión** | Cero falsos positivos por redacción: se comparan el concepto normalizado y los números, no frases |
| RNF-02 | **Rendimiento** | Corre sobre una fase en lo que tarda guardar un archivo |

---

## 6. Diseño y referencias

- **Documento funcional:** el hallazgo H-7 del [2026-08-15 · la-plantilla-del-resultado-de-pruebas](../../../../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md).
- **Pendiente que la origina:** [pendientes/hecho/un-solo-veredicto-por-fase.md](../../../../pendientes/hecho/un-solo-veredicto-por-fase.md).
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Leer el concepto de la sección 6 del `resultado_pruebas` y normalizarlo a «cumple» / «no cumple».
- [ ] Leer el veredicto del `estado-fase` y normalizarlo igual.
- [ ] Comparar los dos y emitir el hallazgo cuando difieran.
- [ ] Leer los criterios en «No» de la sección 5 y cruzarlos con el `estado-fase`.
- [ ] Comparar el conteo de la sección 1 contra el que el `estado-fase` repite.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-014-comparar-los-dos-veredictos](A-EP-004-HU-014-comparar-los-dos-veredictos/estado-fase.md) | Los tres: CA-01, CA-02 y CA-03 | Cerrada el 2026-08-16: **Cumple** |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-003](../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md), la forma del hallazgo | Medio |
| Dependencia | [pendientes/hecho/un-solo-veredicto-por-fase.md](../../../../pendientes/hecho/un-solo-veredicto-por-fase.md), que decide si se compara o se quita la copia. Si se quita, esta historia sobra | Alto |
| Riesgo | Que el veredicto esté escrito con palabras distintas en cada fase y la normalización falle | La plantilla ya fija «Cumple / No cumple» sin estado intermedio; lo que no encaje se reporta como aviso, no como falla |
| Riesgo | Que el hallazgo salga y nadie lo atienda | Depende de [EP-005 · HU-003](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md), que decide qué detiene |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Avisa cuando los dos veredictos difieren
- [ ] Avisa la fase dada por cumplida con un criterio en «No»
- [ ] Avisa el conteo que no cuadra
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Los dos documentos que compara ya existen |
| **N**egociable | Sí | Se puede quedar solo en el veredicto y dejar el conteo para después |
| **V**aliosa | Sí | Es lo que habría cazado la divergencia del 2026-08-15 |
| **E**stimable | Sí | Tres comparaciones entre dos documentos |
| **S**mall (pequeña) | Sí | Cabe en una fase |
| **T**esteable | Sí | Se arma una fase de prueba con la divergencia sembrada |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-7 del 2026-08-15 · `la-plantilla-del-resultado-de-pruebas` |
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Fase `A` (v23.1.0): un programa compara el veredicto del `resultado_pruebas` con el del `estado-fase`. De las dos salidas del pendiente 28 se eligió la que no cambia ningún molde |
