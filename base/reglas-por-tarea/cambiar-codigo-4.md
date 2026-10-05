# Reglas de la tarea `cambiar-codigo`, parte 4 de 4

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## F4 · Todo plan lleva su plan de pruebas y su aprobación explícita
Cada plan de trabajo se redacta junto a su plan de pruebas, se **presenta** y **no se toca código sin un OK explícito** del usuario ([`01·C17`](../01-conducta.md#c17--ante-un-pedido-que-admite-dos-lecturas-reformula-antes-de-mover-nada)); el plan que sale de un análisis aprobado que lo contempla ya lo tiene, y lo cita. Sin la HU que lo respalde, **PAUSAR y retroceder** (depende de [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)).
```
INCORRECTO: usuario dice "arranque con Fase X" → agente redacta plan + implementa
            todo seguido → reporta al final
CORRECTO:   usuario dice "arranque con Fase X" → agente redacta plan + pruebas →
            PAUSA + presenta → usuario aprueba (o pide cambios) → agente implementa
```

Fuente: [02·F4](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md#f4--todo-plan-lleva-su-plan-de-pruebas-y-su-aprobación-explícita)

## F8 · Edita solo los archivos que el plan aprobado declara
Se editan únicamente los archivos de la tabla del plan aprobado ([`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 9). Descubrir a mitad que hace falta otro **detiene la ejecución** y vuelve al análisis: el plan pasa a su versión siguiente con aprobación nueva. Que el cambio sea obvio no autoriza; la aprobación sí ([`base.md`](../02-flujo-de-trabajo/base.md)).
```
INCORRECTO: durante la ejecución el agente descubre que también hay que editar el
            archivo Y → lo edita en el mismo commit "porque era necesario"
CORRECTO:   descubre Y → se detiene → vuelve al análisis → el plan pasa a
            su versión siguiente y el usuario la aprueba → sigue
```

Fuente: [02·F8](../02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md#f8--edita-solo-los-archivos-que-el-plan-aprobado-declara)
