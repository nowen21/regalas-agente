# Resultado de Pruebas — Fase `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` |
| **HU** | [HU-002 Llenar un hueco desde la plataforma](../HU-002-llenar-un-hueco-desde-la-plataforma.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre un documento real de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 6 |
| Ejecutados | 6 |
| Pasaron | 6 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **24** |

**El documento real, llenado y medido:**

| | Cuánto |
|---|---|
| Documento | `EP-001/HU-014.../README.md` |
| Tamaño antes | 237 caracteres |
| Tamaño después | 350 |
| **Caracteres cambiados fuera del hueco** | **0** |
| Finales de línea cambiados | **0** |
| Espacios por llenar que le quedan | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Se llena un hueco y queda en el archivo

Lo escrito queda en el **archivo del proyecto**, y se lee abriéndolo por fuera de la plataforma. La copia de `datos/` queda con lo mismo, para que la cuenta no siga mostrando el hueco que ya se llenó.

**Resultado: pasa.**

### CP-002 — Lo que no es el hueco no cambia

**El caso que decide la fase, comprobado sobre un archivo real.**

| Comprobación | Resultado |
|---|---|
| El archivo entero, con el hueco descontado | **Idéntico** |
| Finales de línea | Los mismos, uno por uno |
| Lo que ve el control de versiones | **Una línea cambiada, ninguna más** |

**Y el defecto que este caso encontró antes de llegar acá:** leer un archivo con los finales de línea de Windows y volver a escribirlo cambia **todos** los renglones si Python los traduce. No se ve mirando el texto y arruina el criterio entero. Se lee y se escribe sin traducir.

**Resultado: pasa.**

### CP-003 — La cuenta de huecos baja

De N a N menos uno, ni más ni menos. Llenar el último deja el documento completo.

**Resultado: pasa.**

### CP-004 — Si el archivo cambió por fuera, se avisa

Leer, cambiar el archivo por fuera, e intentar guardar: **avisa y no escribe**. Lo que escribió el otro sigue ahí, entero.

**Resultado: pasa.**

### CP-005 — Queda registrado

La auditoría dice quién, cuándo, qué documento y **en qué línea estaba el hueco**. El registro va antes del efecto. Un intento que no escribió no deja constancia de un cambio que no hubo.

**Resultado: pasa.**

### CP-006 — No se escribe en el hueco equivocado

| Entrada | Salió |
|---|---|
| Una línea que ya no dice lo mismo | No se escribe, se avisa |
| Una posición donde ya no está la marca | No se escribe, se avisa |
| Una línea que ya no existe | No se escribe, se avisa |
| Dos marcas iguales en la misma línea | Se llena la que se pidió |
| Texto vacío | No hace nada |
| Un documento sin huecos | Lo dice |

**Resultado: pasa.**

---

## 3. Los dos defectos que solo aparecieron corriendo sobre lo real

El plan pedía llenar un documento real. Al hacerlo salieron dos defectos que ninguna prueba con documentos inventados encontraba. **Los dos se arreglaron acá, con el alcance ampliado por el usuario el 2026-09-01.**

### D-01 — La cuenta estaba inflada: 51 de 77 no eran huecos

La marca escrita **dentro de código en la misma línea** se contaba como hueco. Son documentos **hablando de** la convención, que es lo que un estándar escribe todo el tiempo.

| Documento | «Huecos» que reportaba | Qué eran |
|---|---|---|
| La especificación de la marca de espacio por llenar | 7 | Las 7 veces que la nombra |

| Cuenta | Documentos | Huecos |
|---|---|---|
| Antes del arreglo | 54 | 77 |
| **Después** | **25** | **26** |

La fase A ya excluía los bloques cercados por esta misma razón. **Faltaba el código en la misma línea**, y se veía en un solo documento real.

### D-02 — La orden se caía al mostrar un renglón con emoji

La consola de Windows no puede escribir los símbolos que los documentos del ciclo usan en sus tablas de estaciones, y el programa moría en vez de mostrar el hueco. Ahora lo que no se pueda escribir se reemplaza al mostrarlo: perder un signo no cuesta nada; no poder ver el hueco, sí.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El archivo real, antes y después | Solo cambió el hueco |
| Lo que muestra el control de versiones | Una línea, la del hueco |
| Los 26 huecos que quedan | Revisados: son de verdad espacios por llenar |
| La especificación de la marca | Ya sale **completa**, que es lo correcto |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-01--se-llena-un-hueco-y-queda-en-el-archivo) | CP-001, §1 | **Cumple** |
| [CA-02](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-02--lo-que-no-es-el-hueco-no-cambia) | CP-002, §1 | **Cumple** |
| [CA-03](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-03--la-cuenta-de-huecos-baja) | CP-003 | **Cumple** |
| [CA-04](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-04--si-el-archivo-cambió-por-fuera-se-avisa) | CP-004 | **Cumple** |
| [CA-05](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-05--queda-registrado) | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Un documento real llenado de punta a punta | Hecho: quedó en **cero** huecos |
| El archivo comparado entero | Hecho: **cero caracteres cambiados fuera del hueco** |
| Que un cambio ajeno no se pise | Comprobado |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Un hueco se llena desde la plataforma, lo escrito queda en el archivo del proyecto, y **no cambia ni un carácter fuera del hueco**. Es la primera pieza que escribe en el repositorio del usuario, y las dos guardas que lo hacen seguro están probadas: no se escribe donde el documento se movió, y no se pisa lo que escribió otro.

**Lo que esta fase corrigió de la anterior:** la cuenta pasó de 77 a 26. Los 51 que sobraban eran la marca escrita dentro de código, o sea documentos hablando de la convención. **Los dos defectos aparecieron corriendo sobre un documento real, no en las pruebas.**

**Y lo que sigue sin poder decirse:** si llenar así resulta cómodo. Un documento de un hueco no responde esa pregunta; la responde quien llene uno de veinte.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 24 pruebas de la escritura | `plataforma/nucleo/ciclo_de_vida/tests_escritura.py` |
| EV-02 | El documento real llenado y comparado | §1 y §4 |

**Las dos baterías:** 733 pruebas del estándar y 302 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
