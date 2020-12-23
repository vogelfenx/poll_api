from django.db import models


class Pool(models.Model):
    title = models.CharField('Опрос', max_length=100)
    description = models.TextField('Описание', max_length=500)

    # setting auto_now or auto_now_add to True will cause the field to have editable=False
    start_date = models.DateTimeField(
        'Дата старта', auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания')

    def __str__(self):
        return ("%s" % (self.title, ))
