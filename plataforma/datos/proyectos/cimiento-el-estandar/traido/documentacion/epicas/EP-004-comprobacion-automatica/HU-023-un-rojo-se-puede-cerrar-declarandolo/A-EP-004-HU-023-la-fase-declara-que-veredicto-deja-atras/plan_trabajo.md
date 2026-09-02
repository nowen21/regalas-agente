# Plan de Trabajo — Fase `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-023](../HU-023-un-rojo-se-puede-cerrar-declarandolo.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Sale de `S-065`**, comprobado haciéndolo: dos fases verificaron criterios en rojo, midieron que hoy se cumplen, cerraron con «Cumple», **y el número no se movió**.

**CA de la HU que cubre esta fase:** los cinco. Son una sola cosa: una forma de cerrar un rojo que no se pueda usar por accidente.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que una fase pueda **declarar qué veredicto anterior deja atrás**, y que la cuenta lo lea.

**Fuera de alcance:**

- **Cerrar los ocho rojos que tienen fase posterior.** Esta fase da la forma; declarar cada uno es trabajo de quien verifique.
- **Los ocho que no tienen fase posterior.** Ahí no hay nada que declarar.
- **Reescribir veredictos viejos.** Nunca (`20·M11`).

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase.**

### 2.0 La línea base

```
119 en total · 32 sin terminar · 87 terminadas,
de las cuales 66 cumplen, 16 no cumplen y 5 no dicen si cumplen
```

### 2.1 El reparto de los rojos, contado

| Qué | Cuántas |
|---|---|
| Historias terminadas con alguna fase en rojo | **16** |
| Con una fase **posterior** a la última roja | **8** |
| Sin ninguna fase posterior | **8** |
| De las ocho, las que **volvieron a verificar el criterio en rojo** | **2** |

**Las seis restantes trabajaron otro criterio de la misma historia.** Ese dato es el que descarta deducir el reemplazo del orden.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md` | Modificar | Documentación | El campo, opcional y explicado |
| `validadores/fases.py` | Modificar | Servicio | Leerlo, y las condiciones para que valga |
| `validadores/pruebas.py` | Modificar | Test | Los cinco CA |
| `CHANGELOG.md` · `VERSION` | Modificar | Documentación | `20·M10` |

**Los dos cierres de las fases `D` de hoy** se declaran aparte: son quienes van a estrenar el campo, y se dice en el §3 como tarea propia.

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `por_veredicto` | **Ninguno en la firma.** Sigue devolviendo tres valores | 32 pruebas | **Cambia lo que devuelve** solo donde el campo esté escrito. Hoy no está en ninguna: **la primera corrida tiene que dar exactamente lo mismo** |
| El molde `11` | Un campo **opcional** más | El validador de completitud de plantillas | No rompe si es opcional. Se comprueba en la `T-00` |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/validar.py fases`.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El reemplazo se **declara** | Deducirlo del orden de las fases | **Medido:** de ocho candidatas, seis no resolvieron el rojo. Deducirlo las daría por cumplidas |
| Solo vale si **quien declara cumple** | Aceptarlo siempre | Un rojo se taparía con otro rojo |
| Solo puede reemplazar una fase **de la misma historia** | Cualquier fase del árbol | Un rojo ajeno no es de nadie, y abriría la puerta a cerrarlo desde donde no se verificó |
| Un nombre que no resuelve **avisa y no reemplaza** | Ignorarlo en silencio | `04·R4`. Y un campo mal escrito que no dice nada es peor que no tenerlo: parece que funcionó |
| El campo va en el **cierre**, no en el resultado | El resultado, que es quien produce el veredicto | El resultado dice **qué pasó en esta fase**; el reemplazo es una afirmación **sobre otra**. Y el cierre es el documento que la cuenta ya abre |
| El campo es **opcional** | Obligatorio con «ninguna» | Obligar a escribir «ninguna» en 130 fases para que dos digan algo es ruido |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. El reparto de los 16 rojos está contado, y las dos que pueden declararlo, nombradas | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | **Antes de tocar nada:** ver si alguna prueba exige la lista de campos del molde `11` | Test | 0,5 h | — | EV-00 |
| T-01 | El campo en el molde, opcional y explicado | Documentación | 0,5 h | T-00 | EV-01 |
| T-02 | Leer el campo del cierre de cada fase | Backend | 0,5 h | T-01 | EV-02 |
| T-03 | Que solo valga si quien declara cumple, y si la fase nombrada es de la misma historia | Backend | 1 h | T-02 | EV-02 |
| T-04 | Avisar cuando el nombre no resuelve | Backend | 0,5 h | T-03 | EV-03 |
| T-05 | Los cinco CA, con el caso de que **no** se deduzca del orden | Test | 2 h | T-03 | EV-01 a EV-05 |
| T-06 | **Comprobar que sin ninguna declaración el número no cambia** | Calidad | 0,5 h | T-03 | EV-06 |
| T-07 | Declararlo en los dos cierres que sí verificaron | Documentación | 0,5 h | T-06 | EV-07 |
| T-08 | Medir el número antes y después, y **nombrar las dos que se mueven** | Documentación | 0,5 h | T-07 | EV-07 |
| T-09 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-08 | EV-08 |
| T-10 | Sabotear | Calidad | 1 h | T-05 | EV-09 |

