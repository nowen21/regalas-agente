# Funcionalidad implementada — Fase `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-llenar-un-hueco-desde-la-plataforma.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` |
| **Épica / HU** | [EP-013](../../epica.md) · [HU-002](../HU-002-llenar-un-hueco-desde-la-plataforma.md) |
| **Módulo** | Ciclo de vida |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**Un hueco se llena desde la plataforma, y lo escrito queda en el archivo del proyecto.** Es la primera pieza que escribe fuera de `datos/`: hasta hoy la plataforma leía los proyectos y escribía solo sus copias.

**Y no cambia ni un carácter fuera del hueco.** Comprobado sobre un archivo real: 237 caracteres antes, 350 después, y el control de versiones ve **una línea cambiada**.

Con esto `F-014` queda completa, y con ella **la versión 2**.

**Lo que además corrigió de la fase anterior:** la cuenta de espacios por llenar pasó de 77 a **26**. Los 51 que sobraban eran la marca escrita dentro de código, o sea documentos hablando de la convención.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Lo escrito va al archivo original» (`RN-4`) | servicio | `ruta_original` en [plataforma/nucleo/ciclo_de_vida/core.py](../../../../../plataforma/nucleo/ciclo_de_vida/core.py) | ✅ | CP-001 |
| «Se toca solo el hueco» (`RN-5`) | servicio | `reemplazar` en [plataforma/nucleo/ciclo_de_vida/escritura.py](../../../../../plataforma/nucleo/ciclo_de_vida/escritura.py) | ✅ | CP-002 |
| «Si el archivo cambió por fuera, se avisa» (`RN-6`) | servicio | `llenar_el_hueco`, con la huella | ✅ | CP-004 |
| «Escribir queda registrado» (`RN-7`) | servicio | `con_constancia`, antes del efecto | ✅ | CP-005 |
| «El archivo nunca queda a medias» (§6) | servicio | `guardar_de_un_golpe` | ✅ | EV-01 |
| «Después de escribir se vuelve a traer» (`RN-1.1`) | servicio | `_poner_al_dia_la_copia` | ✅ | CP-001 |
| «No se escribe a ciegas en una posición» (§6) | servicio | Se comprueba marca y contexto | ✅ | CP-006 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | El reemplazo que no toca nada más, y el guardado de un golpe |
| T-03 · T-04 | La huella, el aviso, y el registro antes del efecto |
| T-05 · T-06 | La copia al día, y la orden de consola |
| T-07 | **24 pruebas**, más 2 de la cuenta corregida |
| T-08 | **Un documento real llenado**, con cero caracteres cambiados fuera del hueco |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/` | 50 pruebas, en verde |
| La batería de la plataforma completa | 302 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La medición sobre un archivo real | 0 caracteres cambiados fuera del hueco |

**Lo que las pruebas no dicen:** si llenar así resulta cómodo. Un documento de un hueco no responde eso; lo responde quien llene uno de veinte.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py llenar_hueco <proyecto> <documento>
python manage.py llenar_hueco <proyecto> <documento> --numero 1 --texto "lo que va"
```

Sin `--texto` muestra los huecos numerados, con su línea. **Escribe en el archivo del proyecto**, no en la copia, y deja la copia al día.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Se escribe en el archivo original del proyecto** | Decidido con el usuario. La copia se rehace al importar, y el proyecto quedaría igual |
| **Los finales de línea no se traducen** | Traducirlos cambiaría **todos** los renglones sin que se vea, y arruina el criterio que decide la fase |
| **Se escribe al lado y se pone en su sitio de un golpe** | Si el guardado se interrumpe, o está el de antes o está el de después. Nunca a medias |
| **La huella se compara antes de escribir** | Es lo único que distingue «nadie lo tocó» de «alguien más escribió». Adivinar cuál vale no es del programa |
| **Se comprueba el contexto, no solo la posición** | Si el documento se movió, ahí ya vive otra cosa |
| **La marca dentro de código no es un hueco** | Un documento que **habla de** la convención no está incompleto. Eran 51 de 77 |
| **Lo que la consola no pueda escribir se reemplaza al mostrar** | Perder un signo no cuesta nada; no poder ver el hueco, sí |
| **Llenar con nada no hace nada** | Borrar la marca sin poner nada deja el documento peor: ya no se ve que falta |

Señal registrada: [`S-105`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Quedan 25 documentos con 26 espacios por llenar.** Llenarlos es trabajo de contenido, no de esta fase.
- **Sin pantalla**, como el resto del módulo.
- **Si llenar así es cómodo** sigue sin responderse. Se responde llenando un documento de veinte huecos, y hoy el que más tiene tiene dos.
- **Los números de la fase A quedaron viejos.** Su cierre dice 54 documentos y 77 huecos, que era lo cierto ese día con el defecto adentro. No se reescribe: la corrección está acá y en su estado de fase.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Su §13 nombra esta fase, y la §5.1 la cuarta exclusión |
| [documentacion/senales.md](../../../../senales.md) | `S-105` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.** Lo que cambia es que la plataforma pasa a escribir en el proyecto del usuario, y está declarado en la especificación.
