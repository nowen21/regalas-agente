> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F13 · Deja la estructura base puesta antes de trabajar

Antes de cualquier paso del flujo —incluso antes de cargar contexto ([`02·F1`](F1-carga-el-contexto-antes-de-actuar.md))— el agente deja la estructura base puesta: crea la carpeta `proyectos/`, donde vive el código del usuario, y su propio espacio al lado (`.agente/`, `prompts/`, `documentacion/`). Crear una carpeta que la norma exige no es una decisión: es la norma. Lo que **sí** es del usuario es **qué va dentro de `proyectos/`** — el agente no mueve, no reorganiza ni acomoda ahí código que ya exista. El árbol completo está en [`estructura-base.md`](../estructura-base.md); el reparto de mundos, en [`base.md`](../base.md).

```
INCORRECTO: existe código suelto en la raíz → el agente crea `proyectos/` y mueve
            el código del usuario adentro
CORRECTO:   existe código suelto en la raíz → el agente crea `proyectos/` vacía,
            avisa que hay código fuera y espera a que el usuario decida si lo mueve
```

---

### Checklist  ·  **pendiente de aplicar**

El resultado anterior (aplicado contra **v2.5.0** el **2026-08-07**) quedó **anulado** al reescribirse la regla en **v5.0.0**: el gate que detenía el arranque pasó a ser una estructura que el instalador deja puesta. Se vuelve a aplicar el [checklist del estándar](../../20-meta-reglas/checklist.md) en el próximo repaso del capítulo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
