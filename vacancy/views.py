from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden

from django.views import View
from .models import Vacancy

from resume.forms import NewForm


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancies.html', context={'vacancies': vacancies})


class NewVacancy(View):
    def post(self, request, *args, **kwargs):
        form = NewForm(request.POST)
        if form.is_valid():
            descr = form.cleaned_data['description']
            if request.user.is_authenticated and request.user.is_staff:
                new = Vacancy(description=descr, author=request.user)
                new.save()
                return redirect('/home')
            else:
                return HttpResponseForbidden()

        return HttpResponseForbidden()




