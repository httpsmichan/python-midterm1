from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':  # HTTP Method
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Validation
            form.save()  # Creation
            return redirect('login')  # Redirect after creation
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})  # Response
