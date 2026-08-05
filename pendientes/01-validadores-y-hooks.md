# Pendiente · Validadores automáticos + hooks

**Estado:** abierto · anotado 2026-08-04.

Construir una capa de **verificación mecánica** del estándar: scripts que comprueban lo comprobable y hooks que los disparan solos. Hoy el estándar existe solo como texto que el agente interpreta — si se salta una puerta, si el commit no sigue el formato, si una HU va incompleta, **nadie lo detecta**.

## El principio que lo ordena

Una regla vive en **un solo lugar**: el `.md`. El validador **no la reescribe**, solo la hace cumplir. Si la regla se duplica en código, tarde o temprano el `.md` dice una cosa y el `.py` otra.

Criterio para decidir qué se automatiza:

> Si dos personas pueden discutir si se cumplió → se queda en `.md` (lo interpreta el agente).
> Si un script puede decir sí/no sin opinar → validador.

## Qué cubriría

- **Formato de commit** (`09`) — rechazar mensajes que no sigan la convención o que traigan líneas prohibidas.
- **Plantillas completas** (`plantillas/`) — abrir la HU / épica / spec / plan y fallar si faltan secciones obligatorias o quedaron marcadores sin llenar.
- **Trazabilidad** (`13`·DOC3) — recorrer épica → HU → spec → fase → commit y reportar huérfanos: HU sin épica, fase sin plan, criterio de aceptación sin caso de prueba.
- **Puertas del flujo** (`02`) — que no haya código de una fase sin su spec acordada y su plan de trabajo.
- **Precondiciones de cierre** (`cerrar-fase`) — pruebas ejecutadas, checklist de trazabilidad marcado.
- **Coherencia interna del estándar** — enlaces rotos entre archivos de `base/`, referencias a secciones que ya no existen, índice desactualizado.

## Forma propuesta

```
base/*.md            ← la norma (fuente de verdad, versionada)
validadores/*.py     ← comprueban lo comprobable
.claude/hooks        ← disparan los validadores en el momento correcto
```

Cada validador: entrada explícita, salida sí/no + lista de incumplimientos con `archivo:linea`. Sin efectos secundarios: reportan, no arreglan.

## Por qué importa

Es la brecha entre **"el estándar dice"** y **"el estándar se cumple"**. Todo lo demás del backlog agrega cobertura; esto agrega **garantía** sobre la cobertura que ya existe.

## Relación con otros pendientes

- Los validadores son el consumidor natural del [03 · ciclo de vida de pendientes](03-ciclo-de-vida-de-pendientes.md) (avisar de deuda abierta al abrir fase).
- Alimentan las [06 · métricas del proceso](06-metricas-del-proceso.md): cada fallo de validador es un dato.
