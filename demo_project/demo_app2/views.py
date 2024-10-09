from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, "demo_app2/contact.html")
