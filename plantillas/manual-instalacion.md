# Manual de instalación — `<NOMBRE_PROYECTO>`   ·   `[CAPA 3]`

> **Qué es este archivo.** La base de un manual de instalación. Trae todas las partes que un manual
> debe llevar, en el orden en que van, y en cada parte dice qué información lleva y de dónde sale. No
> está atada a ningún lenguaje, sistema operativo, servidor, motor de base de datos ni herramienta:
> para cada proyecto hay que copiarla y llenarla con los datos de ese proyecto. Cuando todas las
> partes quedan llenas, la copia es el manual.
>
> **Cómo se llena.**
>
> 1. Copiar este archivo con el nombre del proyecto.
> 2. Reemplazar cada `<PLACEHOLDER>` por el dato real.
> 3. Llenar cada sección siguiendo su recuadro «Para quien escribe».
> 4. Repetir los bloques marcados «bloque repetible» una vez por componente, ambiente, servicio o
>    herramienta. Borrar los que el proyecto no tenga. La numeración de las secciones que quedan no cambia.
> 5. Borrar todos los recuadros «Para quien escribe»: son instrucciones para quien redacta, y quien
>    instala nunca debe verlos.
> 6. Ejecutar el manual completo, de principio a fin, en una máquina real antes de publicarlo.
> 7. Pasar la lista de comprobación de la sección 23.

## Convenciones de escritura (leer antes de llenar cualquier sección)

Este manual lo va a seguir alguien que no conoce el proyecto y que puede no haber instalado nunca una
aplicación en un servidor. Por eso:

1. **Cuatro partes por procedimiento**, siempre en este orden: precondición, acción, resultado
   esperado y validación. Un comando suelto no es un procedimiento.
2. **Ningún comando sin su etiqueta de ubicación.** La sección 8 las define, y son obligatorias.
3. **Los valores que cambian de un proyecto a otro van como `<PLACEHOLDER>`**, en mayúsculas y entre
   ángulos. Al llenar el manual hay que reemplazarlos todos: no debe quedar ninguno.
4. **Ninguna contraseña, token, llave privada ni secreto real** en el texto. En su lugar va qué es,
   quién lo entrega y dónde queda guardado. Lo que alguna vez estuvo escrito en un documento se
   considera conocido, y hay que cambiarlo.
5. **Nada por supuesto.** Cada requisito lleva primero el comando que comprueba si ya está, y solo
   después el comando que lo instala.
6. **Decir qué es cada cosa la primera vez que aparece.** «Servidor (el computador, casi siempre en
   otro sitio, donde el sistema queda funcionando para todos)». «Terminal (la ventana donde se
   escriben comandos en texto)».
7. **Antes de cambiar algo, mirar cómo está.** Todo paso que escribe, reemplaza o borra abre con el
   comando que muestra el estado actual, y cierra diciendo cómo volver atrás.
8. **Un paso, una cosa.** Si un paso tiene una «y» en el medio, probablemente son dos pasos.
9. **La comprobación va al final de cada paso**, no al final del manual. Si algo falla, así se sabe en
   qué paso falló.
10. **Las diferencias por sistema operativo o por tecnología van en subsecciones dentro del paso**
    (`16.4.1 Windows`, `16.4.2 Linux`), sin alterar la numeración principal.
11. **Acciones en infinitivo, explicaciones en tercera persona**, que es lo que pide
    [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md).
    Acá se agrega lo propio de un manual: **lo que aparece en pantalla va citado tal cual**,
    aunque diga «usted». Eso es una cita, no redacción del manual.
12. **Lo que está escrito se ejecuta, y lo que pasó al ejecutarlo no se cuenta: se vuelve paso.**
    Ninguna sección se da por buena sin haberla corrido en una máquina real, con su salida guardada en
    una carpeta `seguimiento/` al lado del manual. Pero el manual no relata esa ejecución: ni fechas,
    ni duraciones, ni «en este servidor salió...», ni «no hizo falta...». Cada cosa que se aprendió se
    vuelve un paso más, una bifurcación dentro del paso («comprobar con este comando; si sale A,
    seguir; si sale B, hacer esto») o una fila de la sección 19. Nada queda marcado «(por verificar)».
13. **Releer preguntando: «¿alguien que nunca ha abierto una terminal sabría qué tecla oprimir?».**

### Molde del procedimiento

Todo paso que instale, configure o cambie algo va con este molde:

