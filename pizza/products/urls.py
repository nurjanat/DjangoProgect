from django.urls import path
from .views import homepage,AboutUs_page,Contacts_page

urlpatterns = [
    path('products/',homepage),
    path('about_us/',AboutUs_page),
    path('contacts/',Contacts_page)
]

