<!-- sesion: c1d6c769-8894-4763-9898-0b9dc23d8b8a -->
<!-- nombre: preguntado -->

# 2026-08-28 — Plantilla manual instalacion

## Conversación

### 1 · Usuario — 2026-08-28 23:31:47
> <ide_selection>The user selected the lines 1 to 3 from Untitled-1:
> 1 · La comprobación de sesiones no distingue «nadie más lo tocó» de «no tengo registro».
> Es la única que dejó pasar daño real hoy: 712 líneas ajenas en un commit mío, y dijo OK.
>
>
> This may or may not be related to the current task.</ide_selection>
> # Prompt: Crear plantilla base para manual de instalación de proyectos
>
> Actúa como un **arquitecto de software y especialista en documentación técnica**, responsable de definir una estructura estándar, clara y reutilizable para los manuales de instalación de diferentes proyectos de software.
>
> ## Objetivo
>
> Crear la **estructura base de una plantilla de Manual de Instalación** que pueda utilizarse como punto de partida para múltiples proyectos, independientemente de su lenguaje de programación, framework, sistema operativo, arquitectura o infraestructura.
>
> La plantilla **no debe estar diseñada para un proyecto específico**. Debe utilizar variables, campos parametrizables y secciones genéricas que posteriormente puedan completarse con la información particular de cada proyecto.
>
> ## Principios
>
> La plantilla debe:
>
> 1. Ser reutilizable para diferentes proyectos.
> 2. Separar claramente la información general de la información específica del proyecto.
> 3. Permitir documentar instalaciones locales, servidores, ambientes de desarrollo, pruebas y producción.
> 4. Explicar no solamente **qué comando ejecutar**, sino también:
>
>    * dónde ejecutarlo;
>    * en qué ambiente;
>    * con qué usuario;
>    * qué requisito debe estar instalado;
>    * qué resultado se espera;
>    * cómo verificar que la instalación fue exitosa.
> 5. Diferenciar claramente entre:
>
>    * comandos que se ejecutan en el equipo local;
>    * comandos que se ejecutan dentro del servidor;
>    * comandos que se ejecutan dentro de un contenedor;
>    * comandos que se ejecutan desde una herramienta específica.
> 6. Evitar asumir que todos los proyectos utilizan Windows, Linux, Docker, Git, Laravel, Angular, PHP, Python u otra tecnología específica.
> 7. Permitir incorporar instrucciones específicas cuando el proyecto lo requiera.
> 8. Ser suficientemente estructurada para que otra IA pueda utilizarla posteriormente para generar el manual concreto de un proyecto.
>
> ## Estructura requerida
>
> Diseña una estructura profesional que contemple, como mínimo, las siguientes secciones:
>
> ### 1. Información general
>
> Incluir campos para:
>
> * Nombre del proyecto.
> * Código o identificador del proyecto.
> * Versión.
> * Fecha.
> * Responsable.
> * Versión del manual.
> * Estado del documento.
> * Ambiente al que aplica.
>
> ### 2. Objetivo del manual
>
> Definir el propósito del documento y qué proceso de instalación cubre.
>
> ### 3. Alcance
>
> Indicar qué componentes, ambientes e infraestructura están incluidos y cuáles están fuera del alcance.
>
> ### 4. Arquitectura y componentes
>
> Crear una sección para describir brevemente los componentes que deben instalarse, por ejemplo:
>
> * Frontend.
> * Backend.
> * Base de datos.
> * Servidor web.
> * Servicios adicionales.
> * Colas.
> * Caché.
> * Almacenamiento.
> * Servicios externos.
> * Contenedores.
> * Otros componentes.
>
> No asumir tecnologías concretas.
>
> ### 5. Requisitos previos
>
> Crear una tabla parametrizable con:
>
> | Requisito | Versión | Obligatorio | Verificación | Observaciones |
> | --------- | ------- | ----------- | ------------ | ------------- |
>
> Incluir también requisitos relacionados con:
>
> * Sistema operativo.
> * Hardware.
> * Software.
> * Dependencias.
> * Acceso a red.
> * Acceso al servidor.
> * Credenciales.
> * Permisos.
> * Puertos.
> * Variables de entorno.
> * Repositorios.
> * Certificados.
> * Servicios externos.
>
> ### 6. Ambientes y servidores
>
> Crear una sección que permita identificar claramente los diferentes ambientes:
>
> * Desarrollo.
> * Pruebas.
> * QA.
> * Producción.
>
> Para cada ambiente permitir documentar:
>
> * Nombre.
> * Dirección/IP o hostname.
> * Sistema operativo.
> * Usuario requerido.
> * Servicios.
> * Puertos.
> * Ubicación de la aplicación.
> * Observaciones.
>
> Cuando existan instrucciones diferentes entre ambientes, deben quedar claramente separadas.
>
> ### 7. Herramientas de acceso
>
> Crear una sección para documentar las herramientas utilizadas para acceder o administrar los ambientes.
>
> Por ejemplo:
>
> * SSH.
> * Cliente SSH.
> * RDP.
> * VPN.
> * Terminal.
> * Herramientas de administración remota.
>
> Para cada herramienta documentar:
>
> * Nombre.
> * Versión.
> * Propósito.
> * Cómo se obtiene.
> * Configuración requerida.
> * Procedimiento básico de conexión.
>
> Si el proyecto utiliza una herramienta concreta, esta sección debe poder reemplazarse sin modificar la estructura general del manual.
>
> ### 8. Ubicación de los comandos
>
> Crear una sección explicativa que establezca una convención clara para indicar **dónde debe ejecutarse cada comando**.
>
> Definir etiquetas como:
>
> * `[LOCAL]` → terminal del equipo del usuario.
> * `[SERVIDOR]` → terminal después de conectarse al servidor.
> * `[CONTENEDOR]` → terminal dentro del contenedor.
> * `[BASE DE DATOS]` → consola de la base de datos.
> * `[HERRAMIENTA]` → comando ejecutado desde una herramienta específica.
>
> La plantilla debe establecer que **ningún comando importante debe aparecer sin indicar previamente dónde debe ejecutarse**.
>
> Incluir un ejemplo genérico para demostrar esta convención.
>
> ### 9. Obtención del código fuente
>
> Crear una sección para documentar:
>
> * Repositorio.
> * Rama o versión.
> * Método de descarga.
> * Credenciales o permisos necesarios.
> * Ubicación del código.
> * Validación de la versión obtenida.
>
> ### 10. Configuración del proyecto
>
> Crear una sección parametrizable para documentar:
>
> * Variables de entorno.
> * Archivos de configuración.
> * Credenciales.
> * Conexiones a servicios.
> * Configuración de base de datos.
> * URLs.
> * Puertos.
> * Claves.
> * Certificados.
> * Parámetros específicos.
>
> No incluir valores reales sensibles.
>
> ### 11. Instalación de dependencias
>
> Crear una estructura genérica para documentar las dependencias de cada componente.
>
> Para cada dependencia indicar:
>
> * Nombre.
> * Versión.
> * Componente al que pertenece.
> * Comando de instalación.
> * Ubicación donde se ejecuta.
> * Verificación.
>
> ### 12. Base de datos
>
> Crear una sección que permita documentar:
>
> * Motor.
> * Versión.
> * Host.
> * Puerto.
> * Base de datos.
> * Usuario.
> * Creación de esquemas.
> * Migraciones.
> * Scripts.
> * Carga inicial.
> * Datos de configuración.
> * Validación de conexión.
>
> No asumir ningún motor específico.
>
> ### 13. Instalación y configuración de componentes
>
> Crear subsecciones independientes para los componentes que tenga cada proyecto.
>
> Ejemplo:
>
> * Frontend.
> * Backend.
> * API.
> * Servidor web.
> * Worker.
> * Procesos programados.
> * Servicios auxiliares.
>
> La plantilla debe permitir agregar o eliminar componentes sin romper la estructura del manual.
>
> ### 14. Servicios y procesos
>
> Crear una sección para documentar servicios que deban quedar ejecutándose.
>
> Para cada servicio:
>
> * Nombre.
> * Propósito.
> * Comando.
> * Ubicación de ejecución.
> * Usuario.
> * Puerto.
> * Forma de inicio.
> * Forma de detenerlo.
> * Forma de verificarlo.
> * Logs.
>
> ### 15. Configuración del servidor
>
> Crear una sección para documentar configuraciones relacionadas con:
>
> * Servidor web.
> * Firewall.
> * Puertos.
> * Permisos.
> * Directorios.
> * Usuarios.
> * Procesos.
> * Certificados.
> * Variables de entorno.
> * Servicios del sistema.
>
> ### 16. Despliegue
>
> Crear un procedimiento ordenado para pasar la aplicación desde el código fuente hasta un ambiente operativo.
>
> Debe incluir:
>
> 1. Preparación.
> 2. Obtención del código.
> 3. Configuración.
> 4. Instalación de dependencias.
> 5. Base de datos.
> 6. Compilación o construcción.
> 7. Configuración de servicios.
> 8. Inicio.
> 9. Validación.
>
> ### 17. Verificación de la instalación
>
> Crear una lista de comprobaciones que permita determinar objetivamente si la instalación fue exitosa.
>
> Incluir:
>
> * Aplicación disponible.
> * Frontend funcionando.
> * Backend funcionando.
> * API respondiendo.
> * Base de datos accesible.
> * Servicios activos.
> * Puertos disponibles.
> * Procesos ejecutándose.
> * Logs sin errores críticos.
> * Funcionalidad básica validada.
>
> ### 18. Prueba funcional posterior a la instalación
>
> Crear una sección para realizar una prueba mínima que permita confirmar que el sistema no solamente está instalado, sino que **funciona correctamente**.
>
> ### 19. Solución de problemas
>
> Crear una tabla estándar:
>
> | Problema | Posible causa | Diagnóstico | Solución | Verificación |
> | -------- | ------------- | ----------- | -------- | ------------ |
>
> Incluir problemas relacionados con:
>
> * Dependencias.
> * Permisos.
> * Puertos.
> * Base de datos.
> * Variables de entorno.
> * Servicios.
> * Red.
> * Credenciales.
> * Certificados.
> * Comandos ejecutados en el lugar incorrecto.
>
> ### 20. Mantenimiento y operaciones posteriores
>
> Documentar las operaciones necesarias después de la instalación:
>
> * Reinicio.
> * Actualización.
> * Despliegue de nuevas versiones.
> * Limpieza.
> * Logs.
> * Backups.
> * Restauración.
> * Migraciones.
> * Verificación de servicios.
>
> ### 21. Seguridad
>
> Crear una sección para documentar:
>
> * Gestión de credenciales.
> * Usuarios.
> * Permisos.
> * Secretos.
> * Certificados.
> * Puertos expuestos.
> * Accesos remotos.
> * Variables sensibles.
>
> Nunca incluir contraseñas, tokens, claves privadas ni secretos reales.
>
> ### 22. Reversión / rollback
>
> Crear un procedimiento para regresar a la versión anterior cuando una instalación o actualización falle.
>
> ### 23. Checklist final
>
> Crear un checklist reutilizable:
>
> * [ ] Requisitos instalados.
> * [ ] Acceso validado.
> * [ ] Código obtenido.
> * [ ] Dependencias instaladas.
> * [ ] Configuración realizada.
> * [ ] Base de datos configurada.
> * [ ] Servicios configurados.
> * [ ] Aplicación iniciada.
> * [ ] Pruebas realizadas.
> * [ ] Logs revisados.
> * [ ] Instalación aprobada.
>
> ### 24. Control de cambios
>
> Crear una tabla:
>
> | Versión | Fecha | Cambio realizado | Responsable |
> | ------- | ----- | ---------------- | ----------- |
>
> ### 25. Anexos
>
> Dejar espacio para:
>
> * Comandos frecuentes.
> * Configuraciones.
> * Diagramas.
> * Puertos.
> * Variables de entorno.
> * Referencias.
> * Información adicional.
>
> ## Reglas para construir la plantilla
>
> * No inventes información técnica del proyecto.
> * No asumas tecnologías.
> * No incluyas credenciales reales.
> * Utiliza placeholders como `<NOMBRE_PROYECTO>`, `<VERSION>`, `<SERVIDOR>`, `<PUERTO>`, `<USUARIO>`, `<RUTA_APLICACION>`.
> * Cada comando debe indicar explícitamente **dónde se ejecuta**.
> * Cada procedimiento debe indicar:
>
>   1. Precondición.
>   2. Acción.
>   3. Resultado esperado.
>   4. Validación.
> * Cuando existan diferentes sistemas operativos o tecnologías, utilizar subsecciones específicas sin alterar la estructura principal.
> * Mantener una numeración consistente.
> * La estructura debe ser suficientemente genérica para reutilizarla en diferentes proyectos.
> * Evitar explicaciones innecesariamente extensas.
> * Priorizar instrucciones claras, verificables y ejecutables.
> * El documento debe poder ser utilizado tanto por un desarrollador como por una persona encargada de desplegar o instalar el sistema.
>
> ## Resultado esperado
>
> Entrega únicamente la **estructura base de la plantilla del Manual de Instalación**, con sus títulos, subtítulos, tablas, placeholders y convenciones.
>
> No llenes la plantilla con información de un proyecto específico.
>
> El resultado debe quedar preparado para que, posteriormente, otro proceso pueda recibir la información técnica de un proyecto y completar automáticamente esta plantilla para generar su **Manual de Instalación específico**.
>
>
> crearlo en: manual-instalacion.md

