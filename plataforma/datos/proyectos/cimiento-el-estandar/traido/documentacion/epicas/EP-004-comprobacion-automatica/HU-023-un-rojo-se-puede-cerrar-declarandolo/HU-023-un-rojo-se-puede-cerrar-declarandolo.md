# HU-023 — Que un veredicto en rojo se pueda cerrar, declarándolo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-023 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien arregla lo que una fase dejó en rojo
- **Quiero** poder declarar que ese rojo quedó cerrado, y que la cuenta lo lea
- **Para** que el número de trabajo pendiente pueda bajar cuando el trabajo se hace, y no solo subir

---

## 3. Contexto y descripción

**Un rojo no tiene forma de cerrarse.**

Se comprobó haciéndolo: se construyeron dos fases que volvían a verificar criterios declarados en rojo, se midió que hoy se cumplen —el enmascarado corriendo por sus dos mitades, la cadena de trazabilidad en cero sobre 11 épicas y 119 historias— y las dos cerraron con «Cumple».

**El número no se movió.** `16 no cumplen` siguió siendo 16.

El conteo mira **todas** las fases de la historia, y las fases `A` siguen diciendo «No cumple».

### La regla que lo causa es correcta, y le falta una mitad

*«Basta una fase que no cumpla para que la historia no cumpla»* impide que cerrar la primera fase cierre la historia. **Eso está bien.**

Lo que le falta es distinguir dos cosas que hoy se ven igual:

| Lo que pasa de verdad | Lo que la cuenta ve |
|---|---|
| **Todavía no se hizo** | «No cumple» |
| **Se hizo después, y una fase posterior lo verificó** | «No cumple» |

**Así que el número de esta cuenta solo sabe empeorar**: entra cuando una fase cierra en rojo y **no sale nunca**.

### Lo medido antes de diseñar, que cambia el diseño

> Sobre las 119 historias, el 2026-08-27, antes de crear la carpeta de esta historia.

| Qué | Cuántas |
|---|---|
| Historias terminadas **con alguna fase en rojo** | **16** |
| De ellas, con una fase **posterior** a la última roja | **8** |
| Sin ninguna fase posterior — el rojo sigue vivo de verdad | **8** |

**Y tener fase posterior no es haber resuelto el rojo.** De las ocho, **solo dos volvieron a verificar el criterio que estaba en rojo**; las otras seis trabajaron otro criterio de la misma historia.

**Por eso el reemplazo se declara y no se deduce.** Deducirlo del orden taparía seis rojos vivos con trabajo ajeno — la forma optimista de mentir, que es justo lo que esta cuenta vino a impedir.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | Una fase puede declarar **qué veredicto anterior deja atrás**, nombrándolo | La decisión del usuario, 2026-08-27 |
| RN-02 | Solo cuenta el reemplazo si **quien lo declara cumple**. Una fase en rojo no cierra el rojo de otra | Si no, un rojo se taparía con otro |
| RN-03 | El reemplazo se **declara**, nunca se deduce del orden de las fases | `S-065`: seis de ocho candidatas no resolvieron nada |
| RN-04 | Solo se puede reemplazar el veredicto de **una fase de la misma historia** | Un rojo ajeno no es de nadie |
| RN-05 | El veredicto reemplazado **no se borra ni se reescribe** | `20·M11`. El rastro de que estuvo en rojo es la información |
| RN-06 | Si se nombra una fase que no existe, **se avisa y no se reemplaza nada** | `04·R4`: sin poder leerlo, no se afirma |
| RN-07 | El programa **avisa, no corrige** | `EP-004 §10.2` |

### 3.2 Supuestos

- El campo vive en el documento de cierre de la fase, junto al veredicto, que es donde ya se copia el resultado. **Es el documento que el conteo ya abre.**

### 3.3 Fuera de alcance

- **Cerrar los ocho rojos que tienen fase posterior.** Esta historia da la forma; declarar cada uno es trabajo de quien verifique que se resolvió.
- **Los ocho que no tienen fase posterior.** Ahí no hay nada que declarar: el rojo está vivo.
- **Reescribir veredictos viejos.** Nunca.

---

## 4. Criterios de aceptación

### CA-01 — Una fase puede declarar qué veredicto deja atrás

```gherkin
Dado que una fase verificó de nuevo un criterio que otra dejó en rojo
Cuando declara en su cierre qué fase reemplaza
Entonces la cuenta deja de mirar el veredicto de aquella
Y mira el de esta
```

**Cómo validarlo:**
1. Armar un árbol con una historia de dos fases: la primera «No cumple», la segunda «Cumple».
2. Contar. Resultado esperado: la historia **no cumple**.
3. Agregar a la segunda el campo que nombra a la primera.
4. Contar otra vez. Resultado esperado: la historia **cumple**.
- **Aprobado cuando:** el mismo árbol cambia de cuenta según el campo esté o no.

### CA-02 — Una fase en rojo no cierra el rojo de otra

