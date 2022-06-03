from django.contrib import admin
from .models import Note


@admin.register(Note)                           # добавляем модель Note в админку
class ModelAdmin(admin.ModelAdmin):
    # отображение полей в списке в указанном порядке
    list_display = ('nt_title', 'nt_author_id', 'nt_importance', 'nt_public', 'nt_status', 'nt_endtime', 'id')

    # отвечает за отображение полей. Группировака поля в режиме редактирования
    fields = (('nt_title', 'nt_public', 'nt_importance'), 'nt_status', 'nt_description', 'nt_createtime', 'nt_updatetime', 'nt_endtime', 'nt_author')

    # если поле в модели не редактируемое (nt_createtime), то помещаем сюда, если хотим его отображать
    readonly_fields = ('nt_createtime', 'nt_updatetime')

    # поля по которым искать
    search_fields = ['nt_title', 'nt_description']    # [=title] поиск точного совпадения

    # фильтр справа
    list_filter = ['nt_public', 'nt_importance']