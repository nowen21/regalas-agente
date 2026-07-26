# 17 · Interfaz y experiencia de usuario  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Reglas agnósticas para lo que ve y usa el **usuario final**. Aplican a proyectos con interfaz (web, escritorio, móvil); un proyecto sin UI (librería, servicio backend, CLI) las omite. El framework, el sistema de diseño y el estándar de accesibilidad concretos los declara la capa 3.

---

## I1 · Toda vista resuelve sus tres estados

Ninguna pantalla queda en blanco ni muestra un error crudo. Siempre se definen:

- **Vacío:** cuando no hay datos → un mensaje claro y, si aplica, una acción ("Aún no hay X. Crear el primero").
- **Cargando:** mientras trae datos → un indicador (spinner/skeleton), no una pantalla congelada.
- **Error:** cuando algo falla → un mensaje entendible y accionable, **nunca** una traza técnica (`05`·E3).

```
INCORRECTO: la tabla aparece vacía sin explicar si no hay datos o si falló la carga
CORRECTO:   estado vacío ("no hay registros"), estado cargando, y estado de error diferenciados
```

## I2 · Feedback de validación claro

Cuando el usuario se equivoca en un formulario, se le dice **qué campo** y **qué falta**, en su idioma (`01`·C8), antes o al enviar. No se rechaza en silencio ni con un mensaje genérico.

```
INCORRECTO: "Error al guardar" sin decir qué campo está mal
CORRECTO:   "El correo no es válido" junto al campo correspondiente
```

## I3 · Accesibilidad mínima

- Campos con **etiqueta** asociada; imágenes con texto alternativo.
- **Contraste** suficiente entre texto y fondo.
- Navegable por **teclado**, con el **foco visible**.
- No transmitir información **solo** por color.

> El nivel exigido (p. ej. WCAG AA) y si es obligatorio por ley lo declara la capa 3 / `16` (accesibilidad).

## I4 · Texto para el usuario, no jerga

Lo que el usuario lee se entiende sin ser del oficio: **claro, directo, que hasta un niño lo entienda**. Sin siglas internas, sin códigos de sistema, sin jerga técnica. (Esto es lo contrario del estilo de las reglas del agente, que sí es técnico — acá el lector es una persona usando el producto.)

```
INCORRECTO: "Error 422: constraint violation en FK proyecto_id"
CORRECTO:   "No se pudo guardar: primero elegí un proyecto"
```

## I5 · Consistencia con el sistema de diseño

Usar los componentes y patrones que el proyecto ya tiene (el sistema de diseño lo declara la capa 3) antes de inventar unos nuevos. Una pantalla nueva se parece a las demás: mismos componentes, misma ubicación de las acciones, mismos estados.

## I6 · Adaptable

La interfaz se ve y funciona en los tamaños de pantalla que el proyecto soporta (declarados en capa 3). El contenido ancho (tablas, diagramas) no rompe el layout: se desplaza en su propio contenedor.

---

Ver: `01`·C8 (idioma del proyecto), `05`·E3 (mensajes de error accionables), `16` (accesibilidad/WCAG si aplica). El framework y el sistema de diseño concretos van en la capa 3.
