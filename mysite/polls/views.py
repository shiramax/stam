from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question , Answer, Quiz, School ,Course
from django.forms import formset_factory



def index(request):
    school_list = School.objects.order_by('-school_name')
    course_list = Course.objects.order_by('-course_name')
    quiz_list = Quiz.objects.order_by('-name')
    question_list = Question.objects.order_by('-question_text')
    template = loader.get_template('polls/index.html')
    context = {
        'school_list': school_list,
        'course_list': course_list,
        'quiz_list': quiz_list,
        'question_list': question_list

    }
    return HttpResponse(template.render(context, request))



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


