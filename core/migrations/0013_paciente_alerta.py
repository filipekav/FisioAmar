# Generated by Django 2.1.5 on 2019-03-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190301_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='alerta',
            field=models.BooleanField(default=False),
        ),
    ]