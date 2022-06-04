from django.test import TestCase
from django.contrib.auth.models import User
from todo_api.models import Note
from todo_api import filters

# тестируем список записей конкретного автора
# генерируем список разных авторов и записей (пример 2 автора, 2 записи)
# фильтруем по конкретному

class TestTODOAPINoteFilters(TestCase):
    def test_note_filter_by_author_id(self):
        # создаем 2 users
        test_user1 = User(
            username="test_user1",
            password="fake1"
        )
        test_user2 = User(
            username="test_user2",
            password="fake2"
        )
        # test_user1.save()
        # test_user2.save()

        test_user1, test_user2 = User.objects.bulk_create([test_user1, test_user2])
        # наполняем базу 3 записями
        Note(nt_title="title_1", nt_author=test_user1).save()
        Note(nt_title="title_2", nt_author=test_user1).save()
        Note(nt_title="title_2", nt_author_id=test_user2.id).save()  # по внешнему соед 2 польз со 2 записью

        queryset = Note.objects.all()
        filter_author_id = test_user1.id
        expected_queryset = queryset.filter(nt_author_id=filter_author_id)
        actual_queryset = filters.note_filter_by_author_id(
            queryset,
            author_id=filter_author_id,
        )
        # проверяем
        self.assertQuerysetEqual(
            actual_queryset, expected_queryset, ordered=False
        )