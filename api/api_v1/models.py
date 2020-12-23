from django.db import models


class Pool(models.Model):
    title = models.CharField('Опрос', max_length=100)
    description = models.TextField('Описание', max_length=500)
    start_date = models.DateTimeField('Дата старта', auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания')
