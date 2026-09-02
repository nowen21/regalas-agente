# Bitácora de operación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué pasó mientras el sistema estaba en operación**: incidentes, caídas, cambios en caliente y lo que se aprendió de cada uno.

> **Este documento existe casi sin materia, y hay que decir por qué.** Cimiento **no está en operación**: corre en la máquina de quien lo escribió, no le sirve a nadie más, y no ha tenido un solo día de uso por parte de un tercero. Una bitácora de operación de un sistema que no opera no tiene incidentes que anotar. **Existe igual** —lo pide el ciclo, y un documento ausente y uno vacío no se distinguen desde afuera— y declara acá su propio límite.

---

## 1. Desde cuándo se lleva

Desde el **2026-09-02**, la fecha del [acta de entrega](../despliegue/acta-de-entrega.md). Lo anterior a esa fecha es construcción, y está en el [histórico de sesiones](../../historico-chat/README.md) y en las fases de cada épica, no acá.

---

## 2. Incidentes

| Fecha | Qué pasó | Cuánto duró | Qué se hizo | Qué se aprendió |
|---|---|---|---|---|
| — | **Ninguno.** El sistema no está en operación | — | — | — |

**Un renglón vacío no es un sistema estable: es un sistema que nadie ha usado.** La diferencia importa, y por eso se escribe.

---

## 3. Lo que sí pasó durante la construcción, y conviene tener a mano

No son incidentes de operación, pero son las tres formas en que este sistema ha fallado hasta ahora. Quien lo opere debería reconocerlas:

| Qué falló | Cómo se vio | Dónde quedó |
|---|---|---|
| **Un dato escrito a mano al lado de uno derivado** | La columna decía «sin verificar» sobre 35 funcionalidades que la plataforma daba por verificadas | [`S-118`](../../documentacion/senales.md) |
| **Un lector que supone una sola convención** | 107 de 209 fases usaban otra tabla; 76 cerraban con otra marca | [`S-114`](../../documentacion/senales.md) |
| **Una respuesta sobre una copia vieja** | El expediente reportó 22 documentos faltantes que existían | [`S-121`](../../documentacion/senales.md) |

**Las tres se parecen en algo:** el sistema respondía con seguridad sobre algo que ya no era cierto. Ninguna se ve leyendo la respuesta; todas se vieron comparándola con el disco.

---

## 4. Cómo se anota un incidente cuando lo haya

Una fila por incidente, en la tabla del punto 2, con las cinco columnas llenas. **La última es la que hace útil el documento**: un incidente sin qué se aprendió es un incidente que va a volver.

Si el incidente deja una regla nueva, va a `base/` por el procedimiento de siempre; si deja un aprendizaje que no llega a regla, va a [`documentacion/senales.md`](../../documentacion/senales.md).

---

## 5. Cuándo dejar de escribir acá

Cuando el sistema deje de operar. **No cuando deje de fallar**: una bitácora que se abandona porque «ya no pasa nada» pierde justo el tramo que probaría que se estabilizó.
