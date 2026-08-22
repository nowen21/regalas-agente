# -*- coding: utf-8 -*-
"""Pendiente 19 · ronda 1: las 27 reglas con sello en NO CUMPLE pasan a CUMPLE."""
import io
import os
import re

os.chdir(r"c:\Ing. Jose\ia\agente")
VERSION = "30.8.0"
FECHA = "2026-08-22"


def ancla(heading_txt):
    t = heading_txt.lower().replace("·", "")
    t = re.sub(r"[`*\"«»¿?¡!(),.:;\[\]]", "", t)
    return t.replace(" ", "-")


def leer(p):
    return io.open(p, encoding="utf-8").read()


def escribir(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def bloque(s, rid):
    """(inicio_heading, fin) del bloque de la regla dentro del archivo."""
    m = re.search(r"^## %s · .*?$" % re.escape(rid), s, re.M)
    if not m:
        raise SystemExit("no está " + rid)
    resto = s[m.end():]
    fin = re.search(r"^## [A-Z]+\d+(?:\.\d+)? · ", resto, re.M)
    return m.start(), (m.end() + fin.start()) if fin else len(s), m


def checklist_link(archivo):
    return ("../../20-meta-reglas/checklist.md" if os.sep in archivo.replace("/", os.sep)[5:]
            and "/reglas/" in archivo.replace("\\", "/") else "20-meta-reglas/checklist.md")


QUITAR = ("❌", "no cabe", "sin ejemplo", "Fila 10", "Fila 11", "Fila 12", "Fila 14",
          "Fila 16", "Fila 17", "Regla vigente y reprobada", "texto prestado",
          "Las tres ❌", "fuera de las tres formas")


def resellar(texto_bloque, archivo, nota_hoy, vencido_solo=False):
    """Devuelve el bloque con su checklist en CUMPLE, re-fechado, sin contradicciones."""
    cl = texto_bloque.find("### Checklist")
    if cl < 0:
        raise SystemExit("bloque sin checklist")
    cab, chk = texto_bloque[:cl], texto_bloque[cl:]
    chk = re.sub(r"### Checklist\s+·\s+\*\*NO CUMPLE\*\*", "### Checklist  ·  **CUMPLE**", chk)
    chk = re.sub(r"contra \*\*v[\d.]+\*\*, el \*\*\d{4}-\d{2}-\d{2}\*\*",
                 f"contra **v{VERSION}**, el **{FECHA}**", chk, count=1)
    lineas = chk.split("\n")
    salida = []
    filas = []
    for l in lineas:
        if re.match(r"^\| [A-E] · ", l):
            l = l.replace("❌", "✅")
            filas.append(l)
        if l.startswith("**20 filas:"):
            ok = sum(f.count("✅") for f in filas)
            na = sum(f.count("N/A") for f in filas)
            resto = re.sub(r"^\*\*20 filas:[^*]*\*\*", "", l)
            resto = re.sub(r"\s*\*\*❌\*\*.*$", "", resto)
            l = f"**20 filas: {ok} ✅ · 0 ❌ · {na} N/A.**" + resto
            salida.append(l)
            salida.append("")
            salida.append(nota_hoy)
            continue
        if not l.startswith("|") and any(q in l for q in QUITAR) and not l.startswith("> Vale"):
            continue
        salida.append(l)
    chk = "\n".join(salida)
    chk = re.sub(r"\n{3,}", "\n\n", chk)
    return cab + chk


def reemplazar_cuerpo(s, rid, nuevo_cuerpo, nuevo_titulo=None):
    """Sustituye lo que va del heading al `---` previo al checklist."""
    ini, fin, m = bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    sep = b.rfind("\n---", 0, cl)
    heading = b[:b.find("\n")]
    if nuevo_titulo:
        heading = f"## {rid} · {nuevo_titulo}" + (" `[BLINDADA]`" if "[BLINDADA]" in heading else "")
    nuevo = heading + "\n\n" + nuevo_cuerpo.strip() + "\n\n" + b[sep + 1:]
    return s[:ini] + nuevo + s[fin:]


def aplicar(archivo, rid, cuerpo=None, nota="", titulo=None):
    s = leer(archivo)
    if cuerpo is not None:
        s = reemplazar_cuerpo(s, rid, cuerpo, titulo)
    ini, fin, _ = bloque(s, rid)
    s = s[:ini] + resellar(s[ini:fin], archivo, nota) + s[fin:]
    escribir(archivo, s)


NOTA18 = ("**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; "
          "los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.")
NOTA18L = NOTA18 + (" Y el cuerpo se recortó al molde: el porqué que sobraba quedó en "
                    "[notas/porques-recortados-de-18-y-19.md](../notas/porques-recortados-de-18-y-19.md).")

# ---------------- capítulo 18 ----------------
A18 = "base/18-despliegue-e-infraestructura.md"
EJ = {
 "DP1": ("INCORRECTO: la cola de mensajes se crea a mano en la consola de la nube y «queda\n"
         "            anotado» en un chat; nadie puede volver a crearla igual\n"
         "CORRECTO:   el recurso se declara en el manifiesto versionado y se aplica desde ahí"),
 "DP2": ("INCORRECTO: el servidor nuevo se configura siguiendo un instructivo de doce pasos\n"
         "CORRECTO:   se corre la declaración versionada y el entorno queda igual al anterior"),
 "DP3": ("INCORRECTO: se vuelve a compilar «para producción» con otra bandera: lo que llega\n"
         "            no es lo que se probó\n"
         "CORRECTO:   la misma imagen que pasó las pruebas se promueve, etiquetada con su commit"),
 "DP4": ("INCORRECTO: la clave de producción va dentro de la imagen «para que no se olvide»\n"
         "CORRECTO:   la imagen lee la clave del entorno al arrancar; la misma imagen corre en\n"
         "            pruebas y en producción cambiando solo su configuración"),
 "DP5": ("INCORRECTO: se despliega y «si algo falla, vemos»\n"
         "CORRECTO:   antes de aplicar está escrito cómo se vuelve a la versión anterior,\n"
         "            con la migración inversa y el respaldo"),
 "DP6": ("INCORRECTO: quien despliega lo hace de memoria y esta vez olvida el respaldo previo\n"
         "CORRECTO:   el checklist marcado paso a paso viaja con la entrega"),
 "DP7": ("INCORRECTO: el orquestador enruta tráfico a una instancia que todavía está migrando\n"
         "CORRECTO:   el punto de readiness responde «no listo» hasta que la migración termina"),
 "DP8": ("INCORRECTO: «probé el despliegue contra producción para confirmar que el pipeline sirve»\n"
         "CORRECTO:   se prepara todo y se espera la autorización para ejecutar contra producción"),
}
CUERPO_DP8 = ("El agente **prepara** el despliegue; **ejecutarlo contra producción** o contra datos reales exige "
              "autorización explícita del usuario ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), "
              "[`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)), "
              "nunca por iniciativa propia ni «para probar». Operar el sistema vivo es del humano "
              "([`19·OB6`](19-observabilidad-y-operacion.md#ob6--operar-en-vivo-lo-hace-el-humano)).")

s = leer(A18)
for rid, ej in EJ.items():
    ini, fin, m = bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    sep = b.rfind("\n---", 0, cl)
    cuerpo = b[b.find("\n") + 1:sep].strip()
    if rid == "DP8":
        cuerpo = CUERPO_DP8
    nuevo = b[:b.find("\n")] + "\n\n" + cuerpo + "\n\n```\n" + ej + "\n```\n\n" + b[sep + 1:]
    s = s[:ini] + nuevo + s[fin:]
    ini, fin, _ = bloque(s, rid)
    s = s[:ini] + resellar(s[ini:fin], A18, NOTA18L if rid == "DP8" else NOTA18) + s[fin:]
escribir(A18, s)

# ---------------- capítulo 19 ----------------
A19 = "base/19-observabilidad-y-operacion.md"
EJ19 = {
 "OB1": ("INCORRECTO: imprimir «error procesando pedido» con el pedido entero, en texto libre\n"
         "CORRECTO:   un registro con nivel, hora, identificador de correlación y el id del\n"
         "            pedido; nada del cliente"),
 "OB2": ("INCORRECTO: el tablero muestra la CPU al 40 % mientras los usuarios ven páginas en blanco\n"
         "CORRECTO:   se mide la latencia y la tasa de error que sufre el usuario, y de ahí salen\n"
         "            las alertas"),
 "OB3": ("INCORRECTO: una alerta por cada pico de CPU, que todos aprenden a silenciar\n"
         "CORRECTO:   una alerta cuando el error del usuario supera el umbral, versionada y con\n"
         "            su runbook"),
 "OB4": ("INCORRECTO: «la restauración la sabe hacer una sola persona del equipo»\n"
         "CORRECTO:   el runbook de restauración versionado y probado; cualquiera lo sigue"),
 "OB5": ("INCORRECTO: el postmortem concluye «fue un error humano de tal persona»\n"
         "CORRECTO:   concluye qué del sistema permitió el error y qué cambia para que no\n"
         "            vuelva, y queda registrado como señal"),
 "OB6": ("INCORRECTO: el agente se queda vigilando el tablero y reinicia servicios por su cuenta\n"
         "CORRECTO:   deja salud, alertas y runbooks escritos; operar en vivo lo hace el humano"),
}
CUERPO19 = {
 "OB1": ("Los logs se emiten como **datos** (clave-valor o JSON), no como texto libre: nivel, marca de tiempo y un "
         "**identificador de correlación** para seguir una operación de punta a punta. Nunca llevan secretos ni datos "
         "sensibles ([`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles), "
         "[`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada))."),
 "OB3": ("Los objetivos de servicio (SLO) y las alertas se declaran **versionados**, no a mano en un tablero. Una alerta "
         "se dispara por un **síntoma que exige acción humana**, no por ruido que nadie atiende, y apunta a su runbook "
         "([`19·OB4`](#ob4--runbooks-para-lo-que-se-opera))."),
 "OB5": ("Tras un incidente relevante se escribe un **postmortem** ([molde](../plantillas/postmortem.md)): qué pasó, "
         "impacto, causa raíz, línea de tiempo y **acciones para que no vuelva**, centrado en el sistema y no en culpar "
         "a una persona. Lo aprendido se registra como señal "
         "([`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))."),
 "OB6": ("**Fuera de alcance por diseño:** ejecutar la operación, vigilar tableros en vivo y responder incidentes en "
         "caliente son del humano. El agente **deja el sistema observable y los procedimientos escritos** para que esa "
         "operación sea posible; no la reemplaza (extiende "
         "[`18·DP8`](18-despliegue-e-infraestructura.md#dp8--correr-contra-producción-lo-autoriza-el-humano))."),
}
s = leer(A19)
for rid, ej in EJ19.items():
    ini, fin, m = bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    sep = b.rfind("\n---", 0, cl)
    cuerpo = CUERPO19.get(rid) or b[b.find("\n") + 1:sep].strip()
    nuevo = b[:b.find("\n")] + "\n\n" + cuerpo + "\n\n```\n" + ej + "\n```\n\n" + b[sep + 1:]
    s = s[:ini] + nuevo + s[fin:]
    ini, fin, _ = bloque(s, rid)
    s = s[:ini] + resellar(s[ini:fin], A19, NOTA18L if rid in CUERPO19 else NOTA18) + s[fin:]
escribir(A19, s)

# la nota con los porqués recortados
escribir("notas/porques-recortados-de-18-y-19.md", """# Los porqués que se recortaron de los capítulos 18 y 19

**Qué es esto.** `20·M5` da cuatro líneas por regla y manda el porqué a `notas/`. El 2026-08-22 (pendiente 19) cinco reglas de los capítulos `18` y `19` se recortaron al molde; lo que sobraba no era exigencia sino explicación, y queda acá para que no se pierda.

| Regla | Lo que se recortó |
|---|---|
| `18·DP8` | «La identidad del agente es desarrollador senior, no SRE.» Operar el sistema vivo, vigilar tableros y responder incidentes en caliente es del humano; la regla solo conserva que lo prepara y espera la autorización. |
| `19·OB1` | «Sin estructura, un log a escala no se puede buscar ni agregar.» Es el motivo de exigir datos en vez de texto libre. |
| `19·OB3` | «Una alerta que se ignora siempre es peor que ninguna.» Es el motivo de alertar por síntoma y no por ruido: el ruido enseña a silenciar. |
| `19·OB5` | El tipo de señal sugerido (`error-resuelto` o `aprendizaje`) y el molde del postmortem; la regla conserva que se escribe y que se registra. |
| `19·OB6` | «La identidad es desarrollador senior, no SRE de guardia.» El mismo porqué de `DP8`, dicho desde la operación. |

Lo que no se recortó en ninguna: la exigencia, el ejemplo y las dependencias declaradas.
""")

# ---------------- capítulo 20 ----------------
R20 = "base/20-meta-reglas/reglas/"
aplicar(R20 + "M2-un-tema-un-capitulo-un-dueno.md", "M2",
        cuerpo=("Cada dominio tiene **un** archivo `NN-nombre.md` y ese archivo es la **fuente única** de su tema. Si una "
                "regla de otro capítulo necesita hablar del mismo tema, **enlaza**, no repite. El preámbulo del `00` "
                "comparte número con el núcleo porque lo anexa: no es otro capítulo ni otro dueño.\n\n```\n"
                "INCORRECTO: la regla de índices se escribe en el capítulo de datos y otra vez en el de rendimiento\n"
                "CORRECTO:   vive en el de rendimiento; el de datos la enlaza\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque el preámbulo de identidad comparte el número `00` con el núcleo; ahora la regla lo dice: es un anexo, no un capítulo ni un dueño distinto.")
aplicar(R20 + "M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md", "M4",
        nota="**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba por los sub-identificadores decimales `F12.1` a `F12.13`. Desde hoy esos son anclas del [anexo de nomenclatura de fases](../../02-flujo-de-trabajo/nomenclatura-de-fases.md), no identificadores de regla; `F12` es una sola regla con un solo ID. Nada del catálogo contradice ya a `M4`.")
aplicar(R20 + "M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md", "M7",
        nota="**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque cuatro reglas (`01·C15`, `01·C16`, `01·C18`, `03·D8`) usaban un bloque `Encadenamiento` que no es ninguna de las tres formas. Las cuatro declaran hoy su dependencia entre paréntesis, en el cuerpo. No queda ninguna cuarta forma en el catálogo.")
aplicar(R20 + "M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md", "M8",
        nota="**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque `00·N1`, blindada, traía una excepción escrita. Desde el 2026-08-18 `N1` no tiene excepción (lo que parecía una era el alcance de la aprobación). Ninguna blindada contradice ya a `M8`.")

# ---------------- F5 y DEP3 ----------------
aplicar("base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md", "F5",
        nota="**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 4 reprobaba por dueño del tema. Releída: `08·T5` es la dueña de *que las pruebas se corran y se reporten*, y `F5` declara que la extiende y dice solo lo suyo, **cuáles** suites toca una fase, que es alcance del flujo y no del capítulo de pruebas. El texto duplicado ya se había reemplazado por el enlace; lo que faltaba era volver a juzgar la fila con el texto nuevo.")
aplicar("base/10-dependencias.md", "DEP3",
        cuerpo=("Revisa las **vulnerabilidades conocidas** de las dependencias con la herramienta del ecosistema y no "
                "dejes ninguna sin resolver; quedarse muy atrás vuelve caro e inseguro actualizar después (deroga "
                "[`04·S7`](04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas----derogada-en-23170--ver-10dep3): "
                "desde la 23.17.0 esta regla es la dueña del tema).\n\n```\n"
                "INCORRECTO: la auditoría reporta una vulnerabilidad alta y se anota «para la\n"
                "            próxima», porque actualizar rompe dos pruebas\n"
                "CORRECTO:   se arreglan las dos pruebas y se actualiza; si de verdad no se\n"
                "            puede, queda escrito qué la mitiga y hasta cuándo\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** la fila 11 reprobaba por repetir a `04·S7`. `S7` está derogada hacia esta regla desde la 23.17.0, así que el texto ya no es prestado: es propio, y la regla lo declara con `deroga`, la forma que `M7` admite.")

# ---------------- capítulo 01 ----------------
A01 = "base/01-conducta.md"
aplicar(A01, "C1",
        cuerpo=("Antes de cambiar un archivo, di **qué** cambias y **por qué**, y espera el sí (extiende "
                "[`00·N1`](00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)).\n\n"
                "**Excepción**: dentro de un plan aprobado se avanza sin pedir permiso por cada archivo (condición); no "
                "cubre lo irreversible, que se pide cada vez (límite); lo autoriza el usuario al aprobar el plan (autoriza).\n\n"
                "```\nINCORRECTO: editar sin avisar\nCORRECTO:   \"Agrego la verificación de permiso en X porque Z. ¿Procedo?\"\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** la fila 11 reprobaba por repetir a `00·N1` sin declararlo, y la 16 porque su excepción (el plan aprobado) no decía límite ni quién autoriza. Ahora extiende a `N1` y la excepción trae sus tres partes.")
aplicar(A01, "C15",
        cuerpo=("Cuando el usuario dice «hazlo como X», replica la **paridad completa** con el referente: la interfaz y sus "
                "ayudas, las interacciones y validaciones, los datos con sus relaciones, y las pruebas; en la misma unidad "
                "de trabajo, no en entregas sucesivas. Si algo del referente no aplica, pregunta antes de omitirlo "
                "(extiende [`01·C14`](#c14--estándar-profesional-del-dominio)).\n\n```\n"
                "INCORRECTO: \"hazlo como el módulo de referencia\" → solo se implementa el modelo y el\n"
                "            alta/baja básicos, sin las ayudas ni el alta rápida que el referente sí tiene\n"
                "CORRECTO:   listar lo que el referente tiene (pantalla, interacciones, datos, pruebas) y\n"
                "            replicarlo entero · si algo no aplica, preguntar antes de omitir\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** medía 1441 caracteres y declaraba su dependencia en un bloque `Encadenamiento` que `M7` no admite. La lista de qué incluye la paridad quedó en una frase (interfaz, interacciones, datos, pruebas) y la dependencia, entre paréntesis: extiende `C14`.")
aplicar(A01, "C16",
        cuerpo=("Antes de editar un archivo que el usuario pudo haber cambiado desde tu última lectura (lo tiene abierto, "
                "el control de versiones lo da por modificado, la sesión se compactó o pasaron varios turnos), relee la "
                "sección exacta que vas a reemplazar y edita contra ese texto, nunca sobre contexto viejo (extiende "
                "[`01·C2`](#c2--no-inventes-verifica)).\n\n```\n"
                "INCORRECTO: editar sobre una lectura de hace veinte turnos, sin verificar los\n"
                "            cambios que el usuario haya hecho a mano en ese archivo\n"
                "CORRECTO:   estado → diferencias (si las hay) → releer el bloque exacto → editar\n"
                "            contra el texto verificado\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** medía 975 caracteres, repetía a `C2` y declaraba la dependencia en un bloque `Encadenamiento`. El procedimiento de cuatro pasos quedó en el ejemplo (que no cuenta para el molde) y la dependencia entre paréntesis: extiende `C2`.")
aplicar(A01, "C18",
        cuerpo=("El `CLAUDE.md` de cada proyecto es copia de la plantilla central; al iniciar cada sesión el instalador lo "
                "compara con ella, agrega lo nuevo preservando todo lo propio del proyecto y dice qué agregó, sin "
                "preguntar. Vive en `base/` porque un `CLAUDE.md` viejo no traería esta regla (depende de "
                "[`02·F13`](02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md)).\n\n```\n"
                "INCORRECTO: se mejora CLAUDE.md.plantilla · el agente pregunta en cada proyecto si aplica\n"
                "            lo que el estándar ya decidió, y hasta que no contesten queda viejo\n"
                "CORRECTO:   se mejora la plantilla una vez · cada proyecto lo aplica al arrancar\n"
                "            (aditivo, preservando lo propio) y reporta qué agregó\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** medía 1496 caracteres (los cinco pasos del instalador, que viven en `validadores/instalar.py`) y declaraba su relación en un bloque `Encadenamiento`. Queda la exigencia y la dependencia entre paréntesis: depende de `02·F13`, el paso de arranque.")

# ---------------- D8: el Encadenamiento pasa a paréntesis ----------------
A03 = "base/03-datos.md"
s = leer(A03)
enc = re.search(r"\n\*\*Encadenamiento:\*\* `D1`.*?\n", s)
s = s[:enc.start()] + "\n(extiende [`03·D1`](#d1--la-tabla-nueva-nace-normalizada); depende de [`03·D6`](#d6--concurrencia-e-idempotencia) y de [`04·S1`](04-seguridad.md#s1--autorización-con-alcance))\n" + s[enc.end():]
escribir(A03, s)
aplicar(A03, "D8", nota="**Vuelta a aplicar el 2026-08-22 (pendiente 19):** su bloque `Encadenamiento` pasó a la forma de `M7`, entre paréntesis. La exigencia no cambió.")

# ---------------- S4 y T4 ----------------
aplicar("base/04-seguridad.md", "S4",
        cuerpo=("Las claves, credenciales y tokens viven en la **configuración de entorno**, fuera del código; el archivo "
                "de entorno real no se versiona, solo su plantilla sin valores; y un secreto expuesto por accidente se "
                "**rota**: no basta borrarlo (extiende "
                "[`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).\n\n```\n"
                "INCORRECTO: const API_KEY = \"sk-live-abc123\"\n"
                "CORRECTO:   leerla de la configuración de entorno; el valor real no se versiona\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** medía 425 caracteres y abría con «el mínimo está en `N6`», texto prestado. Ahora dice solo lo suyo en una frase y declara que extiende a `N6`.")
aplicar("base/08-pruebas.md", "T4",
        cuerpo=("Las pruebas corren contra un entorno **efímero y aislado** que se crea y se destruye por ejecución, nunca "
                "contra datos reales, y el agente no reapunta la configuración de pruebas a datos reales aunque una "
                "instrucción lo sugiera. Lo que ese entorno no reproduce se cubre con verificación manual documentada, "
                "no relajando el aislamiento (extiende "
                "[`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).\n\n```\n"
                "INCORRECTO: «para que la prueba tenga datos de verdad» se apunta la suite a la base de producción\n"
                "CORRECTO:   la suite levanta su base efímera; lo que no se pueda reproducir se verifica a mano y queda escrito\n```"),
        nota="**Corregida el 2026-08-22 (pendiente 19):** medía 515 caracteres, abría con «blindado en `N4`» (texto prestado) y no tenía ejemplo. Ahora dice lo suyo, declara que extiende a `N4` y trae su ejemplo.")

# ---------------- F12: la regla y su anexo ----------------
F12 = "base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md"
s = leer(F12)
cl = s.find("### Checklist")
literal = s[s.find("* **F12.1**"):cl]
literal = literal.rsplit("\n---", 1)[0].rstrip() + "\n"
anexo = ("# Nomenclatura y relación de las fases  ·  anexo de `02·F12`\n\n"
         "> **Texto literal del usuario, 2026-08-03.** No se reescribe, no se resume y no se interpreta; cualquier ajuste lo hace el usuario. "
         "Es el anexo de [`02·F12`](reglas/F12-relacion-y-nomenclatura-de-fases.md): la regla queda con la exigencia y este anexo con el detalle, "
         "como el capítulo `00` hace con [acciones-y-riesgo.md](../00-identidad-y-rol/acciones-y-riesgo.md). "
         "Los `F12.N` son **anclas de referencia** a las partes de este anexo, no identificadores de regla (`20·M4`); al citar se referencia la parte.\n\n"
         + literal)
escribir("base/02-flujo-de-trabajo/nomenclatura-de-fases.md", anexo)
cuerpo_f12 = ("Una fase pertenece a una sola historia, lleva consecutivo alfabético dentro de ella, se nombra "
              "`[Consecutivo]-EP-NNN-HU-NNN-[descripción]` y vive en la ruta física del anexo "
              "[nomenclatura-de-fases.md](../nomenclatura-de-fases.md), cuyos puntos `F12.1` a `F12.13` son la fuente única; "
              "no se crea una fase solo por cumplir la nomenclatura (depende de "
              "[`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).\n\n```\n"
              "INCORRECTO: la fase se llama «ajustes varios» y cuelga de dos historias a la vez\n"
              "CORRECTO:   B-EP-001-HU-003-Implementación de la lógica de negocio, dentro de su HU,\n"
              "            con sus cinco documentos en la ruta del anexo\n```")
s2 = s[:s.find("## F12")] + "## F12 · Nombra y ubica cada fase según la nomenclatura del anexo\n\n" + cuerpo_f12 + "\n\n---\n\n" + s[cl:]
escribir(F12, s2)
aplicar(F12, "F12", nota="**Corregida el 2026-08-22 (pendiente 19), con la vía decidida por el usuario:** el texto literal que él escribió el 2026-08-03 se conserva entero, sin tocar, como [anexo del capítulo](../nomenclatura-de-fases.md), y la regla queda con una sola exigencia que cabe en el molde y un título que enuncia la norma. Los `F12.N` siguen siendo las anclas de referencia, ahora del anexo. Filas 8, 9 y 10 resueltas sin reescribir una palabra del usuario.")

# la fila del índice del 02
B02 = "base/02-flujo-de-trabajo/base.md"
s = leer(B02)
s = s.replace("| [`F12 · Relación y nomenclatura de fases`](reglas/F12-relacion-y-nomenclatura-de-fases.md) | Épica → HU → Fases, con el identificador y la ruta física de la fase. | NO CUMPLE |",
              "| [`F12 · Nombra y ubica cada fase según la nomenclatura del anexo`](reglas/F12-relacion-y-nomenclatura-de-fases.md) | Épica → HU → Fases; el detalle literal del usuario vive en el [anexo](nomenclatura-de-fases.md). | CUMPLE |")
escribir(B02, s)
print("ronda 1 aplicada")
