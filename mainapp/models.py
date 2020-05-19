from django.db import models
# from django.contrib.auth.models import ParkUser


class BookCategory (models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    min_age = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст', default=12)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.name} : {self.min_age}'

    class Meta:
        ordering = ['name']
        verbose_name = 'категория книг'
        verbose_name_plural = 'Категории книг'


class Book(models.Model):
    category = models.ForeignKey(BookCategory, verbose_name='Категория', on_delete=models.CASCADE) #связь "Один ко многим"
    title = models.CharField(verbose_name='Название', max_length=64)
    price = models.PositiveSmallIntegerField(verbose_name='Цена', default=0)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.title} ({self.category.name}): {self.price} руб'

    class Meta:
        ordering = ['category', 'title']
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'

class Published_books(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    content = models.TextField(verbose_name='Содержание')
    added = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активна', default=False)

    def __str__(self):
        # return f'{self.added:%Y-%m-%d %H:%M:%S}: {self.title} ({self.author})'
        return f'{self.added:%Y-%m-%d %H:%M}: {self.title} - {self.active}'

    class Meta:
        ordering = ['-added', 'title']
        verbose_name = 'вышедшая книга'
        verbose_name_plural = 'Вышедшие книги'

class Interesting_authors(models.Model):
    title = models.CharField(verbose_name='ФИО', max_length=128)
    content = models.TextField(verbose_name='Биография')
    added = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активна', default=False)

    def __str__(self):
        return f'{self.added:%Y-%m-%d %H:%M}: {self.title}  - {self.active}'

    class Meta:
        ordering = ['-added', 'title']
        verbose_name = 'автор'
        verbose_name_plural = 'Топ_авторы'

class Interesting_books(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    content = models.TextField(verbose_name='содержание')
    added = models.DateTimeField(verbose_name='Добавлена',auto_now_add=True)
    active = models.BooleanField(verbose_name='Активна', default=False)

    def __str__(self):
        return f'{self.added:%Y-%m-%d %H:%M}: {self.title}  - {self.active}'

    class Meta:
        ordering = ['-added', 'title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Топ_Книги'