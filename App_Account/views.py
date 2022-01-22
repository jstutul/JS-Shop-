from django.shortcuts import render


# Create your views here.

# Signup view function

def SignupView(request):
    return render(request, 'App_Account/sign-up.html')
