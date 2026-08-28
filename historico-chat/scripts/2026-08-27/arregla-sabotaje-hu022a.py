# -*- coding: utf-8 -*-
"""Dos defectos del guion de sabotaje, encontrados corriendolo.

1. **Se cayo con el archivo saboteado puesto.** `print` de una linea de FAIL con
   caracteres que la consola de Windows no sabe escribir reventó entre el
   sabotaje y la restauracion, y `fases.py` quedo roto en el repositorio. Un
   guion que rompe a proposito **tiene que restaurar pase lo que pase**:
   `try/finally`.

2. **El fallo no se noto.** El guion se corrio con `| tail -45`, asi que el
   codigo de salida que se vio fue el de `tail`, no el de Python: `0`. Un guion
   de sabotaje no se canaliza; se redirige a un archivo y se lee.

El primero es el peligroso: dejar el repositorio saboteado sin decirlo.
"""
import io

F = r"c:\Ing. Jose\ia\agente\historico-chat\scripts\2026-08-27\sabotaje_hu022a.py"
t = io.open(F, encoding="utf-8").read()

# 1. lo que se imprime se limpia de lo que la consola no sabe escribir
viejo_correr = '''    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    return "\\n".join("    " + l for l in lineas)'''
nuevo_correr = '''    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    salida_limpia = "\\n".join("    " + l for l in lineas)
    # La consola de Windows no sabe escribir todo lo que unittest devuelve, y
    # un `print` que revienta entre el sabotaje y la restauracion deja el
    # repositorio roto. Se limpia antes de imprimir.
    return salida_limpia.encode("ascii", "replace").decode("ascii")'''
assert viejo_correr in t
t = t.replace(viejo_correr, nuevo_correr, 1)

# 2. restaurar pase lo que pase
viejo_bucle = '''    io.open(completa, "w", encoding="utf-8", newline="\\n").write(
        t.replace(viejo, nuevo, 1))
    print(correr())
    restaurar()
    print()'''
nuevo_bucle = '''    io.open(completa, "w", encoding="utf-8", newline="\\n").write(
        t.replace(viejo, nuevo, 1))
    try:
        print(correr())
    finally:
        # Pase lo que pase. Sin esto, un `print` que revienta deja el
        # repositorio con el sabotaje puesto — y ya paso una vez.
        restaurar()
    print()'''
assert viejo_bucle in t
t = t.replace(viejo_bucle, nuevo_bucle, 1)

io.open(F, "w", encoding="utf-8", newline="\n").write(t)
print("guion de sabotaje arreglado: try/finally y salida limpia")
