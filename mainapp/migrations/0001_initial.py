# Generated by Django 2.0.2 on 2020-05-13 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['category', 'title'],
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('min_age', models.PositiveSmallIntegerField(default=12, verbose_name='Минимальный возраст')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория книг',
                'verbose_name_plural': 'Категории книг',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Interesting_authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='ФИО')),
                ('content', models.TextField(verbose_name='Биография')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')),
                ('active', models.BooleanField(default=False, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'Топ_авторы',
                'ordering': ['-added', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Interesting_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('content', models.TextField(verbose_name='содержание')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')),
                ('active', models.BooleanField(default=False, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Топ_Книги',
                'ordering': ['-added', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Published_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')),
                ('active', models.BooleanField(default=False, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'вышедшая книга',
                'verbose_name_plural': 'Вышедшие книги',
                'ordering': ['-added', 'title'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.BookCategory', verbose_name='Категория'),
        ),
    ]
