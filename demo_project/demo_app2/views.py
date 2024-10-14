from django.shortcuts import render

# Create your views here.


def contact(request):
    page_info = {"name": "Contact"}
    return render(request, "demo_app2/contact.html", context=page_info)
