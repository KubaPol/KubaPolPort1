from django.db import models


class Artiles(models.Model):
    objects = None
    title = models.CharField('Название', null = True, max_length=50)
    anons = models.CharField('Анонс',  null = True,max_length=250)
    full_text = models.TextField('Статья', null = True)
    date = models.DateTimeField('Дата публикации', null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
