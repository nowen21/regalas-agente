# Etapa 4: Implementación (Codificación)

Cuarta etapa del ciclo de vida del desarrollo de software (SDLC). Convierte las especificaciones del Documento de Diseño en código fuente ejecutable. Es la etapa que consume la mayor cantidad de horas-hombre del proyecto.

---

## 1. Actividades que se realizan

### 1.1 Preparar el entorno de desarrollo
1. Instala y configura el stack definido en el diseño (lenguaje, framework, motor de base de datos), respetando las versiones especificadas
2. Crea el repositorio y define la estructura de carpetas del proyecto
3. Configura la política de ramas (por ejemplo GitFlow o trunk-based)
4. Instala las herramientas de formateo, análisis estático y depuración
5. Verifica que cada desarrollador reproduzca el mismo entorno; usa contenedores si la configuración es compleja
6. Levanta los ambientes separados: desarrollo, pruebas y preproducción

### 1.2 Distribuir el trabajo
- Descompón cada módulo del diseño en tareas asignables
- Asigna las tareas según los módulos de menor acoplamiento primero, para permitir trabajo en paralelo
- Prioriza los componentes de los que dependen otros (base de datos, autenticación, capa de acceso a datos)
- Define la duración estimada de cada tarea y su criterio de terminado (*Definition of Done*)

### 1.3 Construir la base de datos
1. Escribe los scripts de creación de tablas, llaves e índices según el modelo físico
2. Versiona los scripts en el repositorio, nunca modifiques la base a mano
3. Usa una herramienta de migraciones para controlar los cambios de esquema
4. Carga los datos maestros o de catálogo necesarios para operar
5. Prepara un juego de datos de prueba representativo

### 1.4 Codificar los componentes
Sigue este orden dentro de cada módulo:
1. Capa de acceso a datos (entidades y repositorios)
2. Capa de lógica de negocio (servicios y reglas)
3. Capa de exposición (controladores, endpoints)
4. Capa de presentación (interfaz de usuario)

Durante la codificación:
- Aplica los estándares de nombres y estilo acordados
- Implementa el manejo de excepciones desde el inicio, no al final
- Valida todas las entradas, tanto en cliente como en servidor
- Registra eventos en logs con niveles diferenciados (error, advertencia, información)
- No dejes credenciales, llaves ni rutas fijas dentro del código; usa variables de entorno

### 1.5 Escribir pruebas unitarias
- Cubre cada método con lógica de negocio relevante
- Prueba el camino feliz, los casos límite y los casos de error
- Usa objetos simulados (*mocks*) para aislar dependencias externas
- Ejecuta la suite completa antes de cada integración

### 1.6 Integrar el código
1. Sube cambios pequeños y frecuentes al repositorio, no acumules semanas de trabajo
2. Escribe mensajes de commit descriptivos que expliquen el porqué del cambio
3. Sincroniza con la rama principal antes de solicitar la integración
4. Resuelve los conflictos de fusión en tu propia rama

### 1.7 Revisar el código (Code Review)
- Ningún cambio entra a la rama principal sin revisión de al menos un par
- Verifica: cumplimiento del diseño, estándares, cobertura de pruebas, manejo de errores y seguridad
- Ejecuta análisis estático automático para detectar vulnerabilidades y código duplicado
- Registra la deuda técnica que se acepte conscientemente

### 1.8 Automatizar la integración continua (CI)
Configura el pipeline para que en cada envío al repositorio se ejecute automáticamente:
1. Compilación del proyecto
2. Análisis estático de código
3. Pruebas unitarias
4. Reporte de cobertura
5. Generación del artefacto desplegable

Un pipeline en rojo bloquea la integración hasta corregirse.

### 1.9 Documentar durante la construcción
- Comenta el código solo donde el *por qué* no sea evidente; el *qué* debe leerse en el propio código
- Documenta las funciones públicas y las APIs con el formato del lenguaje (Javadoc, docstrings, JSDoc)
- Actualiza el README con instrucciones de instalación y ejecución
- Registra las desviaciones respecto al diseño original y su justificación

### 1.10 Controlar el avance
- Reporta el estado de cada tarea contra lo estimado
- Actualiza la matriz de trazabilidad conforme se completan los requisitos
- Escala de inmediato cualquier bloqueo técnico que supere lo previsto

---

## 2. Buenas prácticas obligatorias