> **Precondición.** Qué debe estar hecho o disponible antes de empezar. Si no se cumple, no se sigue.
>
> **Acción.**
>
> `[UBICACION]` usuario `<USUARIO>`, directorio `<RUTA_APLICACION>`
>
> ```
> <COMANDO>
> ```
>
> **Resultado esperado.** Lo que aparece en pantalla o lo que queda creado cuando el paso sale bien.
>
> **Validación.** El comando o la comprobación independiente que confirma el resultado, con su salida buena.
>
> **Si sale otra cosa.** Qué significa y a qué fila de la sección 19 ir.

---

## 1. Información general

> **Para quien escribe.** Los datos de identificación del documento y del software que instala. La
> versión del proyecto y la versión del manual son distintas y las dos van.

| Dato | Valor |
|---|---|
| Nombre del proyecto | `<NOMBRE_PROYECTO>` |
| Código o identificador | `<CODIGO_PROYECTO>` |
| Versión del software que instala este manual | `<VERSION>` |
| Versión del manual | `<VERSION_MANUAL>` |
| Fecha | `<FECHA>` |
| Responsable | `<RESPONSABLE>` |
| Estado del documento | Borrador · En revisión · Aprobado · Obsoleto |
| Ambiente al que aplica | `<AMBIENTE>` |
| Tiempo estimado de instalación | `<DURACION>` |
| Probado en | `<SISTEMA_OPERATIVO>` `<VERSION_SO>` |

## 2. Objetivo del manual

> **Para quien escribe.** Dos o tres frases: qué proceso cubre el documento, sobre qué software y para
> quién. Sin antecedentes ni justificación.

Este manual describe el procedimiento para instalar y dejar operativo `<NOMBRE_PROYECTO>` versión
`<VERSION>` en el ambiente `<AMBIENTE>`. Está dirigido a `<PERFIL_DESTINATARIO>`.

## 3. Alcance

> **Para quien escribe.** Dos listas: lo que el manual cubre y lo que no. Lo que queda fuera va con el
> nombre de quien sí lo resuelve, para que el lector sepa a quién pedirlo.

**Incluido**

- Componentes: `<COMPONENTE_1>`, `<COMPONENTE_2>`.
- Ambientes: `<AMBIENTE_1>`, `<AMBIENTE_2>`.
- Infraestructura: `<INFRAESTRUCTURA>`.

**Fuera del alcance**

| Qué queda fuera | Quién lo resuelve |
|---|---|
| `<TEMA_FUERA_DE_ALCANCE>` | `<AREA_O_ROL>` |

## 4. Arquitectura y componentes

> **Para quien escribe.** El dibujo de las piezas y cómo se conectan, en palabras corrientes. Sin esto
> el lector ejecuta comandos sin saber para qué y no puede diagnosticar nada. Nombrar cada pieza por su
> función y, entre paréntesis, la tecnología concreta que eligió el proyecto. Borrar las filas de
> componentes que el proyecto no tenga.

```
<DIAGRAMA_DE_COMPONENTES>
```

| Componente | Qué hace | Tecnología | Dónde queda | Depende de | Obligatorio |
|---|---|---|---|---|---|
| Frontend | `<QUE_HACE>` | `<TECNOLOGIA>` | `<RUTA_O_SERVICIO>` | `<COMPONENTE>` | Sí / No |
| Backend | | | | | |
| Base de datos | | | | | |
| Servidor web | | | | | |
| Colas | | | | | |
| Caché | | | | | |
| Almacenamiento | | | | | |
| Servicios adicionales | | | | | |
| Servicios externos | | | | | |
| Contenedores | | | | | |
| `<OTRO_COMPONENTE>` | | | | | |

## 5. Requisitos previos

> **Para quien escribe.** Cada requisito lleva, en la columna «Verificación», el comando que comprueba
> si ya está instalado. La versión va con su operador (`>= 3.11`), no en una frase.

### 5.1 Software y dependencias de base

| Requisito | Versión | Obligatorio | Verificación | Observaciones |
|---|---|---|---|---|
| `<REQUISITO>` | `<VERSION>` | Sí / No | `[LOCAL]` `<COMANDO_DE_VERIFICACION>` | `<NOTA>` |

### 5.2 Sistema operativo y hardware

| Requisito | Valor mínimo | Obligatorio | Verificación | Observaciones |
|---|---|---|---|---|
| Sistema operativo | `<SISTEMA_OPERATIVO>` `<VERSION_SO>` | Sí | `[SERVIDOR]` `<COMANDO>` | |
| Memoria | `<MEMORIA>` | | `[SERVIDOR]` `<COMANDO>` | |
| Disco libre | `<ESPACIO>` | | `[SERVIDOR]` `<COMANDO>` | |
| CPU | `<CPU>` | | | |

