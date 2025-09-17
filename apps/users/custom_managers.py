from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Enter an email")
        if not first_name:
            raise ValueError("Enter a first name")
        if not password:
            raise ValueError("Enter a password")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") != True:
            raise ValueError("Superuser should have is_staff = True")
        if extra_fields.get("is_superuser") != True:
            raise ValueError("Superuser should have is_superuser = True")
        
        return self.create_user(email, first_name, password, **extra_fields)