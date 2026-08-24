# Mantenimiento: ¿cómo se sostiene vivo?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito qué hay que hacer para que el sistema siga sirviendo después de entregado: quién atiende, cómo entra un cambio, respaldos probados, vigilancia, qué hacer cuando falla, y cuándo se apaga. **Es la etapa más larga de todas y la que menos se planea.**

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

## 2. Los cuatro trabajos que caben acá

> Se llaman igual y cuestan distinto. Separarlos es lo que permite decir **cuánto del esfuerzo se va en apagar incendios** y cuánto en mejorar: si todo entra como «mantenimiento», nadie puede defender el presupuesto del año que viene.

| Tipo | Qué es | Ejemplo | Cuánto del esfuerzo se lleva |
|---|---|---|---|
| Corregir | Arreglar lo que está mal | «…» | «…» |
| Adaptar | Ajustarlo a un cambio de afuera, como una ley o una versión nueva | «…» | «…» |
| Mejorar | Lo que alguien pide para trabajar mejor | «…» | «…» |
| Prevenir | Lo que se hace para que no falle después | «…» | «…» |

## 3. Quién lo sostiene

| Qué actividad | Quién responde | Con qué frecuencia | Qué pasa si esa persona no está |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

**Horario de atención, y qué pasa fuera de él:** «…»

## 4. Cómo entra una solicitud, y con qué prioridad

> **Todo entra por el mismo lugar y queda escrito.** Lo que se pide de palabra no existe, y lo que no tiene prioridad acordada la define quien grita más fuerte.

| Gravedad | Qué significa | En cuánto se responde | En cuánto se resuelve |
|---|---|---|---|
| Detiene la operación | «Nadie puede trabajar» | «…» | «…» |
| Estorba, pero hay cómo seguir | «…» | «…» | «…» |
| Molesta | «…» | «…» | «…» |
| Mejora pedida | «…» | «…» | «Entra a la lista, con fecha» |

**Por dónde entra:** «…»

**Quién la clasifica:** «…»

**Quién aprueba que se haga:** «…»

## 5. Antes de tocar: qué se mira

| Qué se evalúa | Cómo queda |
|---|---|
| A qué le pega el cambio | «Qué módulos, qué datos, qué integraciones» |
| Cuánto cuesta | «…» |
| Qué se rompe si sale mal | «…» |
| Quién lo aprueba según ese impacto | «…» |

## 6. Los respaldos

> **Un respaldo que nunca se restauró no es un respaldo: es un archivo.** Lo que se escribe acá no es la configuración, es la última restauración probada.

| Qué se respalda | Cada cuánto | Dónde queda | Cuánto se conserva | Última restauración probada |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «AAAA-MM-DD, por quién» |

## 7. Qué se vigila

| Qué se mira | Cuándo se considera problema | Quién se entera, y cómo |
|---|---|---|
| «Que esté arriba» | «…» | «…» |
| «Cuánto demora en responder» | «…» | «…» |
| «Errores por hora» | «…» | «…» |
| «Espacio y memoria» | «…» | «…» |
| «Intentos de entrar que fallan» | «…» | «…» |

## 8. Qué hacer cuando falla

| Síntoma | Qué revisar primero | Cómo se arregla | A quién se avisa |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

**Qué se hace siempre, pase lo que pase:** «anotar en la bitácora qué pasó, qué se hizo y qué lo causó, aunque se haya resuelto solo.»

**Cuándo se escribe un análisis de lo que falló feo:** «…», con el molde [plantillas/postmortem.md](../../postmortem.md)

## 9. Las rutinas periódicas

| Rutina | Cada cuánto | Quién | Para qué |
|---|---|---|---|
| «Restaurar un respaldo de verdad» | «…» | «…» | «Saber que sirve, no que existe» |
| «Actualizar dependencias con fallas conocidas» | «…» | «…» | «…» |
| «Limpiar o archivar datos viejos» | «…» | «…» | «…» |
| «Revisar quién tiene acceso, y quitarle al que ya no está» | «…» | «…» | «…» |

## 10. Cómo se sube una versión de mantenimiento

| Qué se define | Cómo queda |
|---|---|
| Cada cuánto se publica | «…» |
| Qué se hace con lo urgente que no puede esperar | «…» |
| Cómo se numeran las versiones | «…» |
| Qué se le dice a quien usa | «…» |

## 11. Qué se mide, y a quién se le reporta

| Qué se mide | Cada cuánto | A quién se le reporta |
|---|---|---|
| «Solicitudes recibidas, atendidas y pendientes» | «…» | «…» |
| «Cuánto se demora en responder y en resolver» | «…» | «…» |
| «Tiempo fuera de servicio» | «…» | «…» |
| «Qué proporción del esfuerzo se fue en corregir» | «…» | «…» |

## 12. Cómo se pide un cambio grande

> Un cambio que agrega alcance no se hace porque alguien lo pida en una conversación: **vuelve a entrar por planificación**. El ciclo es un anillo.

| Quién pide | Por dónde entra | Quién decide | Qué se le responde |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 13. El fin de vida

| Qué se define | Cómo queda |
|---|---|
| Cuándo se apaga | «Qué tiene que pasar para que deje de valer la pena sostenerlo» |
| Qué pasa con los datos | «Quién se los queda, en qué formato, por cuánto tiempo» |
| A quién se avisa, y con cuánta anticipación | «…» |
| Qué lo reemplaza, si algo lo reemplaza | «…» |

## 14. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual técnico y de operación | [plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md](../../ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md) | Quien opera | «…» |
| Bitácora de operación | [plantillas/ciclo-vida-proyectos/21-bitacora-de-operacion.md](../../ciclo-vida-proyectos/21-bitacora-de-operacion.md) | Quien opera | «…» |
| Plan de mantenimiento | [plantillas/ciclo-vida-proyectos/22-plan-de-mantenimiento.md](../../ciclo-vida-proyectos/22-plan-de-mantenimiento.md) | Cliente y equipo | «…» |
| Análisis de lo que falló feo | [plantillas/postmortem.md](../../postmortem.md) | Equipo | «Cuando ocurra» |
| Reporte de operación | Sección 11 de este documento | Cliente | «…» |
| Acuerdo de niveles de atención | Sección 4 de este documento | Cliente, se acuerda | «…» |

## 15. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Dar el sistema por operable | haya una restauración de respaldo probada | Sección 6 de este documento |
| Tocar producción por una solicitud | esté registrada, clasificada y aprobada | Secciones 4 y 5 |
| Cerrar un incidente | quede escrito en la bitácora qué lo causó | Sección 8 de este documento |
| Hacer un cambio que agranda el alcance | entre por planificación como trabajo nuevo | Sección 12 de este documento |

## 16. La revisión de esta etapa

**Se revisa cada «…».** Última revisión: «AAAA-MM-DD», por «quién».

«Qué cambió desde la anterior, y qué de este documento dejó de ser cierto.»
