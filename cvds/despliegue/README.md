# Despliegue: ¿qué se entregó, y cómo se instala?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se pone a andar el estándar de trabajo heredable en un proyecto, cómo se vuelve atrás si falla, y qué se entregó con qué evidencia.

> **Escrito como si no hubiera nada construido.** Sale de lo que exigen el [análisis](../analisis-requisitos/README.md) y el [diseño](../diseno/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin abrir).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Lo construido, con veredicto por criterio | Pruebas | No: nada se ha ejecutado |
| Los defectos abiertos y cuáles bloquean | Pruebas | No |
| Los requisitos que solo se comprueban en uso: demora al abrir, portabilidad y que lo nuevo no rompa lo anterior | Análisis | No |

## 2. Dónde corre, y cómo se llega

| Ambiente | Para qué sirve | Quién puede desplegar ahí | En qué se diferencia de producción |
|---|---|---|---|
| El propio repositorio del estándar | Escribir y probar las reglas | El autor | En nada: es donde se usa a diario |
| Un proyecto de prueba, creado y borrado por la prueba | Comprobar la instalación desde cero | La prueba automática | No tiene trabajo real: se puede romper |
| Un proyecto que hereda | Uso real | Quien lo instale, con su aprobación | Tiene código y documentos propios que no se pueden pisar |

## 3. La instalación desde cero

| # | Paso | Cómo se sabe que salió bien |
|---|---|---|
| 1 | Obtener el estándar en la máquina donde corre el agente | Está la carpeta con las reglas y las comprobaciones |
| 2 | Ejecutar el instalador apuntando al proyecto que va a heredar | Dice qué archivos va a agregar, y pide aprobación antes |
| 3 | Aprobar la instalación | Deja el archivo de instrucciones del proyecto y el enganche de sesión |
| 4 | Anotar qué versión se adoptó | El proyecto declara su versión, y el número existe de verdad |
| 5 | Abrir una sesión en el proyecto | Las reglas se cargan solas, y el aviso dice qué versión rige |
| 6 | Correr las comprobaciones sobre el proyecto | Reportan sobre ese proyecto, no sobre el estándar |
| 7 | Levantar la interfaz local, si se quiere ver en pantalla | Lista los documentos del ciclo y lo guardado en la memoria |

**Probada desde cero por «quién», el «AAAA-MM-DD», en «dónde».** Pendiente: es la comprobación que confirma el supuesto 2 de planificación.


### 3.1 Si al guardar aparece «Filename too long»

Pasa en Windows, que no deja escribir rutas de más de 260 caracteres. Se resuelve con un ajuste del control de versiones, en el repositorio donde ocurre:

```
git config core.longpaths true
```

**El instalador ya lo deja puesto** en el proyecto donde corre, así que esto solo hace falta si el repositorio se obtuvo clónandolo y no se ha instalado nada en él.

**Y no es que el instalador haya fallado:** la configuración del control de versiones **no viaja al clonar**. Vive dentro de la carpeta oculta del repositorio, que cada clon crea nueva. No hay forma de que un ajuste puesto acá llegue allá.

**Si prefiere que valga para todo lo que clone de aquí en adelante**, existe la forma que aplica a la máquina entera:

```
git config --global core.longpaths true
```

**Esa decisión es suya y el instalador no la toma.** Cambia configuración fuera del proyecto, y este estándar no toca nada fuera del proyecto sin que se lo pidan.

## 4. Los datos

| Qué se define | Cómo queda |
|---|---|
| Respaldo antes de tocar nada | El proyecto que hereda debe estar en control de versiones y sin cambios sin guardar. Si ya tiene memoria guardada, se respalda antes de actualizar |
| Migración | Solo cuando una versión mayor cambia la forma de un documento; el instalador dice qué rehacer |
| Si la migración falla a mitad | Se descarta lo agregado y el proyecto vuelve a su versión anterior: nada de lo suyo se tocó |

## 5. Cómo se vuelve atrás

| Si falla | Cómo se revierte | Cuánto demora | Qué se pierde |
|---|---|---|---|
| La instalación deja el proyecto raro | Se quitan los archivos agregados y el enganche | Minutos | Nada del proyecto |
| Una versión nueva del estándar molesta | El proyecto se queda en la versión anterior y lo declara | Minutos | Los avisos y comprobaciones nuevas |
| El enganche demora la apertura de la sesión | Se desactiva el enganche y las reglas se cargan a mano | Minutos | La carga automática |
| La interfaz local no levanta | Se lee todo en archivos, como antes | Minutos | Solo la comodidad de la pantalla |

## 6. Qué se le dice a quien usa

| Qué se comunica | A quién | Cuándo | Dónde queda |
|---|---|---|---|
| Qué trae la versión, dicho para quien la usa | Usuario y proyectos que heredan | Al publicarla | El registro de cambios y las notas de versión |
| Qué obliga a rehacer algo | Proyectos que heredan | Antes de que la adopten | La marca de versión mayor |
| Qué quedó sin comprobar | Usuario | Con la entrega | El resultado de pruebas |

## 7. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual de instalación | [plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md](../../plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md) | Quien instala | Pendiente |
| Notas de versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../plantillas/ciclo-vida-proyectos/19-notas-de-version.md) | Quien usa | Pendiente |
| Acta de entrega y aceptación | [plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md](../../plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md) | Usuario, se firma | Pendiente |
| Lista de comprobación del despliegue | [plantillas/checklist-despliegue.md](../../plantillas/checklist-despliegue.md) | Quien despliega | Pendiente |

## 8. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Instalar en un proyecto | esté en control de versiones y sin cambios sin guardar | Sección 4 de este documento |
| Instalar | el usuario apruebe la lista de archivos que se van a agregar | Ningún cambio de estado sin aprobación |
| Dar por entregado | alguien ajeno al autor haya instalado siguiendo solo el texto | Es la comprobación del supuesto 2 |

## 9. La decisión de cierre

**No se entrega todavía**, decidido por el autor el 2026-08-22.

La instalación de la sección 3 está escrita paso a paso, pero **nadie ajeno la ha ejecutado**. Mientras eso no pase, el manual dice lo que el autor cree que hay que hacer, no lo que hay que hacer.

## 10. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que este análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Instalación desde cero | Un programa que la hace, y que no pisa lo que ya existe | [validadores/instalar.py](../../validadores/instalar.py) |
| Lista previa que se marca | Existe como molde, y como recordatorio de lo que la instalación olvida | [plantillas/checklist-despliegue.md](../../plantillas/checklist-despliegue.md) |
| Qué trae cada versión, para quien la usa | Registro escrito en castellano llano, exigido por `M17` | [CHANGELOG.md](../../CHANGELOG.md) y [documentacion/versiones/](../../documentacion/versiones/README.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los ambientes no están escritos, aunque de hecho son tres |
| 2 | la estrategia de entrada existe como adopción por versión, sin documento |
| 3 | la migración tiene programa ([validadores/migraciones.py](../../validadores/migraciones.py)) pero sin ensayo previo con datos reales |
| 4 | la vuelta atrás depende del control de versiones y no está escrita como plan |
| 5 | el manual está repartido entre el [README.md](../../README.md) y `Manual-Estandar-Agente.docx`, que no salen del mismo sitio |

**No existe**

| # | Qué |
|---|---|
| 1 | acta de entrega |
| 2 | lo que recibe quien va a operar el sistema |
| 3 | **y la instalación desde cero nunca la ejecutó alguien ajeno al autor**, que es lo único que demostraría que el manual dice lo que hay que hacer y no lo que el autor cree |
