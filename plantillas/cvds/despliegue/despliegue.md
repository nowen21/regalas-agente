# Etapa 6: Despliegue

Sexta etapa del ciclo de vida del desarrollo de software (SDLC). Lleva el sistema aprobado al ambiente de producción y lo pone a disposición de los usuarios reales. Es la etapa de mayor riesgo operativo del proyecto: los errores aquí afectan directamente al negocio.

---

## 1. Actividades que se realizan

### 1.1 Planificar el despliegue
1. Define la fecha y la ventana horaria, preferiblemente en el período de menor uso del sistema
2. Determina la estrategia de despliegue (ver sección 2)
3. Establece la duración estimada y el punto de no retorno
4. Asigna roles: quién ejecuta, quién valida, quién autoriza el retroceso
5. Define los canales de comunicación durante la ventana y los tiempos de reporte
6. Notifica con anticipación a usuarios, mesa de ayuda y áreas afectadas

### 1.2 Preparar la infraestructura
1. Aprovisiona servidores, almacenamiento y red según la especificación del diseño
2. Instala el sistema operativo, el motor de base de datos y los servicios base con las versiones exactas validadas en pruebas
3. Configura balanceadores, certificados TLS, dominios y reglas de firewall
4. Habilita el monitoreo, la recolección de logs y las alertas antes del despliegue, no después
5. Configura los respaldos automáticos y verifica que la restauración funcione

### 1.3 Preparar el plan de reversión (rollback)
Antes de tocar producción, deja escrito y probado:
- Cómo se revierte la aplicación a la versión anterior
- Cómo se revierten los cambios de esquema de base de datos
- Cuál es el tiempo máximo de recuperación aceptable
- Quién tiene autoridad para ordenar la reversión y bajo qué criterio

Un despliegue sin plan de reversión probado no debe autorizarse.

### 1.4 Ejecutar la lista de verificación previa (pre-deployment checklist)
- El acta de aceptación está firmada
- El artefacto a desplegar es exactamente el mismo que se probó y aprobó
- Existe un respaldo completo y verificado de la base de datos y de la versión actual
- Las variables de entorno y credenciales de producción están configuradas
- Los certificados y licencias están vigentes
- El personal de soporte está disponible durante y después de la ventana
- El plan de reversión está probado

### 1.5 Migrar los datos
Cuando se reemplaza un sistema existente:
1. Extrae los datos del sistema anterior
2. Limpia inconsistencias, duplicados y registros huérfanos
3. Transforma los datos al nuevo modelo
4. Ejecuta una migración de ensayo en preproducción y mide su duración
5. Valida integridad: conteo de registros, sumas de control y muestreo manual
6. Congela el sistema anterior antes de la migración definitiva
7. Ejecuta la migración final y vuelve a validar
8. Conserva el sistema anterior en modo consulta durante un período definido

### 1.6 Desplegar la aplicación
1. Activa el modo de mantenimiento si la estrategia lo requiere
2. Ejecuta los scripts de migración de esquema de base de datos
3. Publica el artefacto de la aplicación
4. Aplica la configuración específica de producción
5. Reinicia los servicios en el orden correcto de dependencias
6. Desactiva el modo de mantenimiento

### 1.7 Verificar después del despliegue (smoke test en producción)
1. Confirma que la aplicación responde y que la versión publicada es la correcta
2. Verifica la conexión a la base de datos y a los servicios externos
3. Ejecuta las transacciones críticas del negocio de extremo a extremo
4. Revisa que los logs no muestren errores nuevos
5. Comprueba tiempos de respuesta, uso de CPU y memoria contra la línea base
6. Valida que los procesos programados y las integraciones funcionen

### 1.8 Capacitar a los usuarios
1. Identifica los perfiles de usuario y el nivel de detalle que requiere cada uno
2. Ejecuta las sesiones de capacitación antes o inmediatamente después de la salida a producción
3. Entrega manuales de usuario y material de apoyo
4. Forma a los usuarios clave que servirán de primer punto de contacto en cada área
5. Capacita a la mesa de ayuda en los incidentes previsibles

### 1.9 Acompañar la puesta en marcha (hypercare)
1. Mantén al equipo de desarrollo disponible durante los primeros días
2. Monitorea métricas y logs con frecuencia elevada
3. Atiende los incidentes con prioridad máxima y tiempos de respuesta acordados
4. Registra las incidencias para alimentar la etapa de mantenimiento
5. Define la duración del período de acompañamiento y su criterio de terminación

### 1.10 Transferir a operación
1. Entrega la documentación operativa al área de soporte e infraestructura
2. Formaliza el traspaso de responsabilidades con acta firmada
3. Establece los niveles de servicio (SLA) para la atención posterior
4. Cierra el proyecto formalmente y libera al equipo

---

## 2. Estrategias de despliegue

