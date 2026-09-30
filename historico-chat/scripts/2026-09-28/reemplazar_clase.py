import io, os

aqui = os.path.dirname(os.path.abspath(__file__))
p = r"C:\Ing. Jose\ia\agente\validadores\pruebas.py"
s = io.open(p, encoding="utf-8", newline="").read()
a = s.index("class RepartoDeLasReglas(unittest.TestCase):")
b = s.index("class LasReglasQuePideLaSolicitud(unittest.TestCase):")
nueva = io.open(os.path.join(aqui, "clase_cargador.py"), encoding="utf-8").read()
if "\r\n" in s[a:b]:
    nueva = nueva.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s[:a] + nueva + s[b:])
