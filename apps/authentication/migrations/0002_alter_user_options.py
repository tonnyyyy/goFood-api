# Generated by Django 4.0.6 on 2022-08-01 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('admin_user', 'Can Admin Usuários'), ('disable_user', 'Can disable Usuário'))},
        ),
    ]
