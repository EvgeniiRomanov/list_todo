from datetime import datetime
from rest_framework import serializers
from . models import Note

# сериализация функциями
# def note_to_json(note) -> dict:
#     return {
#         "nt_id": note.id,
#         "nt_title": note.nt_title,
#         "nt_description": note.nt_description,
#         "nt_status": note.nt_status,
#         "nt_importance": note.nt_importance,
#         "nt_public": note.nt_public,
#         "nt_createtime": note.nt_createtime,
#         "nt_updatetime": note.nt_updatetime,
#         "nt_endtime": note.nt_endtime,
#         "nt_author": note.nt_author_id
#     }
#
#
# def note_created(note) -> dict:
#     return {
#         "nt_id": note.id,
#         "nt_title": note.nt_title,
#         "nt_description": note.nt_description,
#         "nt_status": note.nt_status,
#         "nt_importance": note.nt_importance,
#         "nt_public": note.nt_public,
#         "nt_createtime": note.nt_createtime,
#         "nt_updatetime": note.nt_updatetime,
#         "nt_endtime": note.nt_endtime,
#         "nt_author": note.nt_author_id
#     }


class NoteSerializer(serializers.ModelSerializer):
    """ Сеариализатор для выдачи /notes """
    nt_author = serializers.SlugRelatedField(    # отображаем вместо идентификатора FK имя slug_field
        slug_field="username",                   # новое поле из таблицы с FK для отображения
        read_only=True
    )

    class Meta:
        """ Класс для настройки отображания данных при выводе /notes """
        model = Note                        # accept model
        fields = "__all__"                  # show all fields (либо exclude = ('public', ))
        read_only_fields = ("nt_author", )  # что бы автор ставился тот, кот залогинен, т.о. закрыли запись

    def to_representation(self, instance):
        """Меняем формат вывода даты в ответе"""
        ret = super().to_representation(instance)
        nt_createtime = datetime.strptime(ret['nt_createtime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        nt_updatetime = datetime.strptime(ret['nt_updatetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # nt_endtime = datetime.strptime(ret['nt_endtime'], '%Y-%m-%dT%H:%M:%S.%fZ') # при созд из админки без .%fZ
        ret['nt_createtime'] = nt_createtime.strftime('%d %B %Y %H:%M:%S')
        ret['nt_updatetime'] = nt_updatetime.strftime('%d %B %Y %H:%M:%S')
        # ret['nt_endtime'] = nt_endtime.strftime('%d %B %Y %H:%M:%S')
        return ret


class NoteDetailSerializer(serializers.ModelSerializer):
    """ Сеарилизатор для выдачи /notes/pk """
    nt_author = serializers.SlugRelatedField(   # отображаем вместо идентификатора FK имя slug_field
        slug_field="username",                  # новое поле из таблицы с FK для отображения
        read_only=True
    )

    class Meta:
        """ Класс для настройки отображания данных при выводе /notes/pk """
        model = Note                       # accept model
        fields = "__all__"                 # show all fields (либо exclude = ('public', ))
        read_only_fields = ("nt_author",)  # что бы автор ставился тот, кот залогинен, т.о. закрыли запись

    def to_representation(self, instance):
        """Меняем формат вывода даты в ответе"""
        ret = super().to_representation(instance)
        nt_createtime = datetime.strptime(ret['nt_createtime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        nt_updatetime = datetime.strptime(ret['nt_updatetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # nt_endtime = datetime.strptime(ret['nt_endtime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        ret['nt_createtime'] = nt_createtime.strftime('%d %B %Y %H:%M:%S')
        ret['nt_updatetime'] = nt_updatetime.strftime('%d %B %Y %H:%M:%S')
        # ret['nt_endtime'] = nt_endtime.strftime('%d %B %Y %H:%M:%S')
        return ret