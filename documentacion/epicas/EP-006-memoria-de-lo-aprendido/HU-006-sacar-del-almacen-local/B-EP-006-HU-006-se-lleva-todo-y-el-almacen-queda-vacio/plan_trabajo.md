# Plan de Trabajo — Fase `B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio` |
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [HU-006](../HU-006-sacar-del-almacen-local.md), **una sola** (`F12.1`) |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-01, el almacén local queda vacío**, que dejó la fase [`A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local`](../A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md) en «No cumple» el 2026-08-22, porque el almacén estaba vacío y el programa lo vaciaba, pero fallaba el paso 5: `sueltos()` devuelve **todo** archivo, así que un `config.json` de la herramienta terminaría en `historico-chat/memory/` como si fuera un recuerdo.

**Se lleva todo.** Lo decidió el usuario el 2026-08-30.

**Este rojo no se cerraba midiendo.** Medirlo otra vez daba el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** aplicar la decisión, comprobarla ejecutando, y dejar escrito qué queda cubierto y qué no.

**Fuera de alcance:** los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
107 cumplen, 2 no cumplen, 5 sin veredicto
```

### 2.1 Por qué la decisión es esta

**Por qué manda `01·C19` tal como está escrita.** Exige que el almacén local quede **vacío**, y eso es lo que se sostiene: lo que queda ahí es lo que se pierde. La carpeta de la herramienta no la mira nadie, no se versiona y desaparece con la máquina.

**El costo de la otra salida era peor.** Si el programa dejara ahí lo que no es recuerdo, `revisar()` reprobaría para siempre por un archivo que nadie va a mover, y un reclamo que no se puede cerrar se aprende a ignorar.

**Y el archivo de más no se pierde de vista:** un `config.json` en `historico-chat/memory/` se ve, se lee y se borra cuando estorbe. Uno olvidado en una carpeta de la herramienta, no.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-006-sacar-del-almacen-local.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se lleva todo | Que el programa distinga y deje lo que no es recuerdo | Lo que queda en el almacén es lo que se pierde: esa carpeta no la mira nadie y no se versiona |
| `01·C19` no se toca | Precisarla a «ningún recuerdo queda en el almacén» | Aflojarla dejaría vivo el caso que la regla existe para evitar |
| La prueba comprueba las dos mitades | Comprobar solo que el almacén quedó vacío | Un programa que borrara el almacén sin traer nada también lo dejaría vacío |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Ejecutar el criterio y su contraprueba | Calidad | 0,5 h | — | EV-01 |
| T-02 | Aplicar la decisión del usuario | Implementación | 0,5 h | T-01 | EV-02 |
| T-03 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-02 | EV-02 |

**Total estimado:** 1,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

La contraprueba de la `T-01` no es adorno: es la que sostiene la decisión.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01, el almacén local queda vacío | Ejecutar el criterio con su contraprueba | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas y valores de prueba que la propia prueba arma y borra. Ninguna
credencial real (`00·N6`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `01·C4`, decidir no es del que ejecuta. Es lo que tuvo detenida esta historia.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `20·M11`, lo publicado no se reescribe: se deja atrás.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Cerrar el criterio escondiendo lo que no cubre | Es la mentira optimista que esta cuenta existe para impedir | El límite queda escrito en el cierre | Cerrado |
| B-02 | Que el agente decidiera esto por su cuenta | Es `01·C4` | Se esperó la decisión | Cerrado |

---

## 11. Definition of Done

- [x] El criterio y su contraprueba, ejecutados
- [x] La decisión, aplicada
- [x] El límite, escrito
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
