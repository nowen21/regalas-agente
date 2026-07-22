# 12 · Privacidad y datos personales

> **Capa 2 · agnóstica al stack.** Cómo tratar los datos personales de las personas (clientes, empleados, usuarios). Más allá de la seguridad técnica (`04`), la privacidad es un compromiso con quien confió sus datos, y a menudo una obligación legal. La capa 3 declara el marco normativo aplicable (según país y sector) y la política de retención concreta.

---

## PR1 · Recolectar solo lo necesario (minimización)

No pedir ni almacenar datos personales que la funcionalidad no necesita. Cada dato personal guardado es una responsabilidad y un riesgo.

- Antes de agregar un campo personal, preguntar: ¿lo necesito para esta función?
- Preferir el dato menos sensible que resuelva el problema.

```
INCORRECTO: guardar el número de documento y la dirección "por si acaso"
CORRECTO:   guardar solo lo que la funcionalidad usa de verdad
```

---

## PR2 · Usar los datos solo para lo que se recolectaron

Los datos personales se usan para el propósito con el que se obtuvieron. No reutilizarlos para otro fin (analítica, marketing, compartir con terceros) sin base legítima y, cuando corresponda, consentimiento.

- No enviar datos personales a servicios externos (incluidos los de terceros para logging o analítica) sin necesidad y sin autorización.
- Este principio se refuerza en el núcleo: no enviar contenido a servicios externos sin autorización (`00` · N6).

---

## PR3 · Proteger los datos sensibles en reposo y en tránsito

- Los datos personales y sensibles viajan **cifrados** (`04-seguridad.md` S5) y, cuando su sensibilidad lo amerita, se almacenan cifrados o con acceso restringido (`04-seguridad.md` S6).
- El acceso a datos personales se limita por **permiso y scope**: solo quien tiene razón legítima los ve (`04-seguridad.md` S1).
- Las credenciales y secretos de las personas se guardan con hashing fuerte, nunca en claro (`04-seguridad.md` S5).

---

## PR4 · No exponer datos personales en logs, errores ni mensajes

- Los logs y los mensajes de error **no** incluyen datos personales más allá de lo imprescindible para diagnosticar; preferir identificadores en vez del dato en claro (`05-errores-y-logging.md` E5).
- Los mensajes de cara a otros usuarios no filtran datos de terceros.
- Las pantallas y reportes muestran datos personales solo a quien tiene derecho a verlos.

```
INCORRECTO: loguear el nombre, correo y teléfono completos en cada operación
CORRECTO:   loguear un identificador; el dato personal queda en la BD con acceso controlado
```

---

## PR5 · Retención y borrado

- Definir **cuánto tiempo** se conservan los datos personales; no guardarlos indefinidamente "porque sí".
- Prever el **borrado o anonimización** cuando el dato ya no se necesita o cuando la persona ejerce su derecho (según el marco aplicable).
- Cuidado con la tensión entre borrado y trazabilidad: cuando un registro tiene valor legal/contable que impide borrarlo (`15-registros-inmutables.md`), evaluar **anonimizar** los datos personales conservando el registro contable, en vez de un borrado que rompa la integridad. Esta decisión se documenta.

```
INCORRECTO: conservar para siempre todos los datos personales de cuentas inactivas
CORRECTO:   política de retención definida + borrado/anonimización al cumplirse el plazo
```

---

## Relación con el resto del estándar

- **`04-seguridad.md`** — los controles técnicos (authz, cifrado, almacenamiento) sostienen la privacidad.
- **`05-errores-y-logging.md` E5** — no registrar datos personales innecesarios.
- **`15-registros-inmutables.md`** — anonimizar en vez de borrar cuando el registro debe preservarse.
- **Núcleo `00` · N6** — no enviar datos a servicios externos sin autorización.
