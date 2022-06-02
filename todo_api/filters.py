from django.db.models import QuerySet
from typing import Optional

def note_filter_by_author_id(queryset: QuerySet, author_id: Optional[int]):
    """
    Filter Note records by id author
    :param queryset:
    :param author_id:
    :return:
    """
    if author_id:
        return queryset.filter(author_id=author_id)
    else:
        return queryset

