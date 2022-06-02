import unittest

from rest_framework.test import APITestCase
from rest_framework import status
from todo_api.models import Note
from django.contrib.auth.models import User


class TestNoteListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):                            # тест данные один раз на все тесты
        User.objects.create(username='test1@test.ru')   # создаем пользователя по умолчанию, он будет
                                                       # сидеть в нашей БД для всех тестов, у него author_id=1

    def test_empty_list_objects(self):
        url = '/notes/'                 # путь куда стучаться от корня
        resp = self.client.get(url)     # клиент типа браузера, с которого мы делаем запросы и получаем ответ
        # ожидаем от сервера ответ "status.HTTP_200_OK" и сравниваем с полученными
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        # если база пустая, там пустой список т.к. listcomp во view
        response_data = resp.data       # полученные данные
        exp_data = []                   # ожидаемые данные
        self.assertEqual(exp_data, response_data)