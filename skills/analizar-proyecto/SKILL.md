---
name: analizar-proyecto
description: Diagnostica un proyecto existente antes de desarrollar. Produce inventario (qué hay), brechas (qué falta) y plan priorizado (qué sigue), más la estrategia de pruebas y las tecnologías necesarias. Úsala al llegar a un proyecto nuevo, heredado o sin documentación, o cuando el usuario pide "analiza / audita / diagnostica el proyecto", "qué falta", "por dónde empiezo".
---

# Analizar proyecto

Diagnóstico **de solo lectura** de un proyecto existente. No cambia código: produce un informe para decidir qué hacer. Respeta el núcleo (`00`): nada destructivo, nada sin aprobación.

Sirve para el caso que `02` · F1 no cubre: un proyecto **sin** documentación del estándar, que hay que entender desde cero.

## Método (en orden)

### 1. Inventario — qué hay

Explora el repo (solo lectura) y registra:

- **Stack y estructura:** lenguajes, frameworks, cómo se organiza el código, punto de entrada.
- **Dependencias:** manifiesto + lockfile; versiones, cuáles desactualizadas.
- **Datos:** esquema/migraciones, motor de BD, dónde vive la configuración.
- **Pruebas:** qué hay, con qué framework, cobertura aproximada, si corren.
- **Seguridad/config:** manejo de secretos, autenticación/permisos, `.gitignore`.
- **Documentación:** qué existe (README, docs, specs) y qué tan actual está.
- **Capa 3:** ¿hay `CLAUDE.md`, marco normativo, mapeo de nombres? Si no, anótalo como brecha.

### 2. Evaluación contra el estándar

Recorre la base (`01`–`16`) y marca, por sección, qué se cumple y qué no. Presta atención especial a:

- **Seguridad (`04`)** y **cumplimiento (`16`)**: authz, secretos, inyección; y si hay marco normativo declarado (capa 3), si el desarrollo lo cumple.
- **Datos (`03`)**: normalización, auditoría, hardcode.
- **Pruebas (`08`)**: qué comportamiento crítico está sin cubrir.
- **Documentación (`13`)**: qué decisiones no están registradas.

No inventes hallazgos (`01` · C2): cada afirmación se apoya en un archivo real, con enlace.

### 3. Brechas — qué falta

Lista las brechas encontradas, clasificadas por tipo (funcional, datos, seguridad, cumplimiento, pruebas, rendimiento, documentación) y por **riesgo** (alto/medio/bajo). Una brecha de seguridad o de cumplimiento pesa más que una cosmética.

### 4. Estrategia de pruebas

Define qué pruebas hacen falta y con qué stack:

- Qué **tipos** faltan (unitarias, integración, end-to-end) según el riesgo del sistema.
- Qué **framework/herramientas** de prueba usar (coherente con el stack; ver `08` y `10`).
- Qué debe cubrirse primero: la lógica de negocio y los caminos de error (`08` · T6).
- Qué exige **verificación manual** (lo que el entorno de pruebas no reproduce — `08` · T4).

### 5. Tecnologías necesarias

Lista lo que falta en el stack para cerrar las brechas (una librería, un servicio, una herramienta de CI, un motor de caché…). Cada propuesta se **justifica** y se **consulta** — agregar tecnología es decisión del usuario (`01` · C4, `10` · DEP1), no del agente.

### 6. Plan priorizado — qué sigue

Ordena el trabajo por **riesgo y valor**: primero lo que es peligroso o bloqueante (seguridad, cumplimiento, datos), luego lo importante, luego lo cosmético. Cada ítem: qué es, por qué, y su tamaño aproximado.

Recuerda `02` · F2: lo que sea desarrollo nuevo necesita **spec acordada** antes de código. El plan puede incluir "redactar la spec de X" como primer paso.

## Salida

Un documento de diagnóstico **persistido** en la documentación del proyecto (`13`), no solo en el chat. Estructura:

```
1. Inventario (qué hay)
2. Brechas por tipo y riesgo (qué falta)
3. Estrategia de pruebas (tipos, stack, prioridades)
4. Tecnologías propuestas (con justificación)
5. Plan priorizado (qué sigue, en orden)
```

Cierra proponiendo el **primer paso concreto** y esperando la decisión del usuario. No arranques a implementar desde el diagnóstico: el diagnóstico informa, el usuario decide.
