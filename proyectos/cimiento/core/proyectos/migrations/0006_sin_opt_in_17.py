# -*- coding: utf-8 -*-
"""`EP-028·HU-001` · El capítulo 17 dejó de ser opt-in: sale de las opciones y se
quitan los ajustes `opt_in_17`, que ya no hacen nada. De vuelta, cada proyecto
registrado lo vuelve a tomar de su `CLAUDE.md`."""

from django.db import migrations, models


def quitar(apps, schema_editor):
    for modelo in ("AjusteBase", "AjusteDelProyecto"):
        apps.get_model("proyectos", modelo).objects.filter(clave="opt_in_17").delete()


def volver(apps, schema_editor):
    from core.proyectos.opt_in import del_claude_md
    Proyecto = apps.get_model("proyectos", "Proyecto")
    Ajuste = apps.get_model("proyectos", "AjusteDelProyecto")
    for proyecto in Proyecto.objects.all():
        prendido = del_claude_md(proyecto.ruta).get("17", True)
        Ajuste.objects.get_or_create(proyecto=proyecto, clave="opt_in_17", defaults={"valor": "sí" if prendido else "no"})


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_opt_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajustebase',
            name='clave',
            field=models.CharField(choices=[('rutas_en_avisos', 'Rutas en los avisos'), ('limite_enganche', 'Límite por enganche'), ('limite_archivo', 'Límite por archivo'), ('opt_in_15', 'Patrón opt-in 15 (registros inmutables)'), ('opt_in_16', 'Patrón opt-in 16 (cumplimiento normativo)'), ('opt_in_18', 'Patrón opt-in 18 (despliegue e infraestructura)'), ('opt_in_19', 'Patrón opt-in 19 (observabilidad y operación)'), ('opt_in_21', 'Patrón opt-in 21 (automatización de procesos)'), ('opt_in_22', 'Patrón opt-in 22 (sistemas que aprenden de datos)')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ajustedelproyecto',
            name='clave',
            field=models.CharField(choices=[('rutas_en_avisos', 'Rutas en los avisos'), ('limite_enganche', 'Límite por enganche'), ('limite_archivo', 'Límite por archivo'), ('opt_in_15', 'Patrón opt-in 15 (registros inmutables)'), ('opt_in_16', 'Patrón opt-in 16 (cumplimiento normativo)'), ('opt_in_18', 'Patrón opt-in 18 (despliegue e infraestructura)'), ('opt_in_19', 'Patrón opt-in 19 (observabilidad y operación)'), ('opt_in_21', 'Patrón opt-in 21 (automatización de procesos)'), ('opt_in_22', 'Patrón opt-in 22 (sistemas que aprenden de datos)')], max_length=50),
        ),
        migrations.RunPython(quitar, volver),
    ]
