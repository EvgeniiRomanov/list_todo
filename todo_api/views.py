import datetime

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from . models import Note
from . import serializers, filters


class NoteListCreateAPIView(APIView):
    """ Представления для чтения всех заметок """

    def get(self, request: Request):
        notes = Note.objects.all()                  # читаем все заметки
        serializer = serializers.NoteSerializer(    # отдаем сериалайзеру
            instance=notes,
            many=True,                              # для выдачи списка объектов
        )
        return Response(data=serializer.data)       # выводим в отсериализованной форме

    def post(self, request: Request):
        serializer = serializers.NoteSerializer(
            data=request.data                       # получаем данные json из POST
        )
        # проверка данных
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(nt_author=request.user)  # сохранияем в базе (залогиненный пользователь)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)  # объект уже из БД


class NoteDetailAPIView(APIView):
    """ Представления для чтения отдельных заметок """
    #permission_classes = (IsAuthenticated, )    # теперь сюда только авторизированные

    # @staticmethod
    # def valid_serializer(serializer):
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)              # обработка ошибок если нет такого номера
        serializer = serializers.NoteDetailSerializer(
            instance=note,                                 # по конкретному pk
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """Изменение заметки автором """
        note = get_object_or_404(Note, pk=pk)
        serializer = serializers.NoteDetailSerializer(note, data=request.data)

        if not serializer.is_valid():
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if note.nt_author != request.user:
            return Response(f"Изменить заметку может только автор: {note.nt_author}",
                            status=status.HTTP_403_FORBIDDEN)

        serializer.save(nt_author=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """ Изменение полей заметки автором """
        note = get_object_or_404(Note, pk=pk)
        serializer = serializers.NoteDetailSerializer(note, data=request.data, partial=True)

        if not serializer.is_valid():
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if note.nt_author != request.user:
            return Response(f"Изменить заметку может только автор: {note.nt_author}",
                            status=status.HTTP_403_FORBIDDEN)

        serializer.save(nt_author=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """ Удаление заметки автором """
        note = get_object_or_404(Note, pk=pk)

        if note.nt_author != request.user:
            return Response(f"Удалить заметку может только автор: {note.nt_author}",
                            status=status.HTTP_403_FORBIDDEN)
        note.delete()

        return Response(f"Заметка №{pk} успешно удалена.", status=status.HTTP_204_NO_CONTENT)


class PublicNoteListAPIView(ListAPIView): # ListAPIView возвращает только список объектов с которыми работали, post и put тут нет
    """/notes/public/"""
    queryset = Note.objects.all()   #(public=True) - отображать только пубуличные, но так не хорошо, лучше фильтрами
    serializer_class = serializers.NoteSerializer


    # фильтр только публичные
    def get_queryset(self):
        queryset = super().get_queryset()            # получаем полную копию
        return queryset.filter(nt_public=True).order_by('nt_endtime')       # (nt_author=self.request.user, public = True)
        # return self.order_by_queryset(queryset)                                             # (nt_author_id = 1)
                                                     # order_by (выбор столбца упорядочивания)

    # фильтрация по автору, фильтр по важность, фильтр по публичности
    def filter_queryset(self, queryset):
        queryset = filters.note_filter_by_author_id(
                    queryset,
                    author_id=self.request.query_params.get("nt_author_id", None),
                    )

        queryset = filters.note_filter_by_importance(queryset,
                    importance_id=self.request.query_params.get("nt_importance", None),
                    )

        return filters.note_filter_by_status(queryset,
                    status_id=self.request.query_params.get("nt_status", None),
                    )






   # # фильтрация
   #  def filter_queryset(self, queryset):
   #     # queryset = super().filter_queryset(queryset)   #
   #      #self.request.query_params.get("author_id", None)
   #      return filters.note_filter_by_author_id(
   #          queryset,
   #          author_id=self.request.query_params.get("nt_author_id", None)
   #      )


# # сериализация функциями Read all list
# class NoteListCreateAPIView(APIView):
#     """Read all list"""
#     def get(self, request: Request):
#         objects = Note.objects.all()
#         #objects = get_list_or_404(Note)
#         return Response([serializers.note_to_json(elem) for elem in objects])
#
#     def post(self, request: Request):
#         data = request.data # считываем отправленный кнопкой POST json по http
#         note = Note(**data, nt_author=request.user)  # формируем объект python для базы
#         note.save(force_insert=True) # сохраняем в базе сформированный объект
#         # возвращаем результат пользователю
#         return Response(
#             serializers.note_created(note),
#             status=status.HTTP_201_CREATED
#         )

# сериализация функциями /notes/pk
# class NoteDetailAPIView(APIView):
#     """/notes/pk"""
#     def get(self, request, pk):
#         note = get_object_or_404(Note, pk=pk)            # обработка ошибок если нет такого номера
#         return Response(serializers.note_to_json(note))
#
#     def put(self, request, pk):
#         object = get_object_or_404(Note, pk=pk)
#         object.nt_title = request.data['nt_title']
#         object.nt_description = request.data['nt_description']
#         object.nt_public = request.data['nt_public']
#         object.nt_status = request.data['nt_status']
#         object.nt_importance = request.data['nt_importance']
#
#         object.save(force_update=True)
#
#         return Response(
#             serializers.note_created(object),
#             status=status.HTTP_201_CREATED
#         )
#
#     def patch(self, request, pk):
#         object = get_object_or_404(Note, pk=pk)
#
#
#     def delete(self, request, pk):
#         object = get_object_or_404(Note, pk=pk)
#         object.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


