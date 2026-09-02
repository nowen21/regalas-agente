# HU-001 — Abrir una fase con sus documentos

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-019 El ciclo se opera desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-011` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Ciclo de vida |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien abre una fase cada pocas horas
- **Quiero** que la plataforma la cree con sus cinco documentos y su nombre bien puesto
- **Para** no crear carpetas a mano ni saltarme un documento

---

## 3. Contexto y descripción

**La ficha de `F-011` lo dice así:** *«que nadie cree carpetas y archivos a mano, ni se salte un documento»*.

**El nombre de una fase dice a qué historia pertenece**, y escribirlo a mano es de donde salen las fases que no se sabe de dónde cuelgan. Acá lo arma la plataforma: la letra, la épica, la historia y de qué trata.

**Y una fase sin historia no se abre.** No es comodidad: `02·F0` pide que cada eslabón cuelgue del anterior, y una fase suelta es trabajo que nadie pidió.

### 3.1 Reglas de negocio

- `RN-1` El nombre se arma con el identificador; no se escribe a mano.
- `RN-2` **Sin la historia, la fase no se abre.**
- `RN-3` Quedan los cinco documentos, con el molde del estándar leído en ese momento.
- `RN-4` **Si la carpeta ya existe, no se toca.**
- `RN-5` Abrir queda registrado.

### 3.2 Supuestos

- Que la historia existe, y que los moldes viven en `plantillas/`.

### 3.3 Fuera de alcance

- **Abrir épicas e historias.** La fase es donde duele.
- Llenar los documentos: eso lo hace `F-014`, que ya está.

---

## 4. Criterios de aceptación

### CA-01 — Se abre una fase y quedan sus documentos con el molde

```gherkin
Dada una historia escrita
Cuando se abre una fase suya
Entonces quedan sus cinco documentos, con el molde del estándar
```

**Cómo validarlo:** abriendo y mirando la carpeta.
- **Aprobado cuando:** están los cinco y traen el molde.

### CA-02 — Una fase sin historia no se puede abrir

```gherkin
Dada una historia que no existe
Cuando se intenta abrir una fase suya
Entonces no se crea nada, y se dice por qué
```

**Cómo validarlo:** intentándolo sin la carpeta de la historia.
- **Aprobado cuando:** no se crea nada. **Es el criterio que decide.**

### CA-03 — El nombre sale del identificador

```gherkin
Dados la letra, la épica, la historia y de qué trata
Cuando se arma el nombre
Entonces sale `LETRA-EPICA-HISTORIA-de-que-trata`
```

**Cómo validarlo:** armando nombres, con tildes y con eñes.
- **Aprobado cuando:** sale igual a los que ya están en el repositorio.

### Criterios transversales

- **Abrir sobre una carpeta que ya existe no la toca**, y se dice.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Nada escrito se pisa |
| Portabilidad | El nombre de carpeta no lleva tildes ni eñes |

---

## 6. Diseño y referencias

- Funcionalidad `F-011` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Ciclo de vida](../../../ciclo-de-vida/spec.md).
- Regla `02·F12.6`, que fija cómo se llama una fase.

---

## 7. Tareas técnicas derivadas

1. Armar el nombre desde el identificador.
2. Hallar la carpeta de la historia.
3. Escribir los cinco documentos desde el molde.
4. No tocar lo que ya existe.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [S-EP-019-HU-001-el-nombre-sale-del-identificador](S-EP-019-HU-001-el-nombre-sale-del-identificador/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-001`, que conecta el proyecto |
| **Riesgo 1** | Que abrir dos veces pise trabajo escrito. **No pisa:** avisa |
| **Riesgo 2** | Que un molde pesado haga que nadie llene los documentos. Está declarado en la ficha, y no se resuelve acá |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Los moldes existen en `plantillas/`.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que sin historia no se abre.
- ☑ Comprobado que abrir no pisa.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | Solo necesita el proyecto conectado |
| Negociable | Sí | Cuáles documentos se crean se puede ajustar |
| Valiosa | Sí | Es lo que más se repite en el día a día |
| Estimable | Sí | Es armar un nombre y copiar cinco moldes |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se abre y se mira la carpeta |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
