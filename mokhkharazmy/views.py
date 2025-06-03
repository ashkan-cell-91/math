from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from django.contrib.auth import login
from .forms import RegisterForm
from django.http import JsonResponse


# داده‌های نمونه برای جستجو
data = {
    "python": ["آموزش مقدماتی Python", "بهترین کتاب‌های Python", "فریم‌ورک Django و Python"],
    "javascript": ["ES6 و ویژگی‌های جدید JavaScript", "آموزش React.js", "Node.js و توسعه سمت سرور"],
    "html": ["راهنمای کامل HTML5", "بهترین تمرین‌های طراحی وب", "CSS و طراحی پیشرفته"]
}

def search_data(request):
    if request.method == 'GET':
        query = request.GET.get('q', '').lower()
        results = data.get(query, ["نتیجه‌ای یافت نشد!"])
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'query': query, 'results': results})
        
        return render(request, 'detector/search_data.html', {'results': results, 'query': query})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def home(request):
    all_products = Product.objects.all()
    return render(request, 'detector/index.html', {'products': all_products})

def calculate_shape(request):
    return render(request, 'detector/calculate_shape.html')

def calculater(request):
    return render(request, 'detector/calculater.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "ثبت نام با موفقیت انجام شد!")
            return redirect('home')
        else:
            messages.error(request, "لطفاً خطاهای فرم را اصلاح کنید.")
    else:
        form = RegisterForm()
    
    return render(request, 'detector/register.html', {'form': form})
