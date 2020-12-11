from django.urls import include, path

from . import views

app_name="qa"

urlpatterns = [
    path('', views.main_page, name="empty"),
    path('login/', views.test, name="login"),
    path('signup/', views.test, name="signup"),
    path('question/<int:question_id>/', views.question, name="question"),
    path('ask/', views.test, name="ask"),
    path('popular/', views.popular_questions, name="popular"),
    path('new/', views.test, name="new"),
]
