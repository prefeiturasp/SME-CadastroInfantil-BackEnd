# Generated by Django 3.0.5 on 2020-06-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_dadoscrianca_parentesco_responsavel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadoscrianca',
            name='telefone_opcional',
            field=models.CharField(blank=True, help_text='Telefone 2 do responsavel', max_length=14),
        ),
    ]
