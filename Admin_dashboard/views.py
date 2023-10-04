from django.shortcuts import render, redirect,get_object_or_404
from Job_app.models import ContactMessage
from .models import InsuranceCompany
from django.http import HttpResponseRedirect

def create_insurance_company(request):
    context = {'companies': []}  # Initialize context with an empty list
    
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        insurable_cars = request.POST['insurable_cars']
        non_insurable_cars = request.POST['non_insurable_cars']
        
        company = InsuranceCompany(
            name=name,
            image=image,
            description=description,
            insurable_cars=insurable_cars,
            non_insurable_cars=non_insurable_cars
        )
        company.save()
    
    companies = InsuranceCompany.objects.all()
    context['companies'] = companies  # Update the 'companies' key in the context
    return render(request, 'insure.html', context)

    

# Create your views here.
def home(request):
    
    contact_messages = ContactMessage.objects.all()
    return render(request, 'index.html', {'contact_messages': contact_messages})
def ADMIN_contact(request):
    
    
    return render(request, 'contactMH.html', )



def delete_confirmation(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    context = {
        'message': message,
    }
    return render(request, 'delete.html', context)
def delete_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.delete()
    return redirect('home')
    