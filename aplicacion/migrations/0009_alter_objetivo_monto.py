# Generated by Django 5.0.1 on 2024-02-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_alter_ingreso_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivo',
            name='monto',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
