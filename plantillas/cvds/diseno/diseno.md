# Etapa 3: Diseño

Tercera etapa del ciclo de vida del desarrollo de software (SDLC). Traduce el **qué** definido en el ERS al **cómo** se va a construir el sistema. Es el puente entre los requisitos y el código.

---

## 1. Niveles del diseño

El diseño se trabaja en dos niveles, en este orden:

### 1.1 Diseño de alto nivel (arquitectónico)
Define la estructura global del sistema: qué grandes bloques existen, qué hace cada uno y cómo se comunican entre sí. Responde a preguntas de estructura, no de implementación.

### 1.2 Diseño de bajo nivel (detallado)
Baja al interior de cada bloque: clases, métodos, atributos, algoritmos, estructuras de datos y validaciones. Es lo que el programador leerá para escribir el código.

---

## 2. Actividades que se realizan

### 2.1 Definir la arquitectura del sistema
Selecciona el patrón arquitectónico que mejor responda a los requisitos no funcionales:

| Patrón | Cuándo conviene |
|---|---|
| Monolítico | Equipo pequeño, alcance acotado, despliegue simple |
| Cliente-servidor | Múltiples clientes consumiendo una lógica centralizada |
| Tres capas (presentación / lógica / datos) | Separación clara de responsabilidades, mantenimiento a largo plazo |
| MVC / MVVM | Aplicaciones con interfaz de usuario rica |
| Microservicios | Escalabilidad independiente por módulo, equipos distribuidos |
| Orientada a eventos | Procesamiento asíncrono, alto volumen de mensajes |
| Serverless | Carga intermitente, sin gestión de infraestructura |

Documenta la decisión y **por qué** se descartaron las alternativas.

### 2.2 Descomponer el sistema en módulos
Divide el sistema en componentes con responsabilidad única. Aplica dos principios de control de calidad estructural:

- **Alta cohesión** — Cada módulo hace una sola cosa y todo lo que contiene sirve a ese propósito
- **Bajo acoplamiento** — Los módulos dependen lo mínimo posible entre sí; un cambio interno no obliga a modificar otros

### 2.3 Diseñar la base de datos
1. Selecciona el motor (relacional, documental, clave-valor, grafo) según la naturaleza de los datos
2. Elabora el modelo lógico: entidades, atributos, relaciones y cardinalidades
3. Normaliza hasta tercera forma normal (3FN) y desnormaliza solo donde el rendimiento lo exija
4. Define el modelo físico: tablas, tipos de dato, longitudes, llaves primarias y foráneas
5. Establece índices, restricciones de integridad y valores por defecto
6. Define la política de respaldo, retención y purga de datos
7. Especifica el diccionario de datos campo por campo

### 2.4 Diseñar las interfaces
- **Interfaz de usuario (UI)**: pantallas, navegación, formularios, validaciones visibles, mensajes de error, responsividad y accesibilidad
- **Interfaces internas**: contratos entre módulos (qué entrada recibe cada uno y qué salida devuelve)
- **Interfaces externas**: integraciones con sistemas de terceros, formato de intercambio, autenticación y manejo de fallos de conexión
- **Diseño de la API**: endpoints, métodos, parámetros, códigos de respuesta y versionado

### 2.5 Diseñar los componentes en detalle
Para cada módulo especifica:
- Diagrama de clases con atributos, métodos, visibilidad y relaciones
- Algoritmos críticos en pseudocódigo o diagrama de flujo
- Estructuras de datos internas
- Manejo de excepciones y casos de error
- Reglas de validación

### 2.6 Diseñar la seguridad
- Modelo de autenticación (usuario/contraseña, SSO, tokens, MFA)
- Modelo de autorización: roles, perfiles y matriz de permisos por función
- Cifrado de datos en tránsito y en reposo
- Registro de auditoría: qué eventos se guardan y por cuánto tiempo
- Protección contra vulnerabilidades conocidas (inyección, XSS, CSRF)

### 2.7 Definir el entorno técnico
- Lenguajes, frameworks y librerías, con sus versiones
- Servidores, sistema operativo y servicios de nube
- Herramientas de control de versiones e integración continua
- Entornos separados: desarrollo, pruebas, preproducción y producción

### 2.8 Establecer estándares de desarrollo
- Convenciones de nombres para clases, variables, tablas y archivos
- Estructura de carpetas del proyecto
- Estilo de código y herramienta de formateo automático
- Política de ramas en el repositorio y reglas de revisión de código

### 2.9 Verificar la trazabilidad
Confirma en la matriz de trazabilidad que **cada requisito del ERS** tiene al menos un componente de diseño que lo implementa. Un requisito sin cobertura es un requisito que no se va a construir.

