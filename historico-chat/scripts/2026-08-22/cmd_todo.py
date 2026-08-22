# -*- coding: utf-8 -*-
"""Agrega el subcomando `todo` a validar.py: la corrida completa en una línea."""
import io, os
os.chdir(r"c:\Ing. Jose\ia\agente")
p = "validadores/validar.py"
s = io.open(p, encoding="utf-8").read()

CMD = '''
# `EP-004·HU-008` · Las comprobaciones que **no** entran en la corrida completa,
# cada una con su motivo. Se nombran una por una, no por patrón: una lista ancha
# dejaría fuera, sin que nadie lo note, el subcomando que se registre mañana.
FUERA_DE_LA_CORRIDA = {
    "todo": "es esta misma",
    "linter": "corre la herramienta del proyecto y tarda; va aparte",
    "suite": "corre la suite del proyecto y tarda; va aparte",
    "audit": "sale a la red a preguntar por vulnerabilidades; va aparte",
    "plantilla": "necesita que le digan qué documento revisar",
    "commit": "necesita el mensaje del commit",
    "traza": "necesita la transcripción de una sesión",
    "temas": "escribe un archivo cuando se le pide `--aplicar`",
}


def cmd_todo(a, parser=None, nombres=()):
    """`EP-004·HU-008` · Una línea dice cómo está el proyecto.

    **Por qué no llama a los validadores uno por uno**: cada subcomando sabe
    cosas que su módulo no —qué raíz usar, qué imprimir, qué recorrer—, y
    copiarlas acá sería tener dos versiones de lo mismo. Se corre **el mismo
    subcomando** que correría una persona, con sus valores por defecto.

    **Lo lento y lo que pide argumentos quedan fuera, con su motivo escrito.**
    Es la decisión 23 del pendiente 59: `linter`, `suite` y `audit` van aparte
    porque tardan, y una corrida que tarda no se corre.
    """
    resumen = []
    peor = 0
    for nombre in nombres:
        if nombre in FUERA_DE_LA_CORRIDA:
            continue
        try:
            sub_args = parser.parse_args([nombre])
        except SystemExit:
            resumen.append((nombre, None, "pide argumentos: se corre aparte"))
            continue
        if getattr(sub_args, "raiz", "") is None:
            sub_args.raiz = a.raiz
        elif getattr(a, "raiz", None):
            sub_args.raiz = a.raiz
        try:
            codigo = sub_args.func(sub_args)
        except SystemExit as e:
            codigo = int(getattr(e, "code", 1) or 0)
        except Exception as e:              # noqa: BLE001
            # `EP-004·HU-003` · Que una comprobación reviente no puede llevarse
            # a las otras cuarenta: se anota y la corrida sigue.
            resumen.append((nombre, 1, "reventó: %s" % e))
            peor = 1
            continue
        resumen.append((nombre, codigo, ""))
        peor = max(peor, codigo or 0)
        print()

    print("== Corrida completa · %s ==" % relativo(os.path.abspath(a.raiz)))
    con_falla = [n for n, c, _ in resumen if c == 1]
    rotos = [(n, m) for n, c, m in resumen if m and "reventó" in m]
    for nombre, motivo in FUERA_DE_LA_CORRIDA.items():
        if nombre in nombres and nombre != "todo":
            print("  (fuera: %s — %s)" % (nombre, motivo))
    print("%d comprobación(es) corridas · %d con fallas%s"
          % (len(resumen), len(con_falla),
             (": " + ", ".join(con_falla)) if con_falla else ""))
    for nombre, motivo in rotos:
        print("  %s %s" % (nombre, motivo))
    if not con_falla:
        print("Sin fallas. Los avisos de cada comprobación salen arriba.")
    return 1 if peor else 0

'''

ancla = "def cmd_estandar(a):"
assert ancla in s
s = s.replace(ancla, CMD.lstrip("\n") + "\n" + ancla, 1)

reg = '''    td = sub.add_parser("todo",
                        help="la corrida completa en una línea · todo lo que aplica, menos lo lento")
    td.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    td.set_defaults(func=cmd_todo)

    e = sub.add_parser("estandar", help="enlaces rotos e índices desactualizados")'''
a2 = '''    e = sub.add_parser("estandar", help="enlaces rotos e índices desactualizados")'''
assert a2 in s
s = s.replace(a2, reg, 1)

a3 = """    a = p.parse_args()"""
nuevo3 = """    a = p.parse_args()
    # La corrida completa necesita el analizador entero para poder correr a los
    # demás: se lo pasa acá, que es donde existe.
    if getattr(a, "func", None) is cmd_todo:
        a.func = lambda args: cmd_todo(args, parser=p,
                                       nombres=tuple(sub.choices))"""
assert a3 in s
s = s.replace(a3, nuevo3, 1)
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
