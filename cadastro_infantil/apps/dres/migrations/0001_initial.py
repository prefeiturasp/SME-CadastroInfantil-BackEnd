# Generated by Django 3.0.5 on 2020-06-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CepDistritoDRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_cep', models.CharField(help_text='CEP (00000000)', max_length=8, unique=True)),
                ('nm_distrito', models.CharField(help_text='Nome do Distrito', max_length=50)),
                ('sg_dre', models.CharField(help_text='Sigla da DRE', max_length=3)),
                ('nm_dre', models.CharField(help_text='Nome da DRE', max_length=25)),
            ],
            options={
                'verbose_name': 'DRE',
                'verbose_name_plural': 'DREs',
                'db_table': 'CI_cep_distrito_dre',
            },
        ),
    ]