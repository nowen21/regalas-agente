# HU-002 — Mostrar qué va a hacer antes de hacerlo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — el CA-02 se cerró en la fase `B`: la simulación anuncia también el registro de versión |
---

## 2. Narrativa

- **Como** quien va a instalar en un proyecto que ya tiene trabajo hecho
- **Quiero** ver qué va a tocar antes de que lo toque
- **Para** decidir con la lista a la vista y no arrepentirme después

---

## 3. Contexto y descripción

Instalar en una carpeta vacía no da miedo. En un proyecto con meses de trabajo, sí: nadie quiere correr algo que va a escribir archivos sin saber cuáles.

Un modo que solo muestra resuelve eso. Lista qué va a crear, qué va a modificar y qué va a dejar como está, y no toca nada. Quien lo lea decide.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay un modo que muestra lo que haría y no hace nada |
| RN-02 | La lista distingue lo que se crea, lo que se modifica y lo que se deja igual |
| RN-03 | En ese modo no se escribe ningún archivo |
| RN-04 | Lo que muestra es lo que después hace: sin sorpresas |
| RN-05 | Es el modo por defecto cuando no se pide aplicar |

### 3.2 Supuestos

- Quien instala prefiere mirar antes, sobre todo la primera vez en un proyecto con trabajo.

### 3.3 Fuera de alcance

- Deshacer una instalación ya aplicada.

---

## 4. Criterios de aceptación

### CA-01 — El modo que muestra no toca nada

```gherkin
Dado que se corre el instalador sin pedir aplicar
Cuando termina
Entonces listó lo que haría
Y ningún archivo del proyecto cambió
```

**Cómo validarlo:**

1. Anotar el estado de los archivos del proyecto de prueba.
2. Correr el instalador sin pedir aplicar. Resultado esperado: sale la lista de lo que haría.
3. Comparar los archivos. Resultado esperado: ninguno cambió.
- **Aprobado cuando:** mirar es gratis.

### CA-02 — Lo que muestra es lo que hace

```gherkin
Dado que se vio la lista de lo que haría
Cuando después se corre pidiendo aplicar
Entonces hace exactamente eso
```

**Cómo validarlo:**

1. Guardar la lista del modo que muestra.
2. Correr aplicando. Resultado esperado: los cambios coinciden con la lista.
3. Buscar un cambio que no estuviera en la lista. Resultado esperado: ninguno.
- **Aprobado cuando:** no hay sorpresas entre lo anunciado y lo hecho.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto ya al día muestra una lista vacía y lo dice.
- [ ] **Claridad** — la lista se entiende sin conocer el instalador por dentro.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Inocuidad** | El modo que muestra no escribe nada |
| **Fidelidad** | Lo anunciado y lo hecho coinciden |
| **Claridad** | La lista dice archivo por archivo qué pasaría |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), criterio CAE-02.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Calcular qué se haría, sin hacerlo.
- [ ] Mostrar la lista separada en crear, modificar y dejar igual.
- [ ] Usar el mismo cálculo para mostrar y para aplicar.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [B-EP-007-HU-002-el-registro-de-version-se-anuncia](B-EP-007-HU-002-el-registro-de-version-se-anuncia/estado-fase.md) | CA-02 | **Ejecutada el 2026-08-30.** Veredicto: [**Cumple**](B-EP-007-HU-002-el-registro-de-version-se-anuncia/resultado_pruebas.md#2-veredicto-de-la-fase) — la simulación compara la huella que va a quedar y nombra el archivo del registro. Declara reemplazar el veredicto de la fase `A` |
| [A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer](A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-01 sí; el CA-02 no. Pendiente el commit |

**La fase retro-documenta, y empieza midiendo.** Si el instalador **muestra antes** lo que va a hacer o lo cuenta mientras lo hace es lo que nadie anotó. Se mide antes de proponer: ya pasó que una HU naciera pidiendo algo que ya existía.

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
| Dependencia | HU-001, porque muestra lo que esa historia hace | Alto |
| Riesgo | Que el cálculo del modo que muestra se separe del que aplica | Es el mismo cálculo, usado dos veces |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El modo que muestra no escribe nada
- [ ] Lo anunciado coincide con lo hecho
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Va pegada al instalador de HU-001 |
| **N**egociable | Sí | El formato de la lista se puede discutir |
| **V**aliosa | Sí | Es lo que permite instalar sin miedo |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un modo más |
| **T**esteable | Sí | Se prueba comparando antes y después |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. CA-01 verificado: simular no escribe ni un archivo. CA-02 en «No»: de 13 archivos que aparecen al aplicar, el registro de versión no se anuncia, y la simulación afirma lo contrario |
