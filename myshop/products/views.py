from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from .forms import SignupForm, NewItemForm, EditItemForm, LoginForm


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "products/index.html", {
        "products": products,
        "categories": categories,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:index")
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "products/signup.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or the desired URL after login
            return redirect("products:index")
    else:
        form = LoginForm()
    return render(request, "products/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("products:index")


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_sold=False)
    related_items = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)

    context = {
        "product": product,
        "related_items": related_items,
    }
    return render(request, "products/detail.html", context)


@login_required(login_url="products:login")
def delete(request, pk):
    product = Product.objects.get(created_by=request.user, pk=pk)
    product.delete()
    return redirect("products:index")


def new_item(request):
    form = NewItemForm()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("products:detail", pk=item.id)

    context = {
        "form": form,
        "title": "Add Item"
    }
    return render(request, "products/form.html", context)


def edit_item(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)

    form = EditItemForm(instance=item)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("products:detail", pk=item.id)

    context = {
        "form": form,
        "title": "Edit Item"
    }
    return render(request, "products/form.html", context)


def search(request):
    query = request.GET.get("query", "")
    items = Product.objects.filter(is_sold=False)

    if query:
        items = items.filter(name__icontains=query)

    context = {
        "query": query,
        "items": items,
    }
    return render(request, "products/search.html", context)
