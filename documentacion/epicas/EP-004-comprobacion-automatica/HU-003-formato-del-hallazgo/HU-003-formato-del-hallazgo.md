# HU-003 — Definir el formato de un hallazgo y su severidad

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso — los tres CA cumplidos; el transversal de errores, no |
---

## 2. Narrativa

- **Como** quien recibe el resultado de una comprobación
- **Quiero** que todo hallazgo tenga la misma forma y diga qué regla, dónde y qué se esperaba
- **Para** poder arreglarlo sin abrir el programa que lo encontró

---

## 3. Contexto y descripción

Un hallazgo que dice "hay un error" no sirve. Quien lo lee tiene que ir a buscar dónde, adivinar qué se esperaba y, en el peor caso, abrir el programa para entender qué revisó.

Además hay dos clases de hallazgo que no se pueden mezclar. Uno es el incumplimiento claro, que debe detener el trabajo. El otro es lo que un humano tiene que mirar, que no debe detener nada: las plantillas dicen que se borren las secciones que no apliquen, así que una sección ausente no siempre es una falta.

Un programa que grita por todo se termina apagando. Esta historia fija la forma del hallazgo y las dos severidades, antes de escribir las comprobaciones que las usan.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo hallazgo dice qué regla se incumple, en qué archivo, en qué línea y qué se esperaba |
| RN-02 | Hay dos severidades y solo dos: falla, que detiene, y aviso, que informa |
| RN-03 | La falla es el incumplimiento sin ambigüedad; lo dudoso sale siempre como aviso |
| RN-04 | Un aviso nunca hace fallar la corrida |
| RN-05 | El hallazgo sin regla asociada no se emite: si ninguna regla lo respalda, la comprobación sobra |
| RN-06 | Todos los programas emiten el hallazgo con la misma forma |

### 3.2 Supuestos

- Quien lee el hallazgo conoce el estándar, pero no los programas. Por eso alcanza con citar la regla por su identificador.

### 3.3 Fuera de alcance

- Corregir lo encontrado. Los programas reportan.
- El resumen de la corrida completa. Eso es HU-008.

---

## 4. Criterios de aceptación

### CA-01 — El hallazgo alcanza para arreglar sin abrir el programa

```gherkin
Dado que una comprobación encuentra un incumplimiento
Cuando se emite el hallazgo
Entonces dice la regla, el archivo, la línea y qué se esperaba
Y quien lo lee puede corregirlo sin abrir el programa
```

**Cómo validarlo:**

1. Provocar un incumplimiento a propósito en un archivo de prueba, por ejemplo un enlace que apunte a un archivo que no existe.
2. Correr la comprobación. Resultado esperado: sale un hallazgo con las cuatro piezas.
3. Entregarle ese hallazgo a alguien que no conoce el programa. Resultado esperado: arregla el archivo sin preguntar nada.
- **Aprobado cuando:** las cuatro piezas están y el arreglo se hace sin abrir el código de la comprobación.

### CA-02 — Lo dudoso sale como aviso y no detiene

```gherkin
Dado que una comprobación encuentra algo que puede tener un motivo legítimo
Cuando se emite el hallazgo
Entonces sale con severidad de aviso
Y la corrida termina sin error
```

**Cómo validarlo:**

1. Preparar un caso dudoso, por ejemplo un documento al que le falta una sección que la plantilla permite borrar.
2. Correr la comprobación. Resultado esperado: aparece el hallazgo marcado como aviso.
3. Mirar con qué código terminó la corrida. Resultado esperado: termina en cero, que significa que no detiene.
- **Aprobado cuando:** el aviso se ve y la corrida no se rompe por él.

### CA-03 — Una falla detiene

```gherkin
Dado que una comprobación encuentra un incumplimiento sin ambigüedad
Cuando se emite el hallazgo
Entonces sale con severidad de falla
Y la corrida termina con error
```

**Cómo validarlo:**

1. Provocar un incumplimiento claro, por ejemplo un enlace roto.
2. Correr la comprobación. Resultado esperado: el hallazgo sale marcado como falla.
3. Mirar el código con que terminó. Resultado esperado: termina en uno, que significa que detiene.
- **Aprobado cuando:** la falla se ve y la corrida termina en error.

### Criterios de aceptación transversales

- [ ] **Límites** — un hallazgo sobre un archivo entero, sin línea concreta, tiene forma definida.
- [ ] **Errores** — el archivo que no se puede leer produce un mensaje entendible, no un volcado técnico.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Legibilidad** | El hallazgo se lee en una línea, en una terminal, con tildes y con rutas que llevan espacios |
| **Determinismo** | El mismo insumo produce el mismo hallazgo, con el mismo texto |
| **Uniformidad** | Todos los programas usan la misma forma, sin variantes propias |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.4 filas 3, 5, 7 y 12.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir las piezas del hallazgo y su orden en la salida.
- [ ] Definir las dos severidades y qué hace cada una con el código de salida.
- [ ] Escribir el criterio de cuándo algo es falla y cuándo es aviso.
- [ ] Dejar la forma en un solo sitio, que los demás programas reutilicen.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo](A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md#6-veredicto-de-la-fase) — los tres CA numerados sí; el transversal de errores no. Pendiente el commit |

**La fase retro-documenta.** El formato existe y lo usan los 24 subcomandos, con sus dos severidades. Falta el contrato escrito y la prueba de que el código de salida es el que corresponde.

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
| Dependencia | HU-001, porque el criterio decide qué merece ser hallazgo | Medio |
| Riesgo | Que todo se marque como falla y el control termine ignorado | Lo dudoso sale como aviso, y eso queda escrito como regla de negocio |
| Riesgo | Que cada programa invente su propio formato | La forma vive en un solo sitio y los demás la usan |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La forma del hallazgo está definida y escrita
- [ ] Las dos severidades están definidas, con su efecto en el código de salida
- [ ] Existe un solo sitio del que salen los hallazgos
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Se define antes de escribir cualquier comprobación |
| **N**egociable | Sí | Las piezas del hallazgo se pueden discutir |
| **V**aliosa | Sí | Sin ella, cada hallazgo obliga a abrir el programa |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Una definición y una pieza compartida |
| **T**esteable | Sí | Se prueba provocando un caso de cada severidad |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los tres CA verificados sobre una corrida real de 207 hallazgos, y el contrato de la salida queda escrito. El transversal de errores en «No»: un `.md` que no se puede decodificar tumba la corrida entera |
