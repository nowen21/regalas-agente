# `README.md`

El manual de uso de la carpeta `validadores/`. Este documento habla del archivo `validadores/README.md`, no de esta carpeta de documentación.

## Qué es

Es lo que se lee para **usar** los validadores: cómo se corren, qué revisa cada uno y cuándo arrancan solos. No es código: nadie lo llama y no se ejecuta.

La diferencia con la carpeta `docs/`: el `README.md` cuenta **qué hacen** los validadores, visto desde afuera; los documentos de `docs/` cuentan **cómo están hechos** por dentro.

## Qué contiene

| Parte | De qué trata |
|---|---|
| El principio | Cuándo algo se convierte en validador y cuándo se queda como regla escrita: si un programa puede responder sí o no sin opinar, se hace validador; si dos personas pueden discutirlo, se queda escrito. |
| Falla y aviso | La diferencia entre las dos, y por qué no es un detalle de forma. |
| Uso | Las órdenes que se escriben en la consola: revisar el estándar, revisar un documento contra su molde, revisar el mensaje de un cambio y correr las pruebas. |
| Qué revisa cada uno | Una tabla con los veinte validadores que leen archivos: qué mira cada uno y qué regla está haciendo cumplir. |
| Los que corren una herramienta | Los tres que llaman a una herramienta del proyecto, y por qué esos no arrancan solos. |
| Lo que a propósito no se revisa | Los cinco casos que se dejaron fuera, con el motivo de cada uno. |
| Los que arrancan solos | Los seis, uno por uno: qué los dispara, qué hacen y cómo se activan. |
| Regla de oro | Que acá no se revisa nada que no esté escrito en la norma. Primero se escribe la regla, después se comprueba. |

## Con qué se relaciona

El `README.md` habla de casi todos los archivos de la carpeta, así que queda viejo si:

- se agrega o se quita un validador → hay que tocar la tabla de «qué revisa cada uno»;
- se agrega un programa que arranque solo → hay que tocar esa parte;
- se agrega algo nuevo que se pueda pedir por consola → hay que tocar la parte de uso.

Como vive adentro de este repositorio, sus enlaces los revisa `enlaces.py` cada vez que se cambia un documento.

## Cómo se lee

No se ejecuta. Se abre en `validadores/README.md`.
