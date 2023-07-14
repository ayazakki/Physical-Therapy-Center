from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home,name='home'),
    path('therapist', views.Therapist,name='therapist'),
    path('patient', views.Patient,name='patient'),
    path('devices', views.Device,name='devices'),
    path('maintenance', views.Maintenance,name='Maintenance'),
    path('damage', views.Damage,name='damage'),
    path('treatment', views.Treatment,name='treatment'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('patient/<int:pk>', views.PatientDetailsView.as_view(), name='patient-detail'),
    path('therapist/<int:pk>', views.TherapistDetailsView.as_view(), name='therapist-detail'),
    path('delete_patient/<patient_id>',views.delete_patient,name='delete-patient'),
    path('delete_therapist/<therapist_id>',views.delete_therapist,name='delete-therapist'),
    path('delete_device/<device_id>',views.delete_device,name='delete-device'),
    path('delete_maintenance/<maintenance_id>',views.delete_maintenance,name='delete-maintenance'),
    path('delete_damage/<damage_id>',views.delete_damage,name='delete-damage'),
    path('delete_treatment/<treatment_id>',views.delete_treatment,name='delete-treatment'),
    path('update_patient/<patient_id>',views.update_patient,name='update-patient'),
    path('update_therapist/<therapist_id>',views.update_therapist,name='update-therapist'),
    path('update_device/<device_id>',views.update_device,name='update-device'),
    path('update_damage/<damage_id>',views.update_damage,name='update-damage'),
    path('update_maintenance/<maintenance_id>',views.update_maintenance,name='update-maintenance'),
    path('update_treatment/<treatment_id>',views.update_treatment,name='update-treatment'),
    path('search_center_p', views.search_center_p,name='search-center_p'),
    path('search_center_t', views.search_center_t,name='search-center_t'),
    path('search_center_d', views.search_center_d,name='search-center_d'),

]