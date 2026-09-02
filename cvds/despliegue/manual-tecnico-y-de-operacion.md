# Manual técnico y de operación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se pone a andar Cimiento, cómo se opera y qué hacer cuando algo falla**. Lo que el sistema hace está en las [especificaciones de módulo](../../documentacion/); acá está cómo se corre.

> **Alcance real, dicho de una:** Cimiento corre en la máquina de quien lo usa. No hay servidor, no hay usuarios, no hay despliegue. Este manual describe eso, y no un montaje que no existe.

---

## 1. Qué es y qué necesita

| Frente | Qué |
|---|---|
| **Qué es** | Una aplicación Django que vive en `plataforma/`, dentro del repositorio del estándar |
| **Lenguaje** | Python 3.11 |
| **Base de datos** | SQLite, en `plataforma/indice.sqlite3` |
| **Dependencias** | Django. Las declaradas en `plataforma/requirements/` |
| **Red** | **Ninguna.** Ni la aplicación ni sus pantallas salen a internet |

**Por qué SQLite y no otra cosa.** La base **no es la fuente**: es un índice que se puede borrar entero y rehacer leyendo los archivos del proyecto. Lo dice `DA-01` y lo sostiene todo el diseño: el texto es la verdad.

---

## 2. Cómo se pone a andar

```
cd plataforma
python manage.py migrate
python manage.py runserver
```

Y se abre `http://127.0.0.1:8000/`.

**La primera vez no hay nada, y la pantalla lo dice.** Conectar el primer proyecto es lo que le da algo que mirar.

---

## 3. Cómo se opera

### 3.1 Lo que se hace por pantalla

| Pantalla | Dónde |
|---|---|
| Los proyectos, y conectar uno | `/` |
| El tablero: cómo van y qué se desvió | `/tablero/` |
| Las fases de un proyecto | `/proyecto/<id>/fases/` |
| Qué está comprobado | `/proyecto/<id>/funcionalidades/` |
| Qué está aprobado | `/proyecto/<id>/aprobaciones/` |
| Qué recuerda el agente | `/proyecto/<id>/memoria/` |
| Traer lo que un proyecto tenga escrito | `/proyecto/<id>/traer/` |

### 3.2 Lo que se hace por consola

**Todo cambio de estado va por acá**, y es a propósito: `00·N1` los quiere con confirmación, y una pantalla que cambia cosas sin ella sería media confirmación.

```
python manage.py abrir_fase <proyecto> <letra> <EP-000> <HU-000> "de qué trata"
python manage.py llenar_hueco <proyecto> <documento> --numero N --texto "..."
python manage.py aprobar <proyecto> <documento> --quien "..."
python manage.py memoria <proyecto> --corregir <nombre> --texto "..."
python manage.py que_rige <proyecto> --encender <REGLA> --cuando AAAA-MM-DD
python manage.py armar_expediente <proyecto>
python manage.py comprobar <proyecto>
python manage.py puerta_de_publicacion <proyecto>
```

`python manage.py help` las lista todas, agrupadas por módulo.

---

## 4. Qué se respalda, y qué no hace falta respaldar

| Qué | ¿Respaldar? | Por qué |
|---|---|---|
| El repositorio del proyecto | **Sí** | Es la fuente: los documentos son el sistema |
| `plataforma/indice.sqlite3` | **No hace falta** | Es índice, no fuente; se rehace |
| `plataforma/datos/` | **No hace falta** | Son copias de lo traído; se rehacen al traer otra vez |

**La única excepción son las aprobaciones**, que sí viven solo en la base: quién aprobó y sobre qué texto es un hecho que ocurrió fuera del documento y no se puede reconstruir leyéndolo.

---

## 5. Cómo se rehace lo que se borre

```
python manage.py reconstruir_traido         # el índice de lo traído
python manage.py indexar_conversaciones     # el índice del histórico
```

Y traer de nuevo cada proyecto desde su pantalla, que vuelve a copiar sus documentos.

---

## 6. Qué falla, cómo se ve y qué se hace

| Síntoma | Qué está pasando | Qué se hace |
|---|---|---|
| Un proyecto aparece con la ruta perdida | La carpeta de su código se movió o se borró | Corregir la ruta desde su ficha |
| El expediente reporta documentos que sí existen | **La copia traída quedó vieja** | Traer de nuevo el proyecto |
| Una pantalla sale vacía | Casi siempre no hay datos, y la pantalla lo dice | Leer la frase: distingue «no hay» de una falla |
| La puerta de publicación sale en rojo | Alguna batería no está en verde | Correrla aparte y leer qué falló |
| Una orden imprime caracteres raros | La consola de Windows no habla UTF-8 | No es un fallo: el texto sale igual, solo se ve mal |

**Lo que pasó de verdad, y por eso está en la tabla:** el expediente reportó **22 documentos faltantes que existían** porque la copia traída tenía 546 documentos menos que el disco. Traer de nuevo lo resolvió.

---

## 7. Qué NO cubre este manual

- **Poner Cimiento en un servidor.** No se ha hecho, y el diseño no lo contempla: corre en la máquina de quien lo usa.
- **Varios usuarios a la vez.** No hay cuentas ni permisos, y `Qué está aprobado` confía en quien escribe el nombre.
- **Recuperar una aprobación borrada de la base.** Es lo único no reconstruible; por eso es lo único que hay que respaldar aparte del repositorio.
