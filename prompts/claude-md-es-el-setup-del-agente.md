# El agente se instala solo, leyendo su propio CLAUDE.md

Lo que pidió el usuario, con sus palabras. Rescatado de las sesiones del histórico.

## De [2026-08-08-la-instalacion-se-hace-sola.md](../historico-chat/2026-08-08-la-instalacion-se-hace-sola.md) · 2026-08-08 15:27:10

Corrija el proceso de instalación para que `CLAUDE.md` sea tratado como el **setup principal del agente**.
El objetivo es que, al ejecutar el proceso de instalación, el agente sea capaz de **instalar, configurar y dejar completamente operativo el entorno por sí mismo**, sin depender de que el usuario tenga que intervenir manualmente.
El proceso debe cumplir con lo siguiente:
* `CLAUDE.md` debe contener las instrucciones necesarias para que el agente pueda realizar correctamente su propio proceso de instalación y configuración.
* El agente debe detectar automáticamente el estado actual del proyecto y determinar qué elementos hacen falta.
* Debe crear, modificar o configurar automáticamente los archivos, carpetas, estructuras y componentes necesarios para dejar la instalación completa y funcional.
* **No debe preguntar al usuario** por decisiones que ya estén definidas en `CLAUDE.md`, las reglas del agente o la estructura estándar del proyecto.
* **No debe exigir al usuario guardar, copiar, mover o crear manualmente ningún archivo** como parte del proceso de instalación.
* Si el proyecto no cumple con la estructura requerida, el agente debe realizar las acciones necesarias para adecuarlo automáticamente, siempre respetando las reglas establecidas.
* El proceso debe ser **idempotente**.
* Al finalizar, debe validar que toda la estructura y configuración requerida esté correctamente instalada y operativa.
* Si encuentra un problema que realmente impida continuar y que no pueda resolverse automáticamente sin una decisión del usuario, debe detenerse e informar claramente cuál es el bloqueo y por qué requiere intervención.
