# Pendiente: el freno no deja instalar paquetes en el entorno del proyecto

Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md), que reúne los reportes de scilit.

| | |
|---|---|
| **De dónde sale** | Proyecto scilit, fase `A-EP-005-HU-003-programador-de-tareas`; seguimiento en scilit: [pendiente 14](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/14-esperando-a-cimiento-el-freno-no-deja-instalar-paquetes/pendiente.md) |

## El problema

`validadores/freno.py:55` a `57` detiene todo `pip install` o `python -m pip install` con el motivo «instala paquetes fuera del proyecto (04·S9)», sin mirar dónde instala.

En scilit se corrió `venv/Scripts/python.exe -m pip install django-celery-beat==2.6.0` desde `proyectos/scilit/`: el entorno `venv/` está dentro del proyecto, así que no escribe fuera de él y `04·S9` no aplica. El freno lo detuvo igual.

El usuario de scilit pidió reportarlo: la instalación de un paquete que un plan aprobado declara no debe ser frenada. La fase que lo necesita quedó detenida ([estado de la fase](C:/DesarrollosClaude/personales/scilit/documentacion/epicas/EP-005-seguimiento-del-procesamiento/HU-003-las-tareas-automaticas-arrancan/A-EP-005-HU-003-programador-de-tareas/estado-fase.md)).

Para corregirlo, el freno podría dejar pasar el `pip` de un entorno que está dentro del proyecto (`<proyecto>/**/venv`, `.venv`) cuando el plan aprobado de la fase en curso nombra el paquete en su `requirements.txt`, y seguir frenando la instalación global.

## Por qué importa

Toda fase que agregue una dependencia se detiene y obliga al usuario a instalarla a mano, aunque el plan aprobado ya la incluya.
