# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

p = "pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md"
s = L.leer(p)
s = s.replace("**Estado:** abierto · anotado 2026-08-15",
              "**Estado:** **decidido** el 2026-08-22, con la orden «haga los dos»; abierto hasta que lo que quedó por construir se construya · anotado 2026-08-15", 1)
s += """

---

# Lo que quedaba, resuelto  ·  2026-08-22

El usuario ordenó resolverlo. **Lo primero fue volver a medir**, porque este archivo se escribió el 2026-08-15 y el repositorio cambió desde entonces (es la lección de la señal [S-020](../documentacion/senales.md)). De los once puntos abiertos, **siete estaban contestados por lo que ya está escrito o construido**; los otros cuatro piden trabajo, y va cada uno con su decisión.

## Las que el repositorio ya contesta

| # | Duda | Qué dice el repositorio hoy |
|---|---|---|
| **Capas · 1** | ¿El preámbulo es una capa? | **No.** Los dos capítulos de preámbulo (`00 · Identidad y rol` y `20 · Meta-reglas`) llevan su propia marca `[PREÁMBULO]` en la cabecera, y el `20` declara su límite: *«son de procedimiento, nunca de fondo; no autorizan nada ni relajan nada»*. Una capa ordena qué gana ante un choque; el preámbulo no entra en ese orden porque no exige fondo |
| **Capas · 2** | ¿Cuántas capas hay? | **Cuatro niveles**, y ya está escrito en [`20·M1`](../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y en la tabla de [`base/README.md`](../base/README.md): `[CAPA 1]` núcleo, `[CAPA 2]` convenciones, `[CAPA 2 · opt-in]` y `[CAPA 3]` proyecto. La duda nació cuando la capa del proyecto no existía; hoy existe |
| **Capas · 3** | ¿«Opcional» es marca o capa? | **Marca dentro de la capa 2**, y así está construido: los capítulos `17`, `18`, `19`, `21` y `22` llevan `[CAPA 2 · opt-in]`. No es otra capa porque no cambia quién gana ante un choque: cambia si la regla aplica |
| **EP-001** | ¿Las fases de EP-001 son plan o retrodocumentación? | **Retrodocumentación**, y las fases lo dicen en su propio nombre: `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` y así las demás. Lo que sigue vivo no es la pregunta: es que 34 de esas fases están detenidas, y eso es el [59](59-las-42-dudas-que-detienen-26-fases.md) |
| **Español correcto** | ¿Se escribe la regla? | **No hace falta una regla nueva.** [`01·C8`](../base/01-conducta.md#c8--habla-el-idioma-del-proyecto) fija el idioma, `01·C24` exige traducir el término que no esté en él, y [`00·ID7`](../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) exige que se entienda. Una regla de ortografía y sintaxis correctas es de las que [`20·M19`](../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) desaconseja: no hay forma de comprobarla y ya se cumple |
| **LocalHub sin sello** | ¿Por qué quedó sin sello y AgroSystem sí? | **No se puede investigar desde acá y ya no hace falta.** El registro de proyectos vive hoy en la base de datos de la interfaz, y el sello lo pone `instalar.py` al correr; cualquier proyecto sin sello se resuelve volviendo a correr el instalador, que es lo que la [HU-007 de EP-007](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/HU-007-revisar-que-falta.md) ya comprueba con `validar.py checklist` |
| **`M1` · marca de capa 3** | ¿Se exige que el proyecto marque su ajuste? | **No se agrega la exigencia.** Obligaría a todos los proyectos instalados a escribir algo que hoy no escriben, a cambio de comprobar algo que ya se ve: un ajuste de capa 3 vive en el catálogo del proyecto y [`20·M16`](../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) ya obliga a que nombre la regla de base que concreta. La marca sería una segunda forma de decir lo mismo |

## Las cuatro que piden trabajo, con su decisión

| # | Qué falta | Decisión | Dónde se construye |
|---|---|---|---|
| **2** | El barrido de candidatas a regla no tiene ni molde ni disparador | **Se construye, y el disparador es el cierre de versión**, que es donde el barrido tiene sentido: lo que el usuario pidió dos veces en el tramo se mira antes de publicar. Nace el molde y la meta-regla que lo exige | Fase `C` de [EP-001 · HU-007](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) |
| **8a** | El instalador no agrega al `README` heredado las secciones nuevas, como sí hace con el `CLAUDE.md` | **Se construye igual que el del `CLAUDE.md`**: aditivo, preserva lo propio y reporta qué agregó. Es el mismo mecanismo, aplicado al otro archivo | Fase de [EP-007 · HU-005](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |
| **8b** | El mapa del sitio de [`anatomia/`](../anatomia/mapa-del-sitio.md) se actualiza a mano | **Se comprueba con un validador**, no se actualiza a mano: un mapa que envejece en silencio es peor que no tenerlo, y el precedente está construido (`test_el_mapa_del_amarre_no_envejece.py` hace exactamente eso con el otro mapa) | Fase de [EP-005 · HU-011](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) |
| **8c** | Si la dependencia CA→CA entra a la plantilla de la historia | **Entra, como columna opcional de la tabla de fases**, no como sección nueva: una historia con criterios independientes deja la columna vacía y no paga nada | Fase de [EP-003 · HU-002](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) |
| **8d** | Qué manda entre el brief y el histórico cuando se contradicen | **Manda el brief**, y el histórico dice de dónde salió: el brief es lo acordado hoy y el histórico es lo que se dijo alguna vez. Cuando chocan, lo que hay es un brief desactualizado o una decisión sin registrar, y las dos se arreglan escribiendo el brief. No necesita regla nueva: es el mismo orden que [`20·M6`](../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) fija, con lo específico ganándole a lo general | Se escribe al construir el 8a |
| **8e** | El índice por temáticas del histórico | **Se construye**, generado, no a mano: el índice por título ya existe y el temático se saca leyendo los resúmenes, que es donde están los temas | Fase de [EP-005 · HU-001](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) |

**Ninguna de estas seis se anota y se deja:** se bajan a fase y se construyen, que es lo que [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) pide. Lo que quede sin construir al cerrar la sesión queda dicho acá, con su nombre.
"""
L.escribir(p, s)
print("ok")
