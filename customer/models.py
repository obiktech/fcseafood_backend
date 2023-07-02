from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    fullname = models.CharField(max_length=150, default="Guest")
    usertype = models.CharField(max_length=30,default="customer")
    is_active = models.BooleanField(default=False)
    sessionkey = models.CharField(max_length=256, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.phone

class Pincode(models.Model):
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.pincode
    

class OTP(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    otp = models.CharField(max_length=6)
    sessionkey = models.CharField(max_length=90)


    def __str__(self) :
        return self.phone

class Saved_Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200, default=" ")
    pincode = models.ForeignKey(Pincode, on_delete=models.DO_NOTHING)
