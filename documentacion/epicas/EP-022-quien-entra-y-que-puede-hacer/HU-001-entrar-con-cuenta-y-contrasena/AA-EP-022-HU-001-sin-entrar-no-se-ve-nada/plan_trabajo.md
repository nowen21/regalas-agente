# Plan de Trabajo — Fase `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` (módulo Acceso)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` |
| **Épica** | [EP-022](../../epica.md) |
| **HU** | [HU-001 Entrar con cuenta y contraseña](../HU-001-entrar-con-cuenta-y-contrasena.md), una sola (`F12.1`) |
| **Módulo** | Acceso |
| **Especificación del módulo** | [documentacion/acceso/spec.md](../../../../acceso/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 💬 **Una pregunta del usuario sobre el manual de uso**, el 2026-09-02: *«el que yo lo use no significa que no pueda tener seguridad»*.
- 📋 **Y el pendiente [94](../../../../../pendientes/94-el-control-de-acceso-esta-definido-y-no-construido.md)**, que salió de esa pregunta: el análisis definió los permisos, el diseño los aplazó, y nadie los construyó.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que ninguna pantalla responda sin haber entrado.

**El aplazamiento se levantó antes de su fecha.** El diseño decía «el día que corra en un servidor»; el usuario decidió no esperar a ese día.

**Fuera de alcance:** exponer la plataforma a la red, pedir contraseña para una orden de consola, y recuperar contraseña por correo —no hay correo—.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo verificado antes de empezar:** `django.contrib.auth` no estaba instalada, ninguna de las siete pantallas preguntaba quién entraba, y no había ni un `login_required` en todo el código.

**Y lo que sí estaba resuelto, para no rehacerlo:** no se guardan credenciales de terceros (`RNF-05`, con un módulo que las tapa), no se guardan datos de personas (`RNF-06`), y toda acción queda registrada sin poder editarse (`RNF-12`). Lo que faltaba era el control de acceso, y solo eso.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/acceso/` | Crear | Módulo | Nace |
| `plataforma/nucleo/acceso/middleware.py` | Crear | Guardián | Exige haber entrado |
| `plataforma/nucleo/acceso/views.py` | Crear | Vista | Entrar y salir |
| `plataforma/templates/acceso/entrar.html` | Crear | Plantilla | La única pantalla abierta |
| `plataforma/nucleo/acceso/management/commands/crear_cuenta.py` | Crear | Consola | Crear cuentas |
| `plataforma/config/settings/base.py` | Modificar | Configuración | `auth`, su middleware y las rutas |
| `plataforma/config/urls.py` | Modificar | Rutas | Entrar y salir |
| `plataforma/templates/base.html` | Modificar | Plantilla | Quién entró, y salir |

**Ninguna entidad propia.** Las de `django.contrib.auth`, con sus migraciones y su cifrado.

### 2.2 Matriz de dependencias del refactor

**Cinco archivos de pruebas tuvieron que aprender a entrar.** Ninguna lógica cambió: lo que cambió es que la plataforma dejó de responder a quien no entró, y sus pruebas eran de cuando respondía a todos.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El sistema de Django** | Escribir uno propio | Guardar contraseñas, comparar sin filtrar tiempos, expirar sesiones: cada una tiene una forma correcta y varias que parecen correctas |
| **Middleware, no decorador por vista** | Un `login_required` en cada vista | **Una pantalla nueva nace protegida.** Con decoradores, la que alguien escriba en seis meses nace abierta y nadie lo nota |
| **La lista de lo abierto es corta y se lee** | Dejarla implícita | Cada renglón de esa lista es una decisión, y se ve de un vistazo |
| **Un solo mensaje para los dos errores** | Decir si la cuenta existe | Decirlo confirma qué cuentas hay, que es la mitad del trabajo de quien esté probando |
| **La contraseña se pide sin mostrarla** | Recibirla como argumento | Lo que se escribe en la línea de órdenes queda en el historial de la consola (`00·N6`) |
| **`/esta-viva/` también exige entrar** | Dejarla abierta | Se pensó dejarla —una comprobación de vida que pide contraseña no puede decir «estoy caída»— y se cerró: **revela la ruta de la carpeta de datos** |

### 2.7 Dudas por resolver antes de codificar

Una, y se resolvió mirando el código: si la comprobación de vida podía quedar abierta. Revela una ruta, así que no.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Instalar `auth` con su middleware y sus rutas | Configuración | 30 min | — | CA-01 | EV-01 |
| T-02 | El middleware que exige haber entrado | Guardián | 1,5 h | T-01 | CA-01 | EV-01 |
| T-03 | La pantalla de entrar, con el mensaje único | Vista | 1,5 h | T-02 | CA-02 y CA-03 | EV-01 |
| T-04 | La orden para crear cuentas | Consola | 1 h | T-01 | — | EV-01 |
| T-05 | Quién entró, en la barra de arriba | Plantilla | 30 min | T-03 | — | EV-01 |
| T-06 | Que las pruebas de antes entren | Test | 2 h | T-03 | — | EV-01 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 9 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-07.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Recorriendo **todas las rutas registradas**, sacadas del enrutador | EV-01 | 2026-09-02 | ☑ |
| CA-02 | Pidiendo el tablero, entrando, y mirando dónde queda | EV-01 | 2026-09-02 | ☑ |
| CA-03 | Con la contraseña mala y con una cuenta que no existe | EV-01 | 2026-09-02 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/acceso/tests.py` |

---

## 6. Datos y ambiente de prueba

Cuentas de mentiras de los dos grupos, en la base de pruebas, y una carpeta temporal como proyecto.

---

## 7. Reversión / rollback  ·  Q11

Quitar el middleware y la app deja la plataforma abierta como antes. **Las cuentas creadas quedan**, y eso es lo que hay que saber: se pierden si se borra la base.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md) (una credencial no se escribe, no se registra y no se guarda) y el capítulo [`04`](../../../../../base/04-seguridad.md).
- Producto: las `RN-1` a `RN-5` de la historia, y la sección 8 del diseño.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que una pantalla nueva nazca abierta** | **Alto: se descubre cuando ya se usó** | Middleware, y una prueba que recorre todas las rutas del enrutador | Cerrado |
| B-02 | Que el error confirme qué cuentas existen | Medio | Un solo mensaje para los dos casos | Cerrado |
| B-03 | Que una contraseña quede en el historial de la consola | Medio | Se pide sin mostrarla | Cerrado |
| B-04 | **Que se pierdan las cuentas al borrar la base** | Medio | **Se acepta y se declara:** es lo segundo que no se reconstruye, junto con las aprobaciones | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado contra todas las rutas registradas
- [x] Comprobado que la contraseña no se guarda en claro
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
