from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, full_name=''):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def by_group(self, group_name):
        try:
            group = Group.objects.get(name=group_name)
            return self.filter(groups=group)
        except Group.DoesNotExist:
            return False

    def create_superuser(self, username, email, password=None, full_name=''):
        user = self.create_user(
            username,
            email,
            password=password,
            full_name=full_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=245)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='users', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    @property
    def get_fb_data(self):
        name = None
        profile_picture_url = None
        for social_app in self.socialaccount_set.all():
            if social_app.provider == 'facebook':
                name, profile_picture_url = social_app.extra_data.get('name'), social_app.get_avatar_url()
        return dict(name=name, profile_picture_url=profile_picture_url)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        # The user is identified by username
        return self.username

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_admin(self):
        return self.is_superuser

    objects = UserManager()

    def __str__(self):
        return self.full_name or self.email
