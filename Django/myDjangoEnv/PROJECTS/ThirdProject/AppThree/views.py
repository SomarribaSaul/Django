from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'AppThree/index.html')

def form_name_view(request):
    form= forms.FormName()

    if request.method == 'POST':
        form= forms.FormName(request.POST)
#GRAB THE DATA THROUGH THE SUBMIT BUTTON AND PRINT IT IN THE CONSOLE
        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: " +form.cleaned_data['email'])
            print("TEXT: " +form.cleaned_data['text'])
    return render(request, 'AppThree/form_page.html', {'form': form})
