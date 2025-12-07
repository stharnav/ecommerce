from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.


@login_required
def home(request):
    return render(request, 'dashboard.html')

def products_page(request):
    return render(request, 'products.html')

def dashboard_page(request):
    return render(request,'dashboard.html')

def order_page(request):
    return render(request,'order.html')

def user_page(request):
    return render(request,'users.html')

def settings_page(request):
    return render(request,'settings.html')

@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")

        user.first_name = name
        user.username = username
        user.email = email

        user.save()

        return redirect('settings')

    return render(request, "settings/edit_profile.html", {"user": user})


@login_required
def change_password(request):
    user = request.user

    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not user.check_password(old_password):
            messages.error(request, "Current password is incorrect.")
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect('change_password')

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Password updated successfully!")
        return redirect('change_password')

    return render(request, "settings/change_password.html")

def notification_settings(request):
    return render(request, "settings/notifications.html")

def privacy_settings(request):
    return render(request, "settings/privacy.html")

def system_preferences(request):
    return render(request, "settings/system_preferences.html")
