from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Medico'),
    (3, 'Paciente')
)


from .Address import Address
from .Neighborhood import Neighborhood
from .City import City
from .State import State
from .DayWeek import DayWeek
from .State import State
from .Speciality import Speciality
from .Profile import Profile