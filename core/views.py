from django.shortcuts import render
from .models import Profile, Skill, Experience, Project, Education, OnlineProfile


def home(request):
    context = {
        "profile": Profile.objects.filter(is_active=True).first(),
        "skills": Skill.objects.filter(is_active=True),
        "experiences": Experience.objects.filter(is_active=True),
        "projects": Project.objects.filter(is_active=True),
        "educations": Education.objects.filter(is_active=True),
        "profiles": OnlineProfile.objects.filter(is_active=True),
    }
    return render(request, "core/home.html", context)
