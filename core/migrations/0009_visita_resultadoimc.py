# Generated by Django 2.1.5 on 2019-01-31 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190131_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='resultadoImc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
