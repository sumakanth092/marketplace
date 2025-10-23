from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
def profile_redirect(request):
    user = request.user
    if hasattr(user, 'is_seller') and user.is_seller:
        return redirect('seller_dashboard')
    else:
        return redirect('customer_dashboard')
