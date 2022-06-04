from django.test import TestCase
from todo_api.models import Note
from django.contrib.auth.models import User


class ModelTODOTestCase(TestCase):
    """ Тест на создание заметки в БД"""
    @classmethod
    def setUpTestData(cls):                              # создаем пользователя
        User.objects.create(username='test1@test.ru')    # пользователь по умолч. для всех тестов

    def setUp(self):    # создаем одну заметку
        self.task_name = "Создание тестовой заметки"
        test_user = User.objects.get(username='test1@test.ru')          # достаем пользователя
        self.task = Note(nt_title=self.task_name, nt_author=test_user)  # создаем заметку с необх. полями

    def test_model_can_create_Note(self):
        old_count = Note.objects.count()        # считаем число заметок в БД
        self.task.save()                        # помещаем созданную в def SetUp заметку в БД
        new_count = Note.objects.count()
        self.assertNotEqual(old_count, new_count)