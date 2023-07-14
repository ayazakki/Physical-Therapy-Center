from django.shortcuts import redirect, render
from .models import Therapist as Th
from .models import Patient as Pat
from .models import Damage as dag
from .models import Device as de
from .models import Maintenance as M
from .models import Treatment as Treat
from .forms import TherapistForm,PatientForm,DeviceForm,MaintenanceForm,DamageForm,TreatmentForm
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Patient as pt
from .models import Therapist as the
from .models import Device as dev


def Home(request):
    return render(request, 'index.html')
@login_required
def Treatment(request):
    submitted=False   
    if request.method == "POST":
         form=TreatmentForm(request.POST)
         if form.is_valid():
               form.save()    
               
    else:
       form=TreatmentForm
       if 'submitted' in request.GET:
          submitted=True    

   
    return render(request,'treatment.html',{'form':form,'submitted':submitted})
@login_required
def Therapist(request):
    submitted=False   
    if request.method == "POST":
         form=TherapistForm(request.POST)
         if form.is_valid():
               form.save()    
               return  HttpResponseRedirect('therapist?submitted=True')
    else:
       form=TherapistForm
       if 'submitted' in request.GET:
          submitted=True    

   
    return render(request,'therapist.html',{'form':form,'submitted':submitted})
@login_required
def Patient(request):
    submitted=False   
    if request.method == "POST":
         form=PatientForm(request.POST)
         if form.is_valid():
               form.save()    
               
    else:
       form=PatientForm
       if 'submitted' in request.GET:
          submitted=True    

   
    return render(request,'patient.html',{'form':form,'submitted':submitted})
@login_required
def Device(request):
    submitted=False   
    if request.method == "POST":
        form=DeviceForm(request.POST)
        if form.is_valid():
            form.save()    
               
    else:
        form=DeviceForm
        if 'submitted' in request.GET:
            submitted=True    

   
    return render(request,'devices.html',{'form':form,'submitted':submitted})
@login_required
def Maintenance(request):
    submitted=False   
    if request.method == "POST":
         form=MaintenanceForm(request.POST)
         if form.is_valid():
               form.save()    
               
    else:
       form=MaintenanceForm
       if 'submitted' in request.GET:
          submitted=True    

   
    return render(request,'Maintenance.html',{'form':form,'submitted':submitted})
@login_required
def Damage(request):
    submitted=False   
    if request.method == "POST":
        form=DamageForm(request.POST)
        if form.is_valid():
            form.save()    
            return  HttpResponseRedirect('damage?submitted=True')
    else:
        form=DamageForm
        if 'submitted' in request.GET:
          submitted=True    

   
    return render(request,'damage.html',{'form':form,'submitted':submitted})
@login_required
def alltherapists(request):
    t = Th.objects.all()
    return render(request, 'AllTherapists.html', {'therapist':t})
@login_required
def allpatients(request):
    p = Pat.objects.all()
    return render(request, 'AllPatients.html', {'patients':p})
@login_required
def alldamages(request):
    d = dag.objects.all()
    return render(request, 'AllDamages.html', {'damages':d})
@login_required
def Alldevices(request):
    dd = de.objects.all()
    return render(request, 'Alldevices.html', {'devices':dd})
@login_required
def allmaintenance(request):
    m = M.objects.all()
    return render(request, 'AllMaintenance.html', {'maintenance':m})
@login_required
def alltreatments(request):
    treat = Treat.objects.all()
    return render(request, 'AllTreatments.html', {'treatments':treat})

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PatientDetailsView(generic.DetailView):
    model = Pat
    template_name = 'patient_detail.html'

def delete_patient(request,patient_id):
    item_patient=Pat.objects.get(pk=patient_id)    
    item_patient.delete()
    return redirect('/AllPatients')  
def delete_therapist(request,therapist_id):
    item_therapist=Th.objects.get(pk=therapist_id)    
    item_therapist.delete()
    return redirect('/AllTherapists') 
def delete_device(request,device_id):
    item_device=de.objects.get(pk=device_id)    
    item_device.delete()
    return redirect('/Alldevices') 

def delete_maintenance(request,maintenance_id):
    item_maintenance=M.objects.get(pk=maintenance_id)    
    item_maintenance.delete()
    return redirect('/AllMaintenance') 

def delete_damage(request,damage_id):
    item_damage=dag.objects.get(pk=damage_id)    
    item_damage.delete()
    return redirect('/AllDamages') 

def delete_treatment(request,treatment_id):
    item_treatment=Treat.objects.get(pk=treatment_id)    
    item_treatment.delete()
    return redirect('/AllTreatments') 

def update_patient(request,patient_id):
    patient=Pat.objects.get(pk=patient_id)
    form=PatientForm(request.POST or None,instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/AllPatients')
    return render(request,'update_patient.html',{'patient':patient,'form':form})    
def update_therapist(request,therapist_id):
    therapist=Th.objects.get(pk=therapist_id)
    form=TherapistForm(request.POST or None,instance=therapist)
    if form.is_valid():
        form.save()
        return redirect('/AllTherapists')
    return render(request,'update_therapist.html',{'therapist':therapist,'form':form})

def update_device(request,device_id):
    device=de.objects.get(pk=device_id)
    form=DeviceForm(request.POST or None,instance=device)
    if form.is_valid():
        form.save()
        return redirect('/Alldevices')
    return render(request,'update_device.html',{'device':device,'form':form})

def update_damage(request,damage_id):
    damage=dag.objects.get(pk=damage_id)
    form=DamageForm(request.POST or None,instance=damage)
    if form.is_valid():
        form.save()
        return redirect('/AllDamages')
    return render(request,'update_damage.html',{'damage':damage,'form':form})


def update_maintenance(request,maintenance_id):
    maintenance=M.objects.get(pk=maintenance_id)
    form=MaintenanceForm(request.POST or None,instance=maintenance)
    if form.is_valid():
        form.save()
        return redirect('/AllMaintenance')
    return render(request,'update_maintenance.html',{'maintenance':maintenance,'form':form})

def update_treatment(request,treatment_id):
    treatment=Treat.objects.get(pk=treatment_id)
    form=TreatmentForm(request.POST or None,instance=treatment)
    if form.is_valid():
        form.save()
        return redirect('/AllTreatments')
    return render(request,'update_treatment.html',{'treatment':treatment,'form':form})




def search_center_p(request):
    if request.method == "POST":
        searched = request.POST['searched']
        Patient=pt.objects.filter(first_name__contains=searched)

        return render(request,'search_center_p.html',{'searched':searched,'Patient':Patient})
    else:
        return render(request,'search_center_p.html',{})
    
def search_center_t(request):
    if request.method == "POST":
        searched = request.POST['searched']
        therapist=the.objects.filter(first_name__contains=searched)

        return render(request,'search_center_t.html',{'searched':searched,'therapist':therapist})
    else:
        return render(request,'search_center_t.html',{})


def search_center_d(request):
    if request.method == "POST":
        searchedd = request.POST['searchedd']
        Device=dev.objects.filter(first_name__contains=searchedd)

        return render(request,'search_center_d.html',{'searchedd':searchedd,'Device':Device})
    else:
        return render(request,'search_center_d.html',{})        
    
class TherapistDetailsView(generic.DetailView):
    model = Th
    template_name = 'therapist_detail.html'

