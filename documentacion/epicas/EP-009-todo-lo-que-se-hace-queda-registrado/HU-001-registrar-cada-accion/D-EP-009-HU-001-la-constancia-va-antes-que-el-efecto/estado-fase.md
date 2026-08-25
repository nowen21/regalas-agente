# Estado de fase - D-EP-009-HU-001: la constancia va antes que el efecto   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Auditoría |
| **Épica / HU** | [EP-009](../../epica.md) · [HU-001](../HU-001-registrar-cada-accion.md) |
| **Versión del producto** | 1, fase D de siete |
| **Última actualización** | 2026-08-25 |

---

## 1. En qué estación va

**Estación actual:** 4, pausa y presentación. **Última puerta pasada:** 3.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | La historia aprobada y la fase abierta | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados, esperando lectura | ☐ |
| 5 | Aprobación del plan detallado | 👤 Falta | ☐ |
| 6 | Ejecución continua | El registro escribe, tapa y enlaza | ☐ |
| 7 | Pruebas | Los siete casos con veredicto | ☐ |
| 8 | Cierre de la fase | Documento de cierre, con su deuda | ☐ |
| 9 | Commit único | 👤 Aprobación aparte para guardar | ☐ |

---

## 2. Qué falta para avanzar

**Que el usuario lea los dos planes, y decida las dos dudas.** Son estas:

1. **Cómo llega el enmascarador del estándar a la plataforma:** se importa desde `validadores/`, o se mueve a un sitio que las dos usen. Copiarlo está descartado, porque deja dos listas de secretos que se separan.
2. **Qué identifica una sesión**, para poder enlazarla desde el registro.

Ninguna se decide sin el usuario: la primera puede terminar tocando el estándar, y la segunda fija un dato que después no se cambia sin reescribir lo registrado.

---

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Por qué esta fase va antes que la B | El orden aprobado en la etapa 4: registrar desde el primer día evita un tramo sin historia |
| Cómo se rompe la dependencia con Proyectos | Una acción sin proyecto se registra igual, con el campo vacío |
| Cómo se guarda | Texto que solo se agrega, con lo que la fase A ya construyó |
| Qué se prueba | Siete casos, incluido uno de lo que NO debe pasar: que algo cambie sin quedar registrado |
