

from django.contrib import admin
from django.urls import path


from django.contrib.auth.views import LogoutView

from menu.views import MenuView
from menu.views import SignupView
from menu.views import MyLoginView
from menu.views import UserView

from resume.views import ResumeView, NewResume
from vacancy.views import VacancyView, NewVacancy



urlpatterns = [
    path('', MenuView.as_view()),
    path('home', UserView.as_view()),
    path('admin/', admin.site.urls),
    path('resumes/', ResumeView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('resume/new', NewResume.as_view()),
    path('vacancy/new', NewVacancy.as_view())
]

