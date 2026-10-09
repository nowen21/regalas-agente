# HU-004 · Las épicas, las HU y los documentos de cada fase viven en la base, partidos en campos

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](../epica.md) |
| **Módulo / Componente** | Cimiento |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | XL |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

- **Como** Claude y el freno
- **Quiero** guardar y leer la cadena en tablas con campos
- **Para** que el plan aprobado, los criterios y los resultados se consulten sin leer texto

---

## 3. Contexto y descripción

La cadena (épica, HU y fase) son unos 2.000 archivos. Sale del [análisis 1 del pendiente 142](../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), acuerdos 2 y 3, punto 4 de «Lo que se tiene que hacer».

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

### CA-01 · La cadena tiene sus tablas

**Sale de:** análisis 1 del pendiente 142, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dada una épica, una HU o un documento de fase
Cuando se crea o se cambia
Entonces queda en su tabla, partido en campos
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-02 · Las existentes pasan a la base

**Sale de:** análisis 1 del pendiente 142, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dados los .md de la cadena
Cuando se corre el comando de importación
Entonces quedan en la base
Y sus archivos se borran después de comprobar que todo funciona
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-03 · Los programas que la usan leen la base

**Sale de:** análisis 1 del pendiente 142, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dados andamio, fase, veredicto, plan_vs_hecho, acuerdos, origen y los validadores
Cuando trabajan
Entonces leen y escriben la base
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|

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
