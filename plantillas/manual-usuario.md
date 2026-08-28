# Manual de usuario — «nombre del sistema»   ·   `[CAPA 3]`

> **Qué es este archivo.** Es la **base** de un manual de usuario: tiene todas las partes que un manual
> de usuario debe llevar, en el orden en que se leen, y en cada parte dice **qué va ahí, cómo se
> escribe y de dónde se saca la información**. No está atado a ningún sistema: se copia para cada
> desarrollo y se llena con lo de ese desarrollo. Cuando todas las partes están llenas, la copia **es**
> el manual.
>
> **Cómo se usa.** 1) Copiar este archivo con el nombre del sistema. 2) Reemplazar cada «así» (entre
> comillas angulares) por el dato real. 3) Llenar cada sección siguiendo su recuadro 📋. 4) Borrar los
> recuadros 📋: son instrucciones para quien escribe, y el lector final nunca debe verlos. 5) Pasar la
> lista de comprobación del final antes de publicar.
>
> Base creada el **2026-08-27**.

---

## Reglas para escribir el manual (leerlas antes de llenar cualquier parte)

El manual lo va a leer alguien que **no sabe nada** del sistema, y puede que tampoco sepa mucho de
computadores. Por eso:

1. **Una acción por paso.** «Haga clic en el botón azul que dice **Guardar**». No: «Guarde los cambios».
2. **Decir siempre qué se ve.** Cada paso dice qué aparece en la pantalla **antes** de la acción y qué
   aparece **después**. Si el lector no ve lo que el manual dice, sabe que algo va mal y en qué punto.
3. **Decir qué hacer si no pasa lo esperado.** Cada paso que pueda fallar lleva un «Si en vez de eso
   ve...» con la causa más común y la salida.
4. **Ninguna palabra técnica sin explicarla la primera vez.** «Navegador (el programa con el que entra
   a internet)». Después de explicada se usa normal.
5. **Nombrar las cosas exactamente como salen en pantalla**, en negrita: el botón **Enviar**, el campo
   **Correo electrónico**. Si el texto de la pantalla cambia, el manual cambia.
6. **Una captura de pantalla por paso** que tenga pantalla, con un recuadro señalando dónde se hace
   clic. Las capturas van en una carpeta `imagenes/` junto al manual, con nombre `NN-que-muestra.png`.
7. **Nada de «obviamente», «simplemente», «solo tiene que».** Si fuera obvio no haría falta el manual.
8. **No prometer lo que el sistema no hace.** Lo que se escribe se comprueba haciéndolo en el sistema
   real, no leyendo el código. Lo que no se pudo comprobar se marca «(por verificar)».
9. **Frases cortas. Párrafos de tres líneas o menos.** Listas numeradas para pasos; viñetas para
   opciones.
10. **Releer cada sección preguntando: «¿un niño de doce años entendería qué tiene que hacer?».** Si
    no, reescribir.

---

## 0. Portada e identificación

> 📋 **Qué va aquí:** nombre del sistema, nombre del manual, versión del sistema que documenta, fecha,
> quién lo publica, y a quién va dirigido.
> **Cómo se escribe:** una página, sin texto corrido. Una tabla.
> **De dónde sale:** la versión es la del sistema que está publicado, no la del código en desarrollo.

| Dato | Valor |
|---|---|
| Sistema | «nombre del sistema» |
| Quién lo publica | «entidad o empresa» |
| Versión del sistema que describe | «versión» |
| Fecha de este manual | «fecha» |
| Para quién es | «tipos de persona que lo usan» |
| Versión de este manual | «número» |

---

## 1. Cómo leer este manual

> 📋 **Qué va aquí:** las convenciones: qué significa la negrita, qué son los recuadros de aviso, cómo
> se numeran los pasos, y cómo saltar directo a lo que se necesita.
> **Cómo se escribe:** media página. Un ejemplo de cada convención, para que el lector la reconozca
> después.

Modelo de lo que debe decir:

- Lo que está en **negrita** es texto que aparece tal cual en la pantalla (un botón, un menú, un campo).
- Los recuadros con ⚠️ avisan de algo que puede salir mal o que no se puede deshacer.
- Los recuadros con 💡 dan un atajo o una aclaración; se pueden saltar.
- Cada procedimiento es una lista numerada: se hace en ese orden y no se salta ninguno.
- Si solo necesita una cosa, busque su pregunta en la sección «Qué hacer si...» o en el índice.

