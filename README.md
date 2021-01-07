# django-jobservice

My third Django project, a Job-Service site.

It's the first project involving a DB with Models in Django. It also uses a few forms.

Upon going to the main site, you're greeted with a menu that has the following points:

- Log-In to log-in with your account, this is also the first time I've worked with authentication and user-access-levels
- Sign-Up so users can sign up and create their resume. The Signup-Form is validated for different things, like length and strength of password
- Vacancies which will list job offers
- Resumes which will show users resumes
- Profile so logged-in users can change vacancies/resumes depending on their access
- Log-Out

Every Vacancy/Resume is saved and loaded from a Database via Models.

Noteworthy: Only users with admin/staff-access can add vacancies, and only normal users can add resumes.

Vacancies/resumes are added by Forms with validation and a post-request, after checking users access.

This was my, for now, most involved project with Django, as it uses almost everything I've learned in the previous two projects and more.

I've used class-based views, models, forms, validation, quite a bit of DTL.

**Libraries/Modules used:** None.
