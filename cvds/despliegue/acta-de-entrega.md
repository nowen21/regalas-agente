# Acta de entrega   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja constancia de **qué se entregó, a quién, con qué evidencia y con qué salvedades**. Es el documento que cierra el ciclo hacia afuera.

---

## 1. Qué se entrega, y a quién

| Campo | Valor |
|---|---|
| **Producto** | Cimiento: el cuerpo de reglas heredable, y la plataforma que lo administra |
| **Versión del cuerpo de reglas** | 37.2.2 |
| **Versión del producto** | 5, la última del plan |
| **Fecha de esta acta** | 2026-09-02 |
| **Quien entrega** | Ing. José Dúmar Jiménez Ruíz, con el agente |
| **Quien recibe** | **Ing. José Dúmar Jiménez Ruíz** |

> **Esto es lo primero que hay que decir, y no se disimula: quien entrega y quien recibe son la misma persona.** Cimiento no se le ha entregado a nadie más. Corre en la máquina de quien lo escribió y no ha tenido otro usuario. Un acta de entrega firmada de ida y vuelta por la misma persona **no prueba que el producto sirva**: prueba que está terminado y que se sabe qué es. Eso es lo que este documento certifica, y nada más.

---

## 2. Qué entra en la entrega

| Componente | Dónde | Estado |
|---|---|---|
| El cuerpo de reglas | `base/` | 257 reglas, versión 37.2.2 |
| Los moldes del ciclo | `plantillas/` | 22 moldes |
| Los validadores | `validadores/` | 32 comprobaciones · 733 pruebas |
| La plataforma | `plataforma/` | 13 módulos · 571 pruebas |
| La documentación | `documentacion/` y `cvds/` | 1290 documentos en el expediente |

---

## 3. Con qué evidencia

| Qué se afirma | Cómo se comprueba | Resultado el 2026-09-02 |
|---|---|---|
| Las funcionalidades están construidas | `python manage.py estado_funcionalidades <proyecto>` | **35 de 35** |
| Cada una tiene veredicto | La misma orden | **35 verificadas · 0 que no cumplen** |
| Las pruebas están en verde | `python manage.py test` y `validar.py internas` | **571 + 733, sin fallas** |
| El estándar no se contradice | `validar.py todo` | **32 comprobaciones, 0 fallas** |
| El expediente está completo | `python manage.py armar_expediente <proyecto>` | **0 documentos faltantes** |

**Nada de esta tabla se escribió a mano.** Cada fila sale de correr la orden que dice al lado, y quien reciba puede volver a correrla.

---

## 4. Salvedades — qué NO se está entregando

**Se declaran acá, y no en una nota al pie, porque son las que cambiarían la decisión de alguien que reciba esto de verdad.**

| Salvedad | Alcance |
|---|---|
| **Verificada quiere decir que la fase cerró con veredicto «Cumple»** | No que alguien de afuera haya auditado nada. Nadie ajeno ha revisado este producto |
| **Seis módulos no tienen pantalla** | Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén se operan por consola |
| **Nada se cambia desde la pantalla** | Los cambios de estado van por consola, con su confirmación |
| **El control de acceso ya está construido** | Se levantó el aplazamiento el 2026-09-02 y se construyó con `django.contrib.auth`: cuentas, dos grupos y permisos. **Lo que no tiene es límite de intentos** al entrar, ni recuperación de contraseña |
| **No está puesta en ningún servidor** | Corre en la máquina de quien la usa, y el diseño no contempla otra cosa |
| **33 fases tienen su frase y su tabla en desacuerdo** | Son fases cerradas, y arreglarlas sería reescribirlas |
| **La medición inicial no existe** | El objetivo del proyecto era reducir el tiempo de revisión, y **no hay un antes contra el cual comparar**: debió tomarse antes de empezar y no se tomó |

---

## 5. Qué queda pendiente por parte de quien recibe

- **Correr las dos baterías** en su propia máquina antes de confiar en la tabla del punto 3.
- **Conectar un proyecto propio** y traerlo: es lo que muestra si el estándar sirve fuera de su propio repositorio.
- **Tomar una medición inicial** si va a querer demostrar una mejora. Es lo único de esta lista que no se puede hacer después.

---

## 6. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Quien entrega | Ing. José Dúmar Jiménez Ruíz | ☑ 2026-09-02 |
| Quien recibe | Ing. José Dúmar Jiménez Ruíz | ☐ pendiente de su firma |

> **La firma de recibido queda en blanco a propósito.** Marcarla desde acá sería que el agente firme por el usuario, y una aprobación que no dio una persona no es una aprobación.
