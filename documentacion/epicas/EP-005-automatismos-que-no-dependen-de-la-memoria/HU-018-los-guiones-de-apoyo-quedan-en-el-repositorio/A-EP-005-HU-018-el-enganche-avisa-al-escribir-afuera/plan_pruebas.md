# Plan de Pruebas — Fase `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-018](../HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que escribir fuera del proyecto **avisa en el momento**, que escribir dentro **no avisa**, y que **el enganche está colgado de verdad**.

### 1.2 Alcance

**Entra:** `rutas_fuera.py`, el enganche, lo que el instalador cuelga, y la regla en `base/`.

**No entra:** los 38 guiones que ya se trajeron, mover o borrar archivos, y lo que se escribe por `Bash`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | El contrato del enganche, leído y no supuesto |
| `S-057` | Los cuatro días de incumplimiento, medidos |
| [pendiente 89](../../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md) | Las tres salidas, y cuál quedó fuera |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| «¿está dentro?» | Que acierte en los bordes, no en los casos fáciles |
| El enganche | Que avise con el destino, y que **no reviente nunca** |
| Lo que cuelga el instalador | Que el enganche **exista en la configuración** |
| La regla en `base/` | Que pase su propio checklist y no duplique `S9` |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Unitario** sobre rutas, con carpetas temporales de verdad para que resolver signifique algo. **De sistema** escribiendo un archivo real fuera y mirando si avisa.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Es el riesgo central: un enganche que avisa de más se apaga el mismo día |
| De borde | La carpeta hermana con prefijo compartido, el `..` que vuelve a entrar |
| De entrada mala | Un enganche que revienta detiene el trabajo |
| **De conexión** | Que esté colgado, no solo escrito |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | Avisar de más vuelve inútil el enganche, y con él lo que sí avisa |
| Crítica | CP-005 | Un enganche construido y **no colgado** no sirve de nada. Ya pasó, en `EP-002·HU-004` |
| Alta | CP-001, CP-003 | Que avise donde debe, y el borde que se cuela |
| Media | CP-004, CP-006 | La regla, y que no reviente |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida:** saber si alguna prueba compara la configuración completa del instalador.
- La línea base anotada en el plan §2.0.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- **El enganche probado escribiendo un archivo de verdad fuera del proyecto**, no solo con entradas de mentira.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **Alguna ruta de dentro del proyecto produce aviso.** Cero es cero.
- **La `T-00` encuentra que una prueba compara la configuración completa.** Ahí se para: agregar el enganche la rompería por algo que no es defecto, y hay que decidir antes si se cambia la prueba o el diseño.

**El primero no admite matices.** «Casi no avisa de más» es un enganche que se apaga.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · las pruebas del instalador | CP-000 | De impacto |
| CA-01 — escribir fuera avisa | CP-001 | De partición |
| CA-02 — escribir dentro **no** avisa | CP-002 | Que **no** pase |
| CA-03 — la ruta se resuelve antes de comparar | CP-003 | De borde |
| CA-04 — la regla dice dónde van | CP-004 | De documentación |
| CA-01 · conexión | CP-005 | **De sistema** |
| CA-05 — no revienta | CP-006 | De entrada mala |

---

## 6. Casos de prueba

### CP-000 — Las pruebas del instalador no comparan la configuración completa

| Campo | Valor |
|---|---|
| **Tipo** | De impacto |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: se mide antes de tocar código |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en `pruebas.py` las que miran la configuración que genera el instalador | Se listan |
| 2 | Ver si alguna compara la lista completa de enganches, o cuenta cuántos hay | **Ninguna debería** |
| 3 | Si alguna lo hace, **parar y decidir** antes de agregar nada | — |

---

### CP-001 — Escribir fuera avisa, y dice dónde iba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-01 |
| **Tipo** | De partición |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una ruta de la carpeta temporal del sistema | **Avisa**, y nombra la ruta escrita |
| 2 | Leer el mensaje | Nombra `historico-chat/scripts/AAAA-MM-DD/` |
| 3 | Una ruta de la carpeta personal del usuario | Avisa |
| 4 | Comprobar el archivo después | **No se movió ni se borró** |

**El paso 2 es lo que separa un aviso útil de uno que se ignora.** Decir «está mal» sin decir dónde va obliga a ir a buscarlo, y a la tercera vez nadie va.

---