**Agente** — 2026-08-28 23:40:10
<!-- agente: b4c75537-d011-42c7-860b-fa942f4789fd -->

Ya existe [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md) (407 líneas, misma finalidad). Antes de decidir si se reemplaza, construyo la plantilla con la estructura que pediste, sin tocar la existente.

Heredoc falló por el manejo de comillas; uso Write.

Creado [manual-instalacion.md](manual-instalacion.md) (656 líneas) en la raíz del repo, con las 25 secciones que pediste más un preámbulo de convenciones.

Lo que trae:

- **Molde de procedimiento** de cuatro partes (precondición, acción, resultado esperado, validación) declarado una sola vez y usado en cada paso, con un quinto renglón «Si sale otra cosa» que enruta a la sección 19.
- **Etiquetas de ubicación** `[LOCAL]`, `[SERVIDOR]`, `[CONTENEDOR]`, `[BASE DE DATOS]`, `[HERRAMIENTA]` (sección 8), con el ejemplo genérico y la línea de usuario y directorio.
- **Bloques repetibles** marcados en ambientes (6.2), herramientas (7.N), dependencias (11.N), componentes (13.N) y servicios (14.N): se copian o se borran sin que cambie la numeración de las demás secciones.
- **Recuadros «Para quien escribe»** en cada sección que lo necesita: dicen qué va ahí y de dónde sale el dato. Son las instrucciones que otro proceso lee para llenarla, y el paso 5 del encabezado manda borrarlas antes de publicar.
- Placeholders `<NOMBRE_PROYECTO>`, `<SERVIDOR>`, `<PUERTO>`, `<USUARIO>`, `<RUTA_APLICACION>` y compañía; ninguna tecnología ni credencial concreta.

