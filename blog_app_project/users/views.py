from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')  # redirecting to url pattern in blog home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # to access the form in the template(register.html), we pass it as context
