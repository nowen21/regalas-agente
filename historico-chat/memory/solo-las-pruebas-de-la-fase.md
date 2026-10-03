# En una fase se corren solo las pruebas de esa fase

**Qué se pide.** Al cerrar una fase se corren las pruebas de lo que esa fase construye, y nada más. La suite completa del estándar no entra en el plan de pruebas de una fase.

**Por qué.** Cada funcionalidad tiene su fase y sus pruebas. El 2026-10-02, en la fase A de la HU-003 de EP-023, el agente escribió en el plan de pruebas que se corrieran las 847 pruebas del estándar, sin que nadie lo pidiera, y la corrida tomó unos 25 minutos en cinco partes. El usuario preguntó quién había pedido eso y respondió: «solo las de la fase, para eso cada funcionalidad tiene su fase. No invente».

**Cómo se aplica.**

- La sección 3.5 del plan de pruebas nombra las pruebas de la fase: las que se escriben en ella y las de los programas que cambia.
- La suite completa solo se corre si el usuario la pide.

Relacionado: [la orden se resuelve de una](la-orden-se-resuelve-de-una.md).
