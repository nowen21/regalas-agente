# `hook_sesion.py`

Arranca solo cuando alguien empieza a trabajar: revisa cómo quedó puesto el estándar y le entrega al agente lo que, recién llegado, no puede saber.

## Qué hace

Dos cosas distintas:

**Avisa.** Corre la revisión de `sesion.py` y retorna una línea de resumen que Claude Code le muestra al usuario en pantalla.

**Carga.** Le entrega al agente tres cosas, en este orden:

| Qué le entrega | De dónde sale | Cuánto |
|---|---|---|
| Cómo le llegan las reglas, o la regla que manda detenerse | `cargador.py` | Unas cinco líneas; la regla que manda detenerse, entera |
| Los recuerdos del proyecto | `recuerdos.py` | El índice completo, o sus filas si no cabe |
| Las conversaciones anteriores | `historico.py` | Las últimas que quepan, con el tema de cada una |

**Todo cabe en 10.000 caracteres.** Es el tope de la herramienta por enganche: lo que pasa de ahí lo guarda en un archivo fuera del repositorio y le deja ver al agente solo los primeros 2.000 (documentación de Claude Code, `hooks.md`, sección «JSON output»). Lo que no cabe se recorta desde el final, por líneas enteras, y el texto dice en qué archivo está lo completo.

Las reglas no van acá: llegan con cada mensaje, por `hook_reglas.py`.

Los recuerdos y las conversaciones se cargan **también cuando se trabaja en el estándar mismo**: ahí no hay instalación que revisar, pero los recuerdos y las conversaciones son igual de necesarios.

Siempre termina bien, aunque encuentre problemas. Esto avisa, no traba: que no se pueda empezar a trabajar porque al `CLAUDE.md` le falta una sección sería peor que el problema que resuelve.

## De qué depende y quién lo usa

```
hook_sesion.py
   ├── cargador.py ···· contexto() con cómo llegan las reglas, o el gate
   ├── recuerdos.py ··· contexto() con el índice de la memoria
   ├── historico.py ··· contexto() con el índice de sesiones
   ├── sesion.py ······ revisar() y resumen()
   ├── instalar.py ···· cumple_f13()
   └── comun.py ······· RAIZ y preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code cuando se abre una sesión, con la orden que `instalar.py` dejó escrita en el archivo de ajustes.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `TOPE_DEL_CANAL` | 10.000: los caracteres que la herramienta acepta por enganche |
| `RESERVA_AVISOS` | 600: los caracteres que se apartan para decir qué no cupo |

### Funciones

**`raiz_pedida(argv)`**

- **Recibe:** lo que se escribió en la consola.
- **Hace:** busca `--raiz` y toma lo que viene después.
- **Retorna:** esa carpeta, o la carpeta donde se está parado si no se dijo ninguna.

**`_ruta(modulo)`**

- **Retorna:** dónde está el índice entero que ese módulo recorta.

**`_del_proyecto(proyecto, disponible)`**

- **Recibe:** la carpeta del proyecto y los caracteres que quedan.
- **Hace:** pone la memoria y después el histórico. Al que no cabe le pide la versión recortada y anota el aviso. Si alguno se rompe, deja escrito que no se pudo cargar.
- **Retorna:** los dos textos unidos y los avisos.

**`_reglas(gate_ok)`**

- **Retorna:** el texto de `cargador.contexto`, o el error escrito si se rompe.

**`armar(resumen, hallazgos, reglas, proyecto)`**

- **Hace:** junta la revisión, las reglas, la memoria y el histórico, en ese orden, dentro del tope. Si aun así se pasa, lo avisa.
- **Retorna:** el texto para el agente y los avisos.

**`main()`**

- **Hace:**
  1. Averigua sobre qué carpeta hay que trabajar.
  2. Si es la del estándar mismo, responde sin revisión y sin gate.
  3. Si no, corre la revisión. Si se rompe, responde con el error.
  4. Responde con el resumen, lo que encontró y lo que arma `armar`.
- **Retorna:** siempre `0`, o sea que terminó bien.

**`_responder(resumen, hallazgos, reglas, proyecto)`**

- **Hace:** escribe la respuesta con dos partes:
  - una que Claude Code le muestra al usuario en pantalla: el resumen, y lo que no cupo;
  - otra que le llega al agente: lo que arma `armar`, más lo que no cupo.

Se usan las dos porque la primera depende de que la pantalla la dibuje, y podría no verse.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, para que arranque al abrir una sesión:

```
python "<estandar>/adaptadores/claude-code/hook_sesion.py" --raiz "<proyecto>"
```

Por dentro:

```
Claude Code abre la sesión
        ↓
hook_sesion.py --raiz <proyecto>
        ↓
¿la carpeta es la del estándar mismo?
     sí → sin revisión y sin gate
     no → sesion.revisar(proyecto, estandar)
        ↓
cargador.contexto(estandar, cumple_f13)
     cómo llegan las reglas, o la regla que manda detenerse
        ↓
armar(...)
     revisión + reglas + memoria + histórico, hasta 10.000 caracteres
        ↓
_responder(...)
     una parte → la línea que ve el usuario en pantalla
     otra      → el texto que recibe el agente
        ↓
termina bien, siempre
```

## Ejemplos de lo que retorna

```python
raiz_pedida(['--raiz', 'C:/proyectos/pos'])
'C:\proyectos\pos'

main()
0                # siempre
```

Y esto es lo que imprime, que es lo que Claude Code lee:

```json
{
  "systemMessage": "Estándar cargado · pos · F13 ok · CLAUDE.md al día · enganches puestos",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "[Revisión de arranque del estándar]\nEstándar cargado · pos · …\n\n[LAS REGLAS DEL ESTÁNDAR: LLEGAN CON CADA MENSAJE]\n…\n\n[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]\n…\n\n[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]\n…"
  }
}
```

Cuando algo no cupo, va al final de los dos:

```
[LO QUE NO CUPO EN EL ARRANQUE]
  - el índice del histórico se recortó para caber; completa, en `historico-chat/README.md`
```
