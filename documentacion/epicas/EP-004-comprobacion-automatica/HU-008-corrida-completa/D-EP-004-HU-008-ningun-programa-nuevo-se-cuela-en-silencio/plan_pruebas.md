# Plan de Pruebas — Fase `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **ningún programa del estándar termina con código 0 sin decir nada**, que cada uno nombra a **su** corredor, y que la corrida completa vuelve a terminar con su resumen.

### 1.2 Alcance

**Entra:** la salida y el código de los dos programas que fallaban, el mensaje del guardián común, el orden de lo que la corrida imprime, y la batería entera por la no regresión.

**No entra:** la mudanza del enganche del hash, que es de `EP-005·HU-011`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cuatro decisiones, y por qué la regla se rompió dos veces por el mismo camino |
| [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md) | El `CA-03` y el `CA-04` |
| `pendientes/hecho/ningun-validador-termina-en-silencio.md` | El caso que originó la regla: una métrica falsa escrita desde un silencio |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los dos programas | Que digan quién los corre y salgan con 2 |
| El guardián común | Que el camino viejo siga igual para los otros cuarenta |
| La corrida completa | Que el resumen sea lo último que se lee |
| El contador del amarre | Que los dos programas no pasen a leerse como amarrados |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que no pase** | Un código 0 mudo es el defecto original: afirma sin haber comprobado |
| **De partición** | Programa con corredor propio · con corredor de enganche · punto de entrada de verdad |
| **De no regresión** | Cuarenta módulos ya llaman al guardián; ninguno puede cambiar de comportamiento |
| **De efecto lateral** | El mensaje nuevo nombra un enganche, y hay un contador que busca esa palabra |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Ampliar la prueba no puede volverla más floja**: sería el defecto que la fase arregla |
| Alta | CP-001, CP-003 | Que los dos digan quién los corre, y que el resumen quede de último |
| Media | CP-004, CP-005 | El efecto lateral en el contador y la no regresión |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`test_ninguno_termina_en_silencio.py` y `test_la_corrida_completa_en_una_linea.py` enteras, más la batería interna completa: la fase toca `comun.py`, del que cuelga todo.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- La línea base anotada: cuáles programas fallan y con qué mensaje.

### 4.2 Criterios de salida

- Las trece pruebas de los dos archivos, en verde.
- La batería interna sin fallas de estas causas.
- El recuento del amarre igual que antes.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la prueba ampliada deja pasar un programa que calla**. La ampliación es el punto delicado de la fase: se cambia la comprobación que reporta el defecto, y esa es exactamente la forma de hacer desaparecer un rojo sin arreglar nada.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-03 — cada programa dice quién lo corre | CP-001 | De partición |
| CA-03 — la prueba sigue cazando al que calla | CP-002 | Que **no** pase |
| CA-03 — el resumen es lo último | CP-003 | De sistema |
| CA-04 — el contador del amarre no cambia | CP-004 | De efecto lateral |
| CA-04 — batería entera | CP-005 | De no regresión |

---

## 6. Casos de prueba

### CP-001 — Cada programa dice quién lo corre, y sale con 2

| Programa | Se espera |
|---|---|
| `estacion_commit.py` | nombra el `post-commit` de git · código 2 |
| `rutas_fuera.py` | nombra el enganche del adaptador · código 2 |
| Cualquiera de los otros cuarenta | sigue diciendo `validar.py` · código 2 |

### CP-002 — La prueba sigue cazando al que calla

- **Precondición:** un módulo que no imprima nada y salga con 0.
- **Resultado esperado:** la prueba lo reporta.
- **Por qué es el caso crítico:** la fase **amplía** la comprobación que reportaba el defecto. Si al ampliarla dejara pasar el silencio, el rojo desaparecería sin que nada se hubiera arreglado.

### CP-003 — El resumen es lo último que se lee

- **Acción:** `validar.py todo` y mirar las tres últimas líneas.
- **Resultado esperado:** ahí está el veredicto de la corrida, no el conteo por regla.
- **Y el conteo sigue saliendo entero**, arriba: se movió, no se recortó.

### CP-004 — El contador del amarre no cambia

- **Acción:** `validar.py amarre` antes y después.
- **Resultado esperado:** el mismo número. **Este caso encontró un defecto de verdad:** nombrar el archivo del enganche en el mensaje subía el recuento de 27 a 29.

### CP-005 — No regresión

- **Acción:** `validar.py internas`.
- **Resultado esperado:** ninguna falla nueva, y las cuatro de estas causas en verde.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

El repositorio del estándar. El `CP-002` usa un módulo de mentiras que la propia prueba escribe.

### 7.2 Datos de prueba

Ninguno fuera de eso.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Que alguien lea el mensaje y encuentre lo que buscaba.** Se comprueba que la salida nombre al corredor; que el nombre le sirva a quien lo lee es criterio, y se decide leyéndolo.

---

## 8. Herramientas

`unittest` y `subprocess`. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un programa vuelve a salir con 0 sin decir nada |
| **Alta** | El mensaje manda a quien lee a un comando que no existe |
| **Media** | El resumen deja de ser lo último |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` y se arregla en la fase si cabe en su alcance.

### 9.3 Contenido mínimo de un reporte

Qué se corrió, qué salió, qué se esperaba.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Objetivo |
|---|---|---|
| Programas que salen con 0 sin decir nada | 2 | 0 |
| Fallas de la batería por estas causas | 4 | 0 |

### 12.2 Dónde se miden

`validar.py internas`, y las dos suites de la fase.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Ampliar la prueba hasta que el rojo desaparezca solo | El `CP-002` fija que el silencio se siga cazando |
| Dar por buena la corrida mirando el código de salida | El `CP-003` mira **el texto**, que es lo que lee una persona |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
