from django.shortcuts import render


def homepage(request):
    return render(request=request, template_name="homepage.html")
