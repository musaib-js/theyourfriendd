from django.contrib import admin
from .models import User, Patient, Consultant, Subscription_Packs, Subscribed_Users

# Register your models here.
admin.site.register((User, Patient, Consultant, Subscription_Packs, Subscribed_Users))

admin.site.site_header  =  "Your Friendd Adminstration"  
admin.site.site_title  =  "Your Friendd"
admin.site.index_title  =  "Your Friendd"