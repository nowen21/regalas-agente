# `guardian_version.py` — un cambio de reglas no se guarda sin su versión

**Qué hace.** Mira los archivos que entran en el commit. Si alguno vive en `base/` o en `plantillas/` —lo que viaja a los proyectos que heredan—, exige que en el mismo commit vayan `VERSION` y `CHANGELOG.md`. Si falta alguno, **detiene**.

**Dónde corre.** Dentro de `validar.py versionado --preparados`, que es lo que el enganche de `pre-commit` ya ejecuta. No es un enganche nuevo: se suma al que existe, porque son la misma pregunta en el mismo momento.

## Qué exige, y cuándo se calla

| Qué entra en el commit | Qué pasa |
|---|---|
| Nada de `base/` ni de `plantillas/` | **Se calla.** Cambiar un validador o un documento no cambia lo que se le exige a un proyecto |
| Algo de la norma, con `VERSION` y `CHANGELOG.md` | **Se calla.** Está completo |
| Algo de la norma, sin uno de los dos | **Falla**, y el mensaje dice cuál de los dos falta |
| Algo de la norma mezclado con diez archivos que no lo son | **Falla igual.** Mezclar no esconde |

## Por qué detiene en vez de avisar

Es la decisión 9 del [pendiente 59](../../pendientes/59-las-42-dudas-que-detienen-26-fases.md), con la regla que salió de ahí: **detiene lo que se puede comprobar sin criterio, avisa lo que necesita juicio**. Que un archivo esté o no en el commit se comprueba mirando; no hay nada que interpretar.

Y la evidencia del propio repositorio: *«un aviso que nada respalda se ignora»*. Ya pasó con la brevedad, con las marcas de generación automática y con el desfase de versión.

## Qué no comprueba, y se declara

- **Si la entrada del registro dice la verdad.** Que exista no significa que describa el cambio.
- **Si el tipo de versión es el correcto.** Mayor, menor o parche se decide leyendo qué cambió, y eso lo hace una persona ([`20·M10`](../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) fija el criterio).
- **Los cambios ya guardados.** Mira lo que se va a guardar; sobre el repositorio entero la pregunta no tiene sentido, porque ahí ya está todo.

## Cómo se corre

```
python validadores/validar.py versionado --preparados
```

Sale por el mismo reporte que las demás comprobaciones de qué está versionado.

## Casos que lo protegen

[`validadores/tests/test_el_cambio_de_reglas_lleva_su_version.py`](../tests/test_el_cambio_de_reglas_lleva_su_version.py), siete. El que decide es `CP-003`: un commit que no toca la norma no nota nada. Sin él, la comprobación pediría versión en cada commit de documentación, y a la semana alguien la apaga.
