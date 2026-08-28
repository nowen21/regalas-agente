# Manual de instalación — «nombre del sistema»   ·   `[CAPA 3]`

> **Qué es este archivo.** Es la **base** de un manual de instalación: tiene todas las partes que un
> manual de instalación debe llevar, en el orden en que se ejecutan, y en cada parte dice **qué va
> ahí, cómo se escribe y de dónde se saca la información**. No está atado a ningún sistema ni a ninguna
> herramienta: se copia para cada desarrollo y se llena con lo de ese desarrollo. Cuando todas las
> partes están llenas, la copia **es** el manual.
>
> **Cómo se usa.** 1) Copiar este archivo con el nombre del sistema. 2) Reemplazar cada «así» por el
> dato real. 3) Llenar cada sección siguiendo su recuadro 📋. 4) Borrar los recuadros 📋: son
> instrucciones para quien escribe, y la persona que instala nunca debe verlos. 5) Ejecutar el manual
> completo en una máquina real antes de publicarlo. 6) Pasar la lista de comprobación del final.
>
> Cubre los tres momentos de la vida de una instalación: **instalar desde cero**, **actualizar** una
> instalación que ya existe, y **mantener** la que está funcionando. Si el sistema tiene varias piezas
> (por ejemplo, una parte que ve la gente y una parte que guarda los datos), cada pieza tiene su
> propia parte del manual, en el orden en que se instalan.
>
> Base creada el **2026-08-27**.

---

## Reglas para escribir el manual (leerlas antes de llenar cualquier parte)

Lo va a seguir alguien que **no conoce el sistema** y que puede no haber instalado nunca una aplicación
en un servidor. Por eso:

1. **Cada paso tiene cuatro partes, siempre en este orden:** *qué se va a hacer y por qué*, *el
   comando o la acción exacta, para copiar y pegar*, *lo que debe salir en pantalla* y *qué significa
   y qué hacer si sale otra cosa*. Un comando suelto no es un paso.
2. **Ningún comando sin decir dónde se escribe:** «en su computador» o «dentro del servidor (después de
   entrar)». Confundirlos es la causa más común de que «no funcione».
3. **Decir qué es cada cosa la primera vez.** «Servidor (el computador, normalmente en otro sitio,
   donde el sistema queda funcionando para todos)». «Terminal (la ventana donde se escriben comandos
   en texto)».
4. **Nunca dar por hecho que algo está instalado.** Cada requisito lleva primero el comando para
   **comprobar** si ya está, y solo después el comando para instalarlo.
5. **Antes de cambiar algo, mirar cómo está.** Cada paso que escribe o borra empieza con «ver el estado
   actual», y dice cómo volver atrás.
6. **Ninguna contraseña, clave ni secreto escrito en el manual.** Se dice de dónde sale y quién lo
   entrega. Lo que se escribió alguna vez en un documento se considera conocido y hay que cambiarlo.
7. **Lo que se escribe se ejecuta.** Ninguna sección se da por buena sin haberla corrido en una máquina
   real, con su salida guardada en una carpeta `seguimiento/` junto al manual. Lo no ejecutado se marca
   «(por verificar)».
8. **Un paso, una cosa.** Si un paso tiene «y», probablemente son dos pasos.
9. **Comprobar al final de cada paso, no al final del manual.** Si algo falla, se sabe en qué paso.
10. **Releer preguntando: «¿alguien que nunca ha abierto una terminal sabría qué tecla pulsar?».**

---

## 0. Portada e identificación

> 📋 **Qué va aquí:** nombre del sistema, versión del código que instala este manual (del código, no
> del manual), fecha, sistema operativo y versiones para las que se probó, y en qué máquina se probó.
> **De dónde sale:** de la etiqueta o marca de versión del código y del registro de la instalación
> real que se hizo para escribirlo.

| Dato | Valor |
|---|---|
| Sistema | «nombre del sistema» |
| Versión del código que instala | «marca de versión de cada pieza» |
| Probado en | «sistema operativo y versión» · «versiones de las herramientas necesarias» |
| Fecha de este manual | «fecha» |
| Tiempo estimado | «medido en la última instalación real» |

---

## 1. Cómo leer este manual

> 📋 **Qué va aquí:** las convenciones para el lector: cómo se muestran los comandos, cómo se distingue
> lo que se escribe de lo que sale, los avisos, y qué hacer si un paso falla (parar, no seguir).
> **Cómo se escribe:** un ejemplo de cada cosa.

Modelo de lo que debe decir:

