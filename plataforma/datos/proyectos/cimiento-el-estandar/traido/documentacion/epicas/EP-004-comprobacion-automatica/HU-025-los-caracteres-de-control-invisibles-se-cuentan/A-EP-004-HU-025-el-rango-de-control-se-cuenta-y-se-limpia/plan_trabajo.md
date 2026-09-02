# Plan de Trabajo — Fase `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-025](../HU-025-los-caracteres-de-control-invisibles-se-cuentan.md), **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Defecto.** Al agregarle una fila a la tabla de fases de una historia, la fila que ya estaba empezaba con un carácter invisible en vez de con la barra de la tabla, y por eso **no se renderizaba como fila**: desaparecía del cuadro y quedaba como un párrafo suelto debajo. Estaba en 26 archivos. Sale del [pendiente 92](../../../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md).

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que se cuenten, que la limpieza los quite, y que el árbol quede en cero.

**Fuera de alcance:**

- **Averiguar de dónde salieron.** Nadie sabe qué los metió, y saberlo no es condición para limpiarlos.
- El histórico, que no se reescribe, y la carpeta de datos de la plataforma, que es una copia traída.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
26 archivos con el carácter · 120 historias que cumplen
```

### 2.1 Por qué no lo cazaba nadie

El programa conocía **siete** caracteres invisibles: el espacio duro, el de ancho cero, el guion suave y cuatro más. Ninguno de control estaba en esa lista, ni en el anexo donde la norma los enumera.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/marcas.py` | Modificar | Comprobación | El rango, en la lista y en la limpieza |
| `base/00-identidad-y-rol/marcadores-de-ia.md` | Modificar | Estándar | Su fila, para que la lista y el programa digan lo mismo |
| `validadores/tests/test_los_caracteres_de_control_se_cuentan.py` | Crear | Pruebas | Cinco casos |
| Los archivos que traían el carácter | Modificar | Varias | Solo se les quita lo invisible |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `36.0.3`, parche |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se barre el **rango completo** | Agregar los que aparecieron | Agregar de a uno deja el trabajo a medias por definición: el próximo se cuela igual, y no se ve |
| Salto de línea, retorno y tabulador quedan fuera | Barrer todo | Sí significan algo al escribir; contarlos volvería la comprobación ruido |
| La limpieza los **borra**, no los reemplaza | Poner un espacio | No hay reemplazo que elegir: no significan nada |
| El histórico y los datos de la plataforma no se tocan | Limpiar todo | Una transcripción no se reescribe, y esa carpeta es una copia que se vuelve a traer |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Contar el rango completo | Comprobación | 0,5 h | — | EV-01 |
| T-02 | Que la limpieza los quite | Comprobación | 0,25 h | T-01 | EV-01 |
| T-03 | La fila en el anexo | Estándar | 0,25 h | T-01 | EV-02 |
| T-04 | Limpiar lo que ya lo traía | Documentación | 0,5 h | T-02 | EV-03 |

**Total estimado:** 1,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-04, con la T-03 en paralelo.

Antes de limpiar se comprueba el registro de sesiones: un archivo que otra sesión tenga en curso no se toca.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 · se reporta con su archivo y su línea | La marca aparece en el conteo con su nombre | CP-001 | ☑ |
| CA-02 · el árbol queda en cero | Contar antes y después | CP-005 | ☑ |
| CA-03 · lo legítimo no se toca | Tabulador, salto y retorno | CP-003 | ☑ |

---

## 6. Datos y ambiente de prueba

Cadenas armadas en la propia prueba, y el árbol real para la última.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `00·ID8`, las marcas que este validador comprueba.
- `20·M10`, todo cambio del cuerpo de reglas se versiona y se registra.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la limpieza cambie texto visible | Sería peor que el defecto | La `CP-004` compara el antes y el después | Cerrado |
| B-02 | Tocar archivos que otra sesión tenga en curso | Es el caso de las 712 líneas | Se comprobó el registro antes de limpiar | Cerrado |

---

## 11. Definition of Done

- [x] El rango, contado
- [x] Los archivos, limpios
- [x] La lista escrita y el programa, diciendo lo mismo
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
