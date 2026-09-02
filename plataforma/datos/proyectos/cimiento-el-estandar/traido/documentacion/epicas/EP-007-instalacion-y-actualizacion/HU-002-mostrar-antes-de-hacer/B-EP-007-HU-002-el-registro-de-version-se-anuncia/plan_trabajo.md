# Plan de Trabajo — Fase `B-EP-007-HU-002-el-registro-de-version-se-anuncia` (módulo Instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-007-HU-002-el-registro-de-version-se-anuncia` |
| **Épica** | [EP-007](../../epica.md) |
| **HU** | [HU-002](../HU-002-mostrar-antes-de-hacer.md), **una sola** (`F12.1`) |
| **Módulo** | Instalación |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-02 y el defecto `D-01` de la fase [`A`](../A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md).** La simulación del instalador anunciaba 12 de 13 archivos. El que faltaba era `documentacion/versiones/<fecha>-<version>.md`, **el que deja constancia de qué se instaló**.

**Por qué la fase `A` no lo arregló:** el arreglo toca `instalar.py`, y el §2.1 de su plan aprobado no lo declaraba. `02·F8` no deja tocar lo que el plan no nombra, así que quedó propuesto. **El plan de esta fase lo declara**, y con eso se destraba.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que lo que la simulación anuncia sea exactamente lo que aparece al aplicar, incluido el registro de versión.

**Fuera de alcance:**

- El defecto `D-02` de la fase `A`, sobre la línea que muestra la orden literal de git. No deja ningún CA en «No».
- Cambiar **cuándo** se escribe el registro. Lo que estaba mal era el anuncio, no la regla de cuándo registrar.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
103 cumplen, 6 no cumplen, 5 sin veredicto
```

### 2.1 La causa, y por qué no era una mentira del anuncio

`registrar_version` decide si hay algo que registrar comparando dos juegos de
huellas: las de antes de la corrida y las del proyecto **en ese momento**.

Al aplicar, «ese momento» es después de copiar, y la comparación ve los
cambios. **Al simular, no se ha copiado nada todavía**, así que las dos son
iguales y la respuesta es «no hay actualización que registrar». Después, al
aplicar de verdad, el registro se escribe.

La simulación no estaba mintiendo sobre lo que iba a hacer: **se estaba mirando
en el espejo equivocado**. Lo que tiene que comparar es la huella que va a
quedar, que es la central de cada componente: al terminar de instalar, el
proyecto tiene esa.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Instalación | `_huellas_previstas` y su uso en `registrar_version` |
| `validadores/versiones.py` | Modificar | Instalación | `nombre_previsto`, para poder anunciar el archivo |
| `validadores/pruebas.py` | Modificar | Pruebas | La prueba sale del fallo esperado |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-002-mostrar-antes-de-hacer.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

**Los dos primeros son los que la fase `A` no podía tocar.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Al simular se compara la huella **prevista** | Escribir el registro también en simulación | Simular no escribe nada, y eso es el CA-01, que ya cumplía |
| Se anuncia **el archivo**, no la carpeta | Dejar «registrar la actualización en `versiones/`» | Anunciar el sitio y no la cosa deja el registro fuera de la lista que después se compara |
| El nombre se predice con la misma función que lo elige | Inventar el nombre en el anuncio | Si el nombre se calculara en dos sitios, el anuncio y el archivo se separarían el día que uno cambie |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reproducir el defecto | Calidad | 0,25 h | — | EV-01 |
| T-02 | Que la simulación mire la huella que va a quedar | Instalación | 1 h | T-01 | EV-02 |
| T-03 | Que anuncie el archivo, no la carpeta | Instalación | 0,5 h | T-02 | EV-02 |
| T-04 | Sacar la prueba del fallo esperado | Pruebas | 0,25 h | T-03 | EV-02 |

**Total estimado:** 2 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-03` no es cosmética: sin ella la `T-02` sola no cierra el criterio, porque
la prueba compara **nombres de archivo**, y un anuncio que solo nombra la
carpeta no contiene ninguno.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02, lo que muestra es lo que hace | Simular, aplicar, y comparar los archivos nuevos contra lo anunciado | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Un proyecto de prueba que la propia prueba arma y borra. Ningún proyecto real se
toca.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. El instalador no deja estado fuera del
proyecto que instala.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** El cambio se nota la próxima vez que alguien corra el
instalador sin `--aplicar`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8`, solo se tocan los archivos que el plan declara. Es la regla que dejó este defecto sin arreglar, y por eso este plan los nombra.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la simulación empiece a escribir algo | Rompería el CA-01, que ya cumplía | La prueba de «no escribe ni un archivo» sigue corriendo | Cerrado |
| B-02 | Que el nombre anunciado y el escrito se separen | Volvería el mismo defecto por otra puerta | Los dos salen de `_nombre_libre` | Cerrado |

---

## 11. Definition of Done

- [x] El defecto, reproducido
- [x] Las cuatro pruebas de la clase, en verde
- [x] Ningún fallo esperado en la clase
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
