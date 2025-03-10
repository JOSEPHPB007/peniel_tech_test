from django.shortcuts import redirect, render
from .forms import MemberForm, ProductForm
from .models import Members, Product
from django.shortcuts import render
from django.http import JsonResponse
# from .models import Members, Product

def create_item(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        product_form = ProductForm(request.POST)
        
        if member_form.is_valid() and product_form.is_valid():
            member_form.save()
            product_form.save()
            return redirect('list_item')  # Redirect after saving

    else:
        member_form = MemberForm()
        product_form = ProductForm()
    
    return render(request, 'add.html', {'member_form': member_form, 'product_form': product_form})

def list_item(request):
    members = Members.objects.all()
    products = Product.objects.all()
    return render(request, 'show.html', {'members': members, 'products': products})

def invoice(request):
    members = Members.objects.all()
    products = Product.objects.all()
    return render(request, 'invoice.html', {'members': members, 'products': products})

def calculate_discount(request):
    if request.method == "GET":
        member_id = request.GET.get('member_id')
        product_id = request.GET.get('product_id')

        if member_id and product_id:
            try:
                member = Members.objects.get(id=member_id)
                product = Product.objects.get(id=product_id)

                discount_amount = (product.price * member.discount) / 100
                final_price = product.price - discount_amount

                data = {
                    'product_name': product.productname,
                    'original_price': float(product.price),
                    'discount_percentage': float(member.discount),
                    'discounted_price': float(final_price),
                }
                return JsonResponse(data)

            except Members.DoesNotExist or Product.DoesNotExist:
                return JsonResponse({'error': 'Invalid Member or Product'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
