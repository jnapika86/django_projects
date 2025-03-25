from django.shortcuts import render  
from .models import Product  
def product_list(request):  
    if not Product.objects.exists():  
        Product.objects.create(name='Smasung z flip', description='Smartphone with an Pro features',  price='861')  
        Product.objects.create(name='Nike Airforce', description='Stylish and comfortable sneakers',  price='885')  
        Product.objects.create(name='adidas Ultraboost', description='Premium running shoes',  price='793')  
        Product.objects.create(name='Macbook', description='High-end laptop for productivity', price='500')  
        Product.objects.create(name='Lenovo', description='Powerful laptop with Intel processor',  price='200')  
    products = Product.objects.all()  
    return render(request, 'products.html', {'products': products})