- Los bloques grises son comandos: se copian **completos**, se pegan en la terminal y se pulsa
  **Enter**. Si un bloque tiene varias líneas, se pegan de a una.
- Lo que empieza con `#` dentro de un bloque es una explicación, no se ejecuta.
- «**Debe salir:**» muestra lo que aparece si todo va bien. Si aparece otra cosa, **no siga**: vaya al
  «Si sale otra cosa» de ese paso o a la sección «Solución de problemas».
- `«así»` es un valor que usted reemplaza por el suyo (una dirección, un nombre de usuario).
- ⚠️ marca lo que no se puede deshacer o lo que afecta a otros sistemas de la misma máquina.

---

## 2. Qué se va a instalar y cómo queda armado

> 📋 **Qué va aquí:** el dibujo de las piezas y cómo se conectan, en palabras de todos los días. Sin
> esto el lector ejecuta comandos sin saber para qué, y no puede diagnosticar nada.
> **Cómo se escribe:** un diagrama y una tabla «pieza → qué hace → dónde queda → por dónde se habla
> con ella». Nombrar cada pieza por su función («la puerta de entrada», «la parte que guarda los
> datos») y, entre paréntesis, el nombre del programa concreto que se eligió para este sistema.
> **De dónde sale:** de la arquitectura del sistema y de cómo quedó montada la última instalación.

```
Quien usa el sistema (navegador o aplicación)
        │
        ▼
 «Puerta de entrada» (recibe todas las visitas y las reparte)
        ├── «parte visible»  → los archivos que ve la persona, en «carpeta»
        └── «parte de datos» → el servicio que hace el trabajo, escuchando solo dentro de la máquina
                                    │
                                    ├── «base de datos» (dónde está, quién la administra)
                                    ├── «correo saliente», si el sistema envía correos
                                    └── «otros programas de apoyo» (por ejemplo, uno que genera documentos)
```

| Pieza | Qué hace | Dónde queda | Por dónde se habla con ella |
|---|---|---|---|
| «pieza 1» | «…» | «carpeta o servicio» | «puerto o dirección; público o interno» |
| «pieza 2» | «…» | «…» | «…» |

---

## 3. Quién instala, y qué debe tener antes de empezar

> 📋 **Qué va aquí:** la lista de accesos y datos que hay que **pedir** antes de sentarse, a quién se le
> piden, y cuánto suelen tardar. Es la sección que evita quedarse a medias el primer día.
> **Cómo se escribe:** lista de chequeo. Por cada ítem: qué es, para qué paso se necesita, quién lo
> entrega. **Sin valores**: nunca la contraseña, solo «la entrega el área de ...».
> **De dónde sale:** de los requisitos del sistema y de lo que en la instalación anterior tocó pedir a
> otras áreas.

- [ ] Acceso a la máquina donde se instala (usuario, forma de entrar). Lo entrega «quién».
- [ ] Permiso para ejecutar como administrador en esa máquina.
- [ ] Credenciales de la base de datos. Las entrega «quién». ⚠️ Si traen caracteres especiales,
      ver la sección del archivo de configuración.
- [ ] Datos del correo saliente, si el sistema envía correos. Los entrega «quién».
- [ ] Confirmación de que la red deja llegar a la máquina desde donde estarán los usuarios. La da «quién».
- [ ] El paquete del código de cada pieza. Lo arma el equipo de desarrollo (la sección 9.1 dice cómo).
- [ ] Un computador propio con las herramientas para entrar a la máquina y para subir archivos.

---

## 4. Requisitos de la máquina

> 📋 **Qué va aquí:** cada programa que la máquina necesita, **con el comando para comprobar si ya
> está** y, solo si falta, el comando para instalarlo. Versiones mínimas.
> **Cómo se escribe:** una subsección por requisito, con las cuatro partes de la regla 1. Incluir los
> programas de apoyo que solo se usan en un momento puntual (por ejemplo, uno que convierte documentos):
> son los que se olvidan, y el sistema arranca bien y falla después.
> **De dónde sale:** del archivo de requisitos del proyecto y de lo que la instalación anterior
> descubrió que faltaba.

### 4.1 Sistema operativo, y quién más vive en la máquina
> 📋 Qué sistema operativo y versión. ⚠️ Si la máquina está **compartida con otro sistema**, decirlo
> aquí y nombrar qué no se puede tocar (sus archivos, su puerta de entrada, sus puertos). Cómo verlo.

