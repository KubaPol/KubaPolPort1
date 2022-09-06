# Generated by Django 4.1 on 2022-08-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=250, null=True, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(null=True, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
    ]
