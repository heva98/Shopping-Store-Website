from django.shortcuts import render
from .models import FeatureProduct
from .models import LatestProduct

# Create your views here.

def indexfeature(request):

    featureproducts = FeatureProduct.objects.all()
    
    return render(request, "index.html", {'featureproducts': featureproducts})

def indexlatest(request):

    latestproducts = LatestProduct.objects.all()
    
    return render(request, "index.html", {'latestproducts': latestproducts})