### 4.2 «Lenguaje o entorno de ejecución de la parte de datos»
### 4.3 «Herramienta para compilar la parte visible», si hace falta
### 4.4 «Puerta de entrada» (el programa que recibe las visitas)
### 4.5 «Programas de apoyo» (los que se usan en un momento puntual)
### 4.6 Controles de seguridad del sistema operativo que van a aparecer
> 📋 Explicar en dos frases cada control que la máquina tenga activo: el que decide qué programa puede
> leer qué archivo, y el que decide qué puertos se ven desde fuera. Aclarar que **no se apagan**: se
> les da permiso puntual, y el manual dice cuál en cada paso.
### 4.7 Espacio en disco y memoria

---

## 5. Antes de tocar nada: inventario y respaldo

> 📋 **Qué va aquí:** los comandos para dejar escrito cómo estaba la máquina antes (usuarios, puertos en
> uso, archivos de configuración de la puerta de entrada, servicios activos) y cómo guardar copia de lo
> que se va a cambiar.
> **Por qué:** es lo que permite volver atrás y demostrar que lo que ya estaba no se tocó.
> **Cómo se escribe:** cada comando con su salida esperada, y la instrucción de guardar esa salida en
> `seguimiento/` con la fecha.

---

## 6. Parte A — Instalar «la parte de datos» (el servicio que hace el trabajo)

> 📋 **Cómo se escribe toda esta parte:** un paso por subsección, con las cuatro partes de la regla 1 y,
> al final de cada uno, «Si hay que deshacer lo hecho hasta aquí». El orden de abajo es el habitual;
> se ajusta al sistema, pero **la comprobación va siempre después del paso que comprueba**, no al final.
> **De dónde sale:** del manual anterior de esta pieza si existe (con sus correcciones aplicadas), del
> archivo de configuración de ejemplo del proyecto y de la instalación real.

### 6.1 Crear el usuario de servicio y la carpeta
> 📋 Por qué un usuario propio para este sistema y no reutilizar otro. Qué carpeta. Cómo deshacer.

### 6.2 Copiar el código a la máquina
> 📋 Qué contiene el paquete (lista exacta), cómo subirlo, cómo descomprimirlo, y **cerrar los
> permisos después** (un paquete armado en otro sistema operativo puede llegar con permisos abiertos).
> Cómo comprobar los permisos.

### 6.3 Paquetes del sistema operativo
> 📋 Qué se instala y por qué. Decir qué **no** hizo falta en la instalación real, para que nadie lo
> instale por si acaso.

### 6.4 Entorno aislado y dependencias
> 📋 Qué es un entorno aislado (una carpeta con las librerías solo de esta aplicación, para no mezclar
> con las del sistema). Cómo crearlo, cómo instalar las dependencias, cómo comprobar.

### 6.5 Comprobar que se llega a la base de datos
> 📋 Dos comprobaciones separadas: que la máquina **alcanza** la base (red) y que el usuario **entra**
> (credenciales). Cada una con su comando, su salida buena y su salida mala con causa.

### 6.6 El archivo de configuración
> 📋 Qué es (el único archivo con los datos propios de esta máquina; **no se versiona**). Tabla con
> **cada variable**: nombre, qué controla, ejemplo de valor **ficticio**, obligatoria o no, en qué paso
> se llena. Qué hacer si una clave trae caracteres especiales. Con qué permisos queda el archivo.
> **De dónde sale:** del archivo de configuración de ejemplo del proyecto y de donde el código lee la
> configuración.

### 6.7 Crear las tablas y los datos base
> 📋 Qué hace el proceso (crea tablas, siembra listas y usuarios iniciales). La clave inicial: de dónde
> sale, dónde la muestra el sistema **si la genera él**, y qué hacer con ella (guardarla donde
> corresponda; nunca en este manual). Qué hacer si el proceso falla a medias.

### 6.8 Primer arranque a mano
> 📋 Arrancar en primer plano, ver el arranque con los ojos, probar la dirección de comprobación de
> salud desde la propia máquina. Es para ver los errores **antes** de esconderlo en un servicio. Cómo
> detenerlo.

### 6.9 Dejarlo como servicio permanente
> 📋 Qué es un servicio (algo que arranca solo al encender la máquina y se levanta si se cae). El
> archivo del servicio completo con cada línea explicada. Cómo activarlo, arrancarlo, ver su estado y
> ver su registro.

### 6.10 Conectar la puerta de entrada con esta pieza
> 📋 El bloque de configuración que manda las peticiones de esta pieza al servicio, con cada línea
> explicada. Los permisos del control de seguridad que hagan falta. Comprobar la configuración antes de
> aplicarla. Si el archivo ya existe porque otra pieza se instaló primero, **agregar**, no reescribir.
> Poner aquí, con su explicación, cada detalle que en la instalación real costó encontrar.

