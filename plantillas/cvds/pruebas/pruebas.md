# Etapa 5: Pruebas

Quinta etapa del ciclo de vida del desarrollo de software (SDLC). Verifica que el sistema construido cumpla los requisitos aprobados y detecta los defectos antes de que lleguen a producción. No busca demostrar que el software funciona, sino encontrar en qué condiciones falla.

---

## 1. Niveles de prueba

Se ejecutan en este orden, de lo más pequeño a lo más completo:

### 1.1 Pruebas unitarias
Verifican cada función, método o clase de forma aislada. Las escribe el desarrollador durante la implementación. Se usan objetos simulados (*mocks*) para eliminar dependencias externas.

### 1.2 Pruebas de integración
Verifican que los módulos se comuniquen correctamente entre sí y con recursos externos (base de datos, APIs de terceros, servicios de correo). Aquí aparecen los fallos de contrato entre componentes.

### 1.3 Pruebas de sistema
Verifican el sistema completo contra el ERS, en un ambiente equivalente al de producción. Cubren tanto los requisitos funcionales como los no funcionales.

### 1.4 Pruebas de aceptación (UAT)
Las ejecuta el cliente o los usuarios finales con datos reales. Determinan si el sistema resuelve la necesidad del negocio y si se acepta la entrega.

---

## 2. Tipos de prueba

### 2.1 Pruebas funcionales
Verifican **qué** hace el sistema:

| Tipo | Qué comprueba |
|---|---|
| De humo (*smoke*) | El build es estable y las funciones críticas responden; se corre antes de todo lo demás |
| De regresión | Lo que antes funcionaba sigue funcionando tras un cambio |
| De caja negra | El comportamiento externo, sin conocer el código interno |
| De caja blanca | Los caminos internos del código, la lógica y las condiciones |
| De casos límite | Valores frontera: cero, negativos, máximos, campos vacíos |
| Exploratorias | Búsqueda libre de fallos sin guion previo, basada en la experiencia del tester |

### 2.2 Pruebas no funcionales
Verifican **cómo** se comporta el sistema:

| Tipo | Qué comprueba |
|---|---|
| De rendimiento | Tiempos de respuesta bajo la carga esperada |
| De carga | Comportamiento con el número de usuarios concurrentes previsto |
| De estrés | Punto de quiebre al superar el límite previsto y cómo se recupera |
| De volumen | Manejo de grandes cantidades de datos acumulados |
| De seguridad | Inyección SQL, XSS, CSRF, escalamiento de privilegios, exposición de datos |
| De usabilidad | Facilidad de uso, claridad de mensajes, curva de aprendizaje |
| De compatibilidad | Navegadores, sistemas operativos, resoluciones y dispositivos |
| De accesibilidad | Cumplimiento de WCAG, uso con lector de pantalla y solo teclado |
| De recuperación | Restauración tras caída, corte de red o falla de energía |
| De instalación | El sistema se instala y desinstala correctamente en un entorno limpio |

---

## 3. Actividades que se realizan

### 3.1 Planificar las pruebas
1. Define el alcance: qué se prueba y qué queda explícitamente fuera
2. Selecciona los niveles y tipos aplicables según los requisitos no funcionales del ERS
3. Determina los criterios de entrada (cuándo se puede empezar) y de salida (cuándo se puede terminar)
4. Asigna recursos, roles y cronograma
5. Identifica los riesgos de la etapa y su mitigación

### 3.2 Diseñar los casos de prueba
Para cada requisito del ERS, escribe uno o más casos con esta estructura:

- **ID** del caso (CP-001)
- **Requisito asociado** (RF-08)
- **Objetivo** de la prueba
- **Precondiciones** necesarias
- **Datos de entrada**
- **Pasos** numerados a ejecutar
- **Resultado esperado**
- **Prioridad**

Usa técnicas formales para no depender de la intuición:
- **Partición de equivalencia** — Agrupa entradas que el sistema trata igual y prueba una de cada grupo
- **Análisis de valores límite** — Prueba justo debajo, en y justo arriba de cada frontera
- **Tabla de decisión** — Combina condiciones cuando hay reglas de negocio con múltiples variables
- **Transición de estados** — Recorre el ciclo de vida de las entidades con estados

### 3.3 Preparar el ambiente y los datos
1. Levanta un ambiente separado, equivalente al de producción en versiones y configuración
2. Genera un juego de datos de prueba representativo, incluyendo casos límite
3. Anonimiza cualquier dato tomado de producción
4. Documenta cómo restaurar el ambiente a su estado inicial entre ciclos

### 3.4 Ejecutar las pruebas
1. Corre primero las pruebas de humo; si fallan, devuelve el build sin continuar
2. Ejecuta los casos según su prioridad
3. Registra el resultado de cada caso: aprobado, fallido o bloqueado
4. Documenta cada defecto de inmediato, con evidencia

### 3.5 Reportar y gestionar defectos
Cada defecto se registra con:
- ID, título y descripción
- Pasos exactos para reproducirlo
- Resultado esperado contra resultado obtenido
- Evidencia: captura de pantalla, video, log
- Ambiente y versión donde ocurre
- **Severidad**: impacto técnico (crítica, alta, media, baja)
- **Prioridad**: urgencia de corrección para el negocio
- Responsable asignado

Ciclo de vida del defecto: `Nuevo → Asignado → En corrección → Corregido → En reprueba → Cerrado` (o `Reabierto` si la corrección falló).

