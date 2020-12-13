from django.urls import include, path

from . import views

app_name="qa"

urlpatterns = [
    path('', views.main_page, name="empty"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('question/<int:question_id>/', views.question, name="question"),
    path('ask/', views.ask, name="ask"),
    path('popular/', views.popular_questions, name="popular"),
    path('new/', views.test, name="new"),
]
