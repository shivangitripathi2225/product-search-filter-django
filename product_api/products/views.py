from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = Product.objects.all()

    # Query params
    search = request.GET.get('search')
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    page = request.GET.get('page', 1)

    # Validate page
    try:
        page = int(page)
        if page < 1:
            return JsonResponse({"error": "Page must be >= 1"}, status=400)
    except ValueError:
        return JsonResponse({"error": "Invalid page value"}, status=400)

    page_size = 3

    # Filters
    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category__iexact=category)

    # Validate + apply sorting
    if sort:
        if sort == 'asc':
            products = products.order_by('price')
        elif sort == 'desc':
            products = products.order_by('-price')
        else:
            return JsonResponse(
                {"error": "Invalid sort value. Use 'asc' or 'desc'"},
                status=400
            )

    total = products.count()

    # Pagination
    start = (page - 1) * page_size
    end = start + page_size

    products = products[start:end]

    # Serialize
    data = [
        {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
        }
        for product in products
    ]

    response = {
        "products": data,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size
    }

    return JsonResponse(response)


def index(request):
    return render(request, 'index.html')