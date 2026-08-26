# Resultado de Pruebas — Fase B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma

**Para qué sirve este documento.** Dice qué se ejecutó, con qué y qué dio. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**Cumple**, ciclo 1. Siete casos de siete.** Ejecutado el 2026-08-22 contra la versión 31.3.0, en Windows con Python 3.

## 1. Caso por caso

| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 · la sección nueva llega al proyecto ya instalado | reportada y escrita, con su texto | ✅ |
| CP-02 · lo que el proyecto escribió sigue ahí | palabra por palabra | ✅ |
| CP-03 · sin novedad no reescribe | el archivo queda idéntico | ✅ |
| CP-04 · la sección llega con su cuerpo | más de una línea bajo el título | ✅ |
| CP-05 · el sello queda al día | la huella se reescribe contra la plantilla | ✅ |
| CP-06 · si no existe, se crea entero | `crear historico-chat/README.md` | ✅ |
| CP-07 · no regresión | `suite` y `estandar` sin incumplimientos | ✅ |

## 2. Lo que costó llegar al verde

**Un caso falló en la primera corrida, y el fallo era de la prueba, no del código.** `CP-05` buscaba en el archivo la palabra del identificador del componente; el sello real se escribe como `<!-- huella: … · estandar X.Y.Z -->`. Se corrigió la prueba para mirar el sello que de verdad se escribe. Es la diferencia entre probar lo que uno cree que hace el programa y probar lo que hace.

## 3. Lo que no se probó

**Que corra sobre los proyectos ya instalados.** Eso pasa cuando cada uno vuelva a instalar; lo que esta fase garantiza es que, cuando pase, reciban lo nuevo sin perder lo suyo.