### 6.11 Abrir el puerto en la máquina
> 📋 Comprobar si ya está abierto; abrirlo solo si falta. Aclarar que esto abre el puerto **en la
> máquina**; que la red deje llegar hasta ella lo habilita otra área, y sin eso solo se entra por un
> acceso remoto directo.

### 6.12 Configuraciones que dependen de cómo se publica (orígenes permitidos, correo)
> 📋 Qué hay que ajustar si la parte visible y la parte de datos se sirven desde direcciones distintas.
> Correo: qué variables llenar y con qué comando se prueba; qué hacer si el método de envío está
> bloqueado por política de la organización.

---

## 7. Parte B — Instalar «la parte visible» (lo que ve la persona)

> 📋 **Cómo se escribe:** igual que la Parte A. Si la parte visible se compila (se convierte de código a
> archivos listos para publicar), el paso que más falla es **decir a dónde apunta**: dedicarle una
> subsección propia con el porqué. Si el proyecto cambia de herramienta de compilación o de instalación
> de dependencias, **este manual cambia en el mismo momento**: un manual probado deja de estarlo cuando
> cambia la herramienta con la que se instala.

### 7.1 Instalar las herramientas para compilar
### 7.2 Copiar el código
> 📋 Las entradas exactas que se suben (y cuáles **no**: carpetas de dependencias, resultados de
> compilaciones anteriores), cómo armar el paquete, tamaño esperado.

### 7.3 Decir a dónde apunta — el paso que más falla
> 📋 Dónde se configura la dirección de la parte de datos, por qué conviene una dirección relativa
> (el mismo compilado sirve desde cualquier dirección sin recompilar), cómo ver qué tiene ahora, cómo
> cambiarla, cómo comprobar que no queda rastro de otra dirección.

### 7.4 Instalar dependencias y compilar
> 📋 ⚠️ No correr ninguna corrección automática de dependencias durante la instalación: cambia
> versiones y puede romper la compilación. Qué preguntas hace la herramienta y qué responder. Dónde
> queda el resultado.

### 7.5 Publicar en su carpeta y dar los permisos
> 📋 Copiar, poner dueño y permisos, aplicar el control de seguridad si lo hay. Comprobar.

### 7.6 Conectar la puerta de entrada con esta pieza
> 📋 El bloque de configuración para servir los archivos, con cada línea explicada (incluida la que hace
> que recargar cualquier pantalla no dé «no encontrado»). Si el archivo ya existe, **agregar**, no
> reemplazar.

### 7.7 Comprobar
> 📋 Que la dirección raíz devuelve la pantalla de inicio, que la parte de datos sigue respondiendo, y
> que en lo publicado no queda ninguna dirección absoluta.

---

## 8. Verificación final: cómo saber que quedó bien

> 📋 **Qué va aquí:** una lista de comprobaciones **en orden**, cada una con su comando, su resultado
> bueno y qué significa si falla. Termina con una prueba de extremo a extremo que atraviese todas las
> piezas a la vez (por ejemplo: entrar por el navegador, iniciar sesión y ver una lista que salga de la
> base de datos).
> **De dónde sale:** de la verificación de cada pieza y de la instalación real.

### 8.1 Desde la propia máquina
### 8.2 Desde su computador
> 📋 Si la red todavía no deja llegar, cómo hacer un acceso remoto directo (explicar qué es, el
> comando exacto, y qué dirección abrir después).
### 8.3 La prueba de extremo a extremo
### 8.4 Comprobar que lo que ya estaba en la máquina sigue en pie
### 8.5 Dejar constancia
> 📋 Qué se anota y dónde: fecha, versión instalada de cada pieza, quién, y cualquier desvío del manual.

---

## 9. Actualizar una instalación que ya existe

> 📋 **Qué va aquí:** el procedimiento cuando el sistema **ya está** instalado y llega código nuevo. Es
> distinto de instalar desde cero: hay datos, configuración y archivos de los usuarios que no se pueden
> perder.
> **Cómo se escribe:** los pasos de abajo, cada uno con las cuatro partes, y la «vuelta atrás» escrita
> **antes** de necesitarla.