| Estrategia | Cómo funciona | Cuándo conviene |
|---|---|---|
| **Big bang** | Se reemplaza todo el sistema de una vez | Sistemas pequeños, sin operación crítica continua |
| **Por fases** | Se libera módulo por módulo o área por área | Sistemas grandes, permite corregir sobre la marcha |
| **Paralelo** | El sistema nuevo y el anterior operan a la vez | Sistemas críticos, permite comparar resultados; duplica el esfuerzo operativo |
| **Piloto** | Se libera a un grupo reducido antes de extenderlo | Cuando hay incertidumbre sobre la adopción del usuario |
| **Blue-green** | Dos ambientes idénticos; se conmuta el tráfico al nuevo | Requiere reversión inmediata; duplica infraestructura |
| **Canary** | Se dirige un porcentaje creciente de tráfico a la nueva versión | Detectar fallos con impacto limitado antes del alcance total |
| **Rolling** | Se actualizan los nodos por lotes, sin detener el servicio | Arquitecturas con múltiples instancias |

---

## 3. Documentos que se elaboran

1. **Plan de despliegue** — Documento central: estrategia, cronograma, ventana, responsables y secuencia de pasos.

2. **Lista de verificación previa y posterior** — Puntos de control obligatorios antes y después de la ejecución.

3. **Plan de reversión (rollback)** — Procedimiento paso a paso para volver a la versión anterior.

4. **Manual de instalación y configuración** — Instrucciones reproducibles para levantar el sistema desde cero.

5. **Documento de arquitectura de infraestructura** — Servidores, red, dominios, certificados y dependencias externas.

6. **Plan de migración de datos** — Origen, transformaciones, validaciones y criterios de aceptación de la migración.

7. **Informe de migración de datos** — Registros procesados, rechazados y resultado de la validación de integridad.

8. **Manual de usuario** — Guía funcional por perfil, con capturas y flujos de trabajo.

9. **Manual de operación (runbook)** — Procedimientos rutinarios, arranque y parada de servicios, tareas programadas.

10. **Guía de resolución de incidentes** — Errores conocidos, su diagnóstico y su solución.

11. **Plan de respaldo y recuperación** — Frecuencia, retención, ubicación y procedimiento de restauración.

12. **Plan de capacitación y material de formación** — Agenda, contenidos, asistentes y evaluación.

13. **Notas de versión (release notes)** — Funcionalidades incluidas, correcciones y defectos conocidos.

14. **Bitácora del despliegue** — Registro cronológico de cada paso ejecutado, con hora, responsable y resultado.

15. **Acta de puesta en producción** — Constancia formal de que el sistema entró en operación.

16. **Acta de cierre del proyecto** — Cumplimiento de alcance, cronograma y presupuesto; lecciones aprendidas.

---

## 4. Documentos que se entregan formalmente

### Al cliente o patrocinador (requieren firma)
- Plan de despliegue, aprobado antes de la ejecución
- **Acta de puesta en producción** — Entregable clave de la etapa
- Informe de migración de datos
- Notas de versión con los defectos conocidos
- Acta de cierre del proyecto

### A los usuarios finales
- Manual de usuario por perfil
- Material de capacitación y guías rápidas
- Canal y procedimiento para reportar incidentes

### Al área de operación e infraestructura
- Manual de instalación y configuración
- Manual de operación (runbook)
- Documento de arquitectura de infraestructura
- Plan de respaldo y recuperación
- Plan de reversión
- Credenciales y accesos, entregados por canal seguro

### A la mesa de ayuda y soporte
- Guía de resolución de incidentes
- Listado de defectos conocidos que pasaron a producción
- Acuerdos de nivel de servicio (SLA)
- Rutas de escalamiento con responsables y contactos

### Al equipo de mantenimiento
- Código fuente, repositorio y documentación técnica completa
- Registro de deuda técnica
- Backlog de requisitos aplazados y defectos residuales

---

## 5. Hito de cierre de la etapa

La etapa termina con el **acta de puesta en producción firmada** y la transferencia formal a operación, una vez cumplidas estas condiciones:

- El sistema opera en producción y las transacciones críticas fueron verificadas
- Los datos migrados pasaron la validación de integridad
- Los usuarios están capacitados
- La documentación operativa fue entregada y aceptada
- El período de acompañamiento (hypercare) terminó sin incidentes críticos abiertos
- Los SLA de soporte están vigentes

Desde ese punto, toda solicitud nueva o corrección entra por la etapa de mantenimiento.

---

## 6. Errores frecuentes en esta etapa

- Desplegar sin un plan de reversión probado y descubrir en plena falla que no se sabe cómo volver atrás
- Desplegar un artefacto distinto al que se probó y aprobó
- Configurar producción a mano en lugar de usar scripts reproducibles
- Omitir el respaldo previo o no verificar que la restauración realmente funcione
- Migrar datos sin ensayo previo y descubrir en la ventana real que el proceso tarda el triple
- Habilitar el monitoreo después del despliegue, quedando ciego durante las horas más críticas
- Desplegar un viernes por la tarde o antes de un período de ausencia del equipo
- Capacitar a los usuarios semanas antes y llegar a la salida con todo olvidado
- Entregar a soporte sin documentación operativa ni listado de defectos conocidos
- Dar el proyecto por terminado el día del despliegue, sin período de acompañamiento
- Mantener el sistema anterior apagado sin período de consulta, perdiendo la posibilidad de verificar históricos
