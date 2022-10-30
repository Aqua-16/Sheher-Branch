from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

# extra details
class VisitorDetails(models.Model):
    GENDER =(
        ('MALE','Male'),
        ('FEMALE','Female'),
        ('OTHERS','Others'),
    )
    user= models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
    city= models.CharField(max_length=255,blank=False)
    phone=models.CharField(max_length=10,blank=False)
    sos_contact = models.CharField(max_length=10, blank=True)
    address=models.CharField(max_length=255,blank=False)
    gender=models.CharField(max_length=20,blank=False,choices=GENDER,default=1)
    profile_picture = models.ImageField(default='images\Visitors\default.jpg', upload_to='images\Visitors')


    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
# Create your models here.
