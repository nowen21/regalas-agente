# 02 · Flujo de trabajo

Cómo trabaja el agente: de la solicitud a la tarea terminada. La capa 3 define dónde viven los documentos y cómo se corren las pruebas.

---

## F1 · Carga el contexto antes de actuar

Antes de analizar o implementar, revisa la documentación del proyecto (qué existe, qué se decidió, qué está probado). Aplica también **antes** de decir "esto no existe". Si el usuario menciona algo existente, primero búscalo.
Evita: duplicar lo hecho, contradecir reglas previas, re-entender el proyecto desde cero.

```
INCORRECTO: "agregá validación X" → la diseño desde cero
CORRECTO:   reviso docs → ya hay un servicio que hace algo similar → propongo extenderlo
```

## F2 · Sin spec acordada no hay código

Ningún desarrollo, refactor o migración sin una **spec acordada** (prompt de módulo) que lo respalde: alcance, reglas de negocio, datos, pruebas, permisos. Sin spec, el código es opinión del agente.

1. **¿Existe la spec?** (la capa 3 dice dónde). Si no, el agente **no toca código**: ofrece redactar un borrador y aprobarlo primero.
2. **¿El requerimiento ya está?** Si está y falta implementarlo, hazlo donde debía ir. Si no está, **primero actualiza la spec**, luego codifica.

Excepciones (no requieren spec): correcciones triviales, bugfixes que realinean el código a la spec, config local, comandos que el usuario pide, y lectura/investigación.

```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la spec → si no está: "no está en la spec; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo spec → implemento + pruebas
```

> La capa 3 puede ajustar cuán estricta es, pero viene **activada por defecto**.

## F3 · Plan aprobado = ejecución continua

Aprobado el plan, ejecuta **todos** sus cambios seguidos, sin pedir permiso por cada archivo. Solo pausa si surge algo **no cubierto** por el plan.

```
INCORRECTO: "hago el cambio 1, ¿procedo?" → "el 2, ¿procedo?" → ...
CORRECTO:   ejecuto todo el plan → reporto el resultado
```

## F4 · Todo plan lleva su plan de pruebas

Cada plan se acompaña de las pruebas: qué se prueba, escenarios (feliz, límites, errores, permisos), qué archivo, qué se verifica. Se aprueban juntos.
Si no amerita prueba (visual/trivial), decláralo: "Sin pruebas — cambio visual".

```
INCORRECTO: plan solo → "ya implementé, ¿corro pruebas?"
CORRECTO:   plan + plan de pruebas → aprobación → implementar código + pruebas
```

## F5 · Ejecuta las pruebas antes de dar por terminado

Las pruebas se **corren**, no solo se escriben. La tarea no está lista hasta que pasan.
Reporta el conteo ("9/9 verdes"). Si fallan: diagnostica, corrige, vuelve a correr. Nunca las silencies para que pasen (`00` · N3).

```
INCORRECTO: implementar + escribir pruebas + "listo"
CORRECTO:   implementar + escribir + EJECUTAR + "Verdes 4/4"
```

## F6 · Persiste el trabajo y las decisiones

El chat se pierde; los archivos quedan. Al cerrar, guarda en documentación versionada: qué se planeó, qué se probó, qué quedó, y **las decisiones no obvias con su porqué** (detalle en `13`).

## F7 · Verifica trazabilidad spec → implementación

Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la spec esté en el código, el esquema, las pruebas y los docs. No cierres con faltantes sin justificar (formato en `13` · DOC3).

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + trazabilidad sin faltantes → cierro"
```

---

**Secuencia:** contexto (F1) → spec (F2) → plan + pruebas (F4) → aprobación → ejecutar (F3) → correr pruebas (F5) → persistir (F6) → trazabilidad (F7) → cerrar.
