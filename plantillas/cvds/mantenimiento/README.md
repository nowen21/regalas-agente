# Mantenimiento: ¿cómo se sostiene vivo?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito qué hay que hacer para que el sistema siga sirviendo después de entregado: respaldos probados, vigilancia, qué hacer cuando falla, y cuándo se apaga. **Es la etapa más larga de todas y la que menos se planea.**

> Plantilla. Se llena antes de la primera entrega, no después, y se revisa cada vez que el sistema cambia. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / VIGENTE»** («AAAA-MM-DD»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Lo entregado, con su acta | Despliegue | «…» |
| La deuda declarada y los defectos aceptados | Implementación y pruebas | «…» |
| Las exigencias de disponibilidad y de datos | Análisis | «…» |

## 2. Quién lo sostiene

| Qué actividad | Quién responde | Con qué frecuencia | Qué pasa si esa persona no está |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 3. Los respaldos

> **Un respaldo que nunca se restauró no es un respaldo: es un archivo.** Lo que se escribe acá no es la configuración, es la última restauración probada.

| Qué se respalda | Cada cuánto | Dónde queda | Cuánto se conserva | Última restauración probada |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «AAAA-MM-DD, por quién» |

## 4. Qué se vigila

| Qué se mira | Cuándo se considera problema | Quién se entera, y cómo |
|---|---|---|
| «…» | «…» | «…» |

## 5. Qué hacer cuando falla

| Síntoma | Qué revisar primero | Cómo se arregla | A quién se avisa |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

**Qué se hace siempre, pase lo que pase:** «anotar en la bitácora qué pasó, qué se hizo y qué lo causó, aunque se haya resuelto solo.»

## 6. Las rutinas periódicas

| Rutina | Cada cuánto | Quién | Para qué |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 7. Cómo se pide un cambio

> Después de entregado, un cambio no se hace porque alguien lo pida en una conversación: **vuelve a entrar por planificación**. El ciclo es un anillo.

| Quién pide | Por dónde entra | Quién decide | Qué se le responde |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 8. El fin de vida

| Qué se define | Cómo queda |
|---|---|
| Cuándo se apaga | «Qué tiene que pasar para que deje de valer la pena sostenerlo» |
| Qué pasa con los datos | «Quién se los queda, en qué formato, por cuánto tiempo» |
| A quién se avisa, y con cuánta anticipación | «…» |

## 9. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual técnico y de operación | [plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md](../../ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md) | Quien opera | «…» |
| Bitácora de operación | [plantillas/ciclo-vida-proyectos/21-bitacora-de-operacion.md](../../ciclo-vida-proyectos/21-bitacora-de-operacion.md) | Quien opera | «…» |
| Plan de mantenimiento | [plantillas/ciclo-vida-proyectos/22-plan-de-mantenimiento.md](../../ciclo-vida-proyectos/22-plan-de-mantenimiento.md) | Cliente y equipo | «…» |
| Análisis de lo que falló feo | [plantillas/postmortem.md](../../postmortem.md) | Equipo | «Cuando ocurra» |

## 10. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Dar el sistema por operable | haya una restauración de respaldo probada | Sección 3 de este documento |
| Cerrar un incidente | quede escrito en la bitácora qué lo causó | Sección 5 de este documento |
| Hacer un cambio pedido | entre por planificación como trabajo nuevo | Sección 7 de este documento |

## 11. La revisión de esta etapa

**Se revisa cada «…».** Última revisión: «AAAA-MM-DD», por «quién».

«Qué cambió desde la anterior, y qué de este documento dejó de ser cierto.»
