# Plan de Pruebas — Fase `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-023](../HU-023-un-rojo-se-puede-cerrar-declarandolo.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que un rojo **se puede cerrar declarándolo**, y que **no se cierra de ninguna otra forma**.

### 1.2 Alcance

**Entra:** el campo en el molde, su lectura, las dos condiciones que lo hacen válido, y el aviso cuando el nombre no resuelve.

**No entra:** cerrar los ocho rojos con fase posterior, ni tocar veredictos viejos.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | El reparto de los 16 rojos, y por qué se declara en vez de deducir |
| `S-065` | Que hacer el trabajo y verificarlo no cerraba el rojo |
| `S-055` | Un número de avance necesita una prueba que lo contradiga |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El campo del molde | Que sea **opcional**, y que no rompa la completitud de plantillas |
| La lectura | Que solo valga declarado, y solo si quien declara cumple |
| El alcance | Que no se pueda reemplazar el veredicto de otra historia |
| El aviso | Que nombre lo que se escribió cuando no resuelve |
| Las 32 pruebas de `por_veredicto` | Que sigan pasando |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Unitario** sobre árboles de mentira, y **de sistema sobre el árbol real** para lo que de verdad decide: que sin declaraciones el número no se mueva.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Es el riesgo central: cerrar un rojo por accidente es peor que no poder cerrarlo |
| De partición | Con campo y sin campo, quien declara cumpliendo y no |
| De borde | Fase inventada, fase de otra historia, campo vacío |
| **De inercia** | Con el código puesto y cero declaraciones, la línea idéntica |
| De no regresión | Las 32 de `por_veredicto` |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | Deducir el reemplazo taparía **seis rojos vivos**, medidos |
| Crítica | CP-006 | Si con cero declaraciones el número cambia, algo se está deduciendo |
| Alta | CP-001, CP-002 | Que funcione, y que un rojo no tape otro rojo |
| Media | CP-004, CP-005 | El aviso, y que nada se borre |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida:** saber si alguna prueba exige la lista de campos del molde `11`.
- La línea base y el reparto de los 16 rojos, en el plan §2.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- **Las 32 pruebas de `por_veredicto`, pasando.**
- **Las historias que se mueven, nombradas una por una.**
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **Con el código puesto y cero declaraciones, la línea cambia en algo.** Significaría que el reemplazo se está deduciendo, y hay que entenderlo antes de seguir.
- **Se mueven más de dos historias** tras declarar. Solo dos verificaron de verdad; si se mueven tres, alguna se cerró sin verificar.

**El segundo es el que vale.** «Que bajen los rojos» sería cierto con cualquier implementación, incluida una que los tape todos. **Exactamente dos, con nombre**, no.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · el molde y sus pruebas | CP-000 | De impacto |
| CA-01 — declarar cierra el rojo | CP-001 | De partición |
| CA-02 — una fase en rojo no cierra otro rojo | CP-002 | Que **no** pase |
| CA-03 — no se deduce del orden | CP-003 | Que **no** pase |
| CA-04 — un nombre que no resuelve avisa | CP-004 | De borde |
| CA-05 — el veredicto reemplazado no se borra | CP-005 | De efecto |
| Transversal · inercia | CP-006 | **De sistema** |

---

## 6. Casos de prueba

### CP-000 — El molde admite un campo más

| Campo | Valor |
|---|---|
| **Tipo** | De impacto |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: antes de tocar código |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar las pruebas que miran el molde `11` | Se listan |
| 2 | Ver si alguna exige su lista completa de campos | **Ninguna debería** |
| 3 | Ver si el validador de completitud trataría el campo nuevo como marcador sin llenar | **No**, por ser opcional |

---

### CP-001 — Declarar cierra el rojo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-01 |
| **Tipo** | De partición |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dos fases: la primera «No cumple», la segunda «Cumple», **sin el campo** | La historia **no cumple** |
| 2 | Agregar a la segunda el campo nombrando a la primera | La historia **cumple** |
| 3 | Quitar el campo otra vez | Vuelve a **no cumplir** |

**El paso 3 importa:** comprueba que el cambio lo produce el campo y no otra cosa que se movió de paso.

---

