"""Los dos grupos de Cimiento. Sin permisos de modelo todavía: cada HU que crea
una pantalla de administración agrega los suyos al grupo administrador."""
from django.db import migrations

GRUPOS = ("administrador", "consulta")


def crear(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    for nombre in GRUPOS:
        Group.objects.get_or_create(name=nombre)


def borrar(apps, schema_editor):
    apps.get_model("auth", "Group").objects.filter(name__in=GRUPOS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(crear, borrar),
    ]
