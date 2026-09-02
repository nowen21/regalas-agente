# HU-005 — Crear los modelos de la capa de proyecto: stack, dominio, nombres propios

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — los tres CA y los dos transversales verificados el 2026-08-17 |
---

## 2. Narrativa

- **Como** quien abre una sesión de trabajo en un proyecto
- **Quiero** que el proyecto tenga escrito su stack, su dominio y sus nombres propios
- **Para** que la IA no tenga que adivinar con qué está trabajando ni cómo se llama cada cosa aquí

---

## 3. Contexto y descripción

Las reglas son las mismas para todos los proyectos, y por eso hablan en abstracto: dicen "catálogo", "auditoría", "permiso". Cada proyecto llama a eso de otra forma, guarda sus datos con otro motor y organiza su código a su manera.

Si eso no está escrito, la IA lo deduce del código, y deducir es adivinar. Peor todavía: adivina distinto en cada sesión.

Estos modelos son el puente entre la regla abstracta y el proyecto concreto. También son lo que permite que un programa compruebe reglas que hoy nadie comprueba, porque le dan contra qué comparar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El proyecto declara su stack: lenguajes, motor de datos, cómo se corre y cómo se prueba |
| RN-02 | El proyecto declara su dominio: qué hace el sistema, sus entidades, sus módulos y sus reglas de negocio |
| RN-03 | El proyecto declara cómo llama a cada concepto de las reglas |
| RN-04 | Lo que un programa vaya a leer se escribe en forma fija; lo que lee una persona admite prosa |
| RN-05 | Lo declarado vive en un solo sitio: no se repite en prosa en otro archivo |
| RN-06 | Lo que el proyecto no declara, no se le comprueba |

### 3.2 Supuestos

- Llenar estos documentos es trabajo de una sesión, no de un mes, y se hace al instalar el estándar en el proyecto.

### 3.3 Fuera de alcance

- Llevar los modelos a cada proyecto. Eso es EP-007.
- Los programas que leen la declaración. Eso es EP-004.

---

## 4. Criterios de aceptación

### CA-01 — Los tres modelos existen y no se pisan

```gherkin
Dado que se instala el estándar en un proyecto
Cuando se buscan los modelos de su capa propia
Entonces existen el del stack, el del dominio y el de los nombres
Y ninguno pide un dato que ya pide otro
```

**Cómo validarlo:**

1. Abrir la carpeta de modelos del estándar.
2. Ubicar los tres. Resultado esperado: están, y cada uno dice qué declara.
3. Buscar un dato que aparezca en dos. Resultado esperado: no hay ninguno; si un modelo lo necesita, enlaza al otro.
- **Aprobado cuando:** cada dato tiene un solo dueño.

### CA-02 — Lo que un programa lee tiene forma fija

```gherkin
Dado que un programa va a comparar el código contra lo declarado
Cuando lee la declaración
Entonces encuentra los datos en un formato fijo, no en prosa
```

**Cómo validarlo:**

1. Abrir el modelo de nombres propios.
2. Ubicar la parte que un programa lee. Resultado esperado: es una tabla de claves fijas, con el vocabulario de cada valor escrito.
3. Ubicar la parte que lee una persona. Resultado esperado: está separada y admite frases.
- **Aprobado cuando:** las dos partes conviven sin repetirse.

### CA-03 — Lo no declarado no se comprueba

```gherkin
Dado que un proyecto deja sin declarar una convención
Cuando se corre lo que la comprobaría
Entonces no se inventa ninguna convención
Y queda dicho qué no se está comprobando
```

**Cómo validarlo:**

1. Dejar en blanco una clave del modelo de nombres, en un proyecto de prueba.
2. Correr la comprobación que la usaría. Resultado esperado: no marca nada de esa familia.
3. Leer su salida. Resultado esperado: dice qué quedó sin comprobar y por qué.
- **Aprobado cuando:** el silencio del proyecto no se rellena con suposiciones.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto recién instalado, con los tres documentos vacíos, tiene comportamiento definido.
- [ ] **Privacidad** — los modelos no piden datos personales ni credenciales.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Legibilidad** | Una persona los llena sin ayuda, leyendo el propio modelo |
| **Detectabilidad** | Un programa lee la parte fija sin ambigüedad |
| **Mantenimiento** | Un solo sitio por dato, para que no se contradigan |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el modelo del stack.
- [ ] Escribir el modelo del dominio, con entidades y módulos.
- [ ] Escribir el modelo de nombres propios, con su parte de forma fija.
- [ ] Definir qué claves lee un programa y con qué vocabulario.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3](A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3/resultado_pruebas.md#6-veredicto-de-la-fase) — los tres CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta.** Los tres modelos existen, el instalador los pone en cada proyecto y un programa los lee. Falta su incremento en la especificación y la prueba de que no se pisan entre ellos.

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
| Dependencia | HU-001, porque los modelos usan la marca acordada | Alto |
| Dependencia | EP-001, porque lo que se declara son los nombres concretos de conceptos de las reglas | Alto |
| Riesgo | Que se pida tanto que nadie los llene | Todo admite quedar sin declarar, y no declarar solo apaga comprobaciones |
| Riesgo | Que la parte fija y la prosa digan cosas distintas | Lo declarado no se repite; se enlaza |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Los tres modelos existen
- [ ] La parte que lee un programa está definida con su vocabulario
- [ ] Ningún dato aparece en dos modelos
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la marca de HU-001 |
| **N**egociable | Sí | Qué se declara se puede discutir |
| **V**aliosa | Sí | Es lo que evita que la IA adivine |
| **E**stimable | Sí | Son tres documentos |
| **S**mall (pequeña) | Parcial | Tres modelos en una historia |
| **T**esteable | Sí | Se prueba llenándolos en un proyecto real |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los tres modelos existen, no se pisan y ninguno pide credenciales. Queda escrito por qué lo no declarado no se comprueba: exigir contra una convención que nadie escribió sería inventarla |
