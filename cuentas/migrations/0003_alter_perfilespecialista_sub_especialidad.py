# Generated by Django 4.2.16 on 2024-11-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_perfilespecialista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilespecialista',
            name='sub_especialidad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]