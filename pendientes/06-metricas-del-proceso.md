# Pendiente · Métricas del proceso

**Estado:** abierto · anotado 2026-08-04.

Medir si el estándar **está sirviendo**. Hoy no hay ningún dato: se asume que el flujo mejora el resultado, pero no se sabe qué parte ayuda, cuál estorba y cuál se salta siempre.

## Qué se querría saber

- **Fases reabiertas** — cuántas se dan por cerradas y hay que volver a abrir, y por qué. Es la señal más directa de que una puerta no está filtrando.
- **Puertas que fallan** — qué checkpoint rechaza más seguido. Si una puerta nunca rechaza nada, o no sirve o no se está aplicando.
- **Decisiones escaladas al usuario** — cuántas por fase. Muchas = el filtro de `02` no está filtrando; ninguna = el agente está decidiendo solo cosas que no le tocan.
- **Deuda abierta vs cerrada** — si crece sin parar, el `§Fuera-de-scope` se volvió un basurero.
- **Uso real de la memoria** — cuántas búsquedas encuentran algo útil. Una memoria que nadie consulta con éxito es solo almacenamiento.
- **Retrabajo por spec incompleta** — cambios de spec después de empezar a implementar.

## Forma propuesta

Sin instrumentación nueva donde se pueda evitar: casi todo se deriva de lo que **ya se registra** — `senales.db`, los archivos de fase, `git log`. Un lector que agrega y reporta, no un sistema de telemetría.

[interfaz/](../interfaz/) ya tiene la mitad del camino: lee los archivos y la base reales y muestra conteos. Extenderlo con una vista de proceso es más barato que construir algo aparte.

## Advertencia de diseño

Una métrica visible se convierte en objetivo y deja de medir. "Cero fases reabiertas" se consigue no reabriendo ninguna, no haciéndolas bien. Estas métricas son para **decidir qué reglas cambiar**, no para calificar el trabajo — y conviene que el archivo lo diga cuando se implemente.

## Relación con otros pendientes

- Se alimenta de los [01 · validadores](01-validadores-y-hooks.md): cada fallo de validador es un dato objetivo, sin que nadie tenga que anotarlo.
- Y del [03 · ciclo de vida de pendientes](03-ciclo-de-vida-de-pendientes.md): sin cierre de deuda no hay serie de abierta-vs-cerrada que medir.

Va de último de su bloque porque **no tiene qué medir hasta que 01 y 03 estén hechos**.
