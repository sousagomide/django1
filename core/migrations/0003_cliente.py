# Generated by Django 5.0 on 2023-12-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_produto_nome_produto_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, null=True, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]
