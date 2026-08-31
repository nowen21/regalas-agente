# Resultado de Pruebas — Fase `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si el criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` |
| **HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre el repositorio del estándar |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |

| | Antes | Después |
|---|---|---|
| Enganches en `validadores/` | 1 | **0** |
| Canales que la prueba de la frontera mira | 1 | **2** |
| Recuento del amarre | 27 de 85 | **27 de 85** |

---

## 2. Ejecución caso por caso

### CP-001 — Ningún enganche en la carpeta de lo agnóstico

`hook_estacion.py` se movió con `git mv` a `adaptadores/claude-code/`, y su ruta a `validadores/` sube un nivel más. No queda ningún `hook_*.py` en la carpeta de lo agnóstico.

**Resultado: pasa.**

### CP-002 — El comando que se instala apunta al adaptador, y el enganche corre

```
$ python validadores/instalar.py "c:/Ing. Jose/ia/agente" --aplicar
  · escribir .githooks\post-commit

$ grep hook_estacion .githooks/post-commit
"$PY" "$ESTANDAR/adaptadores/claude-code/hook_estacion.py" --raiz "$(pwd)" || true
```

**Y con un commit de verdad:** el enganche corrió y anotó el hash en la estación 12 de la fase que cerraba, que es lo que hace cuando encuentra su trabajo.

**Resultado: pasa.**

### CP-003 — Lo conectado se cuenta por los dos canales

**Este caso encontró el defecto que la mudanza destapó.** Recién movido, la prueba de la frontera dio rojo: comparaba los enganches del adaptador contra la tabla de la herramienta, y `hook_estacion.py` no está ahí — lo conecta el `post-commit` de git.

`instalar.enganches_enchufados()` ahora junta los dos canales, y **los deriva de las mismas plantillas que se escriben**, no de una lista aparte. Las dos listas coinciden: dieciséis.

**Resultado: pasa.**

### CP-004 — El recuento del amarre no bajó

```
$ python validadores/validar.py amarre
Piezas de `validadores/`: 85 · amarradas a la herramienta: 27 · libres: 58
```

El mismo número de antes. **La igualdad es el resultado esperado:** el recuento mira las dos carpetas, así que mover código no desamarra nada.

**Resultado: pasa.**

### CP-005 — No regresión

Las 27 pruebas de los tres archivos que la fase toca —la frontera, el mapa del amarre y el silencio— en verde, y la batería interna completa sin fallas nuevas.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El `post-commit` generado | Apunta al adaptador |
| La historia del archivo movido | Intacta: `git mv` la conserva |
| El mapa del amarre | Dice dónde vive ahora, y por qué el recuento no se movió |

Ninguna prueba tocó datos reales.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | La comprobación de la frontera miraba **un solo canal**, y el enganche mudado parecía un archivo que nadie usa | Alta | Arreglado acá: la lista se deriva de las dos tablas |
| D-02 | Al decir «lo corre el enganche `hook_rutas.py`», dos programas agnósticos pasaron a **contarse como amarrados a la herramienta**: el contador busca la palabra `hook_` dentro del texto | Media | Arreglado nombrando al corredor sin su archivo. Se vio porque el recuento subió de 27 a 29 |

**El segundo es el interesante:** un mensaje que **habla de** un enganche no es un enganche, y el contador no puede distinguirlo. Es el mismo argumento que ya estaba escrito para `amarre.py`, que se exceptúa a sí mismo porque nombra la herramienta para medirla.

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-04](../HU-011-donde-termina-el-estandar.md#ca-04--el-adaptador-vive-en-un-solo-sitio-separado-de-lo-agnóstico) | CP-001 a CP-004 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Mover el enganche con `git mv` | Hecho |
| La plantilla del `post-commit` al sitio nuevo | Hecha, y el instalador corrido |
| La cuenta de los dos canales | Hecha, derivada de las plantillas |
| El mapa del amarre al día | Hecho |
| El recuento sin bajar | 27 de 85, igual que antes |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El `CA-04` de `HU-011` vuelve a estar cumplido, y esta vez con la comprobación que lo vigila mirando por donde de verdad se conectan los enganches. Lo que la fase agrega sobre la mudanza es eso: **el defecto no era el archivo mal puesto, era que la cuenta de lo conectado estaba incompleta** y por eso la mudanza no se podía hacer sin romper otra prueba.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las nueve pruebas de la frontera | `validadores/tests/test_la_frontera_del_adaptador.py` |
| EV-02 | El `post-commit` apuntando al adaptador | `.githooks/post-commit` |
| EV-03 | El recuento del amarre | `validar.py amarre` |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
