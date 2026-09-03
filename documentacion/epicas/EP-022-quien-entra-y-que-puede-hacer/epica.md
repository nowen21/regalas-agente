# EP-022 — Quién entra y qué puede hacer

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-022 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Acceso |
| **Versión del producto** | 5 |
| **Funcionalidades que cubre** | `F-036`, `F-037` |
| **Estado** | Terminada el 2026-09-02: sus dos historias cumplen |
| **Fecha de apertura** | 2026-09-02 |

---

## 2. Resumen ejecutivo

Que la plataforma sepa quién entró, y que no todos puedan hacer lo mismo.

## 3. Problema y oportunidad

**El análisis definió los permisos y nadie los construyó.** Su sección 6 tiene cuatro actores con lo que cada uno puede y no puede hacer, incluido que **quien recibe un proyecto no entra a la plataforma**.

**El diseño los aplazó, con una condición escrita al lado:** *«un solo usuario en esta versión, sin credenciales propias»*, y a continuación: *«el día que la plataforma corra en un servidor, esta sección se rehace entera. Con un solo usuario en su máquina, no tener credenciales es razonable; **con dos, es una falla**»*.

**Medido el 2026-09-02, antes de empezar:** `django.contrib.auth` no estaba instalada, ninguna de las siete pantallas preguntaba quién entraba, y `aprobar --quien "Nombre"` aceptaba cualquier texto.

**Y el aplazamiento se levantó antes de esa fecha**, por decisión del usuario, al leer el manual de uso: *«el que yo lo use no significa que no pueda tener seguridad»*.

## 4. Objetivo y propuesta de valor

Que una aprobación diga quién la dio **y lo pruebe**.

**Beneficios esperados:**

- Ninguna pantalla responde sin haber entrado.
- El agente no aprueba lo que él mismo construyó.
- `RNF-09` —correr en un servidor— deja de ser el día en que todo queda abierto.

## 5. Alcance

**Dentro:**

- Entrar y salir con cuenta y contraseña (`F-036`).
- Dos grupos con sus permisos, y las órdenes que dejan de aceptar un nombre inventado (`F-037`).

**Fuera:**

- **Exponer la plataforma a la red.** Tener cuentas no la vuelve un servidor: lo vuelve posible sin rehacerla.
- **Pedir contraseña para correr una orden de consola.** Quien alcanza la consola de la máquina ya tiene la máquina.
- **Recuperar contraseña por correo.** No hay correo.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-036` Entrar con cuenta y contraseña | La sesión, y que nada responda sin ella | 5 |
| `F-037` Separar lo que cada grupo puede hacer | Dos grupos con sus permisos | 5 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Entra, y puede todo |
| El agente | Entra, y no aprueba, no publica, no deroga, no administra cuentas |
| El módulo Aprobaciones | Deja de aceptar un nombre que no sea una cuenta |

## 7. Criterios de aceptación de la épica

- **Ninguna pantalla responde sin haber entrado.**
- Entrar lleva a donde se iba, no a la portada.
- **Un intento fallido no dice cuál de los dos datos estuvo mal.**
- El agente no puede aprobar, publicar versiones ni derogar reglas.
- El rechazo dice **qué permiso falta y por qué existe**.
- **Una orden con una cuenta que no existe se rechaza.**
- La contraseña no queda escrita en ningún archivo ni registro.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Pantallas que responden sin haber entrado | **Cero** |
| Aprobaciones con un nombre que no es una cuenta | **Cero** |
| Contraseñas guardadas en claro | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-entrar-con-cuenta-y-contrasena/HU-001-entrar-con-cuenta-y-contrasena.md) | Entrar con cuenta y contraseña | `F-036` | **Terminada el 2026-09-02** |
| [HU-002](HU-002-separar-lo-que-cada-grupo-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer.md) | Separar lo que cada grupo puede hacer | `F-037` | **Terminada el 2026-09-02** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Acceso, con [especificación](../../acceso/spec.md) aprobada el 2026-09-02.

**Se usa el sistema de Django, `django.contrib.auth`, y no se escribe uno propio.** Escribir autenticación es la forma más común de escribirla mal: guardar contraseñas, compararlas sin filtrar tiempos, expirar sesiones. Django ya las tiene resueltas y probadas por mucha más gente de la que va a mirar este repositorio.

**Y el modelo encaja sin forzarlo:** los perfiles del análisis son **grupos** y lo que cada uno puede hacer son **permisos**. Ninguna tabla nueva.

**Va como middleware y no como decorador por vista**, y es la decisión que más protege: **una pantalla nueva nace protegida.** Con decoradores, la que alguien escriba dentro de seis meses nacería abierta y nadie lo notaría, porque funcionar, funciona.

## 11. Dependencias

Depende de `EP-008` —hace falta un proyecto del que colgar los permisos— y le cambia el comportamiento a `EP-017`, cuyo `quien` deja de ser texto libre.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que una pantalla nueva nazca abierta** | Middleware, no decorador |
| **Que el error de entrada confirme qué cuentas hay** | Un solo mensaje para los dos casos |
| Que una contraseña quede en el historial de la consola | La orden la pide sin mostrarla; no se recibe como argumento |
| Que el agente se apruebe a sí mismo | No tiene el permiso, y el rechazo dice por qué |
| Que se pierdan las cuentas al borrar la base | **Se acepta y se declara:** es lo segundo que no se reconstruye, junto con las aprobaciones |

## 13. Supuestos y restricciones

**Supuestos:** quien alcanza la consola de la máquina ya tiene la máquina.

**Restricciones:** la plataforma sigue sin exponerse a la red; no hay correo; lo registrado antes de que hubiera cuentas no se reescribe.

## 14. Hoja de ruta

Versión 5, después de `EP-021`. Sale del pendiente [94](../../../pendientes/94-el-control-de-acceso-esta-definido-y-no-construido.md), que se cierra con ella.

## 15. Definition of Ready

- ☑ El análisis define los actores y sus permisos, desde antes.
- ☑ El diseño rehizo su sección 8 el 2026-09-02.
- ☑ El módulo Acceso, con [especificación](../../acceso/spec.md) aprobada.

## 16. Definition of Done

- ☑ Las dos historias cerradas, con veredicto por criterio.
- ☑ Comprobado contra **todas las rutas registradas**, no contra una lista.
- ☑ Comprobado que el agente no aprueba.
- ☑ Comprobado que la contraseña no se guarda en claro.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-02 | **Terminada**: las dos historias construidas y probadas el mismo día |
| 2026-09-02 | Nace del pendiente 94, que nació de una pregunta del usuario sobre el manual |
