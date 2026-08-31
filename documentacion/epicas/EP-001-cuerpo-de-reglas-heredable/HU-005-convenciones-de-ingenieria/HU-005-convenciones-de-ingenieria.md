# HU-005 — Convenciones de ingeniería agnósticas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Solicitante** | Quien define el estándar |
| **Estado** | Pendiente |
## 2. Narrativa

- **Como** quien trabaja con la IA en proyectos de lenguajes distintos
- **Quiero** que las buenas prácticas de ingeniería estén escritas una sola vez y sin atarse a ningún lenguaje
- **Para** que el mismo criterio valga en todos mis proyectos, sean del stack que sean

## 3. Contexto y descripción

Las buenas prácticas que importan son casi siempre las mismas: validar lo que entra, no repetir código, manejar el error, escribir la prueba, no dejar el dato quemado, documentar la decisión. Lo que cambia entre un proyecto y otro es cómo se escriben, no qué se exige.

Esta historia escribe ese cuerpo de convenciones separado por tema, sin nombrar ningún lenguaje ni ningún framework, para que sirva igual en todos lados. Un proyecto después lo concreta en su capa propia.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Ninguna convención nombra un lenguaje, un framework ni un producto concreto |
| RN-02 | Un tema tiene un solo capítulo dueño. Lo que aparece en dos, se enlaza, no se repite |
| RN-03 | Cada convención es ajustable desde la capa del proyecto |
| RN-04 | Las convenciones que solo aplican a cierto tipo de proyecto se marcan como opcionales |
| RN-05 | Antes de escribir una convención nueva se busca si ya existe una que la cubra |

### 3.2 Supuestos

- Los temas que hoy importan son los del trabajo diario: datos, seguridad, errores, rendimiento, calidad, pruebas, control de versiones, dependencias, configuración, privacidad, documentación y estructura.

### 3.3 Fuera de alcance

- Cómo se concreta cada convención en un lenguaje. Eso lo pone cada proyecto en su capa.
- Comprobar automáticamente que se cumplan. Eso es EP-004.
- Los temas opcionales que hoy ningún proyecto pide, como despliegue u observabilidad.

## 4. Criterios de aceptación

### CA-01 — Una convención sirve igual en dos proyectos de lenguajes distintos

```gherkin
Dado que existe una convención escrita sin nombrar ningún lenguaje
Cuando se aplica en un proyecto de un lenguaje y en otro de un lenguaje distinto
Entonces en los dos exige lo mismo
Y cada proyecto la concreta a su manera desde su capa propia
```

**Cómo validarlo:**

1. Tomar una convención escrita, por ejemplo la que exige validar toda entrada.
2. Leerla parándose en un proyecto de un lenguaje y decir qué exigiría ahí. Resultado esperado: la exigencia se entiende sin traducir nada.
3. Repetir el paso 2 parándose en un proyecto de otro lenguaje. Resultado esperado: la exigencia es la misma, aunque la forma de cumplirla sea distinta.
- **Aprobado cuando:** la convención no nombra ninguna tecnología y las dos lecturas coinciden en qué se exige.

### CA-02 — Un tema no aparece en dos capítulos

```gherkin
Dado que cada tema tiene un solo capítulo dueño
Cuando se busca un tema en todo el cuerpo de convenciones
Entonces aparece exigido en un solo lugar
Y los demás capítulos que lo mencionan lo enlazan en vez de repetirlo
```

**Cómo validarlo:**

1. Elegir un tema que suene a que puede estar en varios lados, por ejemplo el manejo de claves.
2. Buscar ese tema en todos los capítulos. Resultado esperado: aparece exigido en uno solo.
3. Revisar las demás menciones. Resultado esperado: son enlaces a ese capítulo, no exigencias repetidas.
- **Aprobado cuando:** hay una sola exigencia y las demás menciones enlazan.

### CA-03 — Una convención que solo sirve a cierto tipo de proyecto queda marcada como opcional

```gherkin
Dado que hay convenciones que no todos los proyectos necesitan
Cuando se escribe una de esas
Entonces queda marcada como opcional
Y un proyecto que no la activa no queda incumpliendo nada
```

**Cómo validarlo:**

1. Ubicar una convención marcada como opcional.
2. Revisar un proyecto de prueba que no la haya activado. Resultado esperado: no aparece como incumplimiento en ninguna revisión.
3. Activarla en la capa propia de ese proyecto. Resultado esperado: ahora sí aplica y se puede revisar.
- **Aprobado cuando:** sin activar no exige nada, y activada exige.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué pasa cuando una convención choca con otra del mismo nivel.
- [ ] **No regresión** — agregar una convención no invalida las que ya existían.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Portabilidad | Ninguna convención nombra un lenguaje, framework o producto |
| Legibilidad | Cada convención se entiende sin saber del tema |
| Navegabilidad | Desde cualquier capítulo se llega al dueño del tema en un enlace |

## 6. Tareas técnicas derivadas

- [ ] Definir la lista de temas y su capítulo dueño.
- [ ] Escribir las convenciones de cada tema con el molde de HU-001.
- [ ] Marcar las opcionales y decir cómo se activan.
- [ ] Revisar que ninguna nombre una tecnología.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/resultado_pruebas.md#6-veredicto-de-la-fase) — probada sobre **AgroSystem** (PHP) y **RNI** (Angular más Python). El único solape de tema del cuerpo ya estaba derogado hacia su dueño |

**La fase retro-documenta y no toca `base/`.** Los diecisiete capítulos de convenciones existen, todos `[CAPA 2]` y cinco marcados `opt-in`. Lo que falta es demostrarlo: la misma convención cumplida en dos proyectos de lenguajes distintos, y la revisión de si algún tema aparece en dos capítulos.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta historia de usuario |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada criterio | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el criterio quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, por el molde | Alto |
| Dependencia | HU-002, por la marca de capa | Alto |
| Riesgo | Que se cuele una convención atada a un lenguaje | Se revisa una por una antes de aceptarla, y es parte de la definición de terminado |
| Riesgo | Que el cuerpo crezca tanto que la IA no lo lea completo | Un tema, un capítulo, nada duplicado |
| Riesgo | Que dos convenciones exijan lo contrario | Cada una declara de cuál depende y a cuál ajusta |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Lista de temas acordada
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] Cada tema tiene su capítulo con sus convenciones escritas
- [ ] Ninguna convención nombra una tecnología
- [ ] Ningún tema aparece exigido en dos capítulos
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el molde y las capas |
| Negociable | Sí | La lista de temas se discute |
| Valiosa | Sí | Es el grueso de lo que un proyecto hereda |
| Estimable | Sí | Se estima por tema |
| Pequeña | No | Es la historia más grande de la épica. Se corta por capítulo en las fases |
| Testeable | Sí | Se verifica leyendo y buscando tecnologías nombradas |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
