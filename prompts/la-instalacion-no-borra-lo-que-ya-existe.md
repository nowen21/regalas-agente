# Instalar nunca destruye lo que el proyecto ya tiene

Lo que pidió el usuario, con sus palabras. Rescatado de las sesiones del histórico.

## De [2026-08-07-memoria-del-agente-en-el-repo.md](../historico-chat/2026-08-07-memoria-del-agente-en-el-repo.md) · 2026-08-07 17:52:01

mire lo que esta pasando me está borrando la memoria y eso no puede pasar si ya existe debe estar ahí, de hecho se debe validar que si ya está instalado no me toque más la carpeta

## De [2026-08-07-memoria-del-agente-en-el-repo.md](../historico-chat/2026-08-07-memoria-del-agente-en-el-repo.md) · 2026-08-07 16:52:24

por qué si ya hay contenido acá: historico-chat/memory/ lo borra si eso es lo que se busca conservar la memoria del repo ahí y no en el equipo

## De [2026-08-08-sesion.md](../historico-chat/2026-08-08-sesion.md) · 2026-08-08 15:27:10

El proceso debe ser **idempotente**: si se ejecuta nuevamente sobre un proyecto ya instalado, debe detectar lo que ya existe y no duplicar ni sobrescribir innecesariamente elementos.
