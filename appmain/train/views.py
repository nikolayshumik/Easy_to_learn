from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import logout
from django.views.generic import TemplateView

from .models import Topic_to_learn, Tests_to_do


# Create your views here.
# Create your views here.LoginForm,

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def main_page(request):
    return render(request, 'main_page.html')

def theory_page(request):
    topics = Topic_to_learn.objects.all
    return render(request, 'theory_page.html', {'topics': topics})
def topic_page(request, topic_id):
    topic = Topic_to_learn.objects.get(id=topic_id)
    return render(request, 'topic_page.html', {'topic': topic})
def tusks_page(request):
    return render(request, 'tusks_page.html')
def test_page(request):
    tests = Tests_to_do.objects.all
    return render(request, 'test_page.html', {'tests': tests})
def test_chosen(request, test_id):
    test = Tests_to_do.objects.get(id=test_id)
    return render(request, 'test_chosen.html', {'test': test})
def formuls_page(request):
    return render(request, 'formuls_page.html')

def constants_page(request):
    return render(request, 'constants_page.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('dialog_display')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('dialog_display')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'