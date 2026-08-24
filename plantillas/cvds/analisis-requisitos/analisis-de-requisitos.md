# Etapa 2: Análisis de Requisitos

Segunda etapa del ciclo de vida del desarrollo de software (SDLC). Su propósito es determinar **qué** debe hacer el sistema, sin definir todavía **cómo** se va a construir.

---

## 1. Actividades que se realizan

### 1.1 Identificación de fuentes de información
Determina de dónde saldrán los requisitos: usuarios finales, clientes, gerentes, personal de soporte, normativas vigentes y sistemas actuales en operación.

### 1.2 Elicitación (obtención) de requisitos
Recopila las necesidades usando técnicas combinadas:

| Técnica | Cuándo usarla |
|---|---|
| Entrevistas | Profundizar con usuarios clave y tomadores de decisión |
| Encuestas / cuestionarios | Muchos usuarios dispersos, información cuantificable |
| Observación en sitio | El usuario no sabe explicar su proceso, pero sí ejecutarlo |
| Talleres (JAD) | Requisitos con conflicto entre áreas; se negocian en la mesa |
| Análisis de documentos | Existen formatos, manuales o normativas en uso |
| Prototipos desechables | El usuario no logra imaginar el resultado hasta verlo |
| Estudio del sistema actual | Hay un sistema heredado que será reemplazado |

### 1.3 Clasificación de requisitos
Separa lo recopilado en dos grandes grupos:

**Requisitos funcionales** — Lo que el sistema debe hacer.
- Registrar, consultar, modificar y eliminar datos
- Calcular, procesar y transformar información
- Generar reportes y notificaciones
- Controlar accesos y perfiles de usuario
- Integrarse con otros sistemas

**Requisitos no funcionales** — Cómo debe comportarse el sistema.
- Rendimiento: tiempos de respuesta, usuarios concurrentes
- Seguridad: autenticación, cifrado, auditoría
- Usabilidad: curva de aprendizaje, accesibilidad
- Disponibilidad: porcentaje de tiempo operativo, ventanas de mantenimiento
- Escalabilidad: crecimiento esperado de datos y usuarios
- Portabilidad: navegadores, sistemas operativos, dispositivos
- Mantenibilidad: estándares de código, documentación
- Cumplimiento legal: protección de datos, normativa sectorial

### 1.4 Análisis y depuración
Revisa el conjunto recopilado y corrige:
- **Ambigüedades** — "el sistema debe ser rápido" no es medible; conviértelo en "responder en menos de 2 segundos"
- **Contradicciones** — dos áreas pidiendo comportamientos incompatibles
- **Duplicados** — el mismo requisito expresado con distintas palabras
- **Omisiones** — casos de error, validaciones y flujos alternos que nadie mencionó
- **Requisitos fuera de alcance** — lo que excede lo aprobado en la planificación

### 1.5 Priorización
Ordena los requisitos según su importancia. El método más usado es **MoSCoW**:

- **Must have** — Sin esto el sistema no sirve
- **Should have** — Importante, pero el sistema opera sin ello
- **Could have** — Deseable si sobra tiempo y presupuesto
- **Won't have** — Excluido de esta versión, queda registrado para el futuro

### 1.6 Modelado
Representa gráficamente lo que se entendió, para validarlo con el usuario:
- Diagrama de casos de uso (actores y funciones)
- Diagrama de actividades (flujo de los procesos)
- Diagrama de clases conceptual (entidades del negocio)
- Modelo entidad-relación preliminar
- Diagramas de flujo de datos (DFD)
- Prototipos de pantallas o wireframes

### 1.7 Verificación y validación
- **Verificación**: ¿los requisitos están bien escritos? (claros, medibles, sin contradicciones)
- **Validación**: ¿son los requisitos correctos? (el usuario confirma que eso es lo que necesita)

### 1.8 Especificación y aprobación
Consolida todo en el documento formal y obtiene la firma del cliente.

---

## 2. Características de un requisito bien escrito

Cada requisito debe cumplir con lo siguiente:

