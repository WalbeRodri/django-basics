# Generated by Django 5.1.1 on 2024-11-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='insira o nome', max_length=50)),
                ('cpf', models.CharField(help_text='apenas numeros', max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('endereco', models.TextField(max_length=1000)),
                ('telefone', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
