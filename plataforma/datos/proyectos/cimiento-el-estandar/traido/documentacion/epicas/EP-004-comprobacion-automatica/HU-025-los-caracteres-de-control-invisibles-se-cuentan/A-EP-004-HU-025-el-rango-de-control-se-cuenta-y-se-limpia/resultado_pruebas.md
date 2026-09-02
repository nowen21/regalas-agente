# Resultado de Pruebas — Fase `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el contador reconoce el rango completo, la limpieza los quita sin tocar el texto visible, y el árbol quedó en cero.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas en verde | 5 | **5** |
| Archivos limpiados | — | **14** |
| Caracteres de control en el árbol contado | 0 | **0** |
| Palabras del texto que cambiaron | 0 | **0** |

---

## 3. Resultado por caso

| Caso | Resultado |
|---|---|
| CP-001 · el que rompió la fila | Pasa: se cuenta y se nombra |
| CP-002 · el rango, no solo el que apareció | Pasa: cinco puntos distintos |
| CP-003 · lo legítimo no se toca | Pasa: tabulador, salto y retorno, sin hallazgos |
| CP-004 · la limpieza no cambia el texto visible | Pasa: idénticos salvo el carácter |
| CP-005 · el árbol queda en cero | Pasa |

```
Ran 5 tests in 5.709s
OK
```

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué se barre el rango y no los que aparecieron

Agregar de a uno los que van saliendo **deja el trabajo a medias por definición**: el próximo se cuela igual, y nadie lo va a ver, porque el defecto es justamente que no se ve. Se cuentan los del rango y se dejan fuera los tres que significan algo al escribir.

### 4.2 Qué se limpió y qué no

Se limpiaron **14 archivos**. Los que quedan están en dos sitios que no se tocan a propósito: la carpeta de datos de la plataforma, que es una copia traída y se vuelve a traer, y el histórico, que no se reescribe porque es una transcripción.

### 4.3 Se comprobó el registro de sesiones antes de limpiar

Ningún archivo que otra sesión tuviera en curso entró en la limpieza. Es el mismo cuidado que faltó el día de las 712 líneas.

### 4.4 La lista escrita y el programa dicen lo mismo

El anexo que enumera estas marcas recibió su fila. Sin eso, la próxima vez que alguien lea la norma para saber qué se cuenta, la norma le diría menos de lo que el programa hace.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/marcas.py`, el rango en la lista y en la limpieza
- `base/00-identidad-y-rol/marcadores-de-ia.md`, su fila
- `validadores/tests/test_los_caracteres_de_control_se_cuentan.py`
