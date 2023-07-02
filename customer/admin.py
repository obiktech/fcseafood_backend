from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Customer, OTP

@admin.register(Customer)
class CustomerModel(admin.ModelAdmin):
    pass


@admin.register(OTP)
class ManageOtp(admin.ModelAdmin):
    pass