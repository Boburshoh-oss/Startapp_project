from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import *

admin.site.register(Startapper)
admin.site.register(IdeaStartapper)
admin.site.register(AllUsersIdea)
admin.site.register(Staff)
admin.site.register(ApplicationStaff)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'user_type',)
    list_display = ('full_name', 'user_type')


@admin.register(SuccessProjects)
class SuccessProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description',)


@admin.register(AboutUS)
class AboutUSAdmin(TranslatableAdmin):
    list_display = ('post_title',)


admin.site.register(ContacktsProwork)
admin.site.register(CommentOfPost)


@admin.register(ProworkAdress)
class ProworkAdressAdmin(TranslatableAdmin):
    list_display = ('owner', 'branch_name')
