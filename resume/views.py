
from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from .forms import NewForm
from django.http import HttpResponseForbidden


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/resumes.html', context={'resumes': resumes})


class NewResume(View):
    def post(self, request, *args, **kwargs):
        form = NewForm(request.POST)
        if form.is_valid():
            descr = form.cleaned_data['description']
            if request.user.is_authenticated and not request.user.is_staff:
                new = Resume(description=descr, author=request.user)
                new.save()
                return redirect('/home')
            else:
                return HttpResponseForbidden()

        return HttpResponseForbidden()

