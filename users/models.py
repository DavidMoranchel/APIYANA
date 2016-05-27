from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator
# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    #User attributes

    username = models.CharField(
            'Nombre de usuario',
            max_length=30,
            unique=True,
            help_text='Maximo 30 caracteres, letras, digitos, @/./+/-/_ ',
            validators=[
                RegexValidator(
                    r'^[\w.@+-]+$',
                    ('Ingrese un nombre de usuario valido. Solo puede contener '
                     'letrad, numeros ' 'y @/./+/-/_ caracteres.')
                ),
            ],
            error_messages={
                'unique': "El nombre de usuario ya existe",
            },
    )

    email = models.EmailField(
            'email',
            blank= False,
    )

    phone_regex = RegexValidator(
            regex=r'^\+?1?\d{10,15}$',
            message="El numero tiene que tener este formato '55-5555-5555'."
    )


    phone_number = models.CharField(
            validators=[phone_regex],
            blank=False,
            max_length=13,
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number']

    def get_short_name(self):
        "Returns the short name for the user."
        return self.username.encode("utf8")

    def __str__(self):
        return self.username

