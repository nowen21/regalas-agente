# Especificación del módulo Acceso  ·  `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Módulo** | Acceso |
| **Funcionalidades que cubre** | [`F-036`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) entrar con cuenta y contraseña · [`F-037`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) separar lo que cada grupo puede hacer |
| **Épica** | [EP-022](../epicas/EP-022-quien-entra-y-que-puede-hacer/epica.md) |
| **Estado** | Aprobada el 2026-09-02 |
| **Versión del estándar** | 37.2.2 |

---

## 1. Propósito y alcance

**Que la plataforma sepa quién entró, y que no todos puedan hacer lo mismo.**

**Entra:** entrar y salir con cuenta y contraseña, los dos grupos con sus permisos, y que las órdenes de consola dejen de aceptar un nombre inventado.

**No entra:** exponer la plataforma a la red, recuperar contraseñas por correo, y pedir contraseña para correr una orden de consola.

---

## 2. Contexto — qué hay hoy

**El análisis definió los permisos y nadie los construyó.** Su sección 6 tiene cuatro actores con lo que cada uno puede y no puede hacer; el diseño los aplazó a «un solo usuario en esta versión», advirtiendo que **con dos usuarios eso es una falla**.

Medido el 2026-09-02, antes de empezar: `django.contrib.auth` no estaba instalada, ninguna de las siete pantallas preguntaba quién entraba, y `aprobar --quien "Nombre"` aceptaba cualquier texto.

**El aplazamiento lo levantó el usuario**, antes de la fecha que el diseño ponía: *«el que yo lo use no significa que no pueda tener seguridad»*.

---

## 3. Supuestos, dependencias y preguntas abiertas

| # | Qué | Tipo |
|---|---|---|
| 1 | La plataforma corre en la máquina de quien la usa | Supuesto que **sigue vigente**: esto no la expone a la red |
| 2 | Quien alcanza la consola de la máquina ya tiene la máquina | Supuesto, y por eso las órdenes no piden contraseña |
| 3 | Los perfiles del análisis caben en grupos de Django | Verificado al diseñar |
| 4 | Qué pasa con lo registrado antes de que hubiera cuentas | **Decidido:** se queda como está. Reescribirlo sería inventar quién hizo qué |

---

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| `RN-1` | **Ninguna pantalla responde sin haber entrado.** La que no exige entrar es la de entrar |
| `RN-2` | Las contraseñas se guardan cifradas, con lo que trae Django. **Nunca en claro, ni en el registro** |
| `RN-3` | Hay dos grupos: `usuario` y `agente` |
| `RN-4` | **El agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas** |
| `RN-5` | **Una orden de consola solo acepta el nombre de una cuenta que exista.** Un nombre desconocido se rechaza |
| `RN-6` | Lo registrado dice qué cuenta hizo cada acción |
| `RN-7` | **Un intento fallido no dice cuál de los dos datos estuvo mal** |

---

## 5. Modelo de datos

**Ninguna entidad propia.** Se usan las de `django.contrib.auth`:

| Qué | Dónde |
|---|---|
| Las cuentas | `auth_user`, de Django |
| Los grupos | `auth_group`: `usuario` y `agente` |
| Los permisos | `auth_permission`, y su cruce con los grupos |
| La sesión abierta | La tabla de sesiones, que ya existía |

### 5.1 Por qué acá sí hay tablas, y son ajenas

`DA-01` dice que el texto es la verdad y que los módulos calculan al pedir. **Una cuenta no está escrita en ningún documento**: es un hecho de la instalación, como las aprobaciones. Y a diferencia de aquellas, **estas tablas no se escriben acá**: las trae Django, con sus migraciones y su cifrado.

**Se borra la base y las cuentas se pierden.** Es lo segundo que no se reconstruye leyendo el proyecto, junto con las aprobaciones. Queda dicho en el manual técnico.

---

## 6. Comportamiento y flujos

| Flujo | Qué pasa |
|---|---|
| **Entrar** | Formulario de cuenta y contraseña. Si son correctas, se abre la sesión y se va a donde se iba |
| **Salir** | Se cierra la sesión y se vuelve al formulario |
| **Pedir una pantalla sin haber entrado** | Lleva al formulario, **y recuerda a dónde se iba** |
| **Pedir algo que el grupo no puede** | Responde que no, diciendo **qué permiso falta** y que lo tiene el otro grupo |
| **Crear la primera cuenta** | Por consola, en la máquina |

### 6.1 Qué se le dice a quien no logra entrar

**No se dice cuál de los dos datos estuvo mal.** Decir «esa cuenta no existe» le confirma a cualquiera qué cuentas existen. El mensaje es uno solo para los dos casos.

---

## 7. Interfaz

