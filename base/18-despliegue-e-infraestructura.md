# 18 · Despliegue e infraestructura  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Reglas agnósticas para que lo que el agente entrega quede **listo para desplegarse de forma reproducible**. Aplican a proyectos que se despliegan (servicio, web, app); una librería o un script suelto las omiten. El agente **produce los artefactos** (pipeline, manifiestos, scripts, checklist); **no ejecuta** el despliegue en producción — eso lo autoriza y lo corre el humano ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)). La herramienta concreta (CI, orquestador, nube, IaC) la declara la capa 3 (`.agente/stack.md`). Extiende [`09·G6`](09-git.md#g6--integración-continua-el-verde-es-automático-no-manual).

---

## DP1 · El despliegue es un artefacto versionado, no una serie de clics

Todo lo que lleva el código a un entorno vive en el repo como **texto revisable**: pipeline de CI/CD, manifiestos de infraestructura, scripts. Nada de configurar a mano en una consola (click-ops) sin dejar rastro: lo que no está versionado no es reproducible ni auditable, y se pierde cuando cambia la persona.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP2 · Infraestructura como código

La infraestructura (contenedor, red, servicios, recursos de nube) se declara en archivos versionados y se aplica desde ahí, no se crea a mano. Un entorno nuevo se levanta corriendo la declaración, no siguiendo un instructivo. El **estado real** debe poder reconstruirse del código.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP3 · Build una vez, promover el mismo artefacto

Se compila/empaqueta **una sola vez** y ese mismo artefacto inmutable (imagen, paquete) pasa por los entornos (pruebas → staging → producción). No se recompila por entorno: lo que se probó es exactamente lo que se despliega. La versión del artefacto es rastreable al commit.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP4 · Config por entorno, fuera del artefacto

El artefacto es **agnóstico del entorno**; la configuración y los secretos se inyectan al desplegar, no se hornean adentro (`11`, [`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)). Así la misma imagen corre en cualquier entorno cambiando solo su config, y un secreto no viaja dentro del build.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

La fila **11** pasa aunque solape con [`11·CFG1`](11-configuracion-entornos.md#cfg1--la-configuración-vive-fuera-del-código): la enlaza y lo suyo es que la configuración quede **fuera del artefacto** que se despliega, que es otra cosa.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP5 · Release reversible, con plan de vuelta

Toda estrategia de release define **cómo se revierte** antes de aplicarse: volver a la versión anterior del artefacto, revertir la migración ([`03·D2`](03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)), restaurar datos. Preferir releases graduales (canario/azul-verde) cuando el riesgo lo amerite. Un release sin rollback pensado no está listo.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

**Es de las que más falta le hace:** «release reversible con plan de vuelta» se entiende de muchas maneras hasta que se ve una.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP6 · Checklist de despliegue

Cada despliegue no trivial lleva su checklist, del [plantillas/checklist-despliegue.md](../plantillas/checklist-despliegue.md): respaldo previo, migraciones reversibles, orden de pasos, verificación (smoke test) después, y el plan de reversión a mano. El checklist es parte del entregable, no memoria de quien despliega.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP7 · La app expone su salud

El servicio ofrece un punto de **readiness/health** (¿está vivo?, ¿listo para recibir tráfico?) para que el pipeline y el orquestador decidan sin adivinar si el release quedó bien. Migraciones y arranque no dejan el servicio a medias: o queda sano, o el release falla y se revierte.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 12 · sin ejemplo.** **Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP8 · Correr contra producción lo autoriza el humano

El agente **prepara** el despliegue; **ejecutarlo contra producción** (o contra datos reales) requiere autorización explícita del usuario ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)), nunca por iniciativa propia ni "para probar". **Fuera de alcance por diseño:** operar el sistema vivo, vigilar dashboards, responder incidentes en caliente — eso es del humano (la observabilidad la cubre `19`). La identidad del agente es *desarrollador senior*, no SRE.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**Dos filas.**

- **Fila 10 · no cabe:** 427 caracteres, la única del capítulo que se pasa.
- **Fila 12 · sin ejemplo.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

