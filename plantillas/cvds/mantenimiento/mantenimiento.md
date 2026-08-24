# Etapa 7: Mantenimiento

Séptima y última etapa del ciclo de vida del desarrollo de software (SDLC). Comienza cuando el sistema entra en operación y se extiende hasta su retiro definitivo. Es la etapa más larga del ciclo y la que consume entre el 60 % y el 80 % del costo total del software a lo largo de su vida útil.

A diferencia de las etapas anteriores, no termina con un entregable: opera como un ciclo continuo.

---

## 1. Tipos de mantenimiento

Clasificación según el estándar ISO/IEC 14764:

| Tipo | Qué resuelve | Proporción típica |
|---|---|---|
| **Correctivo** | Defectos detectados en operación que impiden el funcionamiento esperado | ~20 % |
| **Adaptativo** | Cambios del entorno: nuevas versiones de sistema operativo, navegadores, motores de base de datos, normativas o integraciones externas | ~25 % |
| **Perfectivo** | Mejoras de funcionalidad, usabilidad o rendimiento solicitadas por los usuarios | ~50 % |
| **Preventivo** | Refactorización, reducción de deuda técnica y ajustes para evitar fallas futuras | ~5 % |

El mantenimiento perfectivo es el mayoritario: la mayor parte del trabajo posterior a la entrega no es corregir errores, sino evolucionar el sistema.

---

## 2. Actividades que se realizan

### 2.1 Recibir y registrar solicitudes
1. Establece un único canal formal de entrada (mesa de ayuda, sistema de tickets)
2. Registra cada solicitud con: solicitante, fecha, descripción, evidencia y área afectada
3. Clasifica la solicitud como incidente (algo falla), requerimiento (algo nuevo) o consulta
4. Rechaza las solicitudes que lleguen por canales informales; sin registro no hay trazabilidad

### 2.2 Clasificar y priorizar
Asigna a cada solicitud:
- **Tipo** de mantenimiento (correctivo, adaptativo, perfectivo, preventivo)
- **Severidad**: impacto técnico y operativo
- **Prioridad**: urgencia para el negocio
- **SLA aplicable**: tiempo máximo de respuesta y de solución

Escala de severidad habitual:

| Nivel | Definición | Respuesta típica |
|---|---|---|
| Crítica | El sistema no opera o hay pérdida de datos | Inmediata, 24/7 |
| Alta | Función crítica degradada, sin solución alterna | Mismo día hábil |
| Media | Función afectada con solución alterna disponible | 2 a 5 días hábiles |
| Baja | Detalle cosmético o mejora menor | Siguiente versión programada |

### 2.3 Analizar el impacto
Antes de tocar el código, para cada cambio:
1. Identifica los módulos, tablas e integraciones afectadas
2. Consulta la matriz de trazabilidad para ubicar los requisitos relacionados
3. Estima el esfuerzo en horas y el costo
4. Evalúa el riesgo de regresión
5. Determina si el cambio requiere ventana de indisponibilidad
6. Presenta el resultado al comité de control de cambios

### 2.4 Aprobar mediante control de cambios
Ninguna modificación entra a producción sin pasar por el procedimiento formal:
1. El solicitante presenta la petición de cambio (RFC)
2. El equipo técnico entrega el análisis de impacto
3. El comité aprueba, rechaza o aplaza
4. Se programa en una versión (release) específica
5. Se comunica la decisión al solicitante

### 2.5 Implementar el cambio
1. Reproduce el problema en un ambiente de desarrollo antes de corregirlo
2. Identifica la causa raíz; no apliques parches sobre el síntoma
3. Modifica el código siguiendo los mismos estándares de la etapa de implementación
4. Actualiza o crea las pruebas unitarias correspondientes
5. Somete el cambio a revisión de pares
6. Actualiza la documentación técnica afectada

### 2.6 Probar el cambio
1. Verifica que el defecto quedó resuelto o que la mejora funciona
2. **Ejecuta la suite completa de regresión** — Es el paso más importante del mantenimiento; un cambio pequeño puede romper funcionalidad no relacionada
3. Prueba en un ambiente equivalente al de producción
4. Obtén la validación del usuario solicitante cuando el cambio sea funcional

### 2.7 Desplegar la versión
1. Agrupa los cambios aprobados en versiones planificadas, salvo las correcciones críticas
2. Aplica el mismo procedimiento y lista de verificación de la etapa de despliegue
3. Prepara el plan de reversión específico para esa versión
4. Publica las notas de versión antes de la salida
5. Verifica en producción y monitorea el comportamiento posterior

### 2.8 Monitorear la operación
De forma permanente:
- Disponibilidad del sistema y de sus integraciones
- Tiempos de respuesta contra la línea base
- Consumo de CPU, memoria y almacenamiento
- Crecimiento del volumen de datos y proyección de capacidad
- Errores en logs y su frecuencia
- Ejecución de procesos programados
- Éxito de los respaldos automáticos

Configura alertas con umbrales definidos; no dependas de que el usuario reporte la caída.

### 2.9 Ejecutar mantenimiento preventivo
De forma programada:
- Actualiza dependencias, librerías y parches de seguridad
- Refactoriza los módulos con mayor deuda técnica registrada
- Depura datos históricos según la política de retención
- Reindexa y optimiza la base de datos
- Prueba la restauración de respaldos; un respaldo no verificado no es un respaldo
- Revisa y renueva certificados y licencias antes de su vencimiento
- Ejecuta análisis de vulnerabilidades periódico

