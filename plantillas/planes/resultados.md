# Resultado de Pruebas — Fase «A-EP01-HU03-Descripción»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

> Plantilla del `resultado_pruebas` de una **fase**. Se guarda en la carpeta de la fase (ruta `02·F12.13`), como `resultado_pruebas.md`. **Se crea junto con los dos planes**, aunque todavía no se haya ejecutado nada: el formato puesto desde el principio se ve, se revisa y no se olvida. Lo que no se ha corrido se escribe **"no ejecutado"**, nunca en blanco ni como aprobado, y el veredicto arranca en *"todavía no se ejecutó"*. Reemplaza los `«…»`, borra las secciones que no apliquen y borra esta caja. **La línea de arriba, la de para qué sirve, se queda.**
>
> **Por qué es un documento aparte y no una sección del plan.** El plan se aprueba **antes** de ejecutar. Si los resultados se escriben encima, se pierde la línea base aprobada y ya no se puede comparar lo que se acordó probar contra lo que se probó. Es también la separación que hace la norma en que se apoya el plan de pruebas (ISO/IEC/IEEE 29119-3), entre el plan y el registro de ejecución.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **HU** | «HU-NNN» |
| **Plan de pruebas de origen** | «`plan_pruebas.md`» |
| **Ciclo** | «1» (se agrega un bloque por cada reprueba, no se pisa el anterior) |
| **Fecha de ejecución** | AAAA-MM-DD |
| **Ejecutado por** | «quién» |
| **Ambiente y versión** | «dónde corrió y sobre qué build» |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | |

**Casos no ejecutados y por qué:** «cuáles y el motivo. Un caso sin ejecutar no se cuenta como aprobado».

---

## 2. Ejecución caso por caso

> **Cada `CP-00N` se escribe como enlace al caso del `plan_pruebas` de la fase, y cada `CA-0N` o `RNF-0N` como enlace a su exigencia en la HU**, acá y en las tablas que siguen. Un identificador suelto obliga a buscarlo a mano, y así es como se termina juzgando un caso sin haber leído lo que exigía.

> **Este documento se arma desde el `plan_pruebas`, no desde lo que se hizo.** Se copia la lista de casos del plan, con su CA y su prioridad, y se le agrega qué pasó. Un caso que esté acá y no en el plan, o al revés, es un defecto de trazabilidad y se arregla antes de dar veredicto.
>
> Ningún caso se marca aprobado sin evidencia.

| Caso | CA | Prioridad (del plan) | Fecha | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | AAAA-MM-DD | Aprobado / Fallido / Bloqueado / No ejecutado | EV-01 | — |

**Correspondencia con el plan:** «N casos en el plan, N acá. Ninguno de más, ninguno de menos». Si no cuadra, decir cuáles bailan y por qué.

**Qué salió distinto de lo esperado:** «para los fallidos, qué se esperaba y qué pasó. Sin esto, "fallido" no sirve para corregir».

---

## 3. Verificaciones manuales  ·  `08·T4`

> Lo que el entorno automático **no** reproduce y hubo que comprobar a mano. Se listan aunque hayan salido bien: lo que no está acá se lee como no probado.

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | | | |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | | CP-001 | Crítica / Alta / Media / Baja | Abierto / Corregido / Verificado / Aceptado | |

**Defectos abiertos que se aceptan y por qué:** «los que se dejan pasar, con quién lo autorizó. Un defecto abierto sin decisión escrita bloquea el cierre».

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

> Esta es la tabla que decide. Un `CA-0N` o un `RNF-0N` sin caso ejecutado **no** se marca cumplido, aunque "se haya visto funcionar". Los requisitos no funcionales llevan su fila igual que los criterios: si van sueltos en un renglón de prosa, nadie los verifica.

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | | Sí / No |

**Los que no cumplen:** «qué falta exactamente y a qué tarea o fase se traslada».

---

## 5.1 Lo que el plan exigía

> Una fila por cada cosa que el `plan_pruebas` fijó como meta. **Se copia del plan, no se inventa acá**: si el plan pedía cubrir el 100% de los casos críticos, esta tabla dice cuánto se cubrió de verdad.

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | | Sí / No |
| Casos críticos y altos ejecutados | Plan §3.4 | 100% | | Sí / No |
| «Métrica propia del plan» | Plan §12.1 | «meta» | | Sí / No |
| Criterios de salida | Plan §4.2 | Todos | | Sí / No |

**Lo que no se cumplió:** «qué meta del plan quedó corta y qué se decidió al respecto. Una meta incumplida sin decisión escrita bloquea el cierre».

---

## 6. Veredicto de la fase

**Concepto:** «Cumple / No cumple». No hay estado intermedio: si algo de lo pedido falta, es **No cumple**. Los defectos van en §4 con su severidad, y ahí se ve qué se aceptó y quién lo aceptó.

**Justificación:** «en dos o tres líneas, apoyada en §5».

**Qué falta para que cumpla** (si no cumple): «lista concreta».

> Este concepto es el que se copia al `estado-fase.md` para pasar la puerta de verificación. La fase **no cierra** con un CA en "No".

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de la corrida / captura / archivo resultante | `«ruta o enlace»` |

---

## 8. Ciclos anteriores

> Cuando hay reprueba, el ciclo nuevo se agrega **encima** y el anterior queda tal cual. Saber que algo falló y después pasó vale más que ver solo el resultado final.

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | | | | Primera corrida |
