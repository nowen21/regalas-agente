Actúa como un **experto en UX/UI, arquitectura de información y diseño de dashboards de monitoreo**, con experiencia en interfaces para análisis de consumo, costos, rendimiento y optimización.

### Contexto

Estamos construyendo un tablero para controlar el consumo de tokens de Cimiento. El objetivo no es únicamente mostrar datos, sino permitir identificar rápidamente:

* cuánto se está consumiendo;
* dónde se están consumiendo los tokens;
* qué elementos generan ese consumo;
* qué procesos no consumen tokens;
* qué procesos que actualmente consumen tokens pueden convertirse en automatizaciones;
* dónde existen oportunidades de optimización;
* cómo evoluciona el consumo en el tiempo.

Actualmente la pantalla tiene 16 bloques seguidos y todos tienen prácticamente el mismo peso visual:

* 2 gráficas;
* 4 cifras grandes;
* 11 tablas;
* 1 franja de contexto.

Esto genera problemas de jerarquía, repetición y dificultad para identificar lo realmente importante.

### Problemas actuales

Debes revisar especialmente estos problemas:

1. No existe una jerarquía clara que indique por dónde empezar.
2. Las cifras principales no muestran el resultado general del período.
3. No existe un total de tokens del período ni una comparación clara con el período anterior.
4. Hay información repetida entre gráficas y tablas.
5. Las tablas obligan a comparar números grandes sin apoyo visual.
6. La información inferior está desordenada y presenta problemas de distribución y alturas.
7. La palabra «Estimado» se repite innecesariamente.
8. El refresco automático de 10 segundos puede interrumpir la lectura del usuario.
9. La información más importante para optimizar y ahorrar tokens queda demasiado abajo.
10. No existe suficiente diferenciación entre información de consumo, información de contexto y oportunidades de ahorro.

### Objetivo del rediseño

Rediseña la experiencia para que el usuario pueda responder rápidamente estas preguntas:

1. **¿Cuánto consumimos?**
2. **¿Estamos consumiendo más o menos que antes?**
3. **¿Dónde se están consumiendo los tokens?**
4. **¿Qué está generando ese consumo?**
5. **¿Qué procesos no necesitan tokens?**
6. **¿Qué procesos pueden automatizarse para dejar de consumir tokens?**
7. **¿Cuánto consumo podría evitarse mediante esas automatizaciones?**
8. **¿Qué está llenando el contexto?**
9. **¿Cómo está evolucionando el consumo?**

### Propuesta de estructura

Evalúa y, si corresponde, implementa una estructura basada en pestañas:

* **Resumen**
* **Dónde se gasta**
* **Qué llena el contexto**
* **Ahorro**
* **Mensajes**

No asumas que esta distribución es obligatoria. Evalúa si realmente es la mejor solución desde UX/UI y modifícala si existe una alternativa mejor.

### Resumen

La primera pantalla debe mostrar lo más importante sin obligar al usuario a recorrer todo el tablero.

Debe evaluar una franja superior con:

* total de tokens del período;
* variación frente al período anterior;
* número de llamadas;
* porcentaje de caché;
* contexto máximo.

Las gráficas deben complementar estas cifras, no repetirlas.

Debe existir una sección visible de **«Candidatos a automatizar»**, mostrando el potencial de ahorro, porque este dato es una de las razones principales del tablero.

### Consumo

Analiza cómo presentar:

* consumo por proyecto;
* consumo por sesión;
* consumo por palabra;
* consumo por trabajo;
* consumo por modelo;
* consumo por agente.

Evita mostrar dos componentes que representen prácticamente la misma información.

Si un filtro ya permite seleccionar un proyecto, determina si tiene sentido mantener una gráfica adicional por proyecto.

### Tipo de tokens

Evalúa reemplazar la tabla de tipos de tokens por una visualización que permita entender rápidamente la distribución:

* entrada;
* caché;
* salida;
* otros tipos que realmente existan.

