# -*- coding: utf-8 -*-
"""Los proyectos que ya existen en esta máquina entran al registro.

Salen de `plantillas/proyectos.md`, la lista que el instalador llenó en cada
máquina. En la base de pruebas no se trae nada: las pruebas parten vacías.
"""
from django.db import migrations

from core.proyectos.registro import proyectos_md, traer_de_proyectos_md


def traer(apps, schema_editor):
    if schema_editor.connection.settings_dict["NAME"].startswith("test_"):
        return
    traer_de_proyectos_md(apps.get_model("proyectos", "Proyecto"), proyectos_md())


class Migration(migrations.Migration):

    dependencies = [
        ("proyectos", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(traer, migrations.RunPython.noop),
    ]
