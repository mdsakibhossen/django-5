from django.shortcuts import render

# Create your views here.


def home(request):
    page_info = {"name": "Home"}
    return render(request, "demo_app/home.html", context=page_info)


def about(request):
    page_info = {"name": "About"}
    return render(request, "demo_app/about.html", context=page_info)