Pasé [validadores/marcas.py](validadores/marcas.py) sobre el archivo: 0 marcas.

**Un asunto que hay que decidir.** Ya existía [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md), 407 líneas, misma finalidad y bastante madura, con su propia estructura (14 secciones, orientada a dos piezas y a la ejecución real previa). No la toqué. Ahora hay dos plantillas para lo mismo, que es justo lo que prohíbe `20·M12`. Las opciones:

1. Fundir las dos en `plantillas/manual-instalacion.md`: la nueva aporta ambientes, herramientas de acceso, etiquetas de ubicación, reversión y anexos; la vieja aporta las reglas de redacción, la carpeta `seguimiento/` y el glosario. Esto sería cambio de `plantillas/`, así que arrastra la cadena de `pendientes/` a historia y fase, más `CHANGELOG.md` y `VERSION`.
2. Dejar la nueva donde está, como documento suelto de trabajo, y no tocar el estándar.
3. Reemplazar la vieja por la nueva (borra 407 líneas: no lo hago sin que lo apruebes explícitamente).

¿Cuál seguimos? Y aparte: no he hecho `commit`.

### 2 · Usuario — 2026-08-28 23:48:50
> adapte la plantilla del manual de instalación al español colombiano, debe ser redactado en tercera persona y en enfinitivo y debe seguir el patrón anti IA

