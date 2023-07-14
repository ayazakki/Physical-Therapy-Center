from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Therapist(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    id=models.AutoField(primary_key=True,max_length=50)
    username=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    date_of_birth=models.DateField()
    gender=[('male','male'),
            ('female','female')]
    gender=models.CharField(max_length=50,choices=gender,null=True)
    phone=models.CharField(max_length=50,null=True)
    university=models.CharField(max_length=50,null=True)
    degree=models.CharField(max_length=50,null=True)
    specialty=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('therapist-detail', args=[str(self.id)])
    
class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Id=models.AutoField(primary_key=True, max_length=50)
    age=models.CharField(max_length=50,null=True)    
    date_of_birth=models.DateField(blank=True,null=True)
    gender=[('male','male'),
            ('female','female')]
    gender=models.CharField(max_length=50,choices=gender,null=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    Responsible_party=models.CharField(max_length=50,null=True,blank=True)
    height=models.CharField(max_length=50,null=True,blank=True)
    weight=models.CharField(max_length=50,null=True,blank=True)
    integrated_doctors=models.TextField(max_length=300,null=True)
    surgical=models.TextField(max_length=300,null=True)
    primary_diagnosis=models.TextField(max_length=300,null=True)

    def get_absolute_url(self):
        return reverse('patient-detail', args=[str(self.Id)])

    def __str__(self):
        return self.first_name
    
class Treatment(models.Model):
    id=models.AutoField(primary_key=True,max_length=50)
    sessions=models.IntegerField()
    date=models.DateField()
    signature=models.CharField(max_length=50)
    notes=models.TextField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE, related_name='treattt' ,null=True,blank=True)
    #therapist=models.ManyToManyField(Therapist)
    def __str__(self):
        return self.signature     


class Device(models.Model):
    name = models.CharField(max_length=50)
    deviceid = models.AutoField(primary_key=True,max_length=50)
    production_date = models.DateField()
    period_of_guarantee = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=4)
    country_of_manfucature = models.CharField(max_length=50)
    company_of_manfucature = models.CharField(max_length=50)
    duration_per_session = models.IntegerField()
    Max_number_per_day = models.IntegerField(blank=True,null=True)
    agent = models.CharField(max_length=50)  
    usage_per_day = models.IntegerField()
    department = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Damage(models.Model):
    #device_name=models.CharField(max_length=50,null=True)
    id=models.AutoField(primary_key=True,max_length=50)
    damage_date=models.DateField(null=True)
    damage_reason=models.TextField(null=True)
    report_date=models.DateField(null=True)
    check_notes=models.TextField(null=True)
    Examination_officer_name=models.CharField(max_length=50,null=True)
    nurse_name=models.CharField(max_length=50,null=True)
    Devicess=models.OneToOneField(Device,related_name='Device',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.damage_reason 
    
class Maintenance(models.Model):
    clinic=models.CharField(max_length=50)
    date_of_supply=models.DateField()
    #name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    agent=models.CharField(max_length=50)
    serial=models.CharField(max_length=50,primary_key=True, help_text='Unique ID for this particular book across whole library')
    company=models.CharField(max_length=50)

    date=models.DateField()
    Eng_signature=models.CharField(max_length=50)
    Company_signature=models.CharField(max_length=50)
    choices=[('yes','yes'),
             ('no','no')]
    device_condition=models.CharField(max_length=50,choices=choices)

    notes=models.TextField()
    device_name=models.OneToOneField(Device,on_delete=models.CASCADE,related_name='main', null=True)

    def __str__(self):
        return self.serial   

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    def __str__(self):
        return str(self.user)
@receiver(post_save,sender=User)    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


