from django.urls import path, include
from .views import home,delete_confirmation,delete_message,ADMIN_contact,create_insurance_company



urlpatterns = [
   
   path('', home, name="home"),
   path('contactADMIN/', ADMIN_contact, name="ContactH"),
   path('delete/confirm/<int:message_id>/', delete_confirmation, name='delete_confirmation'),
   path('delete/<int:message_id>/', delete_message, name='delete_message'),
   path('create/', create_insurance_company, name='create_insurance_company'),
 
 
  

]