**Agente** — 2026-08-28 23:53:04
<!-- agente: 442efa89-c072-4aa3-9969-b42315aca1fd -->

Adaptada la plantilla. Cambios en [manual-instalacion.md](manual-instalacion.md):

**Infinitivo para las acciones, tercera persona para lo que se explica.** Quité el impersonal con «se» de todas las frases que son una acción de quien escribe o de quien instala: «Se copia para cada proyecto y se llena» pasó a «para cada proyecto hay que copiarla y llenarla»; «se reemplaza este bloque» a «basta con reemplazar este bloque»; «Se escribe antes de necesitarlo y se prueba» a «Escribirlo antes de necesitarlo y probarlo»; «lo primero que se revisa» a «lo primero que hay que revisar». Quedan con «se» solo los rótulos de tabla («En qué paso se llena») y las frases que describen el sistema o la norma («Los controles de seguridad no se apagan nunca»), que es donde corresponde.

**La convención quedó escrita en la regla 9**, con la parte que faltaba: el impersonal con «se» no sirve para las acciones, y lo que aparece en pantalla va citado tal cual aunque diga «usted».

**Patrón anti IA.** Pasé [validadores/marcas.py](validadores/marcas.py): 0 marcas. Además, a mano:

- Bajé la negrita de renglón completo a la palabra que importa en las nueve convenciones («**Cuatro partes por procedimiento**», «**Nada por supuesto**»), que era la marca de la sección 2 del anexo.
- Saqué la fórmula «no solo... que está instalado» de la sección 18, reemplazada por «Estar instalado no es funcionar, y esta sección comprueba lo segundo».
- Quité «permite» («Es lo que permite volver atrás» pasó a «Sin eso no hay cómo volver atrás»).
- Los cuatro puntos medios en prosa ya habían salido antes; el único que queda está en celda de tabla, que el anexo exime.