### 5.3 Accesos, permisos y credenciales

> **Para quien escribe.** Lo que hay que pedir antes de sentarse, a quién y cuánto suele tardar. Es la
> sección que evita quedarse a medias el primer día. Sin valores: nunca la contraseña, solo quién la
> entrega.

| Requisito | Obligatorio | Quién lo entrega | Verificación | Observaciones |
|---|---|---|---|---|
| Acceso al servidor `<SERVIDOR>` | Sí | `<AREA_O_ROL>` | `[LOCAL]` `<COMANDO_DE_CONEXION>` | |
| Permisos de administrador en el servidor | | | | |
| Credenciales de base de datos | | | | |
| Acceso al repositorio `<REPOSITORIO>` | | | | |
| Credenciales de servicios externos | | | | |
| Acceso de red hacia `<SERVIDOR>`:`<PUERTO>` | | | | |
| Certificados | | | | |
| Variables de entorno con valores propios del ambiente | | | | |

### 5.4 Puertos

| Puerto | Componente | Protocolo | Alcance | Verificación |
|---|---|---|---|---|
| `<PUERTO>` | `<COMPONENTE>` | `<PROTOCOLO>` | Público / Interno | `[SERVIDOR]` `<COMANDO>` |

## 6. Ambientes y servidores

> **Para quien escribe.** Una fila por ambiente en el resumen, y después un bloque por ambiente con sus
> datos. Cuando un procedimiento cambia según el ambiente, la diferencia va en subsecciones dentro de
> ese paso, nunca en un párrafo suelto.

### 6.1 Resumen de ambientes

| Ambiente | Servidor o hostname | Sistema operativo | Usuario | Ubicación de la aplicación | Estado |
|---|---|---|---|---|---|
| Desarrollo | `<SERVIDOR>` | `<SISTEMA_OPERATIVO>` | `<USUARIO>` | `<RUTA_APLICACION>` | Activo / Inactivo |
| Pruebas | | | | | |
| QA | | | | | |
| Producción | | | | | |

### 6.2 Detalle por ambiente

> **Bloque repetible.** Copiar una vez por cada ambiente de la tabla 6.1.

#### 6.2.N Ambiente `<AMBIENTE>`

| Dato | Valor |
|---|---|
| Nombre | `<AMBIENTE>` |
| Dirección IP o hostname | `<SERVIDOR>` |
| Sistema operativo y versión | `<SISTEMA_OPERATIVO>` `<VERSION_SO>` |
| Usuario requerido | `<USUARIO>` |
| Usuario de servicio | `<USUARIO_SERVICIO>` |
| Servicios que corren allí | `<SERVICIO_1>`, `<SERVICIO_2>` |
| Puertos | `<PUERTO>` |
| Ubicación de la aplicación | `<RUTA_APLICACION>` |
| Ubicación de los registros | `<RUTA_LOGS>` |
| Otros sistemas en la misma máquina | `<SISTEMA_VECINO>`, y qué no se puede tocar de él |
| Observaciones | `<NOTA>` |

## 7. Herramientas de acceso

> **Para quien escribe.** Las herramientas para entrar a cada ambiente y para administrarlo. Si el
> proyecto usa una herramienta distinta, basta con reemplazar este bloque completo, sin tocar el resto
> del manual.

> **Bloque repetible.** Copiar una vez por herramienta.

### 7.N `<HERRAMIENTA>`

| Dato | Valor |
|---|---|
| Nombre | `<HERRAMIENTA>` |
| Versión | `<VERSION_HERRAMIENTA>` |
| Para qué se usa | `<PROPOSITO>` |
| Dónde se obtiene | `<ORIGEN_DE_DESCARGA>` |
| Ambientes en los que aplica | `<AMBIENTE>` |
| Configuración requerida | `<CONFIGURACION>` |

**Procedimiento de conexión**

> **Precondición.** `<QUE_DEBE_ESTAR_LISTO>`
>
> **Acción.**
>
> `[LOCAL]`
>
> ```
> <COMANDO_DE_CONEXION>
> ```
>
> **Resultado esperado.** `<LO_QUE_APARECE_EN_PANTALLA>`
>
> **Validación.** `<COMO_SE_CONFIRMA_QUE_LA_SESION_QUEDO_ABIERTA>`

## 8. Ubicación de los comandos

Ningún comando de este manual aparece sin decir antes dónde se ejecuta. La etiqueta va en la línea
inmediatamente anterior al bloque de comando.

