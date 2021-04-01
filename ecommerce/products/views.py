from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from .models import Product, Cart




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

class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'pr/productdetail.html', {'product': product,'totalitem': totalitem})
        





class ProductView(View):
    def get(self, request):
        totalitem = 0
        Bh = Product.objects.filter(category="BS")
        GT = Product.objects.filter(category="G")
        LD = Product.objects.filter(category="L")
        CM = Product.objects.filter(category="C")
        Pant= Product.objects.filter(category="P")
        Ss= Product.objects.filter(category="T")
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'pr/home.html', { 'LD': LD,'GT': GT,'CM': CM ,'Bh':Bh,'Pant':Pant,'Ss':Ss,'totalitem': totalitem})







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









def Shirts(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        Ss = Product.objects.filter(category='W')
    elif data == 'Long_Tshirt' or data == 'Crop_Tshirt':
        Ss = Product.objects.filter(category='W').filter(Manufacturer=data)
    elif data == 'Below':
        Ss = Product.objects.filter(
            category='W').filter(Selling_Price__lt=10000)
    elif data == 'Above':
        Ss = Product.objects.filter(
            category='W').filter(Selling_Price__gt=10000)
    return render(request, 'pr/T-Shirts.html', {'Ss': Ss, 'totalitem': totalitem})




def Gnts(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        GT = Product.objects.filter(category='G')
    elif data == 'Goldstar' or data == 'Nike':
        GT = Product.objects.filter(category='G').filter(Manufacturer=data)
    elif data == 'Below':
        GT = Product.objects.filter(
            category='G').filter(Selling_Price__lt=10000)
    elif data == 'Above':
        GT = Product.objects.filter(
            category='G').filter(Selling_Price__gt=10000)
    return render(request, 'pr/Gents.html', {'GT': GT, 'totalitem': totalitem})



def Ldes(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        LD = Product.objects.filter(category='L')
    elif data == 'Goldstar' or data == 'Nike':
        LD = Product.objects.filter(category='L').filter(Manufacturer=data)
    elif data == 'Below':
        LD = Product.objects.filter(
            category='L').filter(Selling_Price__lt=10000)
    elif data == 'Above':
        LD = Product.objects.filter(
            category='L').filter(Selling_Price__gt=10000)
    return render(request, 'pr/Ladies.html', {'LD': LD, 'totalitem': totalitem})



def Brs(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        Bh = Product.objects.filter(category='BS')
    elif data == 'Goldstar' or data == 'Nike':
        Bh = Product.objects.filter(category='BS').filter(Manufacturer=data)
    elif data == 'Below':
        Bh = Product.objects.filter(
            category='BS').filter(Selling_Price__lt=10000)
    elif data == 'Above':
        Bh = Product.objects.filter(
            category='BS').filter(Selling_Price__gt=10000)
    return render(request, 'pr/Brush.html', {'Bh': Bh, 'totalitem': totalitem})



def Crm(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        CM = Product.objects.filter(category='C')
    elif data == 'Goldstar' or data == 'Nike':
        CM = Product.objects.filter(category='C').filter(Manufacturer=data)
    elif data == 'Below':
        CM = Product.objects.filter(
            category='C').filter(Selling_Price__lt=10000)
    elif data == 'Above':
        CM = Product.objects.filter(
            category='C').filter(Selling_Price__gt=10000)
    return render(request, 'pr/Cream.html', {'CM': CM, 'totalitem': totalitem})



def Pan(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        Pant = Product.objects.filter(category='P')
    elif data == 'Levis' or data == 'Adidas':
        Pant = Product.objects.filter(category='P').filter(Manufacturer=data)
    elif data == 'Below':
        Pant = Product.objects.filter(
            category='P').filter(Selling_Price__lt=3000)
    elif data == 'Above':
        Pant = Product.objects.filter(
            category='P').filter(Selling_Price__gt=3000)
    return render(request, 'pr/Pants.html', {'Pant': Pant, 'totalitem': totalitem})