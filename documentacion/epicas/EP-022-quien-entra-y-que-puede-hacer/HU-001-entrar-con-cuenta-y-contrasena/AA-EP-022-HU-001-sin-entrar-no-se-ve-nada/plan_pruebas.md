# Plan de Pruebas — Fase `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-entrar-con-cuenta-y-contrasena.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **ninguna pantalla responde sin haber entrado**, que **entrar lleva a donde se iba**, y que **un intento fallido no dice cuál dato estuvo mal**.

### 1.2 Alcance

**Entra:** el guardián, la pantalla de entrar, salir, y la orden que crea cuentas.

**No entra:** los permisos por grupo, que van en la fase `AB`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/acceso/spec.md](../../../../acceso/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Todas las rutas | Sin entrar y habiendo entrado |
| La lista de lo abierto | Que sean dos, y cuáles |
| El mensaje de error | Que sea el mismo para los dos casos |
| La contraseña | Que no aparezca ni se guarde en claro |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **Contra el enrutador, no contra una lista** | Una lista escrita a mano se queda corta el día que alguien agregue una pantalla, y ese es el día en que hay que enterarse |
| **De que NO pase** | Que algo responda sin haber entrado |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001 | **Una pantalla que responde sin haber entrado no se nota: funciona** |
| Alta | CP-002 | Un mensaje que distingue confirma qué cuentas hay |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/acceso/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El pendiente 94 aprobado, y el diseño rehecho.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **alguna contraseña aparece en claro** en un archivo, en el registro o en una respuesta.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-001 | Contra el enrutador |
| CA-02 y CA-03 | CP-002 | De ida y vuelta, y de mensaje |

---

## 6. Casos de prueba

### CP-001 — Sin entrar no se ve nada

**El caso que decide la fase, y se prueba contra el enrutador.**

- **Todas las rutas registradas** se piden sin haber entrado: las que no están declaradas abiertas responden con un envío al formulario.
- **Lo abierto se cuenta**: si esa lista crece, la prueba lo dice.
- Los estáticos sí responden: son la hoja de estilos de la propia pantalla de entrar.
- **Una ruta que nadie ha escrito todavía nace protegida.**
- Habiendo entrado, las pantallas responden.

### CP-002 — Entrar, salir y el mensaje único

- Pedir el tablero sin entrar guarda a dónde se iba, y entrar lleva allá.
- La contraseña correcta abre la sesión.
- **La contraseña mala y la cuenta inexistente reciben el mismo mensaje.**
- La contraseña no aparece en la respuesta, y en la base no está en claro.
- Salir cierra la sesión.

**11 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Cuentas de mentiras de los dos grupos, en la base de pruebas, y una carpeta temporal como proyecto.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Alguien intentando entrar muchas veces.** No hay límite de intentos ni demora entre uno y otro, y ninguna prueba lo mira. Con la plataforma en una máquina no expuesta, el que puede intentar ya está adentro; el día que corra en un servidor, esto hay que mirarlo.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Una pantalla responde sin haber entrado · una contraseña queda en claro |
| **Alta** | El mensaje distingue los dos errores |
| **Media** | Entrar no lleva a donde se iba |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-09-01.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Rutas que responden sin haber entrado | **Cero** |
| Contraseñas escritas en claro | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar contra una lista de rutas escrita a mano | Se sacan del enrutador: así una pantalla nueva entra sola a la prueba |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada la épica entera el 2026-09-01 |