| Etiqueta | Dónde se ejecuta |
|---|---|
| `[LOCAL]` | Terminal del computador de quien instala |
| `[SERVIDOR]` | Terminal del servidor, después de haber entrado con la herramienta de la sección 7 |
| `[CONTENEDOR]` | Terminal dentro del contenedor, después de haber entrado en él |
| `[BASE DE DATOS]` | Consola del motor de base de datos |
| `[HERRAMIENTA]` | Dentro de la herramienta indicada, no en una terminal |

Cuando el comando depende del usuario o del directorio, los dos van en la misma línea de la etiqueta:

```
[SERVIDOR] usuario <USUARIO>, directorio <RUTA_APLICACION>
```

**Ejemplo de la convención**

> **Precondición.** La sesión contra `<SERVIDOR>` está abierta.
>
> **Acción.**
>
> `[SERVIDOR]` usuario `<USUARIO>`, directorio `<RUTA_APLICACION>`
>
> ```
> <COMANDO>
> ```
>
> **Resultado esperado.** `<SALIDA_ESPERADA>`
>
> **Validación.**
>
> `[SERVIDOR]` usuario `<USUARIO>`
>
> ```
> <COMANDO_DE_VERIFICACION>
> ```

Confundir `[LOCAL]` con `[SERVIDOR]` es la causa más común de que un paso «no funcione». Si un paso
falla, lo primero que hay que revisar es la etiqueta.

## 9. Obtención del código fuente

| Dato | Valor |
|---|---|
| Repositorio | `<REPOSITORIO>` |
| Rama o etiqueta de versión | `<RAMA>` |
| Método de descarga | `<METODO>` |
| Credenciales o permisos necesarios | `<QUIEN_LOS_ENTREGA>` |
| Ubicación de destino | `<RUTA_APLICACION>` |
| Qué no viaja en el paquete | `<EXCLUSIONES>` |

> **Precondición.** El acceso al repositorio está confirmado (sección 5.3).
>
> **Acción.**
>
> `[UBICACION]` usuario `<USUARIO>`, directorio `<RUTA_DESTINO>`
>
> ```
> <COMANDO_DE_DESCARGA>
> ```
>
> **Resultado esperado.** El código queda en `<RUTA_APLICACION>`.
>
> **Validación.** Comprobar que la versión obtenida es `<VERSION>`.
>
> `[UBICACION]`
>
> ```
> <COMANDO_QUE_MUESTRA_LA_VERSION>
> ```

## 10. Configuración del proyecto

> **Para quien escribe.** Una fila por variable. En la columna de ejemplo van valores ficticios, nunca
> los reales. Marcar las variables que llevan secretos: su valor lo entrega quien indica la
> sección 5.3.

### 10.1 Archivos de configuración

| Archivo | Ubicación | Se versiona | De dónde sale | Permisos |
|---|---|---|---|---|
| `<ARCHIVO_CONFIGURACION>` | `<RUTA>` | No | `<ARCHIVO_DE_EJEMPLO>` | `<PERMISOS>` |

### 10.2 Variables de entorno y parámetros

| Variable | Qué controla | Obligatoria | Ejemplo ficticio | Es secreto | En qué paso se llena |
|---|---|---|---|---|---|
| `<VARIABLE>` | `<QUE_CONTROLA>` | Sí / No | `<VALOR_FICTICIO>` | Sí / No | `<SECCION>` |

### 10.3 Conexiones a otros servicios

| Servicio | Dirección | Puerto | Usuario | Dónde se configura | Cómo se prueba |
|---|---|---|---|---|---|
| `<SERVICIO_EXTERNO>` | `<HOST>` | `<PUERTO>` | `<USUARIO>` | `<VARIABLE_O_ARCHIVO>` | `<COMANDO>` |

### 10.4 Certificados

| Certificado | Para qué | Ubicación | Vence | Quién lo renueva |
|---|---|---|---|---|
| `<CERTIFICADO>` | `<PROPOSITO>` | `<RUTA>` | `<FECHA>` | `<AREA_O_ROL>` |

## 11. Instalación de dependencias

> **Para quien escribe.** Un bloque por componente. Si el gestor de dependencias cambia, este manual
> cambia en el mismo momento: un manual probado deja de estarlo cuando cambia la herramienta con la que
> se instala. **Aviso:** ninguna corrección automática de dependencias durante la instalación. Cambia
> versiones por su cuenta y rompe lo que ya estaba probado.

> **Bloque repetible.** Copiar una vez por componente.

### 11.N Dependencias de `<COMPONENTE>`

