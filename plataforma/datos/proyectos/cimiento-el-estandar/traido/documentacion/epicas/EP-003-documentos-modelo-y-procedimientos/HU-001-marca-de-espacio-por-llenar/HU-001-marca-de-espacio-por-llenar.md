# HU-001 — Definir cómo se marca un espacio por llenar en un modelo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso |
---

## 2. Narrativa

- **Como** quien recibe un documento para aprobarlo
- **Quiero** que los espacios sin llenar se vean a simple vista
- **Para** no aprobar un documento que todavía trae los huecos del modelo

---

## 3. Contexto y descripción

Un modelo es un esqueleto con huecos. El problema aparece cuando alguien lo llena a medias: los huecos que quedaron se confunden con el texto, y el documento se aprueba con ellos adentro.

Hace falta una marca acordada, una sola, que cumpla dos condiciones: que se note al leer y que un programa la pueda contar. Si cada modelo usa la suya, ninguna de las dos se cumple.

Esta historia va primero porque todos los modelos que vienen después la usan.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay una sola marca para el espacio por llenar, y la usan todos los modelos |
| RN-02 | La marca se nota al leer, sin buscarla |
| RN-03 | Un programa puede encontrarla sin confundirla con el texto normal |
| RN-04 | Un documento entregado con marcas sin reemplazar no está terminado |
| RN-05 | La caja de instrucciones del modelo se borra al llenarlo; lo que explica para qué sirve el documento se queda |

### 3.2 Supuestos

- Los modelos se llenan a mano o con ayuda de la IA, no con un formulario.

### 3.3 Fuera de alcance

- Los modelos en sí. Esta historia define la marca, no los documentos.
- El programa que cuenta las marcas. Eso es EP-004.

---

## 4. Criterios de aceptación

### CA-01 — La marca se ve y se distingue del texto

```gherkin
Dado que un modelo tiene espacios por llenar
Cuando alguien lo abre
Entonces los espacios se distinguen del texto que sí es del modelo
```

**Cómo validarlo:**

1. Abrir cualquier modelo del estándar.
2. Recorrerlo de arriba abajo. Resultado esperado: se pueden señalar los espacios por llenar sin dudar cuáles son.
3. Contarlos a ojo y volverlos a contar buscando la marca. Resultado esperado: el mismo número.
- **Aprobado cuando:** ver la marca no exige leer con atención.

### CA-02 — Todos los modelos usan la misma marca

```gherkin
Dado que existen varios modelos
Cuando se comparan sus espacios por llenar
Entonces todos usan la misma marca
```

**Cómo validarlo:**

1. Tomar tres modelos distintos del estándar.
2. Buscar en cada uno cómo marca sus espacios. Resultado esperado: es la misma en los tres.
3. Buscar alguna marca distinta. Resultado esperado: no aparece ninguna.
- **Aprobado cuando:** hay una sola convención en todo el catálogo.

### CA-03 — Un documento con marcas sin llenar no se da por terminado

```gherkin
Dado que un documento salió de un modelo
Cuando quedó una marca sin reemplazar
Entonces el documento no se considera terminado
```

**Cómo validarlo:**

1. Llenar un modelo dejando a propósito dos marcas.
2. Presentarlo como terminado. Resultado esperado: la regla dice que no lo está, y se puede señalar dónde.
3. Reemplazar las dos marcas. Resultado esperado: ahora sí se puede dar por terminado.
- **Aprobado cuando:** la condición de terminado es objetiva.

### Criterios de aceptación transversales

- [x] **Límites** — está definido qué se escribe cuando una sección no aplica, en vez de dejarla con la marca.
- [x] **No regresión** — los modelos ya escritos se pasan a la marca acordada.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Legibilidad** | La marca no estorba la lectura del modelo |
| RNF-02 | **Detectabilidad** | Un programa la encuentra sin falsos positivos |
| RNF-03 | **Uniformidad** | Una sola marca en todo el catálogo de modelos |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), §5.4 filas 4 y 5.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Elegir la marca y escribir por qué esa y no otra.
- [x] Escribir qué se pone cuando una sección no aplica.
- [x] Pasar los modelos existentes a la marca acordada.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-001-marca-de-espacio-por-llenar](A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md) | CA-01, CA-02 y CA-03 | Estación 11: los tres CA en verde, esperando el commit |

Una sola fase para los tres criterios: los tres se apoyan en la misma decisión (cuál es la marca) y ninguno se puede probar sin ella (`02·F12.10`).

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
| Dependencia | Ninguna: es la primera de la épica | Bajo |
| Riesgo | Que la marca elegida choque con la sintaxis del formato en que se escriben los documentos | Se prueba contra los tres formatos que más se usan antes de fijarla |
| Riesgo | Que se elija una marca que un programa no distinga de un enlace o una casilla | La detectabilidad es criterio de aceptación, no un extra |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [x] La marca está elegida y escrita
- [x] Todos los modelos la usan
- [x] Está definido qué se escribe cuando algo no aplica
- [x] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No necesita ningún modelo escrito |
| **N**egociable | Sí | Cuál es la marca se puede discutir |
| **V**aliosa | Sí | Sin ella, los huecos se aprueban sin que nadie los vea |
| **E**stimable | Sí | Una decisión y su aplicación |
| **S**mall (pequeña) | Sí | Alcance corto |
| **T**esteable | Sí | Se prueba llenando un modelo a medias |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Se abre la fase A con sus dos planes. Verificado que la marca `«…»` ya se usa de hecho en 25 de las 30 plantillas, sin regla que la respalde |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Fase ejecutada: nacen `13·DOC19`, [`DOC20`](../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](../../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md), y 179 huecos pasan a la marca acordada. Los tres CA en verde |
