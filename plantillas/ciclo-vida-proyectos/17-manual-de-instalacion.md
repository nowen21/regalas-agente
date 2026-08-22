# Manual de instalación y despliegue   ·   `[CAPA 3]`

**Para qué sirve este documento.** Con esto, alguien que no estuvo en el desarrollo levanta el sistema desde cero en una máquina limpia, sin preguntar nada. Es la prueba escrita de la reproducibilidad: si un paso vive solo en la memoria de alguien, el sistema no se puede instalar, se puede *volver a adivinar*.

> Plantilla. Se alimenta desde la primera fase (cuando el entorno se arma por primera vez) y se corrige cada vez que un paso cambia. La forma de saber que está bien: seguirlo literal en una máquina limpia y que funcione ([`11·CE1`](../../base/11-configuracion-entornos.md)). Reemplaza los `«…»` y borra esta caja.

## 1. Requisitos previos

| Qué | Versión | Cómo comprobar que está |
|---|---|---|
| «runtime, base de datos, herramienta» | «…» | «`comando --version`» |

## 2. Instalación, paso a paso

> Comandos literales, en orden, desde clonar hasta ver el sistema andando. Cada paso dice qué se espera ver; un paso sin resultado esperado no se puede verificar.

| # | Paso | Comando | Qué se espera ver |
|---|---|---|---|
| 1 | Obtener el código | «`git clone ...`» | «…» |
| 2 | Instalar dependencias | «…» | «…» |
| 3 | Configurar el entorno | «copiar `.env.example` a `.env` y llenar (§3)» | «…» |
| 4 | Preparar la base de datos | «migraciones, datos semilla» | «…» |
| 5 | Arrancar | «…» | «el sistema responde en «dónde»» |

## 3. Las variables de configuración

> Una fila por variable de `.env.example`. **Los valores reales no van acá ni en ningún documento** ([`00·N6`](../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)): esta tabla dice qué es cada una y de dónde se obtiene.

| Variable | Qué es | De dónde sale el valor |
|---|---|---|
| «…» | «…» | «…» |

## 4. Verificación de humo

«Los dos o tres pasos que confirman que la instalación quedó bien: entrar, crear un dato de prueba, verlo. Con lo que se espera ver en cada uno.»

## 5. Despliegue a producción y reversión

«Qué cambia respecto de la instalación local (servidor, dominio, certificados), en pasos igual de literales. Y cómo se vuelve atrás una versión si sale mal: el procedimiento de reversión se escribe antes de necesitarlo. Si el proyecto adoptó el capítulo [`18`](../../base/18-despliegue-e-infraestructura.md), esto lo detalla su checklist de despliegue y acá queda el puntero.»
