from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .decorators import patient_required, consultant_required
from .forms import PatientSignUpForm, ConsultantSignUpForm, PatientForm, ConsultantForm
from .models import Patient, Subscription_Packs, User ,Subscribed_Users, Consultant
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from home.forms import AppointmentForm
from home.models import Appointment


class SignUpView(TemplateView):
    template_name = 'signup.html'

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'patientsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('/auth/patientprofile')

class ConsultantSignUpView(CreateView):
    model = User
    form_class = ConsultantSignUpForm
    template_name = 'doctorsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'consultant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('/auth/consultantprofile')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            if user.is_patient:
                return redirect('/')
            elif user.is_consultant:
                return redirect('/auth/doctordashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

def patientupdate(request):
    user = request.user
    profile = Patient.objects.filter(user = user).first()
    userlogged = Patient.objects.filter(user = user).first()
    form = PatientForm(request.POST, instance = userlogged) 
    context = {'profile':profile, 'form':form}
    if form.is_valid():  
        form.save()  
        messages.success(request, "Details Updated Successfully")
        return redirect('/auth/selectsubscription')  
    else:
         messages.error(request, "Fill the form correctly")
    return render(request, 'patientprofile.html', context)  

def consultantupdate(request):
    user = request.user
    profile = Consultant.objects.filter(user = user).first()
    userlogged = Consultant.objects.filter(user = user).first()
    form = ConsultantForm(request.POST, instance = userlogged) 
    context = {'profile':profile, 'form':form} 
    if form.is_valid():  
        form.save()  
        messages.success(request, "Details Updated Successfully")
        return redirect('/auth/doctordashboard')  
    else:
         messages.error(request, "Fill the form correctly")
    return render(request, 'consultantprofile.html', context)  

@login_required
def doctordashboard(request):
    if request.user.is_authenticated:
        if request.user.is_consultant:
            consultant = Consultant.objects.filter(user = request.user).first()
            appointment = Appointment.objects.filter(doctor = consultant)
            context = {'consultant':consultant, 'appointment':appointment}
            return render(request, 'doctordashboard.html', context)
        return redirect('/')

def bookappointment(request, pk):
    user = request.user
    doctor = Consultant.objects.filter(pk = pk).first()
    # try:
    #     if user in Subscribed_Users:
    #         return redirect('/')
    # except:
    form = AppointmentForm(request.POST) 
    context = {'form':form} 
    if form.is_valid():  
        form.save()  
        messages.success(request, "Appointment Booked Successfully")
        return redirect('/')  
    else:
         messages.error(request, "Fill the form correctly")
    return render(request, 'bookappointment.html', context)  

def doctors(request):
    consultant = Consultant.objects.all()
    context = {'consultant':consultant}
    return render(request, 'doctors.html', context)

def doctorr(request, pk):
    doctor = Consultant.objects.filter(pk = pk).first()
    context = {'doctor':doctor}
    return render(request, 'doctor.html', context)

def meditation(request):
    return render(request, 'meditation.html')
    
def coping(request):
    return render(request, 'coping.html')

def selectsubscription(request):
    subscription = Subscription_Packs.objects.all()
    context = {'subscription': subscription}
    return render(request, 'subscription.html', context)

def subscribe(request, name):
    user  = request.user
    pack = Subscription_Packs.objects.filter(name = name).first()
    newsubscribeduser = Subscribed_Users(user = user, subscription_type = pack)
    newsubscribeduser.save()
    messages.success(request, "You've succesfully subscribed")
    return redirect('/')

def myappointments(request):
    user = request.user
    print(user)
    patient = Patient.objects.filter(user = user).first()
    print(patient)
    name = patient.name
    userappointments = Appointment.objects.filter(name = name)
    context = {'userapp': userappointments}
    return render(request, 'myappointments.html', context)