| Dependencia | Versión | Componente | Comando de instalación | Ubicación | Verificación |
|---|---|---|---|---|---|
| `<DEPENDENCIA>` | `<VERSION>` | `<COMPONENTE>` | `<COMANDO>` | `[UBICACION]` | `<COMANDO_DE_VERIFICACION>` |

> **Precondición.** `<REQUISITO_PREVIO>` está instalado y el código está en `<RUTA_APLICACION>`.
>
> **Acción.**
>
> `[UBICACION]` usuario `<USUARIO>`, directorio `<RUTA_APLICACION>`
>
> ```
> <COMANDO_DE_INSTALACION>
> ```
>
> **Resultado esperado.** `<SALIDA_ESPERADA>`
>
> **Validación.** `<COMANDO_QUE_LISTA_LO_INSTALADO>`

## 12. Base de datos

| Dato | Valor |
|---|---|
| Motor | `<MOTOR_BD>` |
| Versión | `<VERSION_BD>` |
| Host | `<HOST_BD>` |
| Puerto | `<PUERTO_BD>` |
| Nombre de la base | `<NOMBRE_BD>` |
| Usuario de la aplicación | `<USUARIO_BD>` |
| Permisos que necesita ese usuario | `<PERMISOS_BD>` |
| Quién administra el motor | `<AREA_O_ROL>` |

### 12.1 Comprobar el acceso

> **Para quien escribe.** Dos comprobaciones separadas, cada una con su salida buena y su salida mala:
> que la máquina alcanza el motor por red, y que el usuario entra con sus credenciales. Confundirlas
> hace perder horas.

### 12.2 Crear la base y el esquema

### 12.3 Ejecutar las migraciones

### 12.4 Ejecutar los scripts adicionales

### 12.5 Cargar los datos iniciales

> **Para quien escribe.** Qué queda sembrado: listas base, parámetros, usuarios iniciales. Si el proceso
> genera una clave inicial, decir dónde la muestra y qué hacer con ella. La clave nunca va escrita aquí.

### 12.6 Validar la conexión desde la aplicación

## 13. Instalación y configuración de componentes

> **Para quien escribe.** Una subsección por componente de la tabla de la sección 4, en el orden de
> instalación. Agregar o quitar un componente no cambia el resto del manual. Dentro de cada uno, los
> pasos van con el molde de cuatro partes, y cada paso cierra diciendo cómo deshacer lo hecho hasta ahí.

> **Bloque repetible.** Copiar una vez por componente.

### 13.N `<COMPONENTE>`

#### 13.N.1 Preparación: usuario de servicio, directorios y permisos

#### 13.N.2 Ubicar el código

#### 13.N.3 Configurar

#### 13.N.4 Decir a dónde apunta

> **Para quien escribe.** En los componentes que se compilan, este es el paso que más falla: el
> compilado queda apuntando a la dirección equivocada y el error aparece mucho después. Dónde se
> configura la dirección del componente con el que habla, por qué conviene una dirección relativa (el
> mismo compilado sirve desde cualquier dirección, sin volver a compilar), cómo ver cuál tiene ahora y
> cómo comprobar que no quedó rastro de otra.

#### 13.N.5 Construir o compilar, si aplica

#### 13.N.6 Primer arranque en primer plano

> **Para quien escribe.** Arrancar a la vista antes de esconderlo en un servicio es lo que deja ver los
> errores de configuración. Incluir cómo detenerlo.

#### 13.N.7 Conectar con el servidor web o con el componente que lo expone

> **Para quien escribe.** Si el archivo de configuración ya existe porque otro componente entró
> primero, hay que agregar al final, nunca reescribirlo.

#### 13.N.8 Comprobar

#### 13.N.9 Cómo deshacer este componente

## 14. Servicios y procesos

> **Para quien escribe.** Todo lo que debe quedar corriendo después de la instalación. Un bloque por
> servicio. Incluir los procesos programados y los trabajos en segundo plano: son los que se olvidan, y
> el sistema arranca bien y falla después.

> **Bloque repetible.** Copiar una vez por servicio.

### 14.N `<SERVICIO>`

| Dato | Valor |
|---|---|
| Nombre | `<SERVICIO>` |
| Para qué sirve | `<PROPOSITO>` |
| Comando que ejecuta | `<COMANDO>` |
| Dónde se ejecuta | `[UBICACION]` |
| Usuario | `<USUARIO_SERVICIO>` |
| Puerto | `<PUERTO>` |
| Arranca solo al encender la máquina | Sí / No |
| Cómo se inicia | `<COMANDO_DE_INICIO>` |
| Cómo se detiene | `<COMANDO_DE_DETENCION>` |
| Cómo se verifica | `<COMANDO_DE_ESTADO>` |
| Dónde quedan sus registros | `<RUTA_LOGS>` |
| Cómo se leen sus registros | `<COMANDO_DE_LOGS>` |

