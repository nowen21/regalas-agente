# -*- coding: utf-8 -*-
import sys, os, glob, io
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

def poner_exigencia(archivo, rid, nuevo, nota):
    s = L.leer(archivo)
    ini, fin, _ = L.bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    tras = b.find("\n", 0)
    cortes = [i for i in (b.find("\n**Excepción", 0, cl), b.find("\n```", 0, cl)) if i > 0]
    corte = min(cortes)
    b = b[:tras] + "\n\n" + nuevo.strip() + "\n" + b[corte:]
    s = s[:ini] + L.resellar(b, archivo, nota) + s[fin:]
    L.escribir(archivo, s)

R = "base/02-flujo-de-trabajo/reglas/"
NOTA = "**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md)."
B = "../base.md"
C = {
 "F0": "Todo desarrollo —funcionalidad nueva o cambio de comportamiento— recorre `planteamiento → épica → HU → especificación → plan → código`, grande o chico: ningún eslabón se salta ni se fusiona. Si falta el anterior, se pausa y se crea primero (depende de [`02·F2`](F2-sin-especificacion-acordada-no-hay-codigo.md), [`13·DOC15`](../../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)).",
 "F8": "Se editan únicamente los archivos de la tabla del plan aprobado ([`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 9). Descubrir a mitad que hace falta otro **detiene la ejecución**: se pausa, se reporta, se propone ampliar el plan y se espera el OK. Que el cambio sea obvio no autoriza; la aprobación sí ([`base.md`](" + B + ")).",
 "F9": "Aprobado un plan, se entrega **completo**: no se parte en sub-fases nuevas, no se vuelve a preguntar por decisiones que ya cabían dentro ni se ofrecen opciones sobre detalles ya resueltos con criterio profesional. Si el volumen pide subdividir, se propone **antes** de aprobar (extiende [`02·F3`](F3-ejecuta-seguido-el-plan-aprobado.md)).",
 "F10": "Cuando el cambio toca algo que está o puede estar en producción, el plan asume **«probablemente sí lo está»** y declara la estrategia de migración incremental que corresponde; no se posterga la fase preguntando si está en producción. La casuística: [`base.md`](" + B + ") (extiende [`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 12).",
 "F11": "Todos los archivos que una fase modifica pertenecen al módulo que declaró al abrirse ([`13·DOC12`](../../13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)). Si el trabajo alcanza a otros módulos se descompone en **una fase por módulo** y el resto se difiere por escrito, nunca en una «fase transversal», que borra la trazabilidad.",
 "F14": "Un plan de trabajo responde las **trece preguntas** del capítulo antes de que se escriba una línea de código. La que no aplique al alcance se deja con su encabezado y un «No aplica porque …», no se omite; las trece están en [`base.md`](" + B + ") (extiende [`02·F4`](F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) · deroga [`02·F4.1`](F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)).",
 "F16": "Cada intervención del plan dice **qué** se hace, **cómo**, **dónde** exactamente, **por qué** —qué hueco cierra— y con qué **impacto** en el resto. Fuera los verbos vagos y los alcances abiertos; qué se espera de cada componente, en [`base.md`](" + B + ") (extiende [`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · deroga [`02·F4.3`](F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)).",
 "F17": "Cada ruta, firma y dependencia que el plan nombra se comprueba antes contra el proyecto. Quedan prohibidas las marcas de incertidumbre («o donde esté», «o similar», «por confirmar»): lo que no se pueda verificar se declara pregunta abierta y espera al usuario, no se escribe como suposición (depende de [`02·F1`](F1-carga-el-contexto-antes-de-actuar.md)).",
 "F20": "Lo que el agente descubra y «convendría» agregar —limpieza, validación extra, refactor colateral— **para** el trabajo, se **muestra** con su impacto y **espera** la decisión del usuario. Una pregunta pide explicación, no autoriza a editar. Las tres respuestas, en [`base.md`](" + B + ") (extiende [`02·F19`](F19-implementa-literal-el-criterio-de-aceptacion.md)).",
 "F22": "Ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ya cumplía. Lo único que se abre es la fase que la adopta, una por cada HU que la implementaba, y al cerrarla se sube la versión declarada. Fuera de ahí el desfase se reporta y no detiene (depende de [`20·M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).",
 "F23": "Un pendiente no se implementa desde su archivo: baja a historia de usuario de la épica que le corresponda y se construye como fase de esa historia. Que la mejora ya esté acordada y escrita no salta ningún eslabón: el pendiente dice **qué falta**, no cómo se construye ni cómo se comprueba (extiende [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).",
 "F26": "Ninguna épica se deriva sin el **inventario de funcionalidades** aprobado por el usuario, con estado por ítem y lo no decidido marcado «por confirmar» ([`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md)). La épica que no baje de ningún ítem no arranca (extiende [`02·F2`](F2-sin-especificacion-acordada-no-hay-codigo.md)).",
}
for rid, cuerpo in C.items():
    p = glob.glob(R + rid + "-*.md")[0]
    poner_exigencia(p, rid, cuerpo, NOTA)
print("aplicadas", len(C))
