---
name: proponer-alcance
description: Traduce una solicitud del usuario en un alcance concreto (qué se va a hacer y qué NO) antes de especificar o diseñar. Úsala cuando llega un pedido amplio o ambiguo y hay que acordar el alcance, o cuando el usuario dice "quiero X" y no está claro el borde. Es el rol Proponente. Propone, no decide ni escribe código.
---

# Proponer alcance (rol Proponente)

Convierte una solicitud en un **alcance acordado**: qué se construye y qué queda fuera. **Propone, no decide** (`01`·C4): las opciones las elige el usuario. No escribe especificación ni código; es el paso previo a la especificación.

## Procedimiento (en orden)

1. **Entender el pedido** y cargar contexto (`02`·F1). Si hace falta ver qué existe, apoyarse en `analizar-proyecto`.
2. **Definir el alcance:**
   - **Dentro:** qué entra, en términos concretos.
   - **Fuera:** qué NO cubre (para cerrar expectativas, `01`·C3).
3. **Detectar ambigüedad** (`01`·C7): si el pedido admite más de una lectura razonable y cada una da un resultado distinto, **no asumir** — presentar **opciones concretas** para que el usuario elija.
4. **Marcar dependencias y riesgos** de alto nivel: qué debe existir antes, qué podría bloquear.
5. **Presentar** el alcance propuesto (con las opciones abiertas) y **esperar la decisión** del usuario.

## Salida

Una propuesta de alcance corta: dentro / fuera / opciones a decidir / dependencias. Aprobado el alcance, pasa al Escritor de especificación (`generar-spec-modulo`). No redactar la especificación ni tocar código desde aquí.

Ver: `01`·C4 (proponer, no decidir), `01`·C7 (ambigüedad → opciones), `02`·F1 (contexto). Alimenta al Escritor de especificación.
