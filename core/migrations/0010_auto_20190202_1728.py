# Generated by Django 2.1.5 on 2019-02-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_visita_resultadoimc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visita',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visita',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
