import datetime
from django.db import models                             # модели
from django.utils.translation import gettext_lazy as _   # шаблоны с именами
from django.contrib.auth.models import User              # пользователи


class Note(models.Model):
    """ Класс описывающий Заметку """
    class Ratings(models.IntegerChoices):
        SERIOUS = 2, _('Активно')
        WAIT = 1, _('Отложено')
        DONE = 0, _('Выполено')

    nt_title = models.CharField(max_length=255, verbose_name='Заголовок')
    nt_description =  models.TextField(default='', max_length=3000, verbose_name='Текст', )
    nt_importance = models.BooleanField(default=False, verbose_name='Важно')
    nt_public = models.BooleanField(default=False, verbose_name='Опубликовать')
    nt_status = models.IntegerField(default=Ratings.SERIOUS, choices=Ratings.choices,
                                    verbose_name='Статус задачи')
    nt_createtime = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    nt_updatetime = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    nt_endtime = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=1)),
                                      verbose_name='Выполнить к:')
    nt_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):   # отображение запись объекта в читаемой форме
        return f"Заметка №{self.id}"

    class Meta:         # отображение имен для модели
        verbose_name = _('Заметка')
        verbose_name_plural = _('Заметки')

        ordering = ['nt_endtime']