**Español colombiano.** Revisé léxico y tiempos verbales contra la sección 5 del anexo: no hay *ordenador*, *fichero*, *móvil*, *vosotros*, ni pretérito compuesto donde acá va el simple. Ya usaba *computador*, *archivo*, *carpeta*.

Sigue sin resolver lo de la sesión anterior: hay dos plantillas para lo mismo, esta y [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md), que es lo que prohíbe `20·M12`. No he commiteado nada.

Y por el histórico: esta sesión la guardo como `2026-08-28-plantilla-manual-instalacion.md` — se creó la plantilla base del manual de instalación y se adaptó a la norma de redacción del estándar, ¿va?

### 3 · Usuario — 2026-08-29 07:48:32
> si

**Agente** — 2026-08-29 07:52:32
<!-- agente: 69a48d68-ab06-4eff-b542-b01324abf200 -->

Hecho. La sesión quedó como `2026-08-28-plantilla-manual-instalacion.md`, con su línea en el índice, y escribí el resumen que estaba vacío: [historico-chat/resumenes/2026-08-28/plantilla-manual-instalacion.md](historico-chat/resumenes/2026-08-28/plantilla-manual-instalacion.md), con tres hallazgos.

- **H-1.** Quedaron dos plantillas para el mismo documento, la nueva en la raíz y la de `plantillas/`. Sigue sin decidir.
- **H-2.** La norma de redacción que me pediste (español colombiano, tercera persona, infinitivo) no existe en `base/`: solo está escrita dentro del cuerpo de dos plantillas, como regla 11. El anexo [marcadores-de-ia.md](base/00-identidad-y-rol/marcadores-de-ia.md) ya lo declara en su cierre: esa regla «todavía no existe». Por eso la apliqué copiándola de [plantillas/manual-usuario.md](plantillas/manual-usuario.md) y no citando el estándar.
- **H-3.** [validadores/marcas.py](validadores/marcas.py) dio cero sobre la plantilla cuando todavía tenía tres marcas de la lista. Solo cuenta las secciones 2 y 3 del anexo; las demás piden leer, y la salida no lo dice.

