# Funcionalidad implementada — Fase `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` |
| **Épica / HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) · [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md) |
| **Módulo** | Automatismos — enganches |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**No queda ningún enganche en la carpeta de lo agnóstico.** `hook_estacion.py` vive con los otros quince en `adaptadores/claude-code/`.

Y lo que la mudanza destapó, que era el defecto de fondo: **la comprobación de la frontera miraba un solo canal**. Un enganche se conecta por `.claude/settings.json` o por un enganche de git, y este va por el segundo. Ahora la lista de lo conectado se **deriva de las dos tablas** que el instalador escribe.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| CA | Qué lo cumple | Dónde | Evidencia |
|---|---|---|---|
| [CA-04](../HU-011-donde-termina-el-estandar.md#ca-04--el-adaptador-vive-en-un-solo-sitio-separado-de-lo-agnóstico) | El enganche mudado y la cuenta de los dos canales | `adaptadores/claude-code/hook_estacion.py` · `instalar.enganches_enchufados()` | 9 pruebas de la frontera |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El enganche movido con `git mv`, y la plantilla del `post-commit` apuntando al adaptador |
| T-03 · T-04 | `enganches_enchufados()` y la prueba que la usa |
| T-05 | Instalador corrido; el enganche comprobado con un commit de verdad |
| T-06 | El mapa del amarre, con la mudanza y con el porqué de que el recuento no se moviera |
| **Fuera del plan** | Cómo nombran a su corredor `estacion_commit.py` y `rutas_fuera.py`: decir el archivo del enganche los hacía contarse como amarrados |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `test_la_frontera_del_adaptador.py` | 9 pruebas, en verde |
| `test_el_mapa_del_amarre_no_envejece.py` | 12 pruebas, en verde |
| `validar.py amarre` | 27 de 85, igual que antes |
| La batería interna completa | Sin fallas nuevas |

**Lo que las pruebas no dicen:** si un proyecto ya instalado corrió el instalador. Hasta que lo corra, su `post-commit` apunta a la ruta vieja y el enganche no anota nada — sin romper el commit, porque la línea termina en `|| true`.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Nada que correr a mano. El enganche lo llama git después de cada commit, y la ruta la escribe el instalador:

```
python validadores/instalar.py <ruta del proyecto> --aplicar
```

**Al agregar un enganche nuevo**, va en `adaptadores/claude-code/` y se conecta por una de las dos tablas del instalador. La prueba de la frontera se cae si queda uno sin conectar, o un enchufe a un archivo que no está.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| Ampliar la cuenta en vez de exceptuar el archivo | La carpeta de lo agnóstico no admite excepciones, o deja de decir lo que dice |
| La lista se deriva de las plantillas | Una lista escrita al lado envejece sin avisar (`S-091`) |
| Los dos programas nombran a su corredor **sin su archivo** | Nombrarlo los hacía contarse como amarrados a la herramienta: el contador busca la palabra dentro del texto, y un mensaje que **habla de** un enganche no es un enganche |

Señal registrada: [`S-095`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **El contador del amarre no distingue nombrar de ser.** Acá se esquivó cambiando la redacción; el día que otro programa necesite nombrar un enganche en su salida, volverá a pasar. Queda dicho, sin pendiente: hasta hoy son dos casos y los dos se resolvieron escribiendo mejor.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [anatomia/que-esta-amarrado-a-la-herramienta.md](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) | La mudanza, y por qué el recuento no se movió |
| [documentacion/senales.md](../../../../senales.md) | `S-095` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: el estándar no se despliega. Lo que llega a los proyectos es la ruta nueva del enganche, la próxima vez que corran el instalador.