**Total estimado:** 8 h

**Versión: MENOR.** Campo opcional; nadie tiene que cambiar nada de lo que ya tiene. Sube a `35.5.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-06 → T-07

**La `T-06` va antes de declarar nada, y es la que protege todo lo demás.** Con el código puesto y **cero declaraciones escritas**, la línea tiene que dar **exactamente lo mismo que la línea base**. Si cambia aunque sea en uno, el reemplazo se está deduciendo de algo, y ahí se para.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · la fase declara qué veredicto deja atrás | Un árbol que cambia de cuenta según el campo esté o no | EV-02 | | ☐ |
| CA-02 · una fase en rojo no cierra el rojo de otra | Dos rojas, la segunda declarando | EV-02 | | ☐ |
| CA-03 · el reemplazo **no** se deduce del orden | Un árbol sin el campo, **y el árbol real** | EV-06 | | ☐ |
| CA-04 · un nombre que no resuelve avisa | Fase inventada, y fase de otra historia | EV-03 | | ☐ |
| CA-05 · el veredicto reemplazado no se borra | Comparar el documento antes y después | EV-05 | | ☐ |

---

## 6. Datos y ambiente de prueba

Árboles de mentira en carpeta temporal, y el árbol real para la `T-06`. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita para probar (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`. **El campo declarado en los dos cierres queda inerte**, no roto: sin el código que lo lee, es una fila más de una tabla.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar no verá cambiar ningún número**, porque nadie tiene el campo escrito. Lo gana es la posibilidad de cerrar un rojo cuando lo arregle.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base y el reparto de los rojos, medidos antes de planear.
- `04·R4` — un nombre que no se puede resolver no afirma nada.
- `20·M10` — versión y registro de cambios.
- `20·M11` — nada se borra ni se reescribe.
- `13·DOC5` — lo decidido se registra como señal: `S-065`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el reemplazo se deduzca y tape **seis rojos vivos** | Sería la mentira optimista que esta cuenta vino a impedir | `CA-03`, y la `T-06` contra el árbol real | Abierto |
| B-02 | Que un rojo se tape con otro rojo | Lo mismo, por otra puerta | `CA-02` | Abierto |
| B-03 | Que una prueba exija la lista de campos del molde `11` | Rompería por algo que no es defecto | La `T-00`, antes de tocar nada | Abierto |
| B-04 | Que el número baje más de dos | Señal de que algo se dedujo | La `T-08` nombra **cuáles** se mueven, no solo cuántas | Abierto |
| B-05 | Que abrir esta fase mueva la medición | `S-053` | La línea base está en el §2.0 | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados
- [ ] **Con cero declaraciones, la línea idéntica a la base**
- [ ] Las dos que se mueven, **nombradas**
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] `VERSION` en `35.5.0` y su entrada en el `CHANGELOG`
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
