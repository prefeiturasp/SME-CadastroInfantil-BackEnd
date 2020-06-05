# Generated by Django 3.0.5 on 2020-06-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadoscrianca',
            name='filiacao1_sexo',
            field=models.CharField(choices=[('F', 'FEMININO'), ('M', 'MASCULINO'), ('', '')], help_text='Sexo da filiacao I (M/F)', max_length=1),
        ),
        migrations.AlterField(
            model_name='dadoscrianca',
            name='filiacao2_sexo',
            field=models.CharField(blank=True, choices=[('F', 'FEMININO'), ('M', 'MASCULINO'), ('', '')], help_text='Sexo da filiacao II (M/F)', max_length=1),
        ),
        migrations.AlterField(
            model_name='dadoscrianca',
            name='sexo_crianca',
            field=models.CharField(choices=[('F', 'FEMININO'), ('M', 'MASCULINO'), ('', '')], help_text='Sexo da criança (M/F)', max_length=1),
        ),
    ]