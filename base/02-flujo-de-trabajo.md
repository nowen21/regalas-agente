# 02 · Flujo de trabajo

> **Capa 2 · agnóstica al stack.** Cómo desarrolla el agente: la secuencia desde que llega una solicitud hasta que una tarea se declara terminada. Mientras `01-conducta.md` describe *cómo se comporta*, esta sección describe *cómo trabaja*. La capa de proyecto define los detalles concretos (dónde viven los documentos, cómo se corren las pruebas); el flujo es el mismo.

---

## F1 · Cargar el contexto documentado antes de actuar

Antes de analizar, diseñar, corregir o implementar, el agente **revisa primero** la documentación del proyecto (la capa 3 declara dónde vive): qué ya está construido, qué decisiones se tomaron, qué casos están cubiertos por pruebas, qué está pendiente.

Aplica al inicio de cada tarea, antes de proponer un plan, y **antes** de declarar que algo "no existe" o "habría que crearlo". Si el usuario menciona algo existente ("la validación de saldo", "el modal de reportes"), el agente primero busca si ya está documentado o implementado.

Con esto se evita: duplicar lo ya hecho, contradecir reglas de negocio previas, y reiniciar el entendimiento del proyecto desde cero cada sesión.

```
INCORRECTO: "agregá la validación X" → el agente la diseña desde cero
CORRECTO:   el agente revisa la documentación → encuentra un servicio que ya hace algo
            similar → propone extenderlo en vez de duplicar
```

---

## F2 · La especificación es la línea base — sin diseño acordado no hay código

Ningún desarrollo, refactor, migración o cambio funcional se ejecuta sin que exista una **especificación acordada** (el "prompt de módulo" o documento de diseño) que lo respalde. La spec es el contrato entre usuario y agente: define alcance, reglas de negocio, modelo de datos, pruebas, permisos y criterios de aceptación. Sin ella, cualquier código es opinión del agente, no diseño acordado.

**Aplicación:**

1. **¿Existe la spec del módulo?** La capa 3 declara dónde buscarla.
   - **No existe** → el agente **no avanza con código**. Ofrece redactar un borrador con las secciones estándar (contexto, regla de negocio, modelo de datos, fases, pruebas, permisos) para que el usuario lo apruebe. Solo con la spec aprobada se pasa al plan y al código.
   - **Sí existe** → el agente la lee entera antes de proponer cambios.
2. **¿El requerimiento ya está en la spec?**
   - Está y se implementó → decir dónde está y actuar según lo pedido.
   - Está pero falta → implementarlo en la fase donde debía estar (no crear fase nueva).
   - No está → **antes de escribir código, actualizar la spec** con la regla/sección/prueba nueva; luego desarrollar. La spec siempre precede al código.

**Motivación:** la spec es la memoria de largo plazo del diseño. Sin ella, cada sesión reinterpreta el negocio y aparecen contradicciones cuando otro desarrollador (u otro modelo) toca el módulo meses después.

**Excepciones legítimas — no requieren spec previa:** correcciones triviales (tipos, formato, comentarios), bugfixes donde el diseño correcto ya está en la spec (el fix es realinear el código a la spec), configuración de entorno local, comandos operativos que el usuario pide explícitamente, e investigación de solo lectura para responder una pregunta.

```
INCORRECTO: "hacé que el módulo permita X" → el agente escribe código directo
CORRECTO:   busca X en la spec → si no está: "esto no está en la spec del módulo; antes de
            implementarlo necesito agregarlo. ¿Va como mejora a la fase Y o es dominio nuevo?"
            → el usuario aprueba → se actualiza la spec → se planifica → se implementa con pruebas
```

> **Ajuste de capa 3:** un proyecto puede definir cuán estricta es esta regla, pero el estándar la trae **activada por defecto** — es el corazón del método.

---

## F3 · Plan aprobado = ejecución continua