| Práctica | Qué evita |
|---|---|
| Control de versiones en todo el código y scripts | Pérdida de trabajo y cambios sin rastro |
| Commits pequeños y frecuentes | Conflictos de fusión difíciles de resolver |
| Revisión de código por pares | Defectos que llegan a producción |
| Pruebas unitarias desde el primer día | Regresiones al modificar código existente |
| Análisis estático automatizado | Vulnerabilidades y código duplicado |
| Configuración externa al código | Exposición de credenciales y despliegues rígidos |
| Principio DRY (no repetir lógica) | Correcciones aplicadas en un lugar y olvidadas en otro |
| Refactorización continua | Acumulación de deuda técnica |
| Ambiente idéntico entre desarrolladores | El clásico "en mi máquina sí funciona" |

---

## 3. Documentos y artefactos que se elaboran

1. **Código fuente versionado** — Entregable principal de la etapa, alojado en el repositorio.

2. **Scripts de base de datos** — Creación de esquema, migraciones y carga de datos maestros.

3. **Documentación técnica del código** — Generada desde los comentarios estructurados (Javadoc, Swagger/OpenAPI para APIs).

4. **Manual de instalación y configuración** — Pasos para levantar el sistema desde cero en un servidor limpio.

5. **README del proyecto** — Requisitos previos, instalación, ejecución y estructura de carpetas.

6. **Suite de pruebas unitarias** — Código de pruebas, versionado junto al código productivo.

7. **Reporte de cobertura de pruebas** — Porcentaje de código ejercitado por las pruebas.

8. **Reporte de análisis estático** — Vulnerabilidades, duplicación y complejidad ciclomática.

9. **Registro de deuda técnica** — Concesiones aceptadas, con su impacto y plan de pago.

10. **Bitácora de builds** — Historial de compilaciones del pipeline de CI.

11. **Registro de cambios respecto al diseño** — Desviaciones detectadas durante la construcción, con su justificación.

12. **Matriz de trazabilidad actualizada** — Requisito → componente de diseño → archivo de código.

13. **Notas de versión (changelog)** — Funcionalidades incluidas en cada incremento entregado.

---

## 4. Documentos que se entregan formalmente

### Al cliente o patrocinador
- Notas de versión de cada incremento
- Demostración funcional del software construido
- Informe de avance contra el cronograma
- Manual de instalación (si el cliente administra su propia infraestructura)

### Al equipo de pruebas
- Artefacto ejecutable desplegado en el ambiente de pruebas
- Documentación técnica y de API
- Notas de versión con el detalle de lo que entra a probarse
- Matriz de trazabilidad actualizada

### Al equipo interno y a mantenimiento futuro
- Código fuente completo en el repositorio
- Scripts de base de datos versionados
- Registro de deuda técnica
- Registro de decisiones y desviaciones del diseño
- Reportes de cobertura y análisis estático

### Al área de infraestructura
- Manual de instalación y configuración
- Artefacto desplegable y sus dependencias

---

## 5. Hito de cierre de la etapa

La etapa termina cuando se cumplen estas condiciones (*code complete*):

- Todos los requisitos de prioridad **Must have** están codificados
- La suite de pruebas unitarias pasa completa
- El pipeline de integración continua está en verde
- Todo el código fue revisado y fusionado a la rama principal
- El sistema está desplegado y funcionando en el ambiente de pruebas
- La documentación técnica está actualizada

Desde ese punto, el software pasa formalmente al equipo de pruebas para la validación de la etapa siguiente.

---

## 6. Errores frecuentes en esta etapa

- Codificar sin consultar el diseño y terminar construyendo algo distinto a lo especificado
- Dejar las pruebas unitarias "para el final", momento en que nunca se escriben
- Acumular días o semanas de trabajo sin integrar, generando conflictos masivos
- Guardar contraseñas y llaves de API dentro del código fuente
- Omitir el manejo de errores y validaciones porque "esos casos no van a ocurrir"
- Ignorar los estándares de codificación, produciendo un código imposible de mantener
- Aceptar cambios de requisitos directamente del usuario sin pasar por control de cambios
- Reportar tareas como terminadas sin cumplir el criterio de *Definition of Done*
- Acumular deuda técnica sin registrarla, hasta que el sistema se vuelve inmodificable
- Optimizar prematuramente partes del código que nadie ha medido como lentas