### CP-002 — Una fase en rojo no cierra el rojo de otra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-02 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dos fases, **las dos «No cumple»**, la segunda declarando reemplazar a la primera | La historia **no cumple** |
| 2 | Una fase sin veredicto legible que declara reemplazar a una roja | La historia **no cumple** |

**Por qué:** si un rojo pudiera cerrar otro rojo, bastaría escribir el campo en la fase que sigue para vaciar la cuenta entera.

---

### CP-003 — El reemplazo no se deduce del orden

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-03 |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dos fases: roja y luego verde, **sin el campo** | **No cumple** |
| 2 | Tres fases: roja, verde, verde, sin el campo | **No cumple** |
| 3 | **Sobre el árbol real:** las seis historias con fase posterior que no declaran nada | **Siguen contadas como que no cumplen** |

**Es el caso que decide si la fase sirve.** Está medido: de las ocho historias con fase posterior, **seis no resolvieron el rojo** — trabajaron otro criterio. Deducirlo del orden las daría por cumplidas, y eso es peor que no poder cerrar ningún rojo.

---

### CP-004 — Un nombre que no resuelve avisa, y no reemplaza

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-04 |
| **Tipo** | De borde |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Declarar el reemplazo de una fase **inventada** | Avisa **con el nombre escrito**, y no reemplaza |
| 2 | Declarar el reemplazo de una fase de **otra historia** | Avisa, y no reemplaza |
| 3 | El campo presente y **vacío** | No avisa, no reemplaza, no revienta |
| 4 | Declarar el reemplazo de **sí misma** | Avisa, y no reemplaza |

**El paso 4 es el que no se ve venir:** una fase que se nombra a sí misma se daría por cerrada sola.

---

### CP-005 — El veredicto reemplazado no se borra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-05 |
| **Tipo** | De efecto |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el resultado de la fase reemplazada | — |
| 2 | Correr la comprobación | — |
| 3 | Comparar | **Idéntico** |
| 4 | Comprobar que `veredicto_de` de aquella fase **sigue diciendo «No cumple»** | Sí |

**El paso 4 separa «la cuenta lo ignora» de «el dato desapareció».** El rastro de que estuvo en rojo es la información.

---

### CP-006 — Con cero declaraciones, el número no se mueve

| Campo | Valor |
|---|---|
| **HU / CA** | Transversal |
| **Tipo** | **De sistema** |
| **Prioridad** | **Crítica** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con el código puesto y **ninguna declaración escrita**, correr la línea | **Idéntica a la línea base** |
| 2 | Comparar los cinco números uno por uno | Los cinco iguales |
| 3 | Declarar en los dos cierres que sí verificaron | **Se mueven exactamente dos** |
| 4 | Nombrar cuáles | `EP-003·HU-002` y `EP-005·HU-001` |

**El paso 1 es el que protege todo lo demás.** Si con cero declaraciones la línea cambia, **el reemplazo se está deduciendo de algo** — y ahí se para, sin importar qué tan bien se vea el resto.

---

## 7. Datos y ambientes de prueba

Árboles de mentira en carpeta temporal, y el árbol real para `CP-003` paso 3 y `CP-006`. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita para probar (`08·T4`).

**Qué no reproduce el entorno:** un árbol de mentira tiene dos o tres fases. **Por eso los dos casos críticos corren contra el árbol real**, que es el único con dieciséis rojos de verdad.

---

## 8. Herramientas

`unittest`, y un guion de sabotaje que **se restaura con copia**, **restaura en `try/finally`**, limpia sus rastros, y **no se corre por una tubería** (`S-060`).

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Un rojo se cierra sin declararlo, o con una fase que no cumple |
| Alta | Con cero declaraciones el número cambia |
| Media | El aviso no dice qué nombre se escribió |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` antes de tocar código y el `CP-006` antes de declarar nada. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| **Historias que se mueven con cero declaraciones** | **0** |
| **Historias que se mueven al declarar** | **exactamente 2, con nombre** |
| Pruebas de `por_veredicto` que hubo que tocar | 0 |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se pruebe solo que funciona | Cuatro de los siete casos comprueban que **no** cierre |
| Que se mida «bajaron los rojos» y se dé por bueno | La meta es **exactamente dos, con nombre** |
| Que el árbol de mentira no reproduzca el real | `CP-003` paso 3 y `CP-006` corren contra el real |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
