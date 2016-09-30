from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice
# Create your views here.

def index(request):
    print("polls")
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'question_list':question_list}
    return render(request, 'polls/index.html', context )


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    qs = get_object_or_404(Question, pk=question_id)
    print(request.POST['choice'])
    try:
        selected_choice = qs.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context= { 'question' : qs,
                   'error_message': "하나를 골라주세요!"}
        return render(request, 'polls/detail.html', context)
    else:
        print(selected_choice)
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(qs.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',  {'question' : question } )
