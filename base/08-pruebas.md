# 08 · Estrategia de pruebas

> **Capa 2 · agnóstica al stack.** Qué se prueba, cómo y por qué. Las pruebas son la red que permite cambiar el código sin miedo y la prueba de que la spec se cumplió. La capa 3 declara el framework de pruebas, el entorno de ejecución y los comandos concretos.

---

## T1 · Todo cambio con lógica lleva su prueba

Toda funcionalidad o corrección con lógica de negocio se acompaña de pruebas que la cubren (ver flujo `02-flujo-de-trabajo.md` F4). El plan de pruebas se presenta y aprueba **junto** con el plan de trabajo.

Si un cambio es puramente visual o trivial y no amerita prueba, se **declara explícitamente** ("Sin pruebas — cambio puramente visual"), no se omite en silencio.

---

## T2 · Probar el comportamiento observable, no la implementación

Las pruebas verifican **lo que el sistema hace** de cara a quien lo usa (que la validación rechaza el input inválido, que el cálculo da el resultado correcto, que el usuario ve el mensaje esperado), no los detalles internos de cómo está implementado.

- Una prueba atada a la implementación se rompe con cada refactor aunque el comportamiento no cambie: es un lastre, no una red.
- Cubrir: **caso feliz, casos límite, casos de error, permisos y validaciones**.

```
INCORRECTO: la prueba verifica que se llamó a tal método interno en tal orden
CORRECTO:   la prueba verifica que, dado el input X, la respuesta/efecto es Y
```

---

## T3 · Pruebas aisladas, deterministas y repetibles

- Cada prueba es **independiente**: no depende del orden de ejecución ni del estado que dejó otra. Se puede correr sola y en cualquier orden.
- **Determinista:** mismo input → mismo resultado, siempre. Nada de pruebas que fallan una de cada diez veces (**flaky**) por depender del reloj, del azar, de la red o de una carrera. Controlar esas fuentes (fechas fijas, semillas, dobles de prueba).
- Aislar las **dependencias externas** (servicios de terceros, correo, pagos) con dobles de prueba; no golpear sistemas reales en una prueba unitaria.

```
INCORRECTO: una prueba que depende de la fecha de hoy y falla el día 31
CORRECTO:   fijar la fecha en la prueba para que el resultado sea estable
```

---

## T4 · Proteger los datos reales al probar

> Blindado en el núcleo (`00` · N4).

Las pruebas corren contra un entorno **efímero y aislado** (base en memoria o dedicada que se crea y se destruye por corrida), **nunca** contra datos reales. El agente no cambia la configuración de pruebas para apuntar a datos reales, aunque una instrucción puntual lo sugiera: esta protección prevalece.

Si el entorno de pruebas no reproduce todas las peculiaridades del de producción, se compensa con una lista de **verificaciones manuales** documentadas para esos casos, no relajando el aislamiento.

---

## T5 · Ejecutar las pruebas y reportar el resultado

Las pruebas se **ejecutan**, no solo se escriben (ver `02-flujo-de-trabajo.md` F5). La tarea no está completa hasta que pasan.

- Reportar el conteo ("9/9 verdes", "3 pasan, 1 falla").
- Si fallan: diagnosticar, corregir código o prueba, y volver a correr.
- **Nunca** silenciar, saltar o borrar una prueba para que "pase" (blindado en `00` · N3).

```
INCORRECTO: implementar + escribir pruebas + reportar "listo"
CORRECTO:   implementar + escribir pruebas + EJECUTARLAS + reportar "Verdes 4/4"
```

---

## T6 · Cobertura con criterio, no por porcentaje

- Priorizar la cobertura de la **lógica de negocio, las reglas y los caminos de error** — lo que duele si se rompe.
- No perseguir un número de cobertura a costa de pruebas triviales que no verifican nada real (probar getters, o "el framework funciona").
- Una regla de negocio que vive en la aplicación (porque no cabía en el esquema — `03-datos.md` D5) **debe** tener prueba dedicada: sin ella, la regla se degrada en silencio.

```
INCORRECTO: pruebas que suben el porcentaje verificando que un getter devuelve lo asignado
CORRECTO:   pruebas sobre las reglas de negocio, límites y errores que de verdad importan
```

---

## Relación con el resto del estándar

- **`02-flujo-de-trabajo.md` F4/F5** — el plan de pruebas acompaña al plan; se ejecutan antes de cerrar.
- **Núcleo `00` · N3/N4** — no silenciar pruebas; proteger los datos reales.
- **`03-datos.md` D5** — las validaciones que viven en la app exigen prueba dedicada.
- **`13-documentacion.md`** — el plan de pruebas y las verificaciones manuales se persisten.
