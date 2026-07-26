# Aislamiento de contexto · Checkpoints de calidad · Memoria institucional

> Tres capacidades de orquestación/gobernanza. Estado honesto de cada una y qué faltaría. `✅` cubierto · `⚠️` parcial · `⏳` pendiente.

## 1. Aislamiento de contexto — `⚠️` parcial

**Qué es.** Cada rol o tarea trabaja **solo con el contexto que necesita**, aislado del resto. Una estación no ve el ruido de las otras: el Designer recibe la spec, no todo el historial; el Implementer recibe su tarea, no la conversación entera. Evita que el contexto de un rol contamine a otro y mantiene cada paso enfocado (y más barato).

**Hoy.** Hay **disciplina de alcance** —no salir de la tarea (`01`·C3), confirmar que el archivo es de la tarea (`01`·C6)—, pero eso es autocontrol del mismo agente, no aislamiento real.

**Qué faltaría.**
- Que cada rol del orquestador corra como **sub-agente con su propia ventana de contexto**.
- Que el orquestador le pase a cada rol **solo sus entradas** (la spec al Designer, el plan al Implementer), no todo lo anterior.
- **Depende del entorno**: el aislamiento real por sub-agente es una capacidad de Claude Code, no del estándar.

## 2. Checkpoints de calidad — `⚠️` diseñado, sin imponer

**Qué es.** Puntos del flujo donde se **verifica la calidad antes de avanzar**. Son las **puertas** de la línea de montaje: si no pasan, el trabajo no sigue.

**Hoy.** Las verificaciones individuales **ya existen** en la base: pruebas verdes (`02`·F5), trazabilidad spec→implementación (`13`·DOC3), lint sin advertencias (`07`·Q6), pruebas y triangulación (`08`, `T7`). Y las puertas están **diseñadas** por rol (ver [`roles-especializados.md`](roles-especializados.md)). Lo que falta es **quién las impone**.

**Qué faltaría.**
- Definir el **checklist exacto de cada checkpoint** (qué se mide: tests, lint, cobertura de casos, trazabilidad, revisión de seguridad, atributos de calidad `16`·CQ4).
- Que el **orquestador bloquee el avance** si un checkpoint no pasa (no depender de que el agente "se acuerde").

## 3. Memoria institucional — `✅` dentro del proyecto · `⏳` entre proyectos

**Qué es.** El proyecto **retiene el conocimiento** a través del tiempo y de las sesiones: qué se decidió y por qué, para que ninguna sesión (ni otra persona) re-aprenda desde cero.

**Hoy (bien cubierto dentro del proyecto).**
- La **spec es la memoria de largo plazo** del diseño (`02`·F2).
- Se **persisten trabajo y decisiones con su porqué** (`13`·DOC1/DOC2), y se **carga el contexto documentado** antes de actuar (`02`·F1).
- **Trazabilidad** spec→implementación (`13`·DOC3).
- El agente tiene además su **memoria de feedback** propia.

**Qué faltaría (extensión).**
- Una capa **entre proyectos / organizacional**: biblioteca de patrones, lecciones aprendidas y decisiones que aplican a toda la empresa. Hoy cada proyecto guarda lo suyo; el único conocimiento común es el propio estándar.

## Resumen

| Capacidad | Estado | Ligado a |
|---|---|---|
| Aislamiento de contexto | ⚠️ parcial (disciplina de alcance) | sub-agentes de Claude Code + orquestador |
| Checkpoints de calidad | ⚠️ verificaciones existen, falta imponerlas | orquestador (puertas) |
| Memoria institucional | ✅ dentro del proyecto · ⏳ entre proyectos | `13` + `02`; capa org nueva |
