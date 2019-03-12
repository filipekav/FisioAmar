# Generated by Django 2.1.5 on 2019-03-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_paciente_alerta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='alerta',
            new_name='alertaGlicemia',
        ),
        migrations.AddField(
            model_name='paciente',
            name='alertaPA',
            field=models.BooleanField(default=False),
        ),
    ]