## 15. Configuración del servidor

> **Para quien escribe.** Solo lo que hay que tocar en la máquina, no en la aplicación. Los controles
> de seguridad del sistema operativo no se apagan nunca: en lugar de eso, darles el permiso puntual, y
> el manual dice cuál es.

### 15.1 Servidor web

### 15.2 Puertos y firewall

> **Para quien escribe.** Aclarar que abrir el puerto en la máquina no es lo mismo que la red deje llegar
> hasta ella. Lo segundo lo habilita `<AREA_O_ROL>`.

### 15.3 Usuarios, directorios y permisos

### 15.4 Certificados y cifrado del tránsito

### 15.5 Variables de entorno del sistema

### 15.6 Servicios del sistema operativo

### 15.7 Procesos programados

## 16. Despliegue

> **Para quien escribe.** El orden completo, de principio a fin. Esta sección no repite los detalles:
> remite a la sección donde está cada paso. Sirve para ejecutar y para saber cuánto falta.

| Orden | Paso | Sección | Verificación de salida |
|---|---|---|---|
| 1 | Preparación: accesos confirmados, inventario y respaldo de lo que está | 5, 6, 7, 16.1 | `<COMPROBACION>` |
| 2 | Obtención del código | 9 | |
| 3 | Configuración | 10 | |
| 4 | Instalación de dependencias | 11 | |
| 5 | Base de datos | 12 | |
| 6 | Compilación o construcción | 13 | |
| 7 | Configuración de servicios y del servidor | 14, 15 | |
| 8 | Inicio | 14 | |
| 9 | Validación | 17, 18 | |

### 16.1 Inventario y respaldo previos

> **Para quien escribe.** Los comandos que dejan escrito cómo estaba la máquina antes: puertos en uso,
> servicios activos, configuración del servidor web, versión instalada. Sin eso no hay cómo volver
> atrás, ni cómo demostrar que lo que ya estaba quedó intacto. Guardar cada salida con su fecha en
> `<RUTA_EVIDENCIAS>`.

### 16.2 Ventana de ejecución y avisos

| Dato | Valor |
|---|---|
| Ambiente | `<AMBIENTE>` |
| Ventana acordada | `<FECHA_Y_HORA>` |
| Interrupción del servicio | Sí / No, `<DURACION>` |
| A quién se avisa antes y después | `<AREA_O_ROL>` |

## 17. Verificación de la instalación

> **Para quien escribe.** Comprobaciones en orden, cada una con su comando y su resultado bueno. Van
> una vez terminado el despliegue. Borrar las filas que el proyecto no tenga.

| # | Qué se comprueba | Ubicación | Comando o acción | Resultado esperado | Cumple |
|---|---|---|---|---|---|
| 1 | La aplicación responde en `<URL>` | `[LOCAL]` | `<COMANDO>` | `<RESULTADO>` | Sí / No |
| 2 | El frontend carga | | | | |
| 3 | El backend responde | | | | |
| 4 | La API contesta | | | | |
| 5 | La base de datos es accesible desde la aplicación | | | | |
| 6 | Los servicios están activos | | | | |
| 7 | Los puertos están escuchando | | | | |
| 8 | Los procesos están corriendo | | | | |
| 9 | Los registros no tienen errores críticos | | | | |
| 10 | Lo que ya estaba en la máquina sigue funcionando | | | | |

## 18. Prueba funcional posterior a la instalación

> **Para quien escribe.** Una prueba corta que atraviese todas las piezas a la vez. Estar instalado no
> es funcionar, y esta sección comprueba lo segundo. Escribirla como la haría una persona usando la
> aplicación, con el resultado exacto que tiene que ver.

| Dato | Valor |
|---|---|
| Qué se prueba | `<FUNCIONALIDAD_MINIMA>` |
| Con qué usuario | `<USUARIO_DE_PRUEBA>`, lo entrega `<AREA_O_ROL>` |
| Datos de entrada | `<DATOS_FICTICIOS>` |

> **Precondición.** Todas las filas de la sección 17 están en «Sí».
>
> **Acción.** `<PASOS_DE_LA_PRUEBA>`
>
> **Resultado esperado.** `<LO_QUE_DEBE_VERSE>`
>
> **Validación.** `<COMO_SE_CONFIRMA_EN_LOS_REGISTROS_O_EN_LA_BASE_DE_DATOS>`
>
> **Limpieza.** Qué se borra después de la prueba, si dejó datos.

