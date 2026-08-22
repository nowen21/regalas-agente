# Resultado de Pruebas — Fase A-EP-005-HU-006-la-bateria-antes-de-publicar   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-006-la-bateria-antes-de-publicar` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · Antes de publicar corre todo

El enganche existe y lo escribe el instalador en cada proyecto. `PLANTILLA_PRE_PUSH` de [`validadores/instalar.py`](../../../../../validadores/instalar.py):

```sh
echo "pre-push: corriendo la batería antes de publicar…"
for SUB in estandar versionado; do
    "$PY" "$ESTANDAR/validadores/validar.py" "$SUB" --raiz "$(pwd)" || FALLO=1
done
```

Corre al publicar, no al confirmar, y el motivo está escrito en el propio enganche: **publicar es lo que no se deshace**. Un commit se revierte; lo publicado ya lo tiene otro.

**Resultado del criterio: Cumple.**

### CA-02 · Un incumplimiento claro detiene la publicación

Detiene, y **el reparto de qué detiene y qué no está decidido con su motivo escrito en el propio enganche**:

| Qué | Qué hace |
|---|---|
| Enlaces rotos, índices desactualizados, lo que se publica sin versionar | **Detiene** |
| El cuerpo de reglas contra su propio molde | **Informa y no detiene** |

Y la razón de la segunda fila es la que hace que esto sobreviva: *«un estándar con deuda conocida no puede impedir publicar cualquier otra cosa: eso convierte el enganche en un obstáculo permanente, y a la semana alguien lo apaga con `--no-verify`»*.

**Resultado del criterio: Cumple.**

---

## 2. Verificaciones manuales

**Hay un caso vivo hoy mismo, y conviene decirlo porque es la prueba de que el CA-02 funciona.** Este repositorio tiene una falla de `estandar` sin resolver: un enlace roto en `historico-chat/resumenes/indice-tematico.md`, que apunta a un resumen que no existe y que entró en un commit de otra sesión a las 12:10.

Esa falla **impediría publicar**, que es exactamente lo que el CA-02 pide. No es un defecto de esta fase: es su criterio de aceptación cumpliéndose sobre un caso real que nadie preparó.

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Media | La batería del `pre-push` corre `estandar` y `versionado`, y **no corre las pruebas de los validadores**. Un cambio que rompa una prueba se publica igual mientras no rompa enlaces ni versión | **Abierto** |
| D-02 | Baja | El enganche vive en la máquina, no viaja con el repositorio. Un clon nuevo no lo tiene hasta que corra el instalador, y eso no se avisa en ninguna parte | **Abierto** |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, antes de publicar corre todo | El enganche que escribe el instalador, leído | Cumple |
| CA-02, un incumplimiento claro detiene | El reparto entre lo que detiene y lo que informa, con su motivo, y el caso vivo de hoy | Cumple |

## 4.1 Lo que este «Cumple» no dice

«Corre todo» es lo que el criterio pide y lo que el enganche hace, **pero «todo» son dos comprobaciones**. Las pruebas de los validadores quedan fuera, y hoy son 593. Está en el D-01, y se dice acá para que el veredicto no se lea de más.

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios están cubiertos por algo que corre solo y que se instala en cada proyecto, con el reparto entre detener e informar decidido y explicado. Lo que queda es alcance, no funcionamiento, y está anotado.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El enganche | `PLANTILLA_PRE_PUSH` en `validadores/instalar.py` |
| EV-02 | El caso vivo que detendría la publicación | `validar.py estandar`, una falla por un enlace roto |

---

## 7. Ciclos anteriores

Ninguno.
