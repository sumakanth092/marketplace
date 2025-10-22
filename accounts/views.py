from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def seller_dashboard(request):
    return render(request, 'accounts/seller_dashboard.html')

@login_required
def customer_dashboard(request):
    return render(request, 'accounts/customer_dashboard.html')
