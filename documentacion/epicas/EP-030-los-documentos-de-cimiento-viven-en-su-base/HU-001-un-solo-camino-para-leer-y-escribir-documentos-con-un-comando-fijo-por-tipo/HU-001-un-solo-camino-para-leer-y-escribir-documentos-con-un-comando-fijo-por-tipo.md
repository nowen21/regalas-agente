# HU-001 · Un solo camino para leer y escribir documentos, con un comando fijo por tipo

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](../epica.md) |
| **Módulo / Componente** | Cimiento |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** Claude, al crear o cambiar un documento
- **Quiero** usar un comando fijo (crear, ver, editar, listar) en vez de escribir un guion
- **Para** no repetir código de un solo uso

---

## 3. Contexto y descripción

Cada operación sobre un documento termina en un guion nuevo, y los programas leen los .md por caminos distintos. Sale del [análisis 1 del pendiente 142](../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), acuerdos 1, 2 y 3, punto 1 de «Lo que se tiene que hacer».

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

### CA-01 · Un comando fijo crea, muestra, edita y lista un documento

**Sale de:** análisis 1 del pendiente 142, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un tipo de documento registrado
Cuando se corre su comando crear, ver, editar o listar
Entonces la operación se hace en la base
Y no hace falta escribir ningún guion
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-02 · Todo programa lee y escribe documentos por el mismo camino

**Sale de:** análisis 1 del pendiente 142, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un programa que necesita un documento
Cuando lo lee o lo escribe
Entonces usa el camino único de Cimiento
Y no abre el archivo por su cuenta
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-03 · Cada cambio queda en la historia

**Sale de:** análisis 1 del pendiente 142, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un documento
Cuando se cambia por el camino único
Entonces queda una fila en Cambio con el antes y el después
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-030-HU-001-camino-unico-y-comando-documento` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-030-HU-001-camino-unico-y-comando-documento/plan_trabajo.md) | [plan_pruebas.md](A-EP-030-HU-001-camino-unico-y-comando-documento/plan_pruebas.md) | [resultado_pruebas.md](A-EP-030-HU-001-camino-unico-y-comando-documento/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Ninguna | Alto |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 142 |