### 9.1 Preparar los paquetes (en el computador del equipo de desarrollo)
### 9.2 Subirlos y comprobar que llegaron completos
### 9.3 Respaldo de lo que está
### 9.4 Parte de datos: desempaquetar aparte, traer lo que solo vive en la máquina (configuración, entorno aislado, archivos subidos por los usuarios), corregir permisos, e intercambiar
### 9.5 Reiniciar el servicio y comprobar (si el arranque hace trabajo previo, decir cuánto esperar)
### 9.6 Parte visible: intercambiar la carpeta publicada y volver a dar los permisos
### 9.7 Comprobar que se desplegó **lo que se creía** (marca de versión; algo que solo exista en la versión nueva)
### 9.8 Vuelta atrás, paso por paso
### 9.9 Limpieza, cuando lleve unos días estable

---

## 10. Seguridad después de instalar

> 📋 **Qué va aquí:** lo que se hace **una vez que funciona** y que suele olvidarse: cerrar permisos de
> carpetas y archivos (la configuración más cerrada que el resto), **cambiar las claves** que se usaron
> durante la instalación (en qué orden, para no dejar el servicio sin acceso), confirmar que la
> configuración real no está en el control de versiones, cambiar las claves iniciales de los usuarios
> de fábrica, y quién custodia cada secreto.

---

## 11. Mantenimiento

> 📋 **Qué va aquí:** las tareas de rutina con su comando: ver el registro del servicio, reiniciarlo,
> ver el estado de la puerta de entrada, dónde quedan los archivos de los usuarios y cómo respaldarlos,
> cómo limpiar espacio, y qué revisar una vez al mes.

---

## 12. Solución de problemas

> 📋 **Qué va aquí:** tabla **síntoma → causa más probable → cómo confirmarla → qué hacer**, ordenada
> por lo que ve la persona, no por la pieza técnica. Empezar con lo que ya pasó de verdad en la
> instalación anterior: cada tropiezo registrado es una fila.
> **Cómo se escribe:** cada fila se puede seguir sin leer el resto del manual.

| Lo que se ve | Causa probable | Cómo confirmarlo | Qué hacer |
|---|---|---|---|
| «síntoma» | «causa» | «comando o comprobación» | «acción, con el número de la sección» |

---

## 13. Lo que este manual no resuelve (depende de terceros)

> 📋 **Qué va aquí:** lo que hay que pedir a otras áreas y que ninguna cantidad de comandos reemplaza
> (acceso de red, método de envío de correo, cuentas institucionales, custodia de claves), **con el
> mensaje ya redactado** para pedirlo y cómo comprobar cuando respondan.

---

## 14. Registro de instalaciones y control de cambios

> 📋 Dos tablas. **Instalaciones hechas:** fecha, máquina, versión, quién, enlace al seguimiento.
> **Cambios del manual:** fecha, qué cambió, por qué (qué instalación lo enseñó), quién.

| Fecha | Máquina | Versión | Quién | Seguimiento |
|---|---|---|---|---|
| «fecha» | «máquina» | «versión» | «quién» | «enlace» |

| Fecha | Qué cambió en el manual | Motivo | Quién |
|---|---|---|---|
| «fecha» | Se crea el manual a partir de la base | «…» | «…» |

---

## Anexos

### A. Todas las variables de configuración, en una tabla
> 📋 Nombre, qué controla, si es obligatoria, ejemplo ficticio y en qué paso se llena.

### B. Puertos y direcciones
> 📋 Qué escucha dónde, qué es público y qué es interno.

### C. Comandos de un vistazo
> 📋 Los diez comandos que se usan a diario (estado, reinicio, registro, recargar la puerta de entrada,
> acceso remoto), cada uno con una línea de qué hace.

### D. Glosario
> 📋 Terminal, servidor, administrador, servicio, puerto, puerta de entrada, entorno aislado, acceso
> remoto, compilar, archivo de configuración, marca de versión. Una frase cada uno, sin otra palabra
> técnica dentro.

---

## Lista de comprobación antes de publicar el manual

- [ ] Todos los recuadros 📋 se borraron y no queda ningún «así» sin reemplazar.
- [ ] Cada paso tiene las cuatro partes: qué se hace, comando, qué sale y qué hacer si no.
- [ ] Cada comando dice si va en el computador propio o dentro de la máquina.
- [ ] No hay ninguna contraseña, clave ni secreto escrito.
- [ ] Todo se ejecutó de principio a fin en una máquina real siguiendo **solo** el texto, y la salida
      quedó en `seguimiento/`.
- [ ] Cada tropiezo de la instalación anterior está incorporado en su paso o en la solución de problemas.
- [ ] Los comandos usan la herramienta que el proyecto usa **hoy**, no la de la versión anterior.
- [ ] Alguien que nunca instaló el sistema lo siguió y llegó a la verificación final sin preguntar nada.
