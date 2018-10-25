from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question, Choice
from django.utils import timezone
#
# def index(request):
#     return HttpResponse('index!!!')
def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request,'polls/result.html',
                  {'question':question})



def add_question(request):
    text = request.POST['text']

    q = Question(
        question_text=text,
        pub_date = timezone.now())
    q.save()
    return render(request, 'polls/add_question.html', {})

def question(request):
    return render(request, 'polls/question.html', {})


def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html',
                  {'item':question})

def data(request):
    value = request.GET['user_name']
    return HttpResponse(value)

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes +1
    c.save()
    print(choice)
    return render(request, 'polls/vote.html', {})


def index(request):
    list = Question.objects.all()
    return render(request,
                  'polls/index.html',
                  {'question':list})