# Generated by Django 4.2.16 on 2024-11-12 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEspecialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuenta', models.CharField(choices=[('Paciente', 'paciente'), ('Especialista', 'especialista')], max_length=12)),
                ('numero_phone', models.CharField(max_length=30)),
                ('numero_dni', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=100)),
                ('sub_especialidad', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
