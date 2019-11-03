from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "man"
    GENDER_FEMALE = "woman"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_MALE, "여자"),
        (GENDER_MALE, "기타"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "영어"),
        (LANGUAGE_KOREAN, "한국어"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LAUGAUAGE_CHOICES,)