- **Único** — Se enuncia una sola condición por requisito
- **Completo** — No depende de información que no está escrita
- **Consistente** — No contradice a ningún otro requisito
- **Verificable** — Existe una prueba que demuestra si se cumplió
- **Medible** — Los criterios cuantitativos están expresados en números
- **Trazable** — Tiene un identificador único (RF-01, RNF-01) que permite seguirlo hasta el diseño, el código y las pruebas
- **Factible** — Es realizable con la tecnología, el tiempo y el presupuesto disponibles
- **Necesario** — Si se elimina, el usuario pierde algo real

**Formato recomendado:**
> El sistema **debe** [acción] [objeto] [condición] [criterio medible].

Ejemplo: *RF-08: El sistema debe generar el reporte mensual de ventas en formato PDF en un tiempo máximo de 5 segundos.*

---

## 3. Documentos que se elaboran

1. **Documento de Especificación de Requisitos de Software (ERS / SRS)** — Documento central de la etapa. Estándar de referencia: IEEE 830 o ISO/IEC/IEEE 29148.

2. **Catálogo de requisitos funcionales** — Tabla con ID, descripción, prioridad, origen y estado de cada requisito.

3. **Catálogo de requisitos no funcionales** — Igual estructura, con criterios medibles obligatorios.

4. **Documento de casos de uso** — Descripción narrativa de cada caso: actor, precondiciones, flujo principal, flujos alternos, flujos de excepción y postcondiciones.

5. **Modelos y diagramas UML** — Casos de uso, actividades, clases conceptuales, secuencia.

6. **Glosario del proyecto** — Definición de los términos del negocio, para que todos los interesados usen el mismo vocabulario.

7. **Matriz de trazabilidad de requisitos (RTM)** — Relaciona cada requisito con su origen, el módulo de diseño, el componente de código y el caso de prueba que lo valida.

8. **Prototipos o wireframes** — Bocetos navegables de las pantallas principales.

9. **Reglas de negocio** — Políticas, restricciones y fórmulas de cálculo propias de la organización.

10. **Criterios de aceptación** — Condiciones concretas bajo las cuales el cliente dará por recibido cada requisito.

11. **Actas de reuniones de elicitación** — Registro de lo acordado con cada interesado, con fecha y participantes.

12. **Registro de cambios de requisitos** — Bitácora de solicitudes de modificación con su impacto en costo y cronograma.

---

## 4. Documentos que se entregan formalmente

### Al cliente o patrocinador (requieren aprobación firmada)
- Documento de Especificación de Requisitos de Software (ERS)
- Catálogo de requisitos funcionales y no funcionales
- Documento de casos de uso
- Prototipos o wireframes
- Criterios de aceptación
- Glosario del proyecto

### Al equipo interno (uso operativo)
- Matriz de trazabilidad de requisitos
- Modelos y diagramas UML detallados
- Actas de reuniones de elicitación
- Registro de cambios de requisitos

### Al equipo de pruebas
- Criterios de aceptación
- Casos de uso con flujos alternos y de excepción
- Matriz de trazabilidad

---

## 5. Hito de cierre de la etapa

La etapa termina con la **aprobación formal y firmada del ERS** por parte del cliente. Ese documento se convierte en la **línea base de requisitos**.

A partir de ese momento:
- Cualquier requisito nuevo entra por el procedimiento de control de cambios
- Cada cambio se evalúa en impacto de costo, tiempo y alcance antes de aceptarse
- El diseño no debe iniciar sin esa línea base aprobada

---

## 6. Errores frecuentes en esta etapa

- Confundir requisitos con soluciones técnicas (el análisis dice *qué*, no *cómo*)
- Aceptar requisitos ambiguos por evitar la incomodidad de repreguntar
- Entrevistar solo a los jefes y omitir a quienes usarán el sistema a diario
- Ignorar los requisitos no funcionales hasta que aparecen fallas de rendimiento en producción
- No documentar los flujos de error ni las validaciones
- Omitir la firma de aprobación y quedar sin línea base para negociar cambios
- Permitir el crecimiento del alcance sin registrar el impacto en costo y cronograma
