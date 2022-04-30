from django.contrib import admin
from .models import User, Patient, Consultant

# Register your models here.
admin.site.register((User, Patient, Consultant))

admin.site.site_header  =  "Your Friendd Adminstration"  
admin.site.site_title  =  "Your Friendd"
admin.site.index_title  =  "Your Friendd"