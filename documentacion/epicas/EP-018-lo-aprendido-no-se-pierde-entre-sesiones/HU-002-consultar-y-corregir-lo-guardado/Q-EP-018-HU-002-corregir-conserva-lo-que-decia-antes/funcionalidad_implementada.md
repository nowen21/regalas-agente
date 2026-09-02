# Funcionalidad implementada — Fase `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-consultar-y-corregir-lo-guardado.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes` |
| **Épica / HU** | [EP-018](../../epica.md) · [HU-002](../HU-002-consultar-y-corregir-lo-guardado.md) |
| **Módulo** | Memoria |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**El usuario ya puede ver, buscar, corregir y dar de baja lo que el agente recuerda.**

**Corregir conserva lo que decía antes**, debajo y marcado. Un recuerdo corregido cuenta dos cosas y las dos sirven: lo que vale hoy, y lo que se creía ayer. Sin la segunda, la corrección queda sin explicación.

**Dar de baja marca, no borra.** Es exactamente lo que el estándar hace con sus propias reglas (`20·M11`): lo derogado sigue siendo la respuesta a por qué algo se hizo como se hizo.

**Con esta fase cierra `EP-018`, y con ella la versión 4.**

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se busca por palabra» (`RN-1`) | servicio | `buscar` en [plataforma/nucleo/memoria/core.py](../../../../../plataforma/nucleo/memoria/core.py) | ✅ | CP-004 |
| «Corregir conserva lo anterior» (`RN-2`) | servicio | `corregir` | ✅ | CP-005 |
| «Dar de baja no borra» (`RN-3`) | servicio | `dar_de_baja` | ✅ | CP-006 |
| «Una búsqueda vacía se dice» (`RN-4`) | servicio | `buscar` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Corregir conservando, y la marca de baja |
| T-03 · T-04 | Que lo de baja salga de lo vigente, y las dos acciones en consola |
| T-05 | **10 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/memoria/` | 16 pruebas del módulo, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si lo corregido es más cierto que lo anterior.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py memoria <proyecto> --buscar <palabra>
python manage.py memoria <proyecto> --corregir <nombre> --texto "..."
python manage.py memoria <proyecto> --dar-de-baja <nombre>
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Corregir deja lo anterior debajo** | Un recuerdo corregido cuenta dos cosas, y las dos sirven |
| **Dar de baja marca, no borra** | Lo mismo que el estándar con las reglas derogadas (`20·M11`) |
| **La marca va al principio del cuerpo** | Quien abre el archivo tiene que verla antes de leerlo |
| **Lo de baja sale de lo vigente, no del listado** | El usuario tiene que poder ver que existió |

Señal registrada: [`S-112`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Un recuerdo con muchas correcciones se vuelve pesado de leer.** Declarado y aceptado: muchas correcciones son la señal de que ese recuerdo hacía falta.
- **Nada revisa si un recuerdo sigue siendo cierto.**
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/memoria/spec.md](../../../../memoria/spec.md) | Su §13 nombra esta fase, y con ella cierra `EP-018` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
