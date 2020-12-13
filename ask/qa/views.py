from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from .forms import AskForm, AnswerForm, LoginForm, SignupForm

from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login as authlogin



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
    # print(questions)
    paginator, page = paginate(request, questions)
    # return HttpResponse('OK')
    # print(paginator.page_range)
    # for p in paginator.page_range:
        # print("here")
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
    
    
    print("request")
    print(request)
    print(request.session)
    print(request.user)
    print(request.user.id)
    
    print("request_dirs")
    print(dir(request))
    print(dir(request.session))
    print(dir(request.user))
    print("POST")
    print(request.POST)
    
    print(request.COOKIES)
    print(request.session.session_key)
    print(request.session._session_key)
    print("GET")
    print(request.GET)
    
    
    user = request.user
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.question = question_id
            print("HEREEEEE")
            print(user)
            print(user.is_authenticated)
            form._user=user if user.is_authenticated else None
            new_ans = form.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AnswerForm()
    ans = q.answer_set.all()
    return render(request, "question.html", {"question": q, "ans": ans, "form": form})
    
    
    
def ask(request):
    
    user = request.user
    
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user=user if user.is_authenticated else None
            q = form.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AskForm()
    return render(request, "ask.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            authlogin(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            print(user)
            if user:
                return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

        
    
