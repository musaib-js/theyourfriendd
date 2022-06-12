from django.urls import path, include

from. import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/signup/consultant/', views.ConsultantSignUpView.as_view(), name='consultant_signup'),
    path('patientprofile/', views.patientupdate, name= "patientupdate"),
    path('selectsubscription/', views.selectsubscription, name= "selectsubscription"),
    path('selectsubscription/<str:name>', views.subscribe, name= "subscribe"),
    path('consultantprofile/', views.consultantupdate, name= "consultantupdate"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('doctordashboard/', views.doctordashboard, name='doctordashboard'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/<int:pk>', views.doctorr, name='doctorr'),
    path('bookappointment/<int:pk>/', views.bookappointment, name='bookappointment'),
    path('meditation/', views.meditation, name='meditation'),
    path('coping/', views.coping, name='coping'),
    path('myappointments/', views.myappointments, name='myappointments'),
]
