# 12 · Privacidad y datos personales

Cómo tratar los datos de las personas. Más allá de la seguridad técnica (`04`), es un compromiso y a menudo una obligación legal. La capa 3 declara el marco normativo y la retención concretos.

---

## PR1 · Recolecta solo lo necesario (minimización)

No pidas ni guardes datos personales que la función no necesita. Cada dato guardado es riesgo y responsabilidad. Prefiere el dato menos sensible que resuelva el problema.

```
INCORRECTO: guardar documento y dirección "por si acaso"
CORRECTO:   guardar solo lo que la función usa de verdad
```

## PR2 · Úsalos solo para lo que se recolectaron

Los datos se usan para el propósito con que se obtuvieron. No los reutilices para otro fin (analítica, marketing, terceros) sin base legítima y consentimiento. No los envíes a servicios externos sin autorización (`00` · N6).

## PR3 · Protégelos en reposo y en tránsito

Datos personales cifrados en tránsito (`04` · S5) y, si son sensibles, en reposo o con acceso restringido (`04` · S6). Acceso limitado por **permiso y scope** (`04` · S1). Credenciales con hashing fuerte, nunca en claro (`04` · S5).

## PR4 · No los expongas en logs, errores ni mensajes

Logs y errores sin datos personales más allá de lo imprescindible: usa identificadores, no el dato en claro (`05` · E5). Los mensajes a otros usuarios no filtran datos de terceros. Reportes y pantallas muestran datos solo a quien tiene derecho.

```
INCORRECTO: loguear nombre, correo y teléfono en cada operación
CORRECTO:   loguear un identificador; el dato queda en la BD con acceso controlado
```

## PR5 · Retención y borrado

Define **cuánto tiempo** se conservan; no indefinido "porque sí". Prevé **borrado o anonimización** cuando ya no se necesitan o la persona lo pide. Si el registro tiene valor legal/contable que impide borrarlo (`15`), **anonimiza** los datos personales conservando el registro. Documenta la decisión.

```
INCORRECTO: conservar para siempre los datos de cuentas inactivas
CORRECTO:   retención definida + borrado/anonimización al cumplirse el plazo
```

---

Ver: `04` (controles técnicos), `05` E5 (logs), `15` (anonimizar en vez de borrar), `00` N6.
