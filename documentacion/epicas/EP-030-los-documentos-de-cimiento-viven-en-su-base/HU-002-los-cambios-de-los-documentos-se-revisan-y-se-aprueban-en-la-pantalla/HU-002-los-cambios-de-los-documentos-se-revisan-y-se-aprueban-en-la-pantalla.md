# HU-002 · Los cambios de los documentos se revisan y se aprueban en la pantalla

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](../epica.md) |
| **Módulo / Componente** | Cimiento |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** ver qué cambió en cada documento, con el antes y el después, y aprobarlo con un botón
- **Para** revisar el trabajo sin depender de git

---

## 3. Contexto y descripción

Git deja de mostrar los cambios de los documentos que pasan a la base. Sale del [análisis 1 del pendiente 142](../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), acuerdos 5, punto 2 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada documento se guarda partido en campos (acuerdo 2) |
| RN-02 | Los archivos se borran solo después de comprobar que todo funciona con la base (acuerdo 3) |

### 3.2 Supuestos

- La base de Cimiento está disponible donde se trabaja.

### 3.3 Fuera de alcance

- Los `.py`, que siguen como archivos (acuerdo 1).

---

## 4. Criterios de aceptación

### CA-01 · La pantalla muestra lo que cambió

**Sale de:** análisis 1 del pendiente 142, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dados cambios en documentos sin aprobar
Cuando se abre la pantalla de revisión
Entonces se ve cada documento con su antes y su después
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-02 · Se aprueba con un botón

**Sale de:** análisis 1 del pendiente 142, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado un cambio sin aprobar
Cuando se oprime Aprobar
Entonces queda aprobado con la cuenta y la hora
Y se une al botón que guarda en git de la EP-026·HU-007
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo` | CA-01, CA-02 | (vacío) | [plan_trabajo.md](A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo/plan_trabajo.md) | [plan_pruebas.md](A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo/plan_pruebas.md) | [resultado_pruebas.md](A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Las HU anteriores de la EP-030, según la hoja de ruta de la épica | Alto |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 142 |
