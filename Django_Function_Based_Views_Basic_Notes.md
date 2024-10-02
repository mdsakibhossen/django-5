# Django Function-Based Views (FBVs) Notes

## 1. What are Function-Based Views?

Function-Based Views (FBVs) in Django are views that are implemented as Python functions. Each FBV receives an `HttpRequest` object and returns an `HttpResponse` object. FBVs are more straightforward and easier to write for simple logic.

## 2. Basic Structure of a Function-Based View

A typical FBV takes a request object and returns a response:

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('Hello, World!')
```

## 3. Returning a Template Response

FBVs are commonly used with Django’s templating system. You can use render() to return a template:

```python
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html')
```