### 2.10 Gestionar la configuración y las versiones
- Mantén todo el código y los scripts bajo control de versiones
- Aplica versionado semántico (MAYOR.MENOR.PARCHE)
- Etiqueta en el repositorio cada versión desplegada en producción
- Conserva el historial de qué versión estuvo activa en cada período

### 2.11 Medir y reportar
Indicadores del servicio de mantenimiento:
- Tickets recibidos, resueltos y pendientes por período
- Cumplimiento de SLA por nivel de severidad
- Tiempo medio de respuesta y de resolución (MTTR)
- Tiempo medio entre fallas (MTBF)
- Disponibilidad del sistema en porcentaje
- Tasa de reapertura de tickets
- Defectos introducidos por versión (indicador de calidad del propio mantenimiento)

### 2.12 Planificar el retiro del sistema
Cuando el sistema llega al final de su vida útil:
1. Evalúa si conviene reemplazarlo, migrarlo o reconstruirlo
2. Define la fecha de fin de soporte y comunícala con anticipación
3. Planifica la migración de datos al sistema sucesor
4. Establece la política de archivo y retención de datos históricos
5. Ejecuta el retiro y documenta el cierre

---

## 3. Documentos que se elaboran

1. **Plan de mantenimiento** — Alcance del servicio, tipos cubiertos, horarios, equipo asignado y procedimientos.

2. **Acuerdo de Nivel de Servicio (SLA)** — Tiempos de respuesta y solución comprometidos por nivel de severidad, disponibilidad garantizada y penalizaciones.

3. **Registro de incidentes** — Bitácora de cada falla reportada, su diagnóstico, solución y tiempo de atención.

4. **Peticiones de cambio (RFC)** — Una por cada solicitud de modificación, con su análisis de impacto.

5. **Informe de análisis de impacto** — Módulos afectados, esfuerzo, costo y riesgo por cada cambio.

6. **Actas del comité de control de cambios** — Decisiones de aprobación, rechazo o aplazamiento.

7. **Registro de cambios (changelog)** — Historial acumulado de todo lo modificado, versión por versión.

8. **Notas de versión (release notes)** — Contenido de cada entrega: mejoras, correcciones y defectos conocidos.

9. **Documentación técnica actualizada** — ERS, SDD, diccionario de datos y diagramas, mantenidos vigentes.

10. **Manuales de usuario y de operación actualizados** — Reflejan el sistema tal como está hoy, no como se entregó.

11. **Registro de deuda técnica** — Concesiones pendientes, su impacto y el plan de pago.

12. **Informe de monitoreo y disponibilidad** — Métricas del período con comparación contra el SLA.

13. **Informe de indicadores del servicio** — Reporte periódico de los KPI listados arriba.

14. **Bitácora de mantenimiento preventivo** — Actualizaciones, respaldos verificados y optimizaciones ejecutadas.

15. **Base de conocimiento** — Soluciones documentadas de los incidentes recurrentes, para reducir el tiempo de resolución.

16. **Plan de retiro del sistema** — Cronograma, migración de datos y política de archivo, al final de la vida útil.

---

## 4. Documentos que se entregan formalmente

### Al cliente o patrocinador
- Plan de mantenimiento y SLA firmado
- Informe periódico de indicadores y cumplimiento del SLA
- Notas de versión de cada entrega
- Actas del comité de control de cambios
- Cotización y aprobación de los cambios que excedan el contrato de soporte

### A los usuarios finales
- Notas de versión en lenguaje funcional
- Manuales actualizados
- Comunicados de ventanas de mantenimiento programadas

### A la mesa de ayuda y soporte
- Base de conocimiento actualizada
- Guía de resolución de incidentes
- Listado vigente de defectos conocidos
- Rutas de escalamiento

### Al equipo técnico
- Documentación técnica actualizada
- Registro de deuda técnica
- Registro de cambios detallado
- Bitácora de mantenimiento preventivo
- Informes de monitoreo

---

## 5. Cierre del ciclo

El mantenimiento no tiene un hito de cierre como las etapas anteriores. Opera de forma continua hasta el **retiro del sistema**, formalizado con:

- Acta de fin de soporte
- Constancia de migración de datos al sistema sucesor
- Certificado de archivo o destrucción de datos según la política de retención
- Informe final del ciclo de vida completo

Cabe notar que cada cambio significativo dentro del mantenimiento reproduce internamente el ciclo completo: se analiza, se diseña, se codifica, se prueba y se despliega. Por eso el SDLC se representa como un ciclo y no como una línea recta.

---

## 6. Errores frecuentes en esta etapa

- Corregir el síntoma sin buscar la causa raíz, generando reincidencia del mismo incidente
- Omitir las pruebas de regresión porque "el cambio era mínimo"
- Modificar directamente en producción sin pasar por desarrollo ni pruebas
- Aceptar solicitudes por canales informales, sin ticket ni trazabilidad
- No actualizar la documentación, hasta que ningún documento refleja el sistema real
- Ignorar el mantenimiento preventivo hasta que la deuda técnica bloquea cualquier cambio
- Acumular versiones de librerías sin actualizar y quedar expuesto a vulnerabilidades conocidas
- Confiar en respaldos que nunca se probaron al restaurar
- No medir indicadores y quedar sin argumentos para justificar el equipo de soporte
- Perder al equipo original sin transferir conocimiento, dejando un sistema que nadie entiende
- Confundir mantenimiento perfectivo con desarrollo nuevo y absorberlo sin presupuesto ni cronograma
- Extender indefinidamente la vida de un sistema obsoleto por evitar el costo del reemplazo
