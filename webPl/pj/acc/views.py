from django.shortcuts import render
from django.http import HttpResponse
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pybo.models import Question

def index(request):
    return HttpResponse("<h1>Hello ACC</h1>")


def test(request):
    ques_list = Question.objects.all()
    context = {"ques_list":ques_list}
    return render(request, "pybo/test.html", context)
# Create your views here.
