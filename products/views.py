from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product


from .models import Product, Category

@login_required
def product_list(request):
    products = Product.objects.select_related("category").all()
    categories = Category.objects.all()

    query = request.GET.get("q")

    if query:
        products = products.filter(name__icontains=query)

    context = {
        "products": products,
        "categories": categories,
        "query": query,
    }

    return render(
        request,
        "products/product_list.html",
        context,
    )


@login_required
def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(pk=pk)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "products/product_detail.html",
        context,
    )