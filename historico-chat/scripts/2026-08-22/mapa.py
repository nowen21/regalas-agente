# -*- coding: utf-8 -*-
import io, os
os.chdir(r"c:\Ing. Jose\ia\agente")
p = "anatomia/mapa-del-sitio.md"
s = io.open(p, encoding="utf-8").read()

s = s.replace("> Estándar **v1.4.0** · actualizado el **2026-08-07**.",
              "> Estándar **v31.2.0** · actualizado el **2026-08-22**.\n> **No envejece en silencio:** `python validadores/validar.py sitio` reporta la carpeta que existe y no está acá, y la que está acá y ya no existe.")

s = s.replace("| 🟩 **Herramientas** | Programas que comprueban, recuerdan, miden y muestran. Corren sin IA. | `validadores/` · `memoria/` · `metricas/` · `interfaz/` |",
              "| 🟩 **Herramientas** | Programas que comprueban, recuerdan, miden y muestran. Corren sin IA. | `validadores/` · `adaptadores/` · `memoria/` · `metricas/` · `interfaz/` · `evals/` |")
s = s.replace("| 🟨 **Bitácora** | Qué pasó y por qué. No es norma: es memoria escrita. | `historico-chat/` · `notas/` · `pendientes/` · `prompts/` · `anatomia/` |",
              "| 🟨 **Bitácora** | Qué pasó y por qué. No es norma: es memoria escrita. | `historico-chat/` · `notas/` · `pendientes/` · `prompts/` · `anatomia/` · `documentacion/` · `analisis/` |")
s = s.replace("| ⬜ **Apoyo** | Configuración, empaquetado y material que no es del estándar. | `.claude/` · `.claude-plugin/` · `.githooks/` · `diplomado-ia/` |",
              "| ⬜ **Apoyo** | Configuración y empaquetado. | `.claude/` · `.claude-plugin/` · `.githooks/` |")

s = s.replace("├── VERSION ........................... versión del estándar (hoy 1.4.0)",
              "├── VERSION ........................... versión del estándar")

# la zona de herramientas gana adaptadores/ y evals/
a = "├── 🟩 memoria/ ....................... LO QUE NO SE DEBE VOLVER A OLVIDAR"
nuevo = """├── 🟩 adaptadores/ ................... LO QUE ATA EL ESTÁNDAR A UNA HERRAMIENTA
│   ├── contrato.md ................... qué le pide el estándar a cualquier herramienta
│   └── claude-code/ .................. los enganches de esta herramienta, y solo ellos
│
├── 🟩 evals/ ......................... CASOS CON RESPUESTA CONOCIDA PARA MEDIR AL AGENTE
│
""" + a
assert a in s
s = s.replace(a, nuevo, 1)

# la bitácora gana documentacion/ y analisis/
b = "├── 🟨 notas/ ......................... POR QUÉ se decidió algo así (12 notas)"
nuevo_b = """├── 🟨 documentacion/ ................. LA CADENA DEL TRABAJO: épicas, historias y fases
│   ├── epicas/ ....................... EP-001 a EP-007, cada una con sus HU y sus fases
│   ├── senales.md .................... lo aprendido que no se recupera leyendo el código
│   └── automatismos/ ................. qué corre solo y cuándo
│
├── 🟨 analisis/ ...................... MEDICIONES CON FECHA, QUE NO SE REESCRIBEN
│
""" + b
assert b in s
s = s.replace(b, nuevo_b, 1)

s = s.replace("""├── ⬜ prompts/ ....................... (vacía)
│
├── ⬜ diplomado-ia/ .................. apuntes de clase — NO es parte del estándar
│
""", "")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
