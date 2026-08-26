# Resultado de Pruebas — Fase A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · Cada versión tiene su entrada

`validar.py versionado` lo comprueba y hoy devuelve **0 fallas**. El único aviso es viejo y está reconocido en el propio registro:

```
[AVISO] CHANGELOG.md — el registro tiene 2 entradas para la 15.4.0
        — dos sesiones numeraron a la vez (ya reconocido; no se renumera)
```

Vale la pena señalar de qué es ese aviso: **dos sesiones numeraron a la vez**. Es el mismo problema que volvió a ocurrir hoy y que quedó cerrado con el guardián de sesiones mezcladas.

**Resultado del criterio: Cumple.**

### CA-02 · Un cambio sin entrada no pasa

Lo hace el enganche del commit, y tiene sus pruebas: `test_el_cambio_de_reglas_lleva_su_version`, **7 casos, todos en verde**.

Y no es teoría: esta jornada subió la versión cinco veces —de la `31.12.0` a la `32.0.1`— y cada una salió con su entrada, porque sin ella el commit no habría pasado.

**Resultado del criterio: Cumple.**

### CA-03 · El registro se entiende sin haber seguido el cambio

Lo comprueba [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), y no de forma decorativa: mira si la entrada **abre** con un identificador de regla, con una ruta de archivo o con jerga de la casa, porque las tres cosas obligan a conocer el proyecto para entender la primera frase.

**Y hoy reprobó una entrada mía, que es la mejor prueba que podía tener.** La de la `32.0.1` abría así:

> «una ruta que el `CLAUDE.md` del proyecto nombraba de dos formas»

Dos cosas que el lector no tiene por qué saber. Reescrita en llano:

> «una carpeta que el documento del proyecto nombraba de dos formas»

Dice lo mismo, y se entiende sin haber visto nunca este repositorio. **La comprobación encontró el defecto en el mismo día en que se escribió**, no meses después.

**Resultado del criterio: Cumple.**

---

## 2. Verificaciones manuales

La prueba `test_la_entrada_del_registro_se_entiende` corre **sobre el registro real de este repositorio**, no sobre un ejemplo. Por eso pudo fallar con una entrada escrita esta misma tarde: la comprobación no vive en un caso de laboratorio, vive sobre el archivo que de verdad se publica.

Es lo contrario de lo que pasó con el aviso de desfase, que se ve funcionar aquí y no llega a los proyectos. **Este funciona donde importa.**

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Baja | La entrada de la `32.0.1`, escrita hoy, abría con una ruta y con el nombre de un archivo del proyecto | **Corregido** el mismo día |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, cada versión tiene su entrada | `validar.py versionado`, 0 fallas | Cumple |
| CA-02, un cambio sin entrada no pasa | El enganche y sus 7 pruebas, más cinco versiones subidas hoy | Cumple |
| CA-03, se entiende sin haber seguido el cambio | `20·M17` corriendo sobre el registro real, y una entrada de hoy reprobada y corregida | Cumple |

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios están comprobados por programas que corren sobre el archivo real y que hoy encontraron y corrigieron un defecto propio. Es de las pocas comprobaciones del repositorio que se probaron a sí mismas mientras se ejecutaba la fase.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Cada versión con su entrada | `validar.py versionado` |
| EV-02 | El enganche que lo exige | `test_el_cambio_de_reglas_lleva_su_version`, 7 en verde |
| EV-03 | La entrada reprobada y corregida | La `32.0.1` del `CHANGELOG.md` |

---

## 7. Ciclos anteriores

Ninguno.
