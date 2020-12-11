from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Question

from django.core.paginator import Paginator, EmptyPage
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    limit = 10
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

def main_page(request, *args, **kwargs):
    questions = Question.objects.new()
    print(questions)
    paginator, page = paginate(request, questions)
    print(paginator)
    print(page)
    # return HttpResponse('OK')
    return render(request, "main_page.html", {
        "questions": questions,
        "paginator": paginator,
        "page": page,
    })
    
def popular_questions(request, *args, **kwargs):
    questions = Question.objects.popular()
    print(questions)
    paginator, page = paginate(request, questions)
    # return HttpResponse('OK')
    print(paginator.page_range)
    for p in paginator.page_range:
        print("here")
    return render(request, "popular_questions.html", {
        "questions": questions,
        "paginator": paginator,
        "page": page,
    })
    
    
def question(request, question_id):
    try:
        q = Question.objects.get(id=question_id);
    except Question.DoesNotExist:
        raise Http404
    ans = q.answer_set.all()
    return render(request, "question.html", {"question": q, "ans": ans})
