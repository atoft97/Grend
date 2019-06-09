from django.shortcuts import render

# Create your views here.

def HomeView(request):
	return render(request, "home/home.html")


def PriceView(request):
	hei = "hei"
	return render(request, "home/prices.html")