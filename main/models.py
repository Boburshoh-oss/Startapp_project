from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class CustomUser(AbstractUser):
    STARTAPPER = "Startapper"
    DEVELOPER = "Developer"
    PRACTITIONER = "Practitioner"

    USER_TYPE = [
        (STARTAPPER, 'Startapper'),
        (DEVELOPER, 'Developer'),
        (PRACTITIONER, 'Practitioner'),
    ]

    full_name = models.CharField('full name', max_length=200, blank=False, null=False)
    email = models.EmailField('email address', blank=False, null=False, unique=True)
    user_type = models.CharField(max_length=30, choices=USER_TYPE)
    phone = models.CharField(max_length=30, blank=False, null=False, unique=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

TASHKENT = 'Tashkent'
NEWYORK = 'NewYork'
COUNTRY = [
    (TASHKENT, 'Tashkent'),
    (NEWYORK, 'NewYork'),
]

class Startapper(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=400)
    country = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRY)
    image = models.ImageField(upload_to='startapper_file/startapp_image', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=400)
    country = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRY)
    image = models.ImageField(upload_to='staff_image', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ----- {self.user.user_type}"

class IdeaStartapper(models.Model):
    user = models.ForeignKey(Startapper, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='media/startapper_idea', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username}  - {self.file}"

class AllUsersIdea(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='media/alluser_ideas', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name}  - {self.file}"

class ApplicationStaff(models.Model):
    ONLINE = 'Online'
    OFFLINE = 'Offline'
    ONOFF = [
        (ONLINE, 'Online'),
        (OFFLINE, 'Offline')
    ]
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    resume = models.FileField(upload_to='media_staff_resume', blank=True, null=True)
    work_type = models.CharField(max_length=10, choices=ONOFF)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.user.user.user_type} - {self.resume}"

class SuccessProjects(TranslatableModel):
    translate = TranslatedFields(
        title=models.CharField(max_length=255, null=True),
        description=models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='projects_photo', null=True)
    url = models.URLField(max_length=255)


class CommentOfPost(models.Model):
    post = models.ForeignKey(SuccessProjects, on_delete=models.CASCADE, related_name='comment')
    replay_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        username = self.owner.full_name
        return username if username else 'No name'

class AboutUS(TranslatableModel):
    translate = TranslatedFields(
        post_title=models.CharField(max_length=255),
        post_description=models.TextField(null=True)
    )
    post_image = models.ImageField(upload_to='about_us')

    def __str__(self):
        return self.safe_translation_getter('post_title')

class ContacktsProwork(models.Model):
    adress = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    phone_number2 = models.CharField(max_length=255)

    def __str__(self):
        return

class ProworkAdress(TranslatableModel):
    owner = models.ForeignKey(ContacktsProwork, on_delete=models.CASCADE)
    translation = TranslatedFields(
        branch_name=models.CharField(max_length=255)
    )
    location_langitute = models.FloatField(blank=True, null=True)
    location_latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('branch_name',)