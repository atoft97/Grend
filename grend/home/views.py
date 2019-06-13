from django.shortcuts import render

# Create your views here.

def HomeView(request):
	return render(request, "home/home.html")


def PriceView(request):
	return render(request, "home/prices.html")

def ContactInfoView(request):
	return render(request, "home/contact_info.html")