Una vez que el usuario aprueba un plan de trabajo, el agente ejecuta **todos** los cambios del plan de forma continua, sin pedir permiso por cada archivo o sección. La aprobación del plan cubre todo lo que el plan describe.

Solo se pausa y consulta si surge una decisión **no cubierta** por el plan (un archivo inesperado, un conflicto técnico, una ambigüedad nueva).

```
INCORRECTO: plan aprobado → "hago el cambio 1, ¿procedo?" → "ahora el 2, ¿procedo?" → ...
CORRECTO:   plan aprobado → ejecutar todos los cambios → reportar el resultado final
```

---

## F4 · Todo plan de trabajo incluye su plan de pruebas

Cualquier plan que el agente proponga se acompaña de un **plan de pruebas** explícito: qué comportamiento se prueba, qué escenarios se cubren (caso feliz, límites, errores, permisos, validaciones), qué archivo de prueba se crea/modifica y qué se verifica. Ambos se presentan juntos y se aprueban juntos.

Si el cambio es puramente visual o trivial y no amerita prueba, se declara explícitamente ("Sin pruebas — cambio puramente visual"), no se omite en silencio.

```
INCORRECTO: plan de trabajo solo → "ya implementé, ¿corro pruebas?"
CORRECTO:   plan de trabajo + plan de pruebas → aprobación → implementar código + pruebas
```

---

## F5 · Ejecutar las pruebas antes de declarar la tarea completa

Si el plan incluye pruebas, esas pruebas se **ejecutan**, no solo se escriben. La tarea no está completa hasta que pasan.

- Ejecutar las pruebas al terminar la implementación y **reportar el conteo** ("9/9 verdes", "3 pasan, 1 falla").
- Si fallan: diagnosticar, corregir el código o la prueba, y volver a correr.
- No marcar como completa una tarea con pruebas en rojo.
- No silenciar pruebas para que "pasen" (esto está blindado en `00` · N3).

```
INCORRECTO: implementar + escribir pruebas + reportar "listo"
CORRECTO:   implementar + escribir pruebas + EJECUTARLAS + reportar "Verdes 4/4"
```

---

## F6 · Persistir el trabajo y las decisiones en disco

El chat se pierde; los archivos quedan. Al cerrar una unidad de trabajo, lo acordado y lo implementado se persiste en documentación versionada (formato y ubicación los define la capa 3 y `13-documentacion.md`): qué se planeó, qué se probó, qué quedó implementado, y **las decisiones de diseño no obvias con su porqué**.

Sin esto, las próximas sesiones y otros desarrolladores re-descubren cada decisión desde cero.

---

## F7 · Verificar trazabilidad spec → implementación antes de cerrar

Antes de declarar una unidad de trabajo terminada, el agente verifica **ítem por ítem** que toda afirmación técnica de la spec esté realmente reflejada en el código, el esquema, las pruebas y los docs. No se cierra si queda un ítem faltante sin justificar.

Esto evita que una regla explícita de la spec ("el selector se filtra por X", "el método tiene la firma Y") se pierda en el ruido de un plan largo y aparezca meses después como bug. La spec es el contrato; el checklist es la prueba de que se cumplió. El formato del checklist lo detalla `13-documentacion.md`.

```
INCORRECTO: "todas las pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + checklist spec→implementación sin faltantes → cierro"
```

---

## Secuencia resumida

```
solicitud
  → F1 cargar contexto documentado
  → F2 ¿hay spec? (si no, redactarla y aprobarla antes de tocar código)
  → proponer plan + plan de pruebas (F4), explicando el porqué (conducta C1)
  → aprobación del usuario
  → F3 ejecutar el plan completo, continuo
  → F5 ejecutar las pruebas y reportar el conteo
  → F6 persistir trabajo y decisiones
  → F7 verificar trazabilidad spec → implementación
  → declarar terminado (conducta C5: corto y accionable)
```
