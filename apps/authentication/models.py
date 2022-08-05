import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class Role(models.Model):
    NONE = 0
    CUSTOMER = 1
    OWNER = 2
    ROLE_CHOICES = (
        (NONE, 'none'),
        (CUSTOMER, 'customer'),
        (OWNER, 'owner')
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return str(self.get_id_display())


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """Creates a new User, given a username and password."""
        user: User = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates a new User, with superuser status."""
        user: User = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.SET_DEFAULT, default=0)

    @property
    def restaurants(self):
        if (self.role is Role.OWNER):
            return self.restaurant_set.all()
        else:
            return

    @property
    def orders(self):
        if (self.role is Role.CUSTOMER):
            return self.order_set.all()
        else:
            return

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    objects = UserManager()
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.full_name if (self.first_name) else self.username

    class Meta:
        app_label = 'authentication'
