import json, os, subprocess, sys, tempfile, time

RAIZ = r"C:\Ing. Jose\ia\agente"
HOOK = os.path.join(RAIZ, "adaptadores", "claude-code", "hook_sesion.py")
tmp = tempfile.mkdtemp()
p1 = os.path.join(tmp, "p1"); os.makedirs(os.path.join(p1, "proyectos"))
p2 = os.path.join(tmp, "p2"); os.makedirs(p2)
for nombre, raiz in (("estandar", RAIZ), ("proyecto", p1), ("sin-estructura", p2)):
    t = time.perf_counter()
    r = subprocess.run([sys.executable, HOOK, "--raiz", raiz], capture_output=True,
                       input="", text=True, encoding="utf-8")
    s = time.perf_counter() - t
    c = json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]
    marcas = [m for m, t_ in (("mapa", "mapa-de-tareas"), ("gate", "ARRANQUE DETENIDO"),
                              ("N1", "## N1 ·"), ("no-cupo", "NO CUPO"),
                              ("memoria", "MEMORIA DEL AGENTE"), ("historico", "HISTÓRICO DE"))
              if t_ in c]
    print(nombre, r.returncode, len(c), f"{s:.2f}s", marcas)
