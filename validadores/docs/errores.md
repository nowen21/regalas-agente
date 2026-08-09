# `errores.py`

Busca errores que se atrapan y se tiran a la basura, y contraseñas que quedan escritas en el diario del programa.

## Qué hace

Dos búsquedas sobre el código del proyecto:

1. **Error atrapado y tirado a la basura.** Un pedazo de código que atrapa un error y después no hace nada con él: ni lo arregla, ni lo anota, ni avisa. El problema pasa sin dejar rastro y después nadie entiende por qué algo no funcionó. Se reconocen dos formas de escribirlo: `catch (...) {}` con nada adentro, y `except ...: pass`.
2. **Contraseña en el diario.** Mientras corre, un programa va anotando lo que hace en un archivo que después alguien lee para entender qué pasó. Si en la misma línea en que anota algo aparece un campo que se llama como una contraseña, esa contraseña va a quedar escrita ahí, a la vista.

Todo lo que reporta es **aviso**: puede estar hecho a propósito y estar bien. Lo confirma una persona.

## De qué depende y quién lo usa

```
errores.py
   ├── codigo.py ··· archivos() y linea_de()
   └── comun.py ···· AVISO y Hallazgo
```

De Python usa `re`.

Lo usan:

```
errores.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "errores"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué reconoce |
|---|---|
| `_CATCH_LLAVES` | Un `catch` que no tiene nada adentro. Acepta que ese vacío esté repartido en varias líneas. |
| `_EXCEPT_PASS` | Un `except` cuyo único contenido es `pass`, que es la palabra que en Python significa «no hagas nada». |
| `_LOG` | Una línea que anota algo en el diario del programa: `console.log`, `console.error`, `console.warn`, `console.info`, `console.debug`, `Log::`, `logger.`, `logging.`, `log.`, `logger(` o `error_log(`. |
| `_SENSIBLE` | Un campo que se llama como algo que no debe salir a la luz: `password`, `passwd`, `pass`, `contraseña`, `secret`, `token`, `api_key`, `apikey`, `authorization`, `cvv`, `tarjeta`, `card_number` o `numero_tarjeta`. |

### Funciones

**`revisar_texto(texto, donde="", hallazgos=None)`**

- **Recibe:** el contenido de un archivo, cómo nombrarlo al reportar y, si se quiere, una lista donde ir juntando lo encontrado.
- **Hace:**
  1. Busca en el texto completo las dos formas de atrapar un error sin hacer nada, y anota un aviso por cada una, señalando su línea con `codigo.linea_de`.
  2. Recorre el texto línea por línea; si una línea a la vez anota en el diario y nombra un campo delicado, anota un aviso.
- **Retorna:** la lista de hallazgos.

Lo primero se busca en el texto completo porque el vacío puede quedar repartido en varias líneas. Lo segundo se busca línea por línea porque hacen falta las dos mitades juntas para que sea un problema.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** le pide a `codigo.archivos` los archivos de código que git guarda, y pasa cada uno por `revisar_texto`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py errores --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
codigo.archivos(carpeta)
   ↓
revisar_texto(texto, ruta)
   ↓
   en el texto completo:
       catch (Exception $e) { }        → AVISO
       except ValueError:              → AVISO
           pass
   ↓
   línea por línea:
       Log::info("clave: " . $password)  → AVISO
       console.log(token)                → AVISO
```

## Ejemplos de lo que retorna

```python
revisar_texto('try { pagar(); } catch (Exception $e) { }\n', 'app/Pago.php')
[Hallazgo(AVISO, 'app/Pago.php', 1,
          'captura de error vacía (`catch`) — E1 pide manejo visible y trazable')]

revisar_texto('try:\n    pagar()\nexcept ValueError:\n    pass\n', 'app/pago.py')
[Hallazgo(AVISO, 'app/pago.py', 3,
          'captura de error vacía (`except: pass`) — E1 pide manejo visible y trazable')]

revisar_texto('try { pagar(); } catch (Exception $e) { Log::error($e); }\n', 'app/Pago.php')
[]               # el error se maneja: así debe ser

revisar_texto('Log::info("clave: " . $password);\n', 'app/Auth.php')
[Hallazgo(AVISO, 'app/Auth.php', 1,
          'posible secreto en un log — E5: los logs no llevan contraseñas/tokens')]

revisar_texto('console.log("token recibido:", token);\n', 'src/api.js')
[Hallazgo(AVISO, 'src/api.js', 1,
          'posible secreto en un log — E5: los logs no llevan contraseñas/tokens')]

revisar_texto('Log::info("pago registrado: " . $factura->id);\n', 'app/Pago.php')
[]               # no menciona ningún dato sensible

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'app/Servicios/Pasarela.php', 61,
          'captura de error vacía (`catch`) — E1 pide manejo visible y trazable'),
 Hallazgo(AVISO, 'app/Http/LoginController.php', 28,
          'posible secreto en un log — E5: los logs no llevan contraseñas/tokens')]
```
