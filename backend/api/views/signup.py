from django.shortcuts import render, redirect
from ..forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "Thank you! Please wait for admin to appove your registration.")
            # return redirect("singup")
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})
