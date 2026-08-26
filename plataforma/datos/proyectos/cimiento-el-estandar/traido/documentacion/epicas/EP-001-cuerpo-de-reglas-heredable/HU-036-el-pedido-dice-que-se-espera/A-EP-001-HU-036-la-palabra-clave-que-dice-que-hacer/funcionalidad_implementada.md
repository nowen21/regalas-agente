# Funcionalidad implementada — Fase A-EP-001-HU-036 (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 1. Qué quedó hecho

| Qué | Dónde |
|---|---|
| La regla `01·C28`, con su checklist en **CUMPLE** | [base/01-conducta.md](../../../../../base/01-conducta.md) |
| El anexo con las dieciocho palabras y qué autoriza cada una | [base/01-conducta/palabras-clave.md](../../../../../base/01-conducta/palabras-clave.md) |
| La declaración de que no es comprobable por programa | [validadores/reglas-validables.md](../../../../../validadores/reglas-validables.md) |
| La versión **34.0.0**, con su entrada dicha para quien la adopta | [CHANGELOG.md](../../../../../CHANGELOG.md) y [VERSION](../../../../../VERSION) |

## 2. Trazabilidad

| CA | Caso | Veredicto | Evidencia |
|---|---|---|---|
| Transversal · molde y checklist | CP-001 | Cumple | [resultado_pruebas.md](resultado_pruebas.md) |
| CA-01 · sin palabra no se actúa | CP-002 | Sin verificar | Se corre en una sesión nueva |
| CA-02 · con palabra se hace solo eso | CP-003 | Sin verificar | Igual |
| CA-03 · la palabra ajena se trata como ausente | CP-004 | Sin verificar | Igual |
| Regresión | CP-005 | Cumple | [resultado_pruebas.md](resultado_pruebas.md) |

## 3. La deuda que se declara

| # | Qué quedó sin hacer | Por qué | Quién la paga | Para cuándo |
|---|---|---|---|---|
| 1 | Los tres criterios de comportamiento sin comprobar | El agente que escribió la regla no puede probarse a sí mismo: sabe lo que se espera | El autor | En la primera sesión nueva |
| 2 | Ninguna comprobación automática vigila la regla | Ningún programa puede leer un pedido y decir si el agente hizo de más | Nadie: está declarado como límite, no como pendiente | No aplica |

## 4. Lo que se aprendió

**El validador encontró lo que la lectura no.** La regla declaraba extender a `00·N1`, y `M7` prohíbe apoyarse en una regla blindada. Se leyó tres veces sin verlo; lo detuvo la corrida de meta-reglas.

**Una regla que no se puede comprobar por programa no es una regla peor**, pero sí una que hay que mirar en el uso. Por eso su deuda no es «falta el validador»: es que nunca va a haber uno.