Falta tu `/rename plantilla-manual-instalacion` para que la pestaña y `/resume` queden con el mismo nombre: ese comando no lo puedo escribir yo.

Dos cosas pendientes de tu parte: los tres hallazgos están como «pendiente por crear» y el resumen no se puede cerrar hasta que existan los archivos en [pendientes/](pendientes/), ¿los creo? Y sigue abierta la decisión de H-1. No he commiteado nada.

### 4 · Usuario — 2026-08-29 08:02:15
> la plantilla es manual-instalacion no hay más

**Agente** — 2026-08-29 08:11:28
<!-- agente: 4ba652f3-ea2e-4992-8a84-bba2d20c43ee -->

La consolido en una sola, en `plantillas/`, conservando lo que la versión anterior exigía y la nueva no traía.

Hecho: hay una sola plantilla, [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md), 777 líneas. Borré el archivo de la raíz.

**Qué quedó adentro.** La estructura nueva (25 secciones, etiquetas de ubicación, ambientes, herramientas de acceso, reversión, anexos) más lo que la versión anterior exigía y la nueva no traía:

- Las reglas de redacción de la cabecera, que pasaron de 9 a 13: decir qué es cada cosa la primera vez, mirar cómo está antes de cambiar algo, y releer preguntando si alguien que nunca abrió una terminal sabría qué tecla oprimir.
- La regla 12, que es la más propia del molde: lo escrito se ejecuta en una máquina real, la salida queda en `seguimiento/`, y lo que se aprendió se vuelve paso o bifurcación, nunca relato. Nada marcado «(por verificar)».
- El control de cambios sin motivos históricos, la lista de comprobación antes de publicar completa, el aviso de no correr correcciones automáticas de dependencias, y el paso «decir a dónde apunta» para los componentes que se compilan, que es el que más falla.

**Versionado** ([`20·M10`](base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)): `35.10.0` en [CHANGELOG.md](CHANGELOG.md) y [VERSION](VERSION). Lo puse **MENOR** porque ninguna regla de `base/` obliga a que un manual ya escrito siga la plantilla vigente: el que exista se conserva.

**Comprobado:** `validar.py versionado` da 0 fallas (el único aviso es el de la 15.4.0 duplicada, que ya estaba reconocido en el registro). `validar.py marcas` no reporta ni una línea de la plantilla nueva.

El resumen de la sesión ya tiene H-1 cerrado, con lo que se decidió y dónde quedó.

Dos cosas: [plantillas/manual-usuario.md](plantillas/manual-usuario.md) aparece modificado en `git status`, pero eso venía de antes de esta sesión, no lo toqué. Y siguen abiertos H-2 y H-3 sin su archivo en [pendientes/](pendientes/), que es lo que falta para poder cerrar la sesión: ¿los creo? Nada commiteado.

### 5 · Usuario — 2026-08-29 11:47:58
> esto ya quedó: "1 · La comprobación de sesiones no distingue «nadie más lo tocó» de «no tengo registro».
> Es la única que dejó pasar daño real hoy: 712 líneas ajenas en un commit mío, y dijo OK.
> " respuesta si o no

**Agente** — 2026-08-29 11:49:09
<!-- agente: 76ed8cf3-75d5-4797-ad2a-8e245093a1d3 -->

**Sí.** Está en [validadores/sesiones.py](validadores/sesiones.py), documentado en el propio archivo como `EP-005·HU-020`, con el caso de las 712 líneas nombrado y las señales `S-071` y `S-072`.

