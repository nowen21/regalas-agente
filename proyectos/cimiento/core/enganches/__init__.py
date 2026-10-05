"""La lógica de los enganches: lo que corre antes y después de cada acción del
agente y de cada mensaje (el freno, el histórico, el resumen, la memoria).

Python puro, sin Django: los enganches corren en cada mensaje y no pueden pagar
el arranque de Django. `adaptadores/<herramienta>/` solo habla con la
herramienta; la decisión vive acá.
"""
