# Generated by Django 4.2.18 on 2025-02-11 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_pessoa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
    ]
