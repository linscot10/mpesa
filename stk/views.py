from django.shortcuts import render
from .forms import PaymentForm

# Create your views here.
def payment_view(request):
    form=paymentForm()
    return render(request,"payment_form.html",{"form":form})