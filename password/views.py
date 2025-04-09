from django.shortcuts import render
import random
import string
from django.http import JsonResponse

# Create your views here.

def password_generator(length):
  if length < 4:                                                                                                                                            
    return {"error": "Password length should be at least 4."}
  
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  digits = string.digits
  special = string.punctuation

  password = [
      random.choice(lower),
      random.choice(upper),
      random.choice(special),
      random.choice(digits)
  ]
  all_characters = lower + upper + digits + special
  password += random.choices(all_characters, k=length - 4)
  random.shuffle(password)
  return {"password": ''.join(password)}

def generate_password(request):
    try:
        length = int(request.GET.get('length', 12))  # Default to 12 if not given
        result = password_generator(length)
        return JsonResponse(result)
    except ValueError:
        return JsonResponse({"error": "Invalid length value."})
    

def home(request):
   return render(request, "password/index.html")

def about(request):
   return render(request, "password/about.html")