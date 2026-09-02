# HU-001 — Registrar una aprobación con su firma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-017 Una aprobación dice sobre qué texto](../epica.md) |
| **Funcionalidad** | `F-015` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Aprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien aprueba documentos que otros van a usar como base
- **Quiero** que quede registrado quién aprobó, cuándo y sobre qué texto exacto
- **Para** poder demostrar meses después qué fue lo que se autorizó

---

## 3. Contexto y descripción

Hoy las aprobaciones se escriben a mano dentro del documento: **21 documentos** de este repositorio traen esa línea. **Y no dicen sobre qué texto se aprobó.**

**Es la pieza de la que se sostiene todo el gobierno**, y lo dice su propia ficha. Sin ella, «aprobado» es una palabra sin respaldo.

### 3.1 Reglas de negocio

- `RN-1` **La aprobación guarda la huella del texto aprobado.**
- `RN-2` **No se aprueba un documento que no existe.** Sería firmar en blanco.
- `RN-3` **Aprobar queda registrado en la auditoría.**
- `RN-4` **Nada se borra:** cada aprobación se agrega.

### 3.2 Supuestos

- Que el documento vive en el proyecto y se puede leer.

### 3.3 Fuera de alcance

- **Comprobar quién es quien aprueba.** Se registra tal como se declara.
- Migrar las 21 marcas escritas a mano.

---

## 4. Criterios de aceptación

### CA-01 — Queda registrado quién, cuándo y sobre qué texto

```gherkin
Dado un documento que existe
Cuando alguien lo aprueba
Entonces queda quién, cuándo, y la huella del texto
```

**Cómo validarlo:** aprobando un documento de prueba.
- **Aprobado cuando:** la huella guardada es la del texto que había.

### CA-02 — La aprobación se puede consultar meses después

```gherkin
Dado un documento aprobado
Cuando se consulta su historia
Entonces la aprobación sigue ahí
```

**Cómo validarlo:** consultando después de aprobar.
- **Aprobado cuando:** aparece, con todos sus datos.

### CA-03 — No se puede aprobar un documento que no existe

```gherkin
Dado una ruta que no corresponde a ningún documento
Cuando se intenta aprobar
Entonces se rechaza, y no queda nada registrado
```

**Cómo validarlo:** con una ruta inventada, y con un proyecto que no existe.
- **Aprobado cuando:** los dos se rechazan. **Es el caso de «que NO pase».**

### Criterios transversales

- Aprobar queda en la auditoría.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Trazabilidad | Toda aprobación dice sobre qué texto |
| Integridad | Un intento fallido no deja registro de una aprobación que no hubo |

---

## 6. Diseño y referencias

- Funcionalidad `F-015` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-15` del [análisis](../../../../cvds/analisis-requisitos/README.md).

---

## 7. Tareas técnicas derivadas

1. La entidad que guarda la aprobación, con su huella.
2. Aprobar, leyendo el texto que hay.
3. Rechazar lo que no existe.
4. Registrar en la auditoría.
5. Consultar la historia.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto](M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-009`, la auditoría |
| **Riesgo 1** | Que se apruebe sin huella y «aprobado» siga sin decir nada. Sin huella no se guarda |
| **Riesgo 2** | Firmar en blanco un documento que aún no existe. Está impedido |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medidas las 21 marcas escritas a mano.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que la huella es la del texto aprobado.
- ☑ Comprobado que un intento fallido no deja registro.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita la auditoría |
| Negociable | Sí | Qué se guarda además se puede ajustar |
| Valiosa | Sí | Es la pieza de la que se sostiene el gobierno |
| Estimable | Sí | Una entidad y una huella |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se aprueba y se mira lo guardado |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
