# EP-007 — Instalación y actualización en cualquier proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-007 |
| **Brief de origen** | [planteamiento.md](../../../planteamiento.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | M |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Todo lo anterior no sirve de nada si ponerlo a andar en un proyecto cuesta media hora de pasos manuales. Lo que exige configurarse a mano no se configura, o se configura distinto en cada proyecto, que es peor.

Esta épica hace que un proyecto quede listo con una sola línea. El instalador lleva lo que hace falta, deja los automatismos puestos y no toca lo que el proyecto ya tenía escrito.

También resuelve la segunda mitad del problema, que suele olvidarse: mantener al día lo ya instalado. Un proyecto con una copia vieja y un aviso permanente termina ignorando el aviso.

## 3. Problema y oportunidad

### 3.1 Situación actual

Cada proyecto nuevo se configuraría a mano, copiando archivos y ajustando rutas. Nadie hace eso dos veces igual.

### 3.2 Impacto de no hacerlo

Lo construido en las otras épicas se queda en un solo proyecto. Y los que sí lo tengan van quedando con versiones distintas, así que dejan de ser comparables.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Herramientas que exigen configuración manual | Se instalan una vez, no se actualizan nunca, y con el tiempo cada proyecto tiene una versión distinta |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que un proyecto quede listo con una línea, sin pasos manuales, y que lo ya instalado se pueda poner al día sin perder lo que el proyecto escribió por su cuenta.

**Hipótesis de valor.** Si instalar cuesta una línea, se instala en todos los proyectos. Se sabrá cuando un proyecto nuevo pase de cero a trabajando sin ningún paso a mano.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Un proyecto nuevo | Queda listo sin trabajo manual | Cualitativo |
| Un proyecto viejo | Se pone al día sin perder lo suyo | Cualitativo |
| La persona | Deja de repetir la misma configuración | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un instalador que deje el proyecto listo con una sola línea.
- La creación de la estructura de carpetas que el trabajo necesita.
- La puesta de los automatismos, generados y no escritos a mano.
- Un modo que muestre qué va a hacer antes de hacerlo.
- La regla de que instalar no borra lo que el proyecto ya tenía escrito.
- Un modo de actualización que ponga al día lo ya instalado.
- La distinción entre lo generado, que se puede pisar, y lo escrito por la persona, que no.
- Un control que diga si el proyecto tiene todo lo que debería tener.

### 5.2 Fuera del alcance

- Instalar la herramienta con la que se conversa con la IA. Eso se instala una vez en la máquina, aparte.
- Migrar un proyecto a una versión nueva de las reglas. El aviso lo da EP-002; actualizar los archivos es lo que sí entra acá.
- Adivinar las convenciones propias del proyecto.

### 5.3 Diferido

- Actualizar varios proyectos a la vez. Se retoma cuando haya suficientes.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Que lo construido llegue a cualquier proyecto sin trabajo manual, y se mantenga al día |
| 2 | Actores | La persona que instala, el instalador, el proyecto que recibe |
| 3 | Información | Qué componentes hay que llevar, cuáles ya están, cuáles quedaron viejos y cuáles los escribió la persona |
| 4 | Campos | Cada componente instalado tiene campos definidos: nombre, origen, huella de la copia y si es generado o editable. El detalle baja a la historia de usuario |
| 5 | Validaciones | No se pisa un archivo editable; no se instala sobre una estructura que no se pudo leer |
| 6 | Reglas de negocio | Lo generado se reemplaza sin preguntar; lo que escribió la persona nunca se pisa, se avisa y se muestra la diferencia |
| 7 | Estados y transiciones | Un componente está ausente, instalado al día o instalado viejo. De viejo pasa a al día con la actualización |
| 8 | Operaciones | Instalar, previsualizar, actualizar, revisar qué falta |
| 9 | Restricciones | No borra trabajo del proyecto; no necesita internet; no pide configuración a mano |
| 10 | Relaciones | Lleva los componentes que producen las demás épicas |
| 11 | Consultas | Ver qué está instalado, qué falta y qué quedó viejo |
| 12 | Mensajes | Dice qué agregó, qué actualizó y qué no tocó, y por qué |
| 13 | Errores | Ruta que no existe, archivo bloqueado, permisos insuficientes, estructura inesperada |
| 14 | Permisos | Los del sistema de archivos de la máquina |
| 15 | Auditoría | Queda registro de qué se instaló y en qué versión |
| 16 | Resultado final | La épica está completa cuando un proyecto pasa de cero a trabajando con una línea, y uno viejo se pone al día sin perder lo suyo |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 20 | Importación | No aplica porque no hay datos que cargar |
| 22 | Configurabilidad | El proyecto puede tener su propia configuración escrita, y el instalador la respeta |
| 25 | Convivencia | Un proyecto que ya venía trabajando sin esto conserva todo lo que tenía |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La persona | Corre el instalador | Una sola línea, y saber qué va a pasar antes de que pase |
| Un proyecto que ya tenía reglas propias | Recibe la instalación | Que no le borren lo suyo |

**Volumetría estimada.** Varios proyectos, unas decenas de componentes por proyecto.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Un proyecto queda listo con una sola línea, sin pasos manuales.
- [ ] **CAE-02** El instalador muestra qué va a hacer antes de hacerlo.
- [ ] **CAE-03** No se pisa ningún archivo escrito por la persona.
- [ ] **CAE-04** Lo ya instalado se puede poner al día.
- [ ] **CAE-05** Se puede saber qué le falta a un proyecto.
- [ ] **CAE-06** La instalación funciona sin internet y en rutas con espacios y tildes.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Pasos manuales para dejar un proyecto listo | Todos, hoy | Ninguno | Al terminar la épica | Instalación de prueba |
| Proyectos con componentes viejos | Sin medir | Ninguno sin avisar | Cada mes | Control de lo instalado |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| [HU-001](HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md) | Instalar todo con una sola línea | Must | M |
| [HU-002](HU-002-mostrar-antes-de-hacer/HU-002-mostrar-antes-de-hacer.md) | Mostrar qué va a hacer antes de hacerlo | Must | S |
| [HU-003](HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md) | Crear la estructura de carpetas del trabajo | Must | S |
| [HU-004](HU-004-generar-los-automatismos/HU-004-generar-los-automatismos.md) | Generar y poner los automatismos | Must | M |
| [HU-005](HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) | No pisar lo que escribió la persona | Must | M |
| [HU-006](HU-006-poner-al-dia/HU-006-poner-al-dia.md) | Poner al día lo ya instalado | Should | M |
| [HU-007](HU-007-revisar-que-falta/HU-007-revisar-que-falta.md) | Revisar qué le falta al proyecto | Should | M |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Instalador | Nuevo | |
| Automatismos | Sin cambio | Se generan desde acá |
| Estructura del proyecto | Nuevo | La crea el instalador |

### 10.2 Decisiones de arquitectura

- Los automatismos se generan, no se copian a mano, para poder regenerarlos sin perder nada.
- Se compara una huella de cada archivo instalado contra el original, para saber cuál quedó viejo sin tener que leerlo.
- La previsualización va primero siempre, porque el instalador escribe en un repositorio que no es suyo.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Autoinstalación | Si exige configurarla a mano, está mal hecha |
| Reversibilidad | Lo generado se puede regenerar sin pérdida |
| Portabilidad | Windows, con rutas que llevan espacios y tildes |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-001 y EP-003, porque son lo que se instala | Interna | Bloqueante |
| DEP-02 | EP-004, porque el control de lo que falta se apoya en las comprobaciones | Interna | No bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que el instalador borre trabajo del proyecto | Baja | Muy alto | Previsualización obligatoria y nunca pisar lo editable |
| R-02 | Que el aviso de componente viejo se vuelva permanente y se ignore | Alta | Medio | Existe el modo de actualización, para que el aviso tenga salida |
| R-03 | Que falle en rutas con tildes o espacios | Media | Alto | Es el caso normal de la máquina de trabajo, así que se prueba con esas rutas desde el principio |

## 13. Supuestos y restricciones

**Supuestos**

- El proyecto donde se instala está bajo control de versiones, así que un error se puede deshacer.

**Restricciones**

- Sin internet, sin dependencias externas, y con el lenguaje disponible en la máquina.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Instalación con previsualización y estructura | HU-001, HU-002, HU-003 |
| Fase 2 | Automatismos y respeto por lo escrito | HU-004, HU-005 |
| Fase 3 | Actualización y control de lo que falta | HU-006, HU-007 |

## 15. Definition of Ready

- [ ] Lista de componentes que se instalan acordada
- [ ] Distinción entre lo generado y lo editable acordada

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Un proyecto de prueba pasa de cero a trabajando con una línea
- [ ] Un proyecto con reglas propias las conserva intactas
- [ ] Funciona en rutas con espacios y tildes

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
