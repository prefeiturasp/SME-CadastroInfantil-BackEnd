# Generated by Django 3.0.5 on 2021-03-01 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_auto_20200612_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadoscrianca',
            name='cpf',
            field=models.CharField(blank=True, help_text='CPF', max_length=11, null=True),
        ),
    ]
