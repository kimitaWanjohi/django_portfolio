from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Eductation, Experience, Project, Blogs

@admin.register(Eductation)
class EductationAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'school', 'start_date', 'end_date')

@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'company', 'start_date', 'end_date')

@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'live_link', 'source_link', 'start_date', 'end_date')

@admin.register(Blogs)
class BlogsAdmin(SummernoteModelAdmin):
    summernote_fields = ('brief_description',)
    list_display = ('title', 'blog_link', 'blog_image_link')