```gherkin
Dado que una fase declara reemplazar el veredicto de otra
Y ella misma no cumple
Cuando se cuenta
Entonces el reemplazo no vale
```

**Cómo validarlo:**
1. Dos fases, las dos «No cumple», y la segunda declarando que reemplaza a la primera.
2. Contar. Resultado esperado: la historia **no cumple**.
- **Aprobado cuando:** un rojo no se puede tapar con otro rojo.

### CA-03 — El reemplazo no se deduce del orden

```gherkin
Dado que una fase posterior cumple
Y no declara reemplazar nada
Cuando se cuenta
Entonces el rojo anterior sigue contando
```

**Cómo validarlo:**
1. Dos fases: la primera «No cumple», la segunda «Cumple», **sin el campo**.
2. Contar. Resultado esperado: la historia **no cumple**.
3. Comprobar sobre el árbol real que las seis historias con fase posterior **que no declaran nada** siguen contadas como que no cumplen.
- **Aprobado cuando:** sin declaración no hay reemplazo, ni en el árbol de prueba ni en el real.

**Este es el criterio que decide si sirve.** De las ocho historias con fase posterior, **seis no resolvieron el rojo**: trabajaron otro criterio. Deducir el reemplazo del orden las daría por cumplidas.

### CA-04 — Nombrar una fase que no existe se avisa, y no reemplaza nada

```gherkin
Dado que una fase declara reemplazar el veredicto de una fase que no está
Cuando se cuenta
Entonces se avisa con el nombre escrito
Y no se reemplaza nada
```

**Cómo validarlo:**
1. Declarar el reemplazo de una fase inventada.
2. Contar. Resultado esperado: la historia sigue como estaba, y hay un aviso que **nombra lo que se escribió**.
3. Declarar el reemplazo de una fase de **otra** historia. Resultado esperado: se avisa y no se reemplaza.
- **Aprobado cuando:** un nombre que no se puede resolver no cambia ninguna cuenta.

### CA-05 — El veredicto reemplazado no se borra

```gherkin
Dado un veredicto reemplazado
Cuando se abre el documento de aquella fase
Entonces sigue diciendo lo que decía
```

**Cómo validarlo:**
1. Anotar el contenido del resultado de la fase reemplazada.
2. Correr la comprobación.
3. Comparar. Resultado esperado: idéntico.
- **Aprobado cuando:** el rastro de que estuvo en rojo se conserva entero.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | El campo se entiende sin documentación: dice a qué fase reemplaza, por su nombre |
| RNF-02 | **Rendimiento** | Leerlo no agrega un recorrido nuevo del árbol |

---

## 6. Diseño y referencias

- **Dónde se cuenta:** `por_veredicto` en `validadores/fases.py`.
- **Dónde va el campo:** el documento de cierre, junto al veredicto — el que la cuenta ya abre.
- **El molde:** [`11-funcionalidad-implementada.md`](../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md).

---

## 7. Tareas técnicas derivadas

- [ ] «Documentación» El campo en el molde del cierre, opcional y explicado.
- [ ] «Backend» Leerlo, y que solo valga si quien declara cumple.
- [ ] «Backend» Avisar cuando nombra una fase que no existe o es de otra historia.
- [ ] «Pruebas» Los cinco criterios, y el caso de que **no** se deduzca del orden.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras`](A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras/) | CA-01 a CA-05 | (vacío) | [plan_trabajo](A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras/plan_trabajo.md) | [plan_pruebas](A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras/plan_pruebas.md) | | En curso |

**La línea base, medida antes de abrir la carpeta:** `119 en total · 32 sin terminar · 87 terminadas, de las cuales 66 cumplen, 16 no cumplen y 5 no dicen si cumplen`.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que el reemplazo se deduzca del orden y tape seis rojos vivos | `CA-03`, y es el criterio que decide |
| Riesgo | Que un rojo se tape con otro rojo | `CA-02` |
| Riesgo | Que se lea como permiso para cerrar rojos sin verificarlos | El campo obliga a nombrar la fase; quien lo escribe firma que verificó, y su propio cierre lo dice |
| Riesgo | Que el número baje de golpe y se lea como maquillaje | **No va a bajar solo:** de las ocho candidatas, solo dos verificaron de verdad. El `CHANGELOG` lo dirá con los dos números |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible — no aplica: no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [x] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y revisado
- [ ] Pruebas unitarias escritas y en verde
- [ ] Criterios de aceptación validados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de nada abierto |
| **N**egociable | ☑ | El nombre del campo se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Hoy el trabajo de arreglar un rojo no mueve ningún número, así que nadie lo hace |
| **E**stimable | ☑ | Un campo, una condición y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios, con árboles de prueba y contra el árbol real |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-27 | Agente, con el usuario | Creación de la HU. Sale de `S-065`: dos fases verificaron rojos, cerraron con «Cumple», y el número no se movió. El usuario eligió **declarar** el reemplazo en vez de deducirlo del orden |