### CP-002 — Escribir dentro **no** avisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-02 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una ruta de `documentacion/` | **Silencio** |
| 2 | Una de `validadores/` | Silencio |
| 3 | Una de `historico-chat/scripts/2026-08-27/` | Silencio |
| 4 | Una ruta **relativa** dentro del proyecto | Silencio |
| 5 | Una con `..` que sale y **vuelve a entrar** | Silencio |
| 6 | La raíz del proyecto misma | Silencio |

**Por qué es crítico:** el agente escribe decenas de archivos del proyecto por sesión. Un solo falso positivo por sesión convierte el aviso en ruido, y el ruido se apaga.

---

### CP-003 — El borde que se cuela: la carpeta hermana

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-03 |
| **Tipo** | De borde |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una ruta en una carpeta hermana **cuyo nombre empieza igual** — `…/agente-viejo/x.py` frente al proyecto `…/agente` | **Avisa** |
| 2 | Una que empieza dentro y termina fuera con `..` | Avisa |
| 3 | La misma ruta escrita con separadores distintos | Se decide igual |

**El paso 1 es el que un `startswith` no ve.** `…/agente` es prefijo de `…/agente-viejo`, así que comparar cadenas daría la carpeta hermana por dentro — y ahí el enganche calla justo donde debía hablar.

---

### CP-004 — La regla dice dónde van los guiones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-04 |
| **Tipo** | De documentación |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `historico-chat/scripts/` en `base/` | Aparece, con su regla |
| 2 | Comprobar que declara su dependencia con `04·S9` y no lo repite | `M7`, `M12` |
| 3 | Correr `validar.py metareglas` | Sin incumplimientos |
| 4 | Correr `validar.py estandar` | Sin incumplimientos |

---

### CP-005 — El enganche está colgado, no solo escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-01 · conexión |
| **Tipo** | **De sistema** |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador sobre un proyecto de prueba | La configuración nombra el enganche nuevo |
| 2 | **Escribir un archivo de verdad fuera del proyecto** | Aparece el aviso |
| 3 | Borrar ese archivo y dejar el sitio como estaba | Sin rastros |

**Por qué es crítico, y no es teoría:** la fase `B` de `EP-002·HU-004` existió por exactamente esto — **el aviso estaba construido, probado y en verde, y el arranque no lo llamaba**. Se veía funcionar solo donde el agente lo invocaba a mano.

**Una prueba que llame al enganche directamente pasa en verde con el defecto puesto.** Por eso el paso 2 escribe de verdad.

---

### CP-006 — Ninguna entrada mala detiene el trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-05 |
| **Tipo** | De entrada mala |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Entrada sin `file_path` | Silencio, y salida normal |
| 2 | Entrada que no es JSON | Silencio |
| 3 | Ruta vacía | Silencio |
| 4 | Una ruta imposible de resolver | Silencio, y **no revienta** |

---

## 7. Datos y ambientes de prueba

Entradas JSON de mentira y carpetas temporales **de verdad**, creadas y borradas por la prueba — resolver una ruta que no existe no comprueba lo mismo.

**Ninguna prueba usa credenciales** (`00·N6`). Y **el `CP-005` paso 2 escribe un archivo fuera del proyecto a propósito**: es el único caso en que hace falta, se declara acá, y se borra en el paso 3.

---

## 8. Herramientas

`unittest`, y un guion de sabotaje que **se restaura con copia**, limpia sus rastros tras cada sabotaje, **restaura en `try/finally`** y **no se corre por una tubería** (`S-060`).

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Avisa al escribir dentro del proyecto, o no está colgado |
| Alta | La carpeta hermana pasa por dentro |
| Media | El aviso no dice dónde iba |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` antes de tocar código y el `CP-005` al final. La suite completa después.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| **Rutas de dentro que producen aviso** | **0 de 6** |
| **El enganche, colgado y probado escribiendo de verdad** | Sí |
| Entradas malas que detienen el trabajo | 0 de 4 |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se pruebe el enganche llamándolo a mano y quede sin colgar | `CP-005` paso 2 escribe un archivo de verdad |
| Que se prueben rutas fáciles y no los bordes | `CP-003`, con la carpeta hermana que comparte prefijo |
| Que las pruebas creen rutas que no existen | Las carpetas temporales se crean de verdad |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final, como en la `HU-022` |

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