---

## 2. Qué es el sistema y para qué sirve

> 📋 **Qué va aquí:** en una página, qué problema resuelve, qué hace una persona en él de principio a
> fin, y qué obtiene al final.
> **Cómo se escribe:** como se lo contaría a alguien que pregunta en la calle. Sin siglas sin explicar.
> Un dibujo simple del recorrido completo, de la primera acción al resultado final:
> *«entro → hago A → hago B → alguien revisa → obtengo C»*.
> **De dónde sale:** de la definición del sistema y de las historias de usuario; **no** del código.

---

## 3. Quién usa el sistema

> 📋 **Qué va aquí:** cada tipo de persona que entra al sistema, qué puede hacer, qué no, y por dónde
> entra si hay más de una puerta (por ejemplo, una parte pública y una parte interna).
> **Cómo se escribe:** una tabla, una fila por tipo de persona. Los nombres técnicos de los roles se
> traducen: «Revisor (la persona que aprueba lo que otros envían)».
> **De dónde sale:** de la definición de roles y permisos del sistema.

| Quién | Qué hace en el sistema | Por dónde entra |
|---|---|---|
| «tipo de persona 1» | «qué hace» | «pantalla o dirección de entrada» |
| «tipo de persona 2» | «qué hace» | «…» |
| Cualquier persona, sin registrarse | «qué puede hacer sin cuenta, si algo» | «…» |

---

## 4. Lo que necesita antes de empezar

> 📋 **Qué va aquí:** lista de lo que la persona debe tener a la mano **antes** de sentarse: equipo,
> conexión, navegador (cuáles sirven), una cuenta o un correo al que pueda entrar en ese momento, sus
> documentos o datos, y en qué formato.
> **Cómo se escribe:** lista de chequeo con casillas. Por cada archivo que se vaya a subir: nombre,
> formato, tamaño máximo, y un ejemplo de nombre de archivo.
> **De dónde sale:** de los requisitos del sistema y de los límites configurados para subir archivos.

- [ ] «requisito 1»
- [ ] «requisito 2»
- [ ] «documento o dato que debe tener listo»

---

## 5. Cómo entrar al sistema

> 📋 **Qué va aquí:** la dirección exacta que se escribe en el navegador (o cómo se abre la
> aplicación), qué se ve al llegar, y las puertas que existan (una por tipo de persona si son
> distintas).
> **Cómo se escribe:** un procedimiento corto por puerta, con captura de la pantalla de llegada.
> Aviso: si hay una dirección de pruebas y una definitiva, poner la que aplique y decir cuál es.
> **De dónde sale:** de quien publica el sistema (la dirección la define la instalación, no el código).

---

## 6. Parte A — Lo que hace «el tipo de persona externa» (por ejemplo, el usuario final o el cliente)

> 📋 **Cómo se escribe toda esta parte:** en segunda persona y de usted («usted escribe», «le llega»).
> Cada subsección es un procedimiento completo con cinco partes fijas: **para qué sirve**, **qué
> necesita**, **pasos** numerados con captura, **qué ve al terminar** y **si algo sale mal**.
> Una subsección por cada cosa que esa persona puede hacer, en el orden en que normalmente las hace.
> **De dónde sale:** de la lista de pantallas de esa parte del sistema y de sus textos exactos. Los
> estados o etapas por los que pasa lo que la persona hace se sacan de donde el sistema los defina, y
> se traducen a palabras de todos los días.

### 6.1 «Primera acción» (por ejemplo: crear su cuenta)
> 📋 Pantalla, datos que pide, qué pasa al confirmar, errores que puede mostrar y qué hacer en cada uno.

### 6.2 «Segunda acción» (por ejemplo: confirmar su identidad o su correo)
> 📋 Dónde buscar lo que le llega, cuánto tiempo sirve, qué hacer si venció o se escribió mal.

### 6.3 «Tercera acción» (por ejemplo: completar su información)
> 📋 Secciones o pestañas, campos obligatorios y cómo se marcan, cómo agregar más de un elemento, cómo
> guardar y cómo saber que quedó guardado.

