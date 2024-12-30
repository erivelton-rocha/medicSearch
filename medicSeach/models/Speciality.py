from medicSeach.models import *


class Speciality(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
