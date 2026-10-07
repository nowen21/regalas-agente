Actúa como **experto en UX/UI, diseño de productos digitales, accesibilidad y creación de sistemas de diseño**.

Tu tarea es crear una **guía de estilo y un sistema de diseño completo, coherente, reutilizable y escalable** para el proyecto, que establezca el estándar que deben seguir todas las interfaces actuales y futuras.

El objetivo no es diseñar una pantalla específica, sino definir una **base común de UX/UI** que permita que todas las pantallas mantengan la misma identidad visual, comportamiento, estructura y experiencia de usuario.

## Principios fundamentales

El sistema de diseño debe garantizar que la interfaz sea:

- clara;
- sencilla;
- intuitiva;
- consistente;
- accesible;
- fácil de aprender;
- visualmente ordenada;
- responsive;
- reutilizable;
- escalable.

La interfaz debe diseñarse pensando primero en la persona que utiliza el sistema y no en su funcionamiento técnico interno.

El usuario no debe necesitar conocer la arquitectura, estructura interna o términos técnicos del sistema para saber dónde está, qué puede hacer o cómo continuar.

## 1. Fundamentos visuales

Define los estándares para:

- identidad visual;
- paleta de colores;
- colores principales, secundarios y semánticos;
- tipografía;
- tamaños y jerarquías de texto;
- títulos y subtítulos;
- espaciados;
- márgenes;
- tamaños;
- bordes;
- radios;
- sombras;
- iconografía;
- grillas;
- alineación;
- densidad visual;
- puntos de ruptura responsive.

No definas valores arbitrariamente. Cada decisión debe tener una función dentro del sistema.

## 2. Jerarquía visual

Establece claramente cómo diferenciar:

- contenido principal;
- contenido secundario;
- acciones principales;
- acciones secundarias;
- información complementaria;
- advertencias;
- errores;
- confirmaciones;
- estados;
- ayudas.

El usuario debe poder identificar rápidamente qué es importante y cuál es la siguiente acción disponible.

## 3. Componentes

Define componentes reutilizables para elementos como:

- botones;
- campos de formulario;
- selectores;
- buscadores;
- tablas;
- tarjetas;
- pestañas;
- menús;
- navegación;
- breadcrumbs cuando sean necesarios;
- modales;
- paneles;
- alertas;
- notificaciones;
- tooltips;
- indicadores de estado;
- paginación;
- filtros;
- loaders;
- barras de progreso;
- estados vacíos;
- mensajes de error;
- mensajes de éxito;
- confirmaciones.

Para cada componente establece:

- cuándo utilizarlo;
- cuándo no utilizarlo;
- variantes permitidas;
- tamaños;
- comportamiento;
- estados;
- interacción;
- accesibilidad;
- comportamiento responsive.

Evita crear componentes diferentes para resolver el mismo problema.

## 4. Navegación

Define un patrón común para que el usuario siempre pueda reconocer:

- dónde está;
- de dónde viene;
- qué opciones tiene;
- cómo regresar;
- cómo avanzar;
- cómo acceder a las funciones principales.

La navegación no debe asumir que el usuario conoce previamente dónde están las funcionalidades.

## 5. Formularios

Establece estándares para:

- etiquetas;
- campos obligatorios;
- ayudas;
- validaciones;
- mensajes de error;
- agrupación de información;
- acciones principales;
- acciones secundarias;
- confirmaciones.

Los formularios deben solicitar únicamente información que realmente necesite proporcionar el usuario.

Si el sistema puede obtener, calcular o determinar un dato automáticamente, no debe trasladarse innecesariamente esa responsabilidad al usuario.

## 6. Tablas y presentación de información

Define cómo presentar:

- tablas;
- listados;
- resultados;
- filtros;
- búsquedas;
- ordenamientos;
- paginación;
- acciones por registro;
- estados;
- ausencia de información.

Evita mostrar información técnica o columnas que no aporten valor al usuario.

## 7. Estados del sistema

Todo componente que dependa de información o procesos debe contemplar como mínimo:

- estado inicial;
- cargando;
- con información;
- sin información;
- éxito;
- advertencia;
- error;
- deshabilitado, cuando corresponda.

El usuario nunca debe quedar frente a una pantalla sin entender qué está ocurriendo.

## 8. Lenguaje de interfaz

Define reglas de **UX Writing**.

Los textos deben:

- utilizar lenguaje sencillo;
- hablar desde la necesidad del usuario;
- evitar tecnicismos innecesarios;
- indicar claramente qué ocurrió;
- explicar qué debe hacer el usuario cuando realmente sea necesaria una acción;
- evitar trasladar problemas internos del sistema al usuario.

Los botones deben expresar claramente la acción que realizan.

Evita mensajes ambiguos como «Aceptar», «Procesar» o «Ejecutar» cuando pueda utilizarse una acción más específica.

## 9. Accesibilidad

El sistema de diseño debe contemplar buenas prácticas de accesibilidad, incluyendo:

- contraste;
- legibilidad;
- navegación mediante teclado;
- foco visible;
- etiquetas comprensibles;
- estructura semántica;
- estados que no dependan únicamente del color;
- tamaños adecuados para interacción;
- compatibilidad con tecnologías de asistencia cuando corresponda.

La accesibilidad debe formar parte del diseño desde el inicio y no agregarse posteriormente como corrección.

## 10. Responsive

Define cómo deben comportarse las interfaces en:

- escritorio;
- portátil;
- tableta;
- móvil.

No se debe limitar el responsive a reducir tamaños. Debe reorganizarse la información cuando sea necesario para conservar la facilidad de uso.

## 11. Patrones de interacción

Define comportamientos comunes para situaciones repetitivas:

- crear;
- editar;
- eliminar;
- guardar;
- cancelar;
- buscar;
- filtrar;
- confirmar;
- regresar;
- cargar información;
- procesos en ejecución;
- errores;
- acciones irreversibles.

La misma acción debe comportarse de manera coherente en todo el sistema.

## 12. Reutilización y consistencia

Antes de crear un nuevo componente, patrón o estilo, verifica si ya existe uno que resuelva la misma necesidad.

No dupliques componentes con pequeñas diferencias innecesarias.

Una misma necesidad debe resolverse de la misma manera en todas las pantallas.

## 13. Documentación

Documenta el sistema de diseño de manera que cualquier persona que trabaje posteriormente en el proyecto pueda determinar fácilmente:

- qué componente utilizar;
- cómo utilizarlo;
- cuándo utilizarlo;
- qué variantes existen;
- qué comportamiento debe tener;
- qué prácticas están permitidas;
- qué prácticas deben evitarse.

Incluye ejemplos claros cuando sean necesarios.

## 14. Regla de evolución

El sistema de diseño debe ser una **fuente única de referencia para UX/UI**.

Cuando aparezca una necesidad que todavía no esté contemplada:

1. verifica primero si puede resolverse con lo existente;
2. si realmente requiere un nuevo patrón o componente, defínelo de forma general y reutilizable;
3. incorpóralo al sistema de diseño;
4. úsalo posteriormente desde esa definición común.

No resuelvas necesidades repetibles únicamente dentro de una pantalla.

## Resultado esperado

Entrega una **guía de estilo y sistema de diseño que pueda utilizarse como estándar real de construcción**, no solamente como documento visual de referencia.

Debe permitir que una persona pueda desarrollar o rediseñar una pantalla y saber exactamente qué criterios, componentes y patrones debe utilizar sin tener que inventarlos nuevamente.

El resultado debe lograr que todas las interfaces parezcan y se comporten como partes de **un mismo sistema**, independientemente de quién las haya desarrollado.