Un matiz sobre cómo quedó, porque no es lo que decía el reclamo: **no se hizo que la comprobación distinguiera los dos casos, se le quitó el hueco al registro.** Avisar de «no tengo registro» se evaluó y se descartó porque habría hablado en 7 de los últimos 12 commits, con hasta 31 archivos: el registro solo se llenaba desde las herramientas de escritura, y casi todo lo escriben guiones de la terminal, así que «sin registro» significaba «escrito como se escribe casi todo».

Lo que quedó es [`anotar_el_turno`](validadores/sesiones.py#L124), que anota lo que cambió desde la vuelta anterior mirando `git status` y las fechas, sin importar qué lo escribió. Si otra sesión escribe mientras esta trabaja, las dos lo anotan y la comprobación que ya existía ve la colisión.

Está enganchado en [adaptadores/claude-code/hook_turno.py:54](adaptadores/claude-code/hook_turno.py#L54), tiene pruebas en `validadores/pruebas.py`, y está corriendo: el registro de esta sesión ya trae los cinco archivos que tocamos hoy.

### 6 · Usuario — 2026-08-29 11:51:28
> <ide_selection>The user selected the lines 4 to 5 from Untitled-1:
> 2 · 13 historias en rojo. Ocho sin fase posterior; cinco con una que no resolvió el rojo. Desde hoy tienen forma de cerrarse.
>
>
> This may or may not be related to the current task.</ide_selection>
> esto;
> 2 · 13 historias en rojo. Ocho sin fase posterior; cinco con una que no resolvió el rojo. Desde hoy tienen forma de cerrarse.
> ?

**Agente** — 2026-08-29 11:54:08
<!-- agente: 1958b9bc-7c95-49a5-b4bb-ae97991e138d -->

**No, la mitad.** El mecanismo sí; las 13 historias no.

**Lo que sí quedó:** la forma de cerrar un rojo existe y está publicada. Es `EP-004·HU-023`, commit `b3df9f1`, con su fase en estación 13. Una fase declara en su `funcionalidad_implementada.md` el campo **«Reemplaza el veredicto de»**, y [`veredictos_reemplazados`](validadores/fases.py#L671) saca ese rojo de la cuenta con tres condiciones: quien declara tiene que cumplir, la fase nombrada tiene que ser de la misma historia, y no puede nombrarse a sí misma. El veredicto viejo no se toca ([`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)): el rastro de que estuvo en rojo es la información.

**Lo que no quedó:** las 13 siguen en rojo hoy. Acabo de medirlo con el propio contador del repo, `fases.por_veredicto('.')`: **96 cumplen, 13 no cumplen, 5 sin veredicto**. Y el desglose de tu línea sigue exacto: el script [medir-rojos-superados.py](historico-chat/scripts/2026-08-27/medir-rojos-superados.py) cuenta 16 historias con fase roja, 8 con fase posterior y 8 sin ninguna. Solo cuatro archivos del árbol traen el campo «Reemplaza el veredicto de», y uno de esos cuatro es la fase de la propia HU-023. O sea: **tres rojos cerrados con el mecanismo, de los dieciséis.** 16 menos 3 son los 13, y de esos, ocho no tienen fase posterior y cinco la tienen sin haber vuelto a medir el criterio rojo.

Las ocho que no tienen ninguna fase posterior son rojos vivos de verdad: `HU-003-nucleo-que-no-se-sobrescribe`, `HU-006-capa-propia-del-proyecto`, `HU-001-numero-de-version-y-que-significa`, `HU-001-que-se-guarda-tipos-y-alcances`, `HU-002-guardar-en-el-repositorio`, `HU-005-separar-aprendizaje-de-preferencia`, `HU-006-sacar-del-almacen-local` y `HU-002-mostrar-antes-de-hacer`. Esas no se cierran declarando: hay que hacer el trabajo.

### 7 · Usuario — 2026-08-29 11:54:22
> terminélo

**Agente** — 2026-08-29 12:11:24
<!-- agente: 1435e779-c3ff-4eb8-8a1d-76fb2b762060 -->

"Terminarlo" son 13 historias. Primero mido las 5 que pueden cerrarse declarando, para saber cuáles de verdad ya cumplen hoy. Las 8 sin fase posterior son trabajo nuevo y las trato aparte.

Dos de cinco ya cumplen hoy. Sigo con las otras tres.

Las cinco miden verde hoy. Antes de escribir las fases de cierre, miro cómo se hizo el cierre masivo del último commit.

El precedente de la casa: el molde se aprueba una vez y **las cifras de cada fase las mide un programa**, con el criterio de suspensión dentro. Escribo el medidor de los cinco.

Medición reproducible: **5 de 5 se pueden cerrar declarando**. Ahora leo el molde de la fase de cierre para generar las cinco con las cifras medidas.

Tengo el molde y los datos. Escribo el generador, con el criterio de suspensión adentro: la fase que no mida verde no se escribe.

Cuenta movida: **13 rojos → 8**. Ahora pongo al día el `Estado` de las cinco historias.

**Terminado lo que se podía cerrar midiendo: la cuenta pasó de 13 rojos a 8.**

Medí los cinco criterios ejecutándolos, no leyéndolos, y los cinco cumplen hoy:

| Historia | Criterio que estaba en rojo | Qué salió al ejecutarlo |
|---|---|---|
| EP-002 · HU-003 | Una versión que no existe se detecta | `99.9.9` ahora sale como **falla**; antes pasaba en silencio y apagaba el aviso de desfase |
| EP-002 · HU-004 | El aviso llega al abrir sesión | Sale, y la apertura pasa por él: `hook_sesion` → `sesion.revisar` → `version.validar` |
| EP-004 · HU-003 | Un `.md` ilegible no tumba la corrida | Termina en 0, sin volcado, **y sigue contando las 2 marcas del archivo legible** |
| EP-005 · HU-003 | El grave detiene, el resto avisa | El enlace roto devuelve 2; el documento sano, 0 |
| EP-005 · HU-008 | La corrida en una sesión real | El enganche está colgado, y esta sesión dejó su resumen con el índice coherente tras renombrar |

**Cómo, y por qué así.** Seguí el precedente de `af3dbd1`: el molde de fase se aprueba una vez para las cinco, y las cifras de cada documento las mide un programa. Son dos guiones en [historico-chat/scripts/2026-08-29/](historico-chat/scripts/2026-08-29/): el medidor, que ejecuta cada criterio con su contraprueba, y el generador, que **no escribe la fase de una historia cuya medición salga en rojo**. El criterio de suspensión vive dentro del programa, no en la buena voluntad de quien lo corre.

Cada una de las cinco fases nuevas declara en su cierre el campo **«Reemplaza el veredicto de»**, que es el mecanismo de `EP-004·HU-023`. Ningún veredicto viejo se tocó ([`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)): el rastro de que estuvieron en rojo sigue ahí.

**Comprobado:** `validar.py fases` da 0 fallas y su línea dice **123 HU · 9 sin terminar · 114 terminadas, de las cuales 101 cumplen, 8 no cumplen y 5 no dicen si cumplen**. `trazabilidad`, `indices` y `estandar`, 0 fallas. `marcas` no reporta ni una línea de los 25 documentos nuevos. Cero enlaces rotos.

Puse al día el `Estado` y la tabla de fases de las cinco historias.

**Lo que no quedó, y por qué.** Las 8 restantes no tienen ninguna fase posterior: son rojos vivos de verdad y no se cierran declarando, hay que hacer el trabajo. Cada una necesita su propia fase con su plan, sus pruebas y sus puertas de aprobación, así que no las toqué.

Y encontré algo de paso: **26 archivos `.md` traen un `U+0001` pegado dentro**, 13 en `documentacion/`. Rompe la fila de una tabla en silencio, no se ve leyendo, y `marcas.py` no lo cuenta. No lo arreglé: son archivos ajenos al trabajo de hoy y los metería en un commit que no habla de eso. Quedó como H-5 en el resumen.

Las cinco fases están en estación 12 esperando autorización del commit. **No he commiteado nada.**

### 8 · Usuario — 2026-08-30 09:47:03
> haga commit, push y muestre lo que falta
