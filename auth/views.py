from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views import View


def home(request):
    return render(
        request,
        'home.html'
    )


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home.html')

        return render(request, 'signup.html', {'form': form})
