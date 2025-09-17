from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .custom_managers import UserManager


class User(AbstractBaseUser):
    """
    Custom User model:
        * Required fields for a admin:
            - email (USERNAME_FIELD)
            - first_name
        * Authorization by an email
    """
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    bonuses = models.IntegerField(default=0, blank=False)

    # Fields for admin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Проверка разрешений пользователя"""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Проверка разрешений на модуль"""
        return self.is_superuser

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