Una pantalla nueva, **la única que no exige haber entrado**: el formulario de entrar. Y en la barra de arriba, el nombre de la cuenta y el enlace para salir.

---

## 8. Permisos y autorización

**Es el módulo que responde esa pregunta para todos los demás.** Dos grupos:

| Acción | `usuario` | `agente` |
|---|---|---|
| Ver cualquier pantalla | Sí | Sí |
| Escribir documentos, abrir fases, llenar espacios | Sí | Sí |
| **Aprobar un documento** | **Sí** | **No** |
| **Publicar una versión de las reglas** | **Sí** | **No** |
| **Derogar una regla** | **Sí** | **No** |
| **Administrar cuentas** | **Sí** | **No** |

**El agente no aprueba lo que él mismo construyó**, y eso no es desconfianza: es `00·N1`, que pide aprobación de una persona para todo cambio de estado. Un agente que se aprobara a sí mismo volvería la aprobación un trámite.

---

## 9. Marco normativo

`00·N1` (ningún cambio de estado sin aprobación) · `00·N6` (una credencial no se escribe, no se registra y no se guarda) · `04` seguridad de la aplicación · `RNF-09`, que pide poder correr en un servidor · la sección 6 del análisis y la 8 del diseño.

---

## 10. Plan de pruebas

| Qué | Cuántas |
|---|---|
| Sin entrar no se ve nada | 8 |
| Entrar, salir y volver a donde se iba | 6 |
| Lo que el agente no puede | 6 |
| La contraseña no aparece en ninguna parte | 3 |
| Las órdenes rechazan una cuenta que no existe | 4 |
| **Total** | **27** |

---

## 11. Criterios de aceptación

| ID | Criterio | Estado |
|---|---|---|
| CA-01 | Ninguna pantalla responde sin haber entrado | ☑ |
| CA-02 | Entrar lleva a donde se iba, no a la portada | ☑ |
| CA-03 | Un intento fallido no dice cuál dato estuvo mal | ☑ |
| CA-04 | El agente no puede aprobar, publicar ni derogar | ☑ |
| CA-05 | El rechazo dice qué permiso falta | ☑ |
| CA-06 | Una orden con una cuenta que no existe se rechaza | ☑ |
| CA-07 | La contraseña no queda escrita en ningún archivo ni registro | ☑ |

---

## 12. Decisiones tomadas

| Decisión | Por qué |
|---|---|
| **El sistema de Django, no uno propio** | Escribir autenticación es la forma más común de escribirla mal |
| **Dos grupos, no cuatro** | De los cuatro actores del análisis, dos no entran: un proyecto no es una persona, y quien recibe tiene prohibido entrar |
| **El agente no aprueba** | `00·N1`: la aprobación es de una persona |
| **Las órdenes no piden contraseña** | Quien alcanza la consola ya tiene la máquina. Lo que sí se exige es que la cuenta exista |
| **El error de entrada no distingue** | Decir «esa cuenta no existe» confirma qué cuentas hay |
| **Lo registrado antes no se reescribe** | Poner una cuenta a lo que se hizo sin cuentas sería inventar quién lo hizo |

---

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-036 | RF-36 | [HU-001 Entrar con cuenta y contraseña](../epicas/EP-022-quien-entra-y-que-puede-hacer/HU-001-entrar-con-cuenta-y-contrasena/HU-001-entrar-con-cuenta-y-contrasena.md) | [AA-EP-022-HU-001-sin-entrar-no-se-ve-nada](../epicas/EP-022-quien-entra-y-que-puede-hacer/HU-001-entrar-con-cuenta-y-contrasena/AA-EP-022-HU-001-sin-entrar-no-se-ve-nada/estado-fase.md), cerrada el 2026-09-02 |
| F-037 | RF-37 | [HU-002 Separar lo que cada grupo puede hacer](../epicas/EP-022-quien-entra-y-que-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer.md) | [AB-EP-022-HU-002-el-agente-no-aprueba](../epicas/EP-022-quien-entra-y-que-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer/AB-EP-022-HU-002-el-agente-no-aprueba/estado-fase.md), cerrada el 2026-09-02 |

---

## 14. Cruces con otros módulos

| Módulo | Cómo se cruzan |
|---|---|
| [Seguridad](../seguridad/spec.md) | Son dos cosas distintas: aquel **tapa credenciales** para que no queden escritas; este **dice quién entra**. Juntos cubren `RNF-05` y el control de acceso |
| [Aprobaciones](../aprobaciones/spec.md) | `quién` deja de ser un texto libre: tiene que ser una cuenta |
| [Auditoría](../auditoria/spec.md) | Lo registrado dice qué cuenta hizo cada acción |
| [Reglas](../reglas/spec.md) | Publicar y derogar quedan fuera del alcance del agente |

---

## 15. Cambios después de aprobada

Ninguno todavía.