## 19. Solución de problemas

> **Para quien escribe.** Ordenar la tabla por lo que ve la persona, no por la pieza técnica. Cada fila
> se debe poder seguir sin leer el resto del manual. Empezar con lo que ya pasó de verdad en la
> instalación anterior: cada tropiezo registrado es una fila.

| Problema | Posible causa | Diagnóstico | Solución | Verificación |
|---|---|---|---|---|
| `<SINTOMA>` | Dependencia faltante o con otra versión | `<COMANDO>` | `<ACCION>`, sección `<N>` | `<COMANDO>` |
| | Permisos insuficientes sobre `<RUTA>` | | | |
| | Puerto ocupado o cerrado | | | |
| | La base de datos no responde o rechaza al usuario | | | |
| | Variable de entorno vacía o mal escrita | | | |
| | El servicio no arranca, o se cae al poco tiempo | | | |
| | La red no deja llegar al servidor | | | |
| | Credenciales vencidas | | | |
| | Certificado vencido o no confiable | | | |
| | El comando se ejecutó en el lugar equivocado (sección 8) | | | |

## 20. Mantenimiento y operaciones posteriores

| Operación | Cuándo | Ubicación | Comando o procedimiento | Verificación |
|---|---|---|---|---|
| Reiniciar el sistema | `<CUANDO>` | `[UBICACION]` | `<COMANDO>` | `<COMPROBACION>` |
| Actualizar a una versión nueva | | | | |
| Desplegar un cambio | | | | |
| Revisar los registros | | | | |
| Rotar y limpiar registros | | | | |
| Liberar espacio en disco | | | | |
| Respaldar la base de datos | | | | |
| Respaldar los archivos de los usuarios | | | | |
| Restaurar desde un respaldo | | | | |
| Ejecutar migraciones nuevas | | | | |
| Verificar que los servicios siguen activos | | | | |
| Renovar certificados | | | | |

## 21. Seguridad

> **Para quien escribe.** Lo que queda por hacer una vez que el sistema funciona, y que suele
> olvidarse. Ninguna contraseña, token, llave privada ni secreto real va escrito en esta sección ni en
> ninguna otra.

### 21.1 Credenciales y secretos

| Secreto | Para qué | Dónde se guarda | Quién lo custodia | Cada cuánto se cambia |
|---|---|---|---|---|
| `<NOMBRE_DEL_SECRETO>` | `<PROPOSITO>` | `<GESTOR_O_UBICACION>` | `<AREA_O_ROL>` | `<PERIODO>` |

### 21.2 Cambios obligatorios después de instalar

- [ ] Cambiar las claves usadas durante la instalación, en el orden que no deje al servicio sin acceso.
- [ ] Cambiar las claves iniciales de los usuarios que el sistema crea de fábrica.
- [ ] Confirmar que el archivo de configuración real no quedó en el control de versiones.
- [ ] Cerrar los permisos del archivo de configuración y de los directorios de la aplicación.

### 21.3 Usuarios y permisos

| Usuario | Para qué | Permisos | Puede iniciar sesión | Quién lo aprueba |
|---|---|---|---|---|
| `<USUARIO>` | `<PROPOSITO>` | `<PERMISOS>` | Sí / No | `<AREA_O_ROL>` |

### 21.4 Superficie expuesta

| Puerto o dirección | Qué expone | Alcance | Por qué está abierto |
|---|---|---|---|
| `<PUERTO>` | `<COMPONENTE>` | Público / Interno | `<JUSTIFICACION>` |

## 22. Reversión

> **Para quien escribe.** El procedimiento para volver a la versión anterior. Escribirlo antes de
> necesitarlo y probarlo al menos una vez. Una reversión que nunca corrió no cuenta como probada.

| Dato | Valor |
|---|---|
| Cuándo se decide revertir | `<CRITERIO>` |
| Quién lo autoriza | `<AREA_O_ROL>` |
| Tiempo estimado | `<DURACION>` |
| Qué se pierde al revertir | `<IMPACTO>` |

| Orden | Paso | Ubicación | Comando o procedimiento | Verificación |
|---|---|---|---|---|
| 1 | Detener los servicios | `[UBICACION]` | `<COMANDO>` | `<COMPROBACION>` |
| 2 | Restaurar el código de la versión anterior | | | |
| 3 | Restaurar la configuración | | | |
| 4 | Revertir los cambios de base de datos | | | |
| 5 | Restaurar los archivos de los usuarios | | | |
| 6 | Iniciar los servicios | | | |
| 7 | Repetir la verificación de la sección 17 | | | |
| 8 | Avisar a `<AREA_O_ROL>` | | | |

