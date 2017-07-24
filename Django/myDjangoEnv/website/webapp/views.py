from django.shortcuts import render
from webapp.forms import NewUserForm

# Create your views here.
def index(request): #HOMEPAGE
    return render(request, 'webapp/index.html')

def users(request):
    form= NewUserForm() #Instance

    if request.method == 'POST':    #If someone hits submit
        form= NewUserForm(request.POST)   #We pass that "request.POST" as argument

        if form.is_valid():    #And if is valid
            form.save(commit= True)  #We'll save that form using the save method
            return index(request)  #Then returns to HOMEPAGE
        else:
            print('ERROR FORM INVALID')
    return render(request, 'webapp/users.html', {'form': form})
