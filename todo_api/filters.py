from django.db.models.query import QuerySet
from typing import Optional


def note_filter_by_author_id(queryset: QuerySet, author_id: Optional[int]):
    """
    Фильтрация заметок по идентификатору автора
    :param queryset:запрос
    :param author_id: идентификатор автора
    :return: Заметки с указанным идентификатором автора
    """
    if author_id:
        return queryset.filter(nt_author_id=author_id)
    else:
        return queryset


def note_filter_by_importance(queryset: QuerySet, importance_id: Optional[bool]):
    """
    Фильтрация заметок по признаку важности
    :param queryset: запрос
    :param importance_id: идентификатор важности (True или False)
    :return: Заметки отфильтрованные по важности
    """
    if importance_id:
        return queryset.filter(nt_importance=importance_id)
    else:
        return queryset


def note_filter_by_status(queryset: QuerySet, status_id: Optional[int]):
    """
    Фильтрация заметок по статусу
    :param queryset: запрос
    :param status_id: статус 2 - Активно, 1 - Отложено, 0 - Выполнено.
    :return: Заметки с указанным статусом
    """
    if status_id:
        return queryset.filter(nt_status=status_id)
    else:
        return queryset