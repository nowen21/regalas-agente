# EP-014 — Ninguna clave queda escrita

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-014 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Seguridad |
| **Versión del producto** | 3, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-031` |
| **Estado** | Aprobada el 2026-09-01 |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que una clave pegada en una conversación o tecleada en un documento no quede escrita para siempre. Es el único daño de la versión 3 que **no se puede deshacer**.

## 3. Problema y oportunidad

**Situación actual, medida el 2026-09-01.** La pieza que tapa claves existe y funciona, pero **la usa un solo camino de los seis que escriben**:

| Camino que escribe | Tapa hoy |
|---|---|
| Auditoría | **Sí** |
| Ciclo de vida, al llenar un hueco | No |
| Importación | No |
| Almacén · Expediente · Medición | No |

**Qué cuesta.** La ficha de `F-031` lo dice: es el único daño de la lista que no se deshace. Una clave escrita en un documento versionado queda en el historial aunque se borre después.

**Y hay un daño simétrico que la medición destapó.** Sobre los 1 002 documentos guardados, el tapador cambiaría **7 documentos y 21 fragmentos**. Los 21 son claves inventadas, y están en los documentos de las fases **que construyeron el tapador**: son sus casos de prueba escritos.

```
| 1 | Registrar una acción con `password: "inventada123"` | ... |
```

Tapar al importar corrompería justo los documentos que documentan el tapador, **en silencio y sin vuelta atrás**. Es el mismo caso que ya apareció con los espacios por llenar: un documento que **habla de** algo parece contenerlo.

## 4. Objetivo y propuesta de valor

Que **lo que se teclea se tape, y lo que se copia no**, y que lo que no se tapa se diga en vez de callarse.

**Beneficios esperados:**

- Una clave pegada al llenar un documento no llega al archivo.
- Los documentos que ya existen entran como están, sin que nadie los altere.
- Quien trae un proyecto sabe **cuántos** de sus documentos parecen traer credenciales.

## 5. Alcance

**Dentro:**

- Tapar en el camino que escribe lo que una persona acaba de teclear.
- Avisar, al importar, cuántos documentos parecen traer credenciales, sin tocarlos.
- Declarar, camino por camino, cuál tapa y cuál no, y por qué.

**Fuera:**

- **Tapar lo que se importa.** Decidido el 2026-09-01 con la medición delante: alteraría 7 documentos reales sin vuelta atrás.
- Reconocer formas nuevas de credencial: eso vive en el estándar, y la plataforma lo usa por un puente.
- Quitar del historial de versiones una clave ya escrita. Eso no lo puede hacer la plataforma.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-031` Tapar toda credencial antes de escribirla | El texto con la clave tapada, y el nombre de la variable intacto | 3 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Escribe, y a veces pega una clave sin darse cuenta |
| El agente | Lo mismo, y además registra lo que hace |
| El estándar | Es quien sabe **reconocer** una credencial. La plataforma no duplica esa lista |

## 7. Criterios de aceptación de la épica

- Lo que se teclea desde la plataforma llega al archivo **con la clave tapada**.
- **El nombre de la variable queda intacto:** tapar el nombre haría el documento ilegible sin proteger nada.
- Lo importado **no se altera**, y lo que parezca traer credenciales se dice con su número.
- Cada camino que escribe declara si tapa o no, y por qué.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Claves que llegan a un archivo por un camino que teclea | **Cero** |
| Documentos importados alterados | **Cero** |
| Documentos con apariencia de credencial que entran sin avisar | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-tapar-la-clave-al-escribirla/HU-001-tapar-la-clave-al-escribirla.md) | Tapar la clave al escribirla | `F-031` | Aprobada el 2026-09-01 |

## 10. Consideraciones técnicas

**El módulo Seguridad ya existe** y no tenía especificación: se escribe en esta épica. Su pieza es un puente hacia `validadores/enmascarar.py`, que es quien conoce las formas de credencial.

**Por qué un puente y no una copia:** dos listas de secretos se separan, y la que quede vieja deja pasar una clave el día que aparezca una forma nueva.

**Decisión que la gobierna:** [`00·N6`](../../../base/00-nucleo-blindado.md), blindada: una credencial no se escribe, no se registra y no se guarda.

## 11. Dependencias

Depende de `EP-009`, la auditoría, que es el primer camino que ya tapa. Y de `EP-013`, que abrió el camino que teclea.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Tapar de más, y corromper un documento sin vuelta atrás** | Se mide antes: hoy serían 7 documentos, todos ejemplos escritos. Por eso lo importado no se tapa |
| Tapar de menos, y que una clave quede escrita | El reconocimiento vive en el estándar, con sus pruebas, y no se duplica |
| Que un camino nuevo nazca sin tapar | Cada camino queda declarado en la especificación, con su razón |

## 13. Supuestos y restricciones

**Supuestos:** que el enmascarador del estándar está disponible. Si no está, **se revienta en vez de escribir sin tapar**.

**Restricciones:** lo importado no se altera; el nombre de la variable no se tapa; el reconocimiento no se duplica.

## 14. Hoja de ruta

Versión 3. Va primero de esa versión: es lo más pequeño, lo único con daño irreversible, y ya tenía la mitad construida.

## 15. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ Medido qué caminos tapan hoy y qué pasaría si taparan todos.
- ☑ El módulo Seguridad, con [especificación](../../seguridad/spec.md) aprobada el 2026-09-01.
- ☑ La historia escrita y aprobada.

## 16. Definition of Done

- ☑ La historia cerrada, con veredicto por criterio.
- ☑ Comprobado que llenar un hueco con una clave la tapa.
- ☑ Comprobado que importar **no altera** ningún documento.
- ☑ El aviso de importación, medido sobre los 1 002 documentos reales.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Cerrada**: su historia construida y probada el mismo día |
| 2026-09-01 | Nace de `F-031`, que estaba construida a medias sin épica ni historia: el puente existía y lo usaba un solo camino. La medición sobre los 1 002 documentos guardados fijó el alcance |