La visualización debe permitir identificar rápidamente cuánto representa cada tipo y no solamente mostrar cifras.

### Tablas

Cuando se utilicen tablas:

* incluir porcentajes cuando aporten valor;
* utilizar barras de proporción cuando faciliten la comparación;
* evitar obligar al usuario a comparar manualmente números de muchos dígitos;
* ordenar los datos de forma que lo más relevante aparezca primero;
* destacar valores anormales o especialmente altos cuando corresponda;
* evitar columnas que repitan información;
* mostrar unidades de manera clara.

No agregues gráficos o barras únicamente como decoración. Cada elemento visual debe ayudar a interpretar los datos.

### Ahorro y automatización

Esta sección debe tener especial importancia.

Debe permitir diferenciar claramente:

**Procesos que no consumen tokens**
→ procesos que ya funcionan mediante automatizaciones tradicionales.

**Procesos que consumen tokens**
→ procesos que requieren interacción con el modelo.

**Procesos que consumen tokens y podrían automatizarse**
→ oportunidades concretas para eliminar o reducir consumo.

Cuando sea posible, mostrar:

* proceso;
* consumo actual;
* frecuencia;
* consumo estimado;
* posibilidad de automatización;
* ahorro potencial.

El objetivo es que el tablero no se limite a decir cuánto se consumió, sino que ayude a tomar decisiones sobre **dónde dejar de consumir tokens**.

### Contexto

Organiza la información relacionada con lo que ocupa el contexto, por ejemplo:

* enganches;
* archivos;
* herramientas;
* otros elementos que realmente tengan impacto.

Debe ser fácil identificar qué elementos tienen mayor impacto y cuáles podrían optimizarse.

### Tiempo y actualización

No vuelvas a renderizar todo el tablero cada 10 segundos.

Evalúa una estrategia en la que:

* cifras y gráficas puedan actualizarse automáticamente;
* las tablas se actualicen con menor frecuencia o mediante una acción explícita;
* exista un indicador como «Actualizado hace X segundos»;
* la actualización no interrumpa la lectura ni cambie innecesariamente la posición del usuario.

### Diseño visual

Utiliza principios de:

* jerarquía visual;
* agrupación por propósito;
* consistencia;
* reducción de carga cognitiva;
* comparación rápida;
* accesibilidad;
* diseño responsive;
* lectura progresiva.

No agregues colores, iconos, animaciones, tarjetas, gráficas o elementos visuales solamente para hacer que el tablero se vea más elaborado.

Cada elemento debe responder a una necesidad concreta.

### Antes de modificar

Antes de implementar el rediseño:

1. Revisa completamente la estructura actual.
2. Identifica qué información existe actualmente.
3. Identifica información duplicada.
4. Identifica información que falta.
5. Determina qué información es principal, secundaria y de detalle.
6. Identifica qué componentes pueden reutilizarse.
7. Verifica cómo funcionan actualmente los filtros y la actualización de datos.
8. No elimines información sin determinar primero si tiene utilidad.
9. No agregues información que no pueda obtenerse realmente.
10. No cambies la lógica de negocio para solucionar un problema que sea únicamente de presentación.

### Resultado esperado

Propón una estructura final del tablero explicando brevemente:

* qué debe aparecer primero;
* qué debe ir en cada pestaña;
* qué información debe eliminarse por duplicada;
* qué información debe agruparse;
* qué información debe destacarse;
* qué visualización corresponde a cada tipo de dato;
* cómo debe funcionar la actualización;
* cómo debe mostrarse el ahorro potencial;
* cómo debe diferenciarse lo que consume tokens de lo que puede automatizarse sin tokens.

Después de definir la propuesta, implementa el rediseño respetando la estructura y tecnología existente.

**Regla principal:** el tablero debe ayudar a **entender, controlar y reducir el consumo de tokens**, no simplemente mostrar una gran cantidad de datos.