## 23. Lista de comprobación final

- [ ] Requisitos previos instalados y verificados.
- [ ] Accesos y credenciales validados.
- [ ] Código fuente obtenido, en la versión `<VERSION>`.
- [ ] Dependencias instaladas.
- [ ] Configuración aplicada.
- [ ] Base de datos creada, migrada y con sus datos iniciales.
- [ ] Servicios configurados y arrancando solos.
- [ ] Aplicación iniciada y respondiendo.
- [ ] Verificación de la sección 17 completa.
- [ ] Prueba funcional de la sección 18 superada.
- [ ] Registros revisados, sin errores críticos.
- [ ] Cambios de seguridad de la sección 21.2 hechos.
- [ ] Procedimiento de reversión probado.
- [ ] Instalación aprobada por `<RESPONSABLE>`.

**Comprobaciones del documento, antes de publicarlo**

- [ ] Todos los recuadros «Para quien escribe» se borraron.
- [ ] No queda ningún `<PLACEHOLDER>` sin reemplazar.
- [ ] Cada procedimiento tiene precondición, acción, resultado esperado y validación.
- [ ] Cada comando lleva su etiqueta de ubicación.
- [ ] No hay ninguna contraseña, token ni llave escrita.
- [ ] El manual se ejecutó completo en una máquina real, siguiendo solo el texto, y su salida quedó en
      `seguimiento/`.
- [ ] Cada tropiezo de la instalación anterior quedó convertido en paso, en bifurcación o en fila de la
      sección 19, y el manual no lo cuenta como historia: sin fechas, sin duraciones, sin «en este
      servidor».
- [ ] No queda ninguna marca «(por verificar)».
- [ ] Los comandos usan la herramienta que el proyecto usa hoy, no la de la versión anterior.
- [ ] Alguien que nunca instaló el sistema lo siguió y llegó a la verificación final sin preguntar nada.

## 24. Control de cambios

> **Para quien escribe.** Qué cambió en el manual, sin el motivo histórico: el manual no cuenta qué
> instalación enseñó qué. El registro de qué máquina quedó con qué versión tampoco va acá, porque es
> operación y vive en el seguimiento.

| Versión | Fecha | Cambio realizado | Responsable |
|---|---|---|---|
| `<VERSION_MANUAL>` | `<FECHA>` | Se crea el manual a partir de la plantilla | `<RESPONSABLE>` |

## 25. Anexos

### A. Comandos frecuentes

| Comando | Qué hace | Ubicación |
|---|---|---|
| `<COMANDO>` | `<QUE_HACE>` | `[UBICACION]` |

### B. Puertos y direcciones

| Puerto | Componente | Alcance | Ambiente |
|---|---|---|---|
| `<PUERTO>` | `<COMPONENTE>` | Público / Interno | `<AMBIENTE>` |

### C. Variables de entorno, en una sola tabla

| Variable | Obligatoria | Ejemplo ficticio | Ambiente |
|---|---|---|---|
| `<VARIABLE>` | Sí / No | `<VALOR_FICTICIO>` | `<AMBIENTE>` |

### D. Archivos de configuración

| Archivo | Ubicación | Se versiona |
|---|---|---|
| `<ARCHIVO_CONFIGURACION>` | `<RUTA>` | Sí / No |

### E. Diagramas

```
<DIAGRAMA>
```

### F. Glosario

> **Para quien escribe.** Una frase por término, sin meter otra palabra técnica dentro. Los mínimos:
> terminal, servidor, servicio, puerto, contenedor, entorno aislado, migración, compilar, registro,
> archivo de configuración, respaldo.

| Término | Qué es |
|---|---|
| `<TERMINO>` | `<EXPLICACION_EN_UNA_FRASE>` |

### G. Referencias

| Documento | Dónde está |
|---|---|
| `<DOCUMENTO>` | `<UBICACION>` |

### H. Lo que este manual no resuelve

> **Para quien escribe.** Lo que hay que pedir a otras áreas y que ningún comando reemplaza: acceso de
> red, cuentas institucionales, certificados, custodia de secretos. Dejar redactado el mensaje con el
> que se pide, y la comprobación para cuando respondan.

| Qué falta | A quién se pide | Cómo se comprueba cuando respondan |
|---|---|---|
| `<PENDIENTE_EXTERNO>` | `<AREA_O_ROL>` | `<COMPROBACION>` |
