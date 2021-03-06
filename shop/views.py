from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list_view(request,  category_slug=None):
    category=None
    categories=Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category':category, 'categories': categories, 'products':products})


def product_detail_view(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    try:
        related = Product.objects.filter(category=product.category).exclude(id=product.id)
    except Product.DoesNotExist:
        pass
    cart_product_form = CartAddProductForm()
    context = {'product':product,'cart_product_form':cart_product_form, 'related':related}
    return render(request, 'shop/product/detail.html',context)
