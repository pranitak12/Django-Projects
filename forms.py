from django import forms
from .models import service,service_booking,car,car_details,team,reviews 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class services(forms.ModelForm):
    class Meta():
        model = service
        fields = '__all__'

class book_service(forms.ModelForm):
    class Meta():
        model = service_booking
        fields = '__all__'

class teams(forms.ModelForm):
    class Meta():
        model = team
        fields = '__all__'

class review(forms.ModelForm):
    class Meta():
        model = reviews
        fields = '__all__'

class cars(forms.ModelForm):
    class Meta():
        model = car
        fields = '__all__'

class car_info(forms.ModelForm):
    class Meta():
        model = car_details
        fields = '__all__'

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ("username","email","password1","password2")