### 3.6 Reprobar y ejecutar regresión
1. Verifica que el defecto corregido efectivamente se resolvió
2. Ejecuta la suite de regresión para confirmar que la corrección no rompió nada más
3. Automatiza los casos de regresión que se repiten en cada ciclo

### 3.7 Verificar la cobertura
Confirma en la matriz de trazabilidad que cada requisito del ERS tiene al menos un caso de prueba ejecutado. Un requisito sin caso asociado es un requisito no verificado.

### 3.8 Ejecutar las pruebas de aceptación
1. Entrega al cliente el ambiente, los datos y el guion de pruebas
2. Acompaña la ejecución sin intervenir en las decisiones del usuario
3. Registra las observaciones y clasifícalas como defecto o como nuevo requisito
4. Obtén la firma del acta de aceptación

---

## 4. Criterios de entrada y salida

### Criterios de entrada
- El código está completo y desplegado en el ambiente de pruebas
- Las pruebas unitarias pasan y el pipeline está en verde
- Los casos de prueba están diseñados y aprobados
- El ambiente y los datos de prueba están listos

### Criterios de salida
- Se ejecutó el 100 % de los casos de prioridad alta
- No quedan defectos abiertos de severidad crítica ni alta
- Los defectos medios y bajos pendientes están documentados y aceptados por el cliente
- La cobertura de requisitos está completa en la matriz de trazabilidad
- Los requisitos no funcionales cumplen los umbrales medibles del ERS
- El acta de aceptación está firmada

---

## 5. Documentos que se elaboran

1. **Plan de Pruebas** — Documento central de la etapa. Estándar de referencia: IEEE 829 o ISO/IEC/IEEE 29119.

2. **Estrategia de pruebas** — Enfoque general, niveles, tipos, herramientas y grado de automatización.

3. **Casos de prueba** — Catálogo completo con la estructura descrita arriba.

4. **Guiones de prueba (scripts)** — Código de las pruebas automatizadas, versionado en el repositorio.

5. **Matriz de trazabilidad de pruebas** — Requisito → caso de prueba → resultado.

6. **Especificación de datos de prueba** — Juegos de datos, su origen y cómo regenerarlos.

7. **Bitácora de ejecución** — Registro de qué se ejecutó, cuándo, en qué versión y con qué resultado.

8. **Reporte de defectos** — Listado completo con severidad, prioridad, estado y responsable.

9. **Informe de resultados de pruebas** — Casos ejecutados, aprobados, fallidos y bloqueados, con porcentajes.

10. **Informe de pruebas de rendimiento** — Métricas obtenidas contra los umbrales exigidos.

11. **Informe de pruebas de seguridad** — Vulnerabilidades detectadas y su clasificación.

12. **Reporte de cobertura** — Porcentaje de requisitos y de código cubierto.

13. **Acta de pruebas de aceptación (UAT)** — Resultado de la validación del usuario, firmada.

14. **Informe de cierre de pruebas** — Resumen ejecutivo, defectos residuales aceptados y recomendación de liberar o no.

---

## 6. Documentos que se entregan formalmente

### Al cliente o patrocinador (requieren aprobación firmada)
- Plan de pruebas (para validar el alcance antes de ejecutar)
- Informe de resultados de pruebas
- Informe de cierre de pruebas con los defectos residuales aceptados
- **Acta de aceptación (UAT)** — Entregable clave de la etapa
- Informes de rendimiento y seguridad, cuando el contrato los exija

### Al equipo de desarrollo
- Reporte de defectos con pasos de reproducción y evidencia
- Bitácora de ejecución por versión
- Informes de rendimiento y seguridad con el detalle técnico

### Al equipo interno de calidad
- Casos de prueba y guiones automatizados
- Matriz de trazabilidad de pruebas
- Especificación de datos de prueba
- Reportes de cobertura

### Al área de despliegue y operación
- Informe de cierre de pruebas
- Listado de defectos conocidos que pasan a producción
- Configuración validada del ambiente

---

## 7. Hito de cierre de la etapa

La etapa termina con el **acta de aceptación firmada por el cliente** y el informe de cierre de pruebas que recomienda liberar el sistema.

A partir de ese momento:
- El sistema queda autorizado para desplegarse en producción
- Los defectos residuales aceptados pasan al backlog de mantenimiento
- La suite de regresión automatizada queda como activo permanente del proyecto

---

## 8. Errores frecuentes en esta etapa

- Probar solo el camino feliz y omitir los flujos de error y los valores límite
- Empezar a probar sin criterios de salida definidos, dejando la etapa sin punto final claro
- Confundir severidad con prioridad y corregir primero lo que no bloquea al negocio
- Reportar defectos sin pasos reproducibles, obligando al desarrollador a adivinar
- Probar en un ambiente distinto al de producción y descubrir fallos de configuración después del despliegue
- Omitir las pruebas de regresión y reintroducir defectos ya corregidos
- Dejar los requisitos no funcionales sin probar hasta que el sistema colapsa con usuarios reales
- Usar datos de producción sin anonimizar, exponiendo información sensible
- Aceptar que el propio desarrollador sea el único que prueba su código
- Recortar la etapa de pruebas para recuperar el retraso acumulado en las etapas anteriores
- Tratar las solicitudes nuevas del usuario durante UAT como defectos, en lugar de canalizarlas por control de cambios
