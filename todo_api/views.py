import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

# Create your views here.
class SimpleView(View):
    def get(self, request: HttpRequest):
        html = f"{datetime.datetime.now()+ datetime.timedelta(days=1)}"

        return HttpResponse(html)


# datetime.min = datetime(1, 1, 1)
# datetime.max = datetime(9999, 12, 31, 23, 59, 59, 999999)
# datetime.resolution = timedelta(microseconds=1)