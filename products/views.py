from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product

def home_view(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def granite_view(request):
    products = Product.objects.filter(category=1)
    return render(request, 'products/granite.html', {'products': products})

def porcelain_view(request):
    products = Product.objects.filter(category=2)
    return render(request, 'products/porcelain.html', {'products': products})

def stainless_view(request):
    products = Product.objects.filter(category=3)
    return render(request, 'products/stainless.html', {'products': products})

def contact_view(request):
    return render(request, 'products/contact.html')

def admin_login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        
        # التحقق من بيانات الأدمن
        user = authenticate(request, username=username_input, password=password_input)
        if user is not None and user.is_staff:
            login(request, user)
            # التوجيه الصحيح للوحة التحكم بالشرطة العادية
            return redirect('/my-admin/')
        else:
            error_message = 'اسم المستخدم أو كلمة المرور غير صحيحة، أو ليس لديك صلاحيات إدارية!'
            return render(request, 'products/login.html', {'error': error_message})
            
    return render(request, 'products/login.html')

# صفحة لوحة التحكم الرئيسية (عرض المنتجات)
@login_required(login_url='admin_login')
def custom_admin_dashboard(request):
    products = Product.objects.all()
    return render(request, 'products/admin_dashboard.html', {'products': products})

# صفحة إضافة منتج جديد
@login_required(login_url='admin_login')
def admin_add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        
        Product.objects.create(
            name=name, 
            description=description, 
            price=price, 
            image=image, 
            category=category
        )
        return redirect('admin_dashboard')
        
    return render(request, 'products/admin_add.html')

# صفحة حذف منتج
@login_required(login_url='admin_login')
def admin_delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('admin_dashboard')

# صفحة تعديل منتج
@login_required(login_url='admin_login')
def admin_edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.category = request.POST.get('category')
        
        # إذا تم رفع صورة جديدة، نقوم بتحديثها، وإلا نبقي القديمة
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
            
        product.save()
        return redirect('admin_dashboard')
        
    return render(request, 'products/admin_edit.html', {'product': product})