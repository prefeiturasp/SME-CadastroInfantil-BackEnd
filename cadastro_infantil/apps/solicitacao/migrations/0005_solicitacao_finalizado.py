# Generated by Django 3.0.5 on 2020-06-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0004_auto_20200609_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='finalizado',
            field=models.BooleanField(default=False, help_text='FLAG que este processo de solicitacao está finalizada'),
        ),
    ]
