# Estructura de un proyecto Django  ·  `[CAPA 3]`

> Plantilla. La estructura estándar de **todo** proyecto Django: se copia a la documentación de
> arquitectura del proyecto, se reemplazan los `«…»` con lo propio y se borra esta caja. Lo que no
> lleva marca no es opcional: es la parte que todo proyecto Django cumple igual.

## La estructura

```
«nombre-del-proyecto»/
├── .venv/                    · el entorno del proyecto · NO se versiona
├── .env                      · credenciales de este equipo · NO se versiona
├── .env.example              · las mismas variables, sin valores · sí se versiona
├── manage.py
├── requirements/
│   ├── base.txt              · las dependencias de producción: «Django x.y, motor de BD, …»
│   ├── local.txt             · `-r base.txt` más lo de desarrollo
│   └── lock.txt              · las versiones exactas, transitivas incluidas (`10·DEP2`)
├── config/                   · configuración del proyecto
│   ├── settings/
│   │   ├── base.py           · lo común a cualquier equipo
│   │   └── local.py          · lo del equipo de desarrollo
│   ├── urls.py
│   └── wsgi.py · asgi.py
├── static/                   · SOLO lo propio del proyecto
├── staticfiles/              · lo que junta `collectstatic` · NO se versiona
├── templates/                · plantillas de todo el proyecto
└── «paquete»/                · los módulos del dominio, uno por carpeta
    ├── «modulo-1»/           · «qué resuelve»
    ├── «modulo-2»/           · «qué resuelve»
    ├── «…»
    └── templates/«paquete»/  · plantillas propias

    y dentro de cada módulo, siempre lo mismo:
        models.py · admin.py · forms.py · views.py · tests.py · apps.py · migrations/
```

## Cuatro cosas que esta estructura da por sentadas

**El proyecto descarga sus dependencias.** Nada de terceros se copia al repositorio. Se declara en
`requirements/` y lo instala pip dentro de `.venv/`. Por eso no hay `static/vendor/`: lo que un
paquete trae de estáticos lo junta `collectstatic` en `staticfiles/`, que tampoco se versiona porque
se regenera con una orden. `lock.txt` fija las versiones exactas, transitivas incluidas, para que dos
equipos instalen lo mismo ([`10·DEP2`](../base/10-dependencias.md)).

**Las credenciales no viven en el código.** El archivo que las tiene (`.env`) no entra al
repositorio. Lo que sí entra es `.env.example`, con las mismas variables y sin un solo valor: es la
lista de lo que hay que llenar para que el proyecto arranque en otro equipo (base `11`).

**Un módulo, una carpeta.** No se agrupa por tipo de archivo (un `models/` con todos los modelos, un
`views/` con todas las vistas), sino por módulo: cada carpeta tiene adentro su modelo, su panel, sus
formularios, sus vistas y sus pruebas. Así se localiza cualquier archivo por convención, borrar un
módulo es borrar una carpeta, y quien llega abre una carpeta y ve el dominio
([`14·EST1`](../base/14-estructura-codigo.md)). La ruta queda declarada en
`.agente/mapeo-nombres.md`, que es lo que la hace comprobable por un programa.

**Cada módulo es una aplicación de Django.** Es lo que hace que la carpeta sea de verdad
autocontenida: cada una tiene su `apps.py` y sus propias migraciones, y se registra en
`INSTALLED_APPS` en orden de dependencia: los catálogos y tablas de referencia primero, las
operaciones que cruzan entidades al final.