### 2.10 Revisar y aprobar el diseño
Realiza una revisión técnica formal con el equipo y el arquitecto antes de liberar la etapa.

---

## 3. Diagramas que se elaboran

- **Diagrama de arquitectura** — Vista general de capas y componentes
- **Diagrama de componentes (UML)** — Módulos y sus interfaces
- **Diagrama de despliegue (UML)** — Distribución en servidores y nodos físicos
- **Diagrama de clases detallado (UML)** — Atributos, métodos y relaciones
- **Diagrama de secuencia (UML)** — Interacción entre objetos a lo largo del tiempo
- **Diagrama de estados (UML)** — Ciclo de vida de las entidades con estados definidos
- **Modelo entidad-relación (MER)** — Estructura de la base de datos
- **Diagramas de flujo** — Lógica de algoritmos complejos
- **Mapa de navegación** — Recorrido del usuario entre pantallas
- **Mockups de alta fidelidad** — Diseño visual definitivo de la interfaz

---

## 4. Documentos que se elaboran

1. **Documento de Diseño de Software (SDD)** — Documento central de la etapa. Estándar de referencia: IEEE 1016.

2. **Documento de arquitectura** — Patrón elegido, justificación, alternativas descartadas y restricciones técnicas.

3. **Diseño de base de datos** — Modelo lógico, modelo físico y estrategia de índices.

4. **Diccionario de datos** — Cada campo con su nombre, tipo, longitud, obligatoriedad, valores permitidos y descripción.

5. **Especificación de interfaces (UI)** — Mockups, guía de estilo, comportamiento de cada control y mensajes al usuario.

6. **Especificación de API** — Contrato de cada endpoint con ejemplos de petición y respuesta.

7. **Diseño detallado de componentes** — Clases, métodos, algoritmos y pseudocódigo.

8. **Documento de arquitectura de seguridad** — Autenticación, autorización, cifrado y matriz de permisos.

9. **Registro de decisiones de arquitectura (ADR)** — Una ficha por decisión: contexto, opciones evaluadas, decisión tomada y consecuencias.

10. **Estándares de codificación** — Convenciones obligatorias para el equipo.

11. **Matriz de trazabilidad actualizada** — Requisito → componente de diseño.

12. **Plan de pruebas preliminar** — Estrategia de pruebas derivada del diseño, insumo para la etapa siguiente.

13. **Especificación del entorno técnico** — Infraestructura, versiones y configuración de cada ambiente.

---

## 5. Documentos que se entregan formalmente

### Al cliente o patrocinador (requieren aprobación firmada)
- Documento de arquitectura (versión resumida, sin detalle técnico interno)
- Mockups de alta fidelidad y mapa de navegación
- Documento de arquitectura de seguridad
- Cronograma actualizado con el detalle de construcción por módulo

### Al equipo de desarrollo (uso operativo)
- Documento de Diseño de Software completo
- Diseño detallado de componentes y diagramas UML
- Diseño físico de base de datos y diccionario de datos
- Especificación de API
- Estándares de codificación
- Registro de decisiones de arquitectura

### Al equipo de pruebas
- Plan de pruebas preliminar
- Matriz de trazabilidad actualizada
- Especificación de interfaces y de API

### Al área de infraestructura
- Diagrama de despliegue
- Especificación del entorno técnico

---

## 6. Hito de cierre de la etapa

La etapa termina con la **revisión técnica formal aprobada** y la firma del Documento de Diseño de Software, que se convierte en la **línea base de diseño**.

A partir de ese momento:
- La codificación puede iniciar con especificaciones estables
- Todo cambio de diseño entra por control de cambios con evaluación de impacto
- La estimación de esfuerzo se refina, porque ya se conoce el detalle de los componentes

---

## 7. Errores frecuentes en esta etapa

- Saltar directamente a codificar sin diseño, y descubrir el problema arquitectónico cuando ya hay miles de líneas escritas
- Sobrediseñar: construir flexibilidad para escenarios que nadie pidió y que probablemente no ocurran
- Diseñar sin considerar los requisitos no funcionales, y descubrir en producción que el sistema no soporta la carga real
- Producir módulos con alto acoplamiento, donde cualquier cambio obliga a tocar medio sistema
- Dejar la seguridad como un añadido posterior en lugar de diseñarla desde el inicio
- No documentar por qué se tomó cada decisión de arquitectura; seis meses después nadie recuerda el motivo
- Perder la trazabilidad y llegar a pruebas con requisitos que ningún componente implementa
- Diseñar la base de datos sin proyectar el crecimiento del volumen de datos
