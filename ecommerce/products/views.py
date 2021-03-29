from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages




def add_to_cart(request):
 return render(request, 'pr/addtocart.html')

def checkout(request):
 return render(request, 'pr/checkout.html')

def customerregistration(request):
 return render(request, 'pr/customerregistration.html')

def home(request):
 return render(request, 'pr/home.html')

def orders(request):
 return render(request, 'pr/orders.html')

def product_detail(request):
 return render(request, 'pr/productdetail.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'pr/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'pr/customerregistration.html', {'form': form, 'active': 'btn-primary'})



def loginVew(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'pr/login.html', context)



def profile(request):
 return render(request, 'pr/profile.html')