from django.shortcuts import render

# Create your views here.
def item_list(request):
    return render (request, 'shop/item_list.html')