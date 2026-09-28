# Manual de instalación y despliegue   ·   `[CAPA 3]`

**Para qué sirve este documento.** Con esto, alguien que no estuvo en el desarrollo levanta el sistema desde cero en una máquina limpia, sin preguntar nada. Es la prueba escrita de la reproducibilidad: si un paso vive solo en la memoria de alguien, el sistema no se puede instalar, se puede *volver a adivinar*.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla. Se alimenta desde la primera fase, cuando el entorno se arma por primera vez, y se corrige cada vez que un paso cambia. Está bien cuando seguirlo literal en una máquina limpia funciona ([`11·CE1`](../../base/11-configuracion-entornos.md)).
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

## 1. Requisitos previos

> Lista lo que debe estar instalado en la máquina antes de empezar, con la versión exigida y el comando que confirma que está.

| Qué | Versión | Cómo comprobar que está |
|---|---|---|
| «runtime, base de datos, herramienta» | «…» | «`comando --version`» |

## 2. Instalación, paso a paso

> Son los comandos literales, en orden, desde clonar hasta ver el sistema andando. Cada paso dice qué se espera ver: un paso sin resultado esperado no se puede verificar.

| # | Paso | Comando | Qué se espera ver |
|---|---|---|---|
| 1 | Obtener el código | «`git clone ...`» | «…» |
| 2 | Instalar dependencias | «…» | «…» |
| 3 | Configurar el entorno | «copiar `.env.example` a `.env` y llenar (§3)» | «…» |
| 4 | Preparar la base de datos | «migraciones, datos semilla» | «…» |
| 5 | Arrancar | «…» | «el sistema responde en «dónde»» |

## 3. Las variables de configuración

> Tiene una fila por variable de `.env.example`, con qué es y de dónde se obtiene su valor. Los valores reales no van acá ni en ningún documento ([`00·N6`](../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).

| Variable | Qué es | De dónde sale el valor |
|---|---|---|
| «…» | «…» | «…» |

## 4. Verificación de humo

> Confirma, apenas termina la instalación, que el sistema responde de verdad.

«Los dos o tres pasos que confirman que la instalación quedó bien: entrar, crear un dato de prueba, verlo. Con lo que se espera ver en cada uno.»

## 5. Despliegue a producción y reversión

> Dice cómo se pasa de la instalación local a producción y cómo se deshace una versión que salió mal.

«Qué cambia respecto de la instalación local (servidor, dominio, certificados), en pasos igual de literales. Y cómo se vuelve atrás una versión si sale mal: el procedimiento de reversión se escribe antes de necesitarlo. Si el proyecto adoptó el capítulo [`18`](../../base/18-despliegue-e-infraestructura.md), esto lo detalla su checklist de despliegue y acá queda el puntero.»
