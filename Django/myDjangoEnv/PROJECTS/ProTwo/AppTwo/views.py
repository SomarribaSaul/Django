from django.shortcuts import render
from AppTwo.models import User   #Grab information from the model to show
# Create your views here.
from AppTwo.forms import NewUserForm  #Grab information from the form to save

def index(request): #HOMEPAGE
    return render(request, 'AppTwo/index.html')
#RETURNING INFORMATION FROM THE MODEL
# def users(request): #USERS PAGE VIEW
#     user_list= User.objects.order_by('first_name')
#     user_dict= {'users': user_list}
#     return render(request, 'AppTwo/users.html', context=user_dict)

def users(request):
    form= NewUserForm() #Instance

    if request.method == 'POST':    #If someone hits submit
        form= NewUserForm(request.POST)   #We pass that "request.POST" as argument

        if form.is_valid():    #And if is valid
            form.save(commit= True)  #We'll save that form using the save method
            return index(request)  #Then returns to HOMEPAGE
        else:
            print('ERROR FORM INVALID')
    return render(request, 'AppTwo/users.html', {'form': form})