### 6.4 «Cuarta acción» (por ejemplo: subir archivos)
> 📋 Cuáles, cuáles son obligatorios, cómo subir cada uno, cómo saber que subió bien, cómo reemplazar
> uno, qué significa borrar uno.

### 6.5 «Quinta acción» (por ejemplo: enviar para revisión)
> 📋 Qué significa enviar y qué ya no se puede cambiar después. Qué exige el sistema para dejar enviar
> y qué mensaje sale si falta algo. Qué se recibe al enviar (un número, un comprobante) y para qué
> sirve guardarlo.

### 6.6 Consultar cómo va lo que envió
> 📋 La pantalla de seguimiento. Cada estado en palabras de todos los días, en una tabla:

| Lo que muestra la pantalla | Qué significa para usted | Qué puede hacer |
|---|---|---|
| «estado 1» | «…» | «…» |
| «estado 2» | «…» | «…» |

### 6.7 Corregir lo que le devolvieron
> 📋 Cómo ver el motivo, cómo corregir, cómo volver a enviar. Aclarar qué se corrige y qué no.

### 6.8 Obtener el resultado final (por ejemplo: descargar un documento)
> 📋 Desde dónde, con qué botón, qué archivo baja y dónde queda. Qué pasa si la descarga falla.

### 6.9 «Acciones que puede hacer cualquier persona sin cuenta», si las hay
> 📋 Por ejemplo, comprobar si un documento es auténtico. Aclarar que no hace falta registrarse.

### 6.10 Avisos y notificaciones
> 📋 Qué avisos le llegan, por dónde, en qué momento, y qué hacer si no llegan.

---

## 7. Parte B — Lo que hace «el tipo de persona interna» (por ejemplo, el funcionario u operador)

> 📋 **Cómo se escribe toda esta parte:** igual que la Parte A, pero el lector es alguien con cuenta
> interna. Una subsección por cada pantalla o función del menú. Antes de cada procedimiento decir **qué
> rol lo puede hacer**: si el lector no ve el botón, es porque su rol no lo tiene, no porque el manual
> esté mal.
> **De dónde sale:** de la lista de pantallas de la parte interna y de la tabla de permisos por rol.
> Si ya existe un manual parcial de alguna función, se toma de base y se ajusta a estas reglas.

### 7.1 Iniciar sesión
> 📋 Pantalla, usuario y contraseña, segundo factor si lo hay, mensajes de error y qué significan, qué
> hacer si olvidó la clave, aviso de sesión por vencer y cómo extenderla.

### 7.2 La pantalla de inicio o tablero
> 📋 Qué muestra cada cifra o tarjeta, qué **no** significa, y cómo llegar desde ahí a la lista que
> respalda cada número.

### 7.3 «Función 1» (por ejemplo: repartir el trabajo)
### 7.4 «Función 2» (por ejemplo: revisar y aprobar o devolver)
> 📋 Cómo abrir cada elemento, cómo aprobar o devolver, qué escribir en el motivo (lo va a leer la
> persona externa: escribirlo para ella), y qué le pasa al elemento después de cada decisión.

### 7.5 «Función 3» (por ejemplo: consultar y ver el detalle)
> 📋 Buscar, filtrar, ordenar; abrir el detalle y qué pestañas tiene; imprimir; exportar. Si alguna
> exportación **no está disponible**, el manual lo dice y explica por qué; no se promete.

### 7.6 «Función 4» (por ejemplo: aprobar de forma definitiva)
> 📋 Quién puede, qué exige el sistema antes, qué pasa al confirmar, y qué mensaje sale si algo falla.

### 7.7 Usuarios, roles y permisos
> 📋 Crear un usuario, asignarle rol, desactivarlo. Qué es un rol (un paquete de permisos) y cuáles
> vienen de fábrica. Cambiar permisos y qué efecto tiene de inmediato.

### 7.8 Listas de opciones configurables (catálogos)
> 📋 Qué son, cómo agregar, editar y desactivar un valor, y qué pasa con los registros que ya lo usaban.

### 7.9 Estadísticas e informes
> 📋 Qué muestra cada gráfico, para qué periodo, y cómo leerlo.

