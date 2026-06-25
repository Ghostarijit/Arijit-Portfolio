from django.contrib import admin
from .models import Profile, Skill, Experience, Project, Education, OnlineProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "email", "is_active"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["category", "order", "is_active"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_title", "company", "start_date", "end_date", "is_active"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "tech_stack", "is_active"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["degree", "institution", "year_range", "is_active"]


@admin.register(OnlineProfile)
class OnlineProfileAdmin(admin.ModelAdmin):
    list_display = ["platform", "url", "is_active"]
