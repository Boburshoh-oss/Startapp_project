from django.contrib import admin
from .models import CustomUser, Startapper, IdeaStartapper, AllUsersIdea, ApplicationStaff, SuccessProjects, \
    CommentOfPost,AboutUS, ContacktsProwork, ProworkAdress , Staff


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Startapper)
admin.site.register(IdeaStartapper)
admin.site.register(AllUsersIdea)

admin.site.register(ApplicationStaff)
admin.site.register(SuccessProjects)
admin.site.register(CommentOfPost)
admin.site.register(AboutUS)
admin.site.register(ContacktsProwork)
admin.site.register(ProworkAdress)
admin.site.register(Staff)