### 7.10 Avisos del usuario interno
> 📋 Qué avisos recibe, dónde los ve, cómo marcarlos como leídos.

### 7.11 Cerrar sesión
> 📋 Dónde está el botón, por qué importa en un equipo compartido, qué pasa si se deja abierta.

---

## 8. El recorrido completo (de principio a fin)

> 📋 **Qué va aquí:** un solo dibujo o tabla con los estados por los que pasa lo que la persona externa
> envía, quién lo mueve de cada estado al siguiente, y qué ve cada quien en ese momento. Es la sección
> que une las Partes A y B.
> **Cómo se escribe:** diagrama de cajas y flechas, seguido de una tabla «estado → quién lo cambia →
> qué ve la persona externa → qué ve la persona interna».
> **De dónde sale:** de donde el sistema defina sus estados (una sola fuente; si hay dos, preguntar
> cuál manda).

```
«estado inicial» ──(quién / qué acción)──▶ «estado 2» ──(quién / qué acción)──▶ «estado 3»
       ▲                                                                        │
       └───────────── «estado de devolución» ◀──(quién / qué acción)────────────┤
                                                                                │
                                               (quién / qué acción) ──▶ «estado final» ──▶ «resultado»
```

---

## 9. Mensajes que muestra el sistema y qué significan

> 📋 **Qué va aquí:** tabla con cada mensaje que puede aparecer (texto exacto), en qué pantalla, qué lo
> causa y qué debe hacer la persona.
> **Cómo se escribe:** una fila por mensaje, ordenados por pantalla. Se llena recorriendo el sistema y
> buscando en el código los textos que se muestran al usuario (avisos, ventanas de error, respuestas de
> error del servidor).

| Mensaje (texto exacto) | Dónde sale | Por qué sale | Qué hacer |
|---|---|---|---|
| «texto» | «pantalla» | «causa» | «acción» |

---

## 10. Qué hacer si... (preguntas frecuentes)

> 📋 **Qué va aquí:** las situaciones reales que llegan a soporte, en forma de pregunta, con la
> respuesta en pasos. Fuentes: lo que ya preguntaron los usuarios, y **cada defecto que un usuario
> vivió** (cada uno es una pregunta de esta lista, aunque ya esté corregido).
> **Cómo se escribe:** «**No me llegó el correo.** → 1. Revise correo no deseado. 2. Espere dos
> minutos. 3. Pulse **Reenviar**. 4. Si en diez minutos no llega, escriba a ...».

---

## 11. Glosario

> 📋 **Qué va aquí:** cada palabra que el sistema usa y que no es de uso diario, con su explicación en
> una frase, sin otra palabra técnica dentro. Orden alfabético.

| Palabra | Qué significa |
|---|---|
| «término» | «explicación en una frase» |

---

## 12. A quién pedir ayuda

> 📋 **Qué va aquí:** el canal de soporte para cada tipo de persona (correo, teléfono, horario), y qué
> información dar al escribir (número o identificador, pantalla donde estaba, texto del mensaje,
> hora). **No inventar datos de contacto**: se piden a quien publica el sistema.

---

## 13. Control de cambios de este manual

> 📋 Una fila por cada vez que el manual cambia: fecha, qué cambió, por qué (qué versión del sistema o
> qué hallazgo lo motivó), quién.

| Fecha | Qué cambió | Motivo | Quién |
|---|---|---|---|
| «fecha» | Se crea el manual a partir de la base | «…» | «…» |

---

## Anexo — Lista de comprobación antes de publicar el manual

- [ ] Todos los recuadros 📋 se borraron y no queda ningún «así» sin reemplazar.
- [ ] Cada procedimiento se ejecutó en el sistema real siguiendo **solo** el texto del manual, y salió.
- [ ] Cada paso con pantalla tiene su captura, y la captura muestra lo que el texto dice.
- [ ] Cada palabra técnica está explicada la primera vez que aparece, o está en el glosario.
- [ ] Alguien que **no** conoce el sistema lo leyó y pudo hacer el recorrido completo sin preguntar.
- [ ] Los textos en negrita coinciden letra por letra con la pantalla.
- [ ] Ninguna sección dice «obviamente», «simplemente» ni «solo tiene que».
- [ ] Los datos de contacto de la sección 12 los confirmó quien publica el sistema.
