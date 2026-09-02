# EP-019 — El ciclo se opera desde la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-019 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Ciclo de vida |
| **Versión del producto** | 5, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-011`, `F-012`, `F-013` |
| **Estado** | Terminada el 2026-09-01: sus tres historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Abrir una fase con sus documentos, ver en cuál estación va cada una, y no dejar pasar la puerta que falta.

## 3. Problema y oportunidad

**Hoy las fases se abren a mano**, carpeta por carpeta y documento por documento. La ficha de `F-011` dice para qué sirve automatizarlo: *«que nadie cree carpetas y archivos a mano, ni se salte un documento»*.

**Y el estado depende de que alguien lo recuerde.** Este repositorio tiene **209 fases**. Una se mira abriendo su documento; doscientas no se miran de ninguna forma.

**El caso que lo vuelve urgente lo dio el propio repositorio al medirlo:** hay fases que dicen ir en la estación 12 y tienen la 4 pendiente en su tabla. Nadie lo había visto porque nadie puede leer doscientos documentos a la vez.

## 4. Objetivo y propuesta de valor

Que el estado de una fase salga **de lo escrito**, y no de la memoria de nadie.

**Beneficios esperados:**

- Una fase se abre con sus cinco documentos y su nombre bien puesto.
- Se ve, de un golpe, en qué va cada fase y qué le falta.
- La puerta que falta se dice por su nombre, no como «no se puede avanzar».

## 5. Alcance

**Dentro:**

- Abrir una fase con sus cinco documentos (`F-011`).
- Ver la estación actual y la puerta pendiente de cada fase (`F-012`).
- Impedir pasar sin la puerta cumplida, diciendo cuál falta (`F-013`).

**Fuera:**

- **Abrir épicas e historias.** La fase es donde duele; una épica se escribe una vez cada varias semanas.
- **Marcar las estaciones.** Las marca quien hace el trabajo; acá se leen.
- Reescribir las fases viejas para que usen la tabla de hoy.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-011` Crear épicas, historias y fases con su molde | La fase abierta, con sus cinco documentos | 5 |
| `F-012` Ver en qué estación va cada fase | La estación actual y la puerta pendiente, de todas | 5 |
| `F-013` Impedir avanzar sin la puerta cumplida | El paso, o el rechazo diciendo cuál puerta falta | 5 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Abre fases y mira cómo van |
| El agente | Consulta la puerta antes de avanzar |
| El módulo Auditoría | Guarda que se abrió una fase |

## 7. Criterios de aceptación de la épica

- Una fase se abre con sus cinco documentos, tomados del molde.
- **Una fase sin historia no se abre.**
- El nombre sale del identificador, no se escribe a mano.
- Se ve la estación actual de cualquier fase, y qué le falta.
- Una fase detenida dice desde cuándo.
- **El rechazo dice cuál puerta falta**, no solo que falta.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Fases abiertas sin alguno de sus cinco documentos | **Cero** |
| Fases que pisan trabajo ya escrito al abrirse | **Cero** |
| Rechazos que no nombran la puerta | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-abrir-una-fase-con-sus-documentos/HU-001-abrir-una-fase-con-sus-documentos.md) | Abrir una fase con sus documentos | `F-011` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-ver-en-que-estacion-va-cada-fase/HU-002-ver-en-que-estacion-va-cada-fase.md) | Ver en qué estación va cada fase | `F-012` | **Terminada el 2026-09-01** |
| [HU-003](HU-003-impedir-avanzar-sin-la-puerta-cumplida/HU-003-impedir-avanzar-sin-la-puerta-cumplida.md) | Impedir avanzar sin la puerta cumplida | `F-013` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Crece el módulo Ciclo de vida**, que ya existía con [especificación](../../ciclo-de-vida/spec.md) aprobada.

**Sin entidad en la base.** El estado de una fase está escrito en su `estado-fase.md`: `DA-01`.

**Y hay que leer lo que hay, no lo que debería haber.** Al correrlo contra las 209 fases apareció que **107 no usan la tabla de trece estaciones** —83 traen once y 24 traen menos— y que **76 cierran con `✅` en vez de `☑`**. Ninguna se reescribe: son fases cerradas, y el que se adapta es el que lee.

## 11. Dependencias

Depende de `EP-008`, que conecta los proyectos, y de `EP-009`, donde queda registrado que se abrió una fase.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que abrir una fase pise trabajo escrito** | Si la carpeta existe, no se toca |
| Que se abran fases sueltas | Sin historia no se abre |
| **Que una puerta estorbe y se termine saltando** | Se comprueban tres, no trece |
| Que se acuse de contradicción a una fase de otro modelo | Solo se compara cuando la tabla es de trece |

## 13. Supuestos y restricciones

**Supuestos:** que la historia existe antes que la fase, y que los moldes viven en `plantillas/`.

**Restricciones:** las fases cerradas no se reescriben; las estaciones las marca una persona; esto no es un candado, es un aviso.

## 14. Hoja de ruta

Versión 5. Va primero de esa versión: las otras dos épicas leen lo que esta ordena.

## 15. Definition of Ready

- ☑ Las tres funcionalidades están en el inventario, con su ficha.
- ☑ Medidas las 209 fases del repositorio, y sus modelos de tabla.
- ☑ El módulo Ciclo de vida, con [especificación](../../ciclo-de-vida/spec.md) aprobada.

## 16. Definition of Done

- ☑ Las tres historias cerradas, con veredicto por criterio.
- ☑ Comprobado que abrir no pisa.
- ☑ Comprobado que sin historia no se abre.
- ☑ Comprobado que el rechazo nombra la puerta.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las tres historias construidas y probadas el mismo día |
| 2026-09-01 | Nace del inventario aprobado, para operar el ciclo desde la plataforma |
