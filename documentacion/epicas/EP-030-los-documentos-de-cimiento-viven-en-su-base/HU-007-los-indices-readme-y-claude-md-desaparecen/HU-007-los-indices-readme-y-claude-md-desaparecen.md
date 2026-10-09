# HU-007 · Los índices README y CLAUDE.md desaparecen

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](../epica.md) |
| **Módulo / Componente** | Cimiento |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

- **Como** Claude
- **Quiero** recibir por los enganches lo que hoy dice CLAUDE.md, y consultar listas en vez de índices
- **Para** que no queden archivos que nadie necesita

---

## 3. Contexto y descripción

404 índices solo sirven para navegar carpetas, y CLAUDE.md se lee del disco. Sale del [análisis 1 del pendiente 142](../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), acuerdos 1 y 3, punto 7 de «Lo que se tiene que hacer».

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

### CA-01 · Los README de índice se quitan

**Sale de:** análisis 1 del pendiente 142, punto 7 de «Lo que se tiene que hacer»

```gherkin
Dados los README de índice
Cuando ya no queda nada que los necesite
Entonces se borran
Y las listas salen de consultas a la base
```

**Cómo validarlo:** se define en el plan de pruebas de la fase.

### CA-02 · CLAUDE.md llega por los enganches

**Sale de:** análisis 1 del pendiente 142, punto 7 de «Lo que se tiene que hacer»

```gherkin
Dado lo que dice CLAUDE.md
Cuando abre una sesión
Entonces el enganche se lo pasa a Claude desde la base
Y el archivo ya no existe
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
