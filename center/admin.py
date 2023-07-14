from django.contrib import admin
from .models import Damage,Treatment,Maintenance,Therapist,Patient, Device,Profile

admin.site.register(Damage)
admin.site.register(Treatment)
admin.site.register(Maintenance)
admin.site.register(Therapist)
admin.site.register(Patient)
admin.site.register(Device)
admin.site.register(Profile)
