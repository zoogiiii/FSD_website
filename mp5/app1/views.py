from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Granite
from .models import ContactMessage  
import json

def home(request):
    granites = Granite.objects.all()
    return render(request, 'app1/home.html', {'granites': granites})

def about(request):
    return render(request, 'app1/about.html')

@csrf_exempt  # Temporarily exempt CSRF protection for form testing
def contact(request):
    if request.method == 'POST':
        try:
            # Get POST data (form submission)
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Validation: Ensure required fields are filled
            if not name or not email or not message:
                return JsonResponse({'success': False, 'message': 'All fields are required!'})

            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()

            return JsonResponse({'success': True, 'message': 'Thank you for contacting us!'})
        except Exception as e:
            # Debugging line to log the error
            print("Error while saving contact form data:", str(e))
            return JsonResponse({'success': False, 'message': 'Something went wrong!'})

    
    return render(request, 'app1/contact.html')
