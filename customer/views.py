from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import OTP, Customer
import random
from hashlib import md5
def sessionkeygen(data):
    data = data+str(random.randint(1000,10000))
    hash = md5(bytes(data, "utf-8")).hexdigest()
    return hash


def generateotp(phone, sessionkey):
    otp = str(random.randint(1000,9999))
    otpobj = OTP.objects.filter(phone=phone)
    # print(OTP.objects.all())
    print(len(otpobj))
    if(len(otpobj) ==0):
        print("craete")
        otpobj = OTP(phone=phone, otp=otp, sessionkey=sessionkey)
        otpobj.save()
        return 0
    else:
        print("update")
        otpobj = otpobj.first()
        otpobj.otp= otp
        otpobj.sessionkey=sessionkey
        otpobj.save()
        return 0
    

def verify_otp(phone,otp, sessionkey):
    otpobj = OTP.objects.filter(phone=phone, sessionkey=sessionkey)
    # print(OTP.objects.all())
    print(otpobj)
    
    if(len(otpobj) ==0):
        
        return 2
    else:
        
        otpobj = otpobj.first()
        print(otp)
        if otpobj.otp == otp:
            customer = Customer.objects.filter(phone=phone)
            if(len(customer) ==0):
                cust = Customer(phone=phone, sessionkey=sessionkeygen(phone))
                cust.save()
                return cust.sessionkey
                
            elif customer.first().is_active:
                customer.first().sessionkey =sessionkeygen(phone)
                customer.first().save()
                return customer.first().sessionkey
            else:
                return 4
        else:
            return 1
        
@api_view(["POST"])
def getotp(r):
    try:

        data = r.data
        phone = data["phone"]
        sessionkey = data["sessionkey"]
        print(len(phone))
        if len(phone) != 10:
            return Response({"status":2})
        else:
            status = generateotp(phone=phone, sessionkey=sessionkey)
            return Response({"status":status})
    except Exception as e:
        print(e)
        return Response({"status":2})

@api_view(["POST"])
def verifyotp(r):
    try:

        data = r.data
        phone = data["phone"]
        otp=data["otp"]
        sessionkey = data["sessionkey"]
        print(len(phone))
        if len(phone) != 10:
            return Response({"status":2})
        else:
            status = verify_otp(phone=phone,otp=otp, sessionkey=sessionkey)
            if(type(status) == type("")):
                print(status)
                return Response({"status":0, "token":status})
            return Response({"status":status})
    except Exception as e:
        print(e)
        return Response({"status":2})
    

def checkotp(r):
    if r.method=="POST":
        phone =r.POST["phone"]
        otp = otpobj = OTP.objects.filter(phone=phone)
        if(len(otp) >0):
            otp = otp.first()

            return render(r, "checkotp.html", {"otp":otp.otp})
        else:
            return render(r, "checkotp.html", {"otp":""})
    
    else:
        return render(r, "checkotp.html", {"otp":""})