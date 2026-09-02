# Funcionalidad implementada — Fase `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` (módulo Medición)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` |
| **Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Módulo** | Medición |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**El reporte dejó de encabezarse con la forma de redactar del usuario.** Antes arriba estaban «debe quedar», «puede cerrar» y «debe tener»; ahora está lo que de verdad tuvo que repetir:

```
 11  estoy preguntando     8 sesiones
 15  plan trabajo          7 sesiones
  7  historico chat        7 sesiones
  9  espanol colombiano    5 sesiones
```

**«Español colombiano» pasó del puesto 21 al cuarto**, y sigue ahí después del filtro, que era la comprobación que importaba.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Qué | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| El vocabulario de la casa | servicio | `vocabulario_de_la_casa` en [plataforma/nucleo/medicion/repeticion.py](../../../../../plataforma/nucleo/medicion/repeticion.py) | ✅ | CP-001 |
| Que no se lleve lo que sí es tema | servicio | El umbral y su resguardo | ✅ | CP-002 |
| Las rutas pegadas | servicio | `sin_lo_de_la_maquina` | ✅ | CP-003 |
| Mínimo de sesiones distintas, y orden | servicio | `correcciones` | ✅ | CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-00 | Se midieron las tres formas; dos se descartaron con su número |
| T-01 · T-02 | El vocabulario calculado, y la frase que lo usa descartada |
| T-03 | Las rutas pegadas: dos filas menos |
| T-04 · T-05 | El mínimo de sesiones, el orden nuevo, y el resguardo de corpus chico |
| T-06 · T-07 | 9 pruebas nuevas y el reporte antes y después |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/medicion/` | 47 pruebas, en verde |
| El caso que decide: que el filtro no se lleve lo bueno | «Español colombiano» sigue |
| Las dos baterías del repositorio | En verde |

**Lo que las pruebas no dicen:** si de esas filas nace una regla. Es juicio, y es el riesgo 2 de la historia.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Igual que antes; lo que cambió es qué sale:

```
python manage.py correcciones_que_se_repiten --desde 2026-08-01
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El vocabulario se calcula sobre el corpus** | Una lista a mano acierta en lo que uno se imagina y envejece con el proyecto |
| Una palabra en más del cuarto de las sesiones es vocabulario | Un número absoluto no sirve a la vez para diez sesiones y para mil |
| **Con pocas sesiones no se filtra** | El filtro se llevaría todo, y un reporte vacío se lee como «no hubo nada» |
| **Repetir en un solo día no cuenta** | Tres veces el mismo día es insistir; tres días distintos es una regla que falta |
| Una ruta pegada no es una frase | «ing jose» encabezaba con doce sesiones, y es el nombre de una carpeta |
| **La mejora aprobada se midió antes de construirla** | No funcionaba. Costó veinte minutos saberlo y evitó entregar algo que no servía |

Señal registrada: [`S-100`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **El umbral se calibró contra este trabajo.** En un proyecto que hable de otra cosa habrá que volver a mirarlo. Queda dicho, sin pendiente: hoy hay un solo corpus.
- **Sin pantalla**, como las dos fases anteriores.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/senales.md](../../../../senales.md) | `S-100` |

No se creó módulo nuevo ni cambió ninguna ruta.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

Nada que desplegar y ninguna migración: el módulo solo lee.
