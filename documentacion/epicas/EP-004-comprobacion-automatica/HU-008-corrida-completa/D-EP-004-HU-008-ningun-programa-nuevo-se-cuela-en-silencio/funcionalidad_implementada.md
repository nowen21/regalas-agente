# Funcionalidad implementada — Fase `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` |
| **Épica / HU** | [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../../epica.md) · [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md) |
| **Módulo** | Comprobación automática |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**Ningún programa del estándar sale con 0 sin decir nada.** Los dos que faltaban ahora dicen quién los corre, y salen con 2 para que un guion que los llame por error distinga «no comprobé nada» de «comprobé y hay fallas».

**Y la corrida completa vuelve a terminar con su veredicto.** El conteo por regla, que se agregó después y había quedado debajo del resumen, ahora sale antes: se movió entero, no se recortó.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| CA | Qué lo cumple | Dónde | Evidencia |
|---|---|---|---|
| [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | El guardián que nombra al corredor, y el orden de la salida | `comun.no_es_punto_de_entrada` · `validar.cmd_todo` | 13 pruebas |
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | Las cuatro fallas de estas causas, en verde | La batería interna | `validar.py internas` |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | `no_es_punto_de_entrada(la_corre=…)`, opcional, con el camino viejo intacto |
| T-02 | `estacion_commit.py` nombra el `post-commit`; `rutas_fuera.py`, el enganche del adaptador |
| T-03 | La prueba acepta «enganche» además de `validar.py`, y se comprobó con sabotaje que sigue cazando el silencio |
| T-04 | El conteo por regla, antes del resumen |
| T-05 | Batería interna corrida y comparada con la línea base |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `test_ninguno_termina_en_silencio.py` | 6 pruebas, en verde |
| `test_la_corrida_completa_en_una_linea.py` | 7 pruebas, en verde |
| Sabotaje: un módulo que calla | **Se caza**, y la corrida falla |
| La batería interna completa | Sin fallas de estas causas |

**Lo que las pruebas no dicen:** si el mensaje le sirve a quien lo lee. Se comprueba que nombre al corredor; que ese nombre lleve a alguna parte lo decide una persona.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

```
python validadores/validar.py todo     # el veredicto queda en las últimas líneas
```

**Al escribir un programa nuevo en `validadores/`**, se cierra con el guardián:

```python
if __name__ == "__main__":
    comun.no_es_punto_de_entrada("<subcomando>")           # si cuelga de validar.py
    comun.no_es_punto_de_entrada(la_corre="<quién lo corre>")   # si lo llama otro
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| El mensaje nombra al corredor de verdad | Decirles «es una pieza de `validar.py`» los mandaría a un subcomando que no existe |
| Nombrar al corredor **sin su archivo** | El contador del amarre busca la palabra dentro del texto, y subió de 27 a 29 |
| El conteo sube, el resumen baja | El conteo dice qué regla cambiar y vale entero; lo último tiene que ser el veredicto |
| La prueba se amplía y **se sabotea** | Cambiar la comprobación que reporta un defecto es la forma más fácil de hacer desaparecer un rojo sin arreglar nada |

Señal registrada: [`S-096`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Ninguno.** Lo que queda de la batería son fallas de otras causas, ajenas a esta historia.
- **Lo que sí queda dicho:** las dos reglas se rompieron porque algo nuevo se agregó sin pasar por donde la regla vigila, y la prueba lo decía desde entonces **sin que nadie la corriera**. Eso ya tiene dueño: `EP-005·HU-021` puso a correr las 650.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/senales.md](../../../../senales.md) | `S-096` |

No se creó módulo nuevo ni cambió ninguna ruta: los mapas quedan como estaban.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: el estándar no se despliega, y lo que se tocó es su propia salida por consola.
