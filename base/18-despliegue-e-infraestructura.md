# 18 · Despliegue e infraestructura  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-031](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-031-el-capitulo-18-despliegue-e-infraestructura/HU-031-el-capitulo-18-despliegue-e-infraestructura.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

**Opt-in.** Reglas agnósticas para que lo que el agente entrega quede **listo para desplegarse de forma reproducible**. Aplican a proyectos que se despliegan (servicio, web, app); una librería o un script suelto las omiten. El agente **produce los artefactos** (pipeline, manifiestos, scripts, checklist); **no ejecuta** el despliegue en producción — eso lo autoriza y lo corre el humano ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)). La herramienta concreta (CI, orquestador, nube, IaC) la declara la capa 3 (`.agente/stack.md`). Extiende [`09·G6`](09-git.md#g6--las-pruebas-y-el-linter-corren-solos-en-cada-cambio-propuesto).

---

## DP1 · El despliegue es un artefacto versionado, no una serie de clics

Todo lo que lleva el código a un entorno vive en el repo como **texto revisable**: pipeline de CI/CD, manifiestos de infraestructura, scripts. Nada de configurar a mano en una consola (click-ops) sin dejar rastro: lo que no está versionado no es reproducible ni auditable, y se pierde cuando cambia la persona.

```
INCORRECTO: la cola de mensajes se crea a mano en la consola de la nube y «queda
            anotado» en un chat; nadie puede volver a crearla igual
CORRECTO:   el recurso se declara en el manifiesto versionado y se aplica desde ahí
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP2 · Infraestructura como código

La infraestructura (contenedor, red, servicios, recursos de nube) se declara en archivos versionados y se aplica desde ahí, no se crea a mano. Un entorno nuevo se levanta corriendo la declaración, no siguiendo un instructivo. El **estado real** debe poder reconstruirse del código.

```
INCORRECTO: el servidor nuevo se configura siguiendo un instructivo de doce pasos
CORRECTO:   se corre la declaración versionada y el entorno queda igual al anterior
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP3 · Build una vez, promover el mismo artefacto

Se compila/empaqueta **una sola vez** y ese mismo artefacto inmutable (imagen, paquete) pasa por los entornos (pruebas → staging → producción). No se recompila por entorno: lo que se probó es exactamente lo que se despliega. La versión del artefacto es rastreable al commit.

```
INCORRECTO: se vuelve a compilar «para producción» con otra bandera: lo que llega
            no es lo que se probó
CORRECTO:   la misma imagen que pasó las pruebas se promueve, etiquetada con su commit
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP4 · Config por entorno, fuera del artefacto

El artefacto es **agnóstico del entorno**; la configuración y los secretos se inyectan al desplegar, no se hornean adentro (`11`, [`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)). Así la misma imagen corre en cualquier entorno cambiando solo su config, y un secreto no viaja dentro del build.

```
INCORRECTO: la clave de producción va dentro de la imagen «para que no se olvide»
CORRECTO:   la imagen lee la clave del entorno al arrancar; la misma imagen corre en
            pruebas y en producción cambiando solo su configuración
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

La fila **11** pasa aunque solape con [`11·CFG1`](11-configuracion-entornos.md#cfg1--la-configuración-vive-fuera-del-código): la enlaza y lo suyo es que la configuración quede **fuera del artefacto** que se despliega, que es otra cosa.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP5 · Release reversible, con plan de vuelta

Toda estrategia de release define **cómo se revierte** antes de aplicarse: volver a la versión anterior del artefacto, revertir la migración ([`03·D2`](03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)), restaurar datos. Preferir releases graduales (canario/azul-verde) cuando el riesgo lo amerite. Un release sin rollback pensado no está listo.

```
INCORRECTO: se despliega y «si algo falla, vemos»
CORRECTO:   antes de aplicar está escrito cómo se vuelve a la versión anterior,
            con la migración inversa y el respaldo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

**Es de las que más falta le hace:** «release reversible con plan de vuelta» se entiende de muchas maneras hasta que se ve una.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP6 · Checklist de despliegue

Cada despliegue no trivial lleva su checklist, del [plantillas/checklist-despliegue.md](../plantillas/checklist-despliegue.md): respaldo previo, migraciones reversibles, orden de pasos, verificación (smoke test) después, y el plan de reversión a mano. El checklist es parte del entregable, no memoria de quien despliega.

```
INCORRECTO: quien despliega lo hace de memoria y esta vez olvida el respaldo previo
CORRECTO:   el checklist marcado paso a paso viaja con la entrega
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP7 · La app expone su salud

El servicio ofrece un punto de **readiness/health** (¿está vivo?, ¿listo para recibir tráfico?) para que el pipeline y el orquestador decidan sin adivinar si el release quedó bien. Migraciones y arranque no dejan el servicio a medias: o queda sano, o el release falla y se revierte.

```
INCORRECTO: el orquestador enruta tráfico a una instancia que todavía está migrando
CORRECTO:   el punto de readiness responde «no listo» hasta que la migración termina
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DP8 · Correr contra producción lo autoriza el humano

El agente **prepara** el despliegue; **ejecutarlo contra producción** o contra datos reales exige autorización explícita del usuario ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)), nunca por iniciativa propia ni «para probar». Operar el sistema vivo es del humano ([`19·OB6`](19-observabilidad-y-operacion.md#ob6--operar-en-vivo-lo-hace-el-humano)).

```
INCORRECTO: «probé el despliegue contra producción para confirmar que el pipeline sirve»
CORRECTO:   se prepara todo y se espera la autorización para ejecutar contra producción
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad. Y el cuerpo se recortó al molde: el porqué que sobraba quedó en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Dos filas.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

