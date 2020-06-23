# Generated by Django 3.0.5 on 2020-06-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0005_solicitacao_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='agrupamento',
            field=models.CharField(blank=True, choices=[('BERCARIO I', 'BERCARIO I'), ('BERCARIO II', 'BERCARIO II'), ('MINI GRUPO I', 'MINI GRUPO I'), ('MINI GRUPO II', 'MINI GRUPO II'), ('INFANTIL I', 'INFANTIL I'), ('INFANTIL II', 'INFANTIL II'), ('INFANTIL II', 'INFANTIL II'), ('SEM AGRUPAMENTO', 'SEM AGRUPAMENTO')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='finalizado',
            field=models.BooleanField(default=False, help_text='FLAG que este processo de solicitacao está finalizado'),
        ),
    ]
