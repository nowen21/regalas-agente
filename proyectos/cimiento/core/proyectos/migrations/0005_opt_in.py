# -*- coding: utf-8 -*-
"""`EP-026·HU-009` · Los capítulos opt-in pasan a ser ajustes, y cada proyecto
registrado lleva a la base lo que dice su `CLAUDE.md`, para que nada cambie el día
del paso (RN-04). De vuelta, se quitan los ajustes opt-in."""

from django.db import migrations, models


def pasar(apps, schema_editor):
    from core.proyectos.opt_in import pasar_a_la_base
    pasar_a_la_base(apps.get_model("proyectos", "Proyecto"), apps.get_model("proyectos", "AjusteDelProyecto"))


def quitar(apps, schema_editor):
    for modelo in ("AjusteBase", "AjusteDelProyecto"):
        apps.get_model("proyectos", modelo).objects.filter(clave__startswith="opt_in_").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_tres_capas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajustebase',
            name='clave',
            field=models.CharField(choices=[('rutas_en_avisos', 'Rutas en los avisos'), ('limite_enganche', 'Límite por enganche'), ('limite_archivo', 'Límite por archivo'), ('opt_in_15', 'Patrón opt-in 15 (registros inmutables)'), ('opt_in_16', 'Patrón opt-in 16 (cumplimiento normativo)'), ('opt_in_17', 'Patrón opt-in 17 (interfaz / UI)'), ('opt_in_18', 'Patrón opt-in 18 (despliegue e infraestructura)'), ('opt_in_19', 'Patrón opt-in 19 (observabilidad y operación)'), ('opt_in_21', 'Patrón opt-in 21 (automatización de procesos)'), ('opt_in_22', 'Patrón opt-in 22 (sistemas que aprenden de datos)')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ajustedelproyecto',
            name='clave',
            field=models.CharField(choices=[('rutas_en_avisos', 'Rutas en los avisos'), ('limite_enganche', 'Límite por enganche'), ('limite_archivo', 'Límite por archivo'), ('opt_in_15', 'Patrón opt-in 15 (registros inmutables)'), ('opt_in_16', 'Patrón opt-in 16 (cumplimiento normativo)'), ('opt_in_17', 'Patrón opt-in 17 (interfaz / UI)'), ('opt_in_18', 'Patrón opt-in 18 (despliegue e infraestructura)'), ('opt_in_19', 'Patrón opt-in 19 (observabilidad y operación)'), ('opt_in_21', 'Patrón opt-in 21 (automatización de procesos)'), ('opt_in_22', 'Patrón opt-in 22 (sistemas que aprenden de datos)')], max_length=50),
        ),
        migrations.RunPython(pasar, quitar),
    ]
