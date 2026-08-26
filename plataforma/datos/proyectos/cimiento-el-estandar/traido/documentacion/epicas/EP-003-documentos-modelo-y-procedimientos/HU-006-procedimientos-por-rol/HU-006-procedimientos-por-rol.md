# HU-006 — Escribir los procedimientos de cada rol del trabajo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Procedimientos guiados |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien depende de que la IA trabaje igual todos los días
- **Quiero** un procedimiento escrito para cada rol del trabajo
- **Para** que el resultado no dependa de cómo se le haya pedido esa vez

---

## 3. Contexto y descripción

Un modelo dice cómo se ve el documento terminado, pero no cómo se llega a él: qué se lee primero, qué se pregunta, qué se verifica antes de escribir.

Sin eso, cada sesión reinventa el camino. Y como el camino cambia, el resultado cambia, aunque el modelo sea el mismo.

Un procedimiento es un libreto corto: qué necesita para arrancar, qué pasos sigue, qué produce y cuándo se detiene a preguntar. Uno por rol: analizar, proponer alcance, escribir la especificación, diseñar, planear, implementar, revisar y cerrar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay un procedimiento por rol del trabajo |
| RN-02 | Cada procedimiento declara qué necesita para arrancar y qué produce |
| RN-03 | Un procedimiento no arranca sin la entrada que necesita: la pide y espera |
| RN-04 | El procedimiento produce el documento con su modelo, no un formato propio |
| RN-05 | Ningún procedimiento aprueba en nombre de la persona |
| RN-06 | Un procedimiento se puede leer solo, sin haber leído los otros |

### 3.2 Supuestos

- La IA sigue instrucciones escritas mejor que instrucciones dadas de palabra en cada sesión.

### 3.3 Fuera de alcance

- El procedimiento que dirige a los demás. Eso es HU-007.
- Los puntos de aprobación. Eso es HU-008.
- Que se disparen solos. Eso es EP-005.

---

## 4. Criterios de aceptación

### CA-01 — Cada rol tiene su procedimiento, con entrada y salida declaradas

```gherkin
Dado que el trabajo tiene roles definidos
Cuando se busca el procedimiento de uno
Entonces existe
Y declara qué necesita para arrancar y qué documento produce
```

**Cómo validarlo:**

1. Listar los roles del trabajo según la épica.
2. Buscar el procedimiento de cada uno. Resultado esperado: existe uno por rol.
3. Abrir dos. Resultado esperado: los dos dicen su entrada y su salida en las primeras líneas.
- **Aprobado cuando:** no queda ningún rol sin libreto.

### CA-02 — Sin la entrada, el procedimiento no arranca

```gherkin
Dado que un procedimiento necesita un documento previo
Cuando ese documento no existe
Entonces el procedimiento lo pide y se detiene
```

**Cómo validarlo:**

1. Pedirle a la IA que ejecute el procedimiento de planear, sin que exista la especificación.
2. Observar qué hace. Resultado esperado: dice qué falta y se detiene.
3. Crear lo que falta y volver a pedirlo. Resultado esperado: ahora sí arranca.
- **Aprobado cuando:** ningún procedimiento inventa su entrada.

### CA-03 — El mismo encargo da el mismo tipo de resultado

```gherkin
Dado que se ejecuta el mismo procedimiento en dos sesiones distintas
Cuando se comparan los dos documentos que produjo
Entonces tienen las mismas secciones y el mismo nivel de detalle
```

**Cómo validarlo:**

1. Ejecutar el procedimiento de escribir la especificación sobre el mismo módulo, en dos sesiones separadas.
2. Comparar los dos documentos. Resultado esperado: mismas secciones, mismo orden.
3. Comparar el detalle. Resultado esperado: comparable, sin que uno traiga la mitad.
- **Aprobado cuando:** el resultado deja de depender de la sesión.

### Criterios de aceptación transversales

- [ ] **Límites** — un procedimiento que recibe una entrada incompleta tiene comportamiento definido: la completa o la devuelve.
- [ ] **Autorización** — ninguno se salta un punto donde aprueba una persona.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Brevedad** | Un procedimiento se lee de una vez; si no cabe, es más de un rol |
| **Independencia** | Se entiende sin leer los demás |
| **Claridad** | Escrito para que lo siga alguien que no diseñó el método |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), criterio CAE-02.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Listar los roles del trabajo y qué produce cada uno.
- [ ] Escribir el procedimiento de cada rol, con su entrada y su salida.
- [ ] Enlazar cada procedimiento con el modelo del documento que produce.
- [ ] Probar cada uno con un caso real.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol/resultado_pruebas.md) — probada sobre once corridas del mismo encargo, que es el que la fase esperaba y ocurrió solo |

**La fase retro-documenta.** Los diez procedimientos de rol existen y se invocan. Falta la tabla que diga, con su cita, qué recibe y qué entrega cada uno — y la prueba de que el mismo encargo da el mismo tipo de resultado, que nunca se midió.

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
| Dependencia | HU-002 a HU-005, porque cada procedimiento produce uno de esos documentos | Alto |
| Riesgo | Que los procedimientos crezcan hasta que nadie los siga | Se exige que cada uno se lea de una vez |
| Riesgo | Que se contradigan entre ellos | Cada uno declara su entrada y su salida, y eso hace visible el choque |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Hay un procedimiento por rol
- [ ] Cada uno declara entrada y salida
- [ ] Cada uno produce su documento con el modelo que le toca
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita los modelos de HU-002 a HU-005 |
| **N**egociable | Sí | Cuántos roles hay se puede discutir |
| **V**aliosa | Sí | Es lo que hace que el trabajo no dependa del día |
| **E**stimable | Sí | El alcance lo fija la lista de roles |
| **S**mall (pequeña) | No | Son ocho procedimientos |
| **T**esteable | Sí | Se prueba ejecutando cada uno dos veces |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
