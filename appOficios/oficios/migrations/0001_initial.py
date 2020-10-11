# Generated by Django 3.0.8 on 2020-10-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('codigo_de_oficio', models.CharField(max_length=500, verbose_name='Código de oficio')),
                ('unidad_academica', models.CharField(max_length=500, verbose_name='Unidad acádemica')),
                ('a_quien_se_dirige', models.CharField(max_length=500, verbose_name='A quién va dirigido')),
                ('asunto', models.TextField(verbose_name='Asunto')),
                ('oficio', models.FileField(upload_to='', verbose_name='Oficio')),
            ],
            options={
                'ordering': ['-codigo_de_oficio'],
            },
        ),
        migrations.AddIndex(
            model_name='oficio',
            index=models.Index(fields=['codigo_de_oficio'], name='oficios_ofi_codigo__9d1b5d_idx'),
        ),
    ]
