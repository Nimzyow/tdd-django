from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List


# Create your views here.
def home_page(request: HttpRequest):
    '''
    Instead of building our own HttpResponse, we now use the Django render
    function.  It takes the request as its first parameter (for reasons
    we'll go into later) and the name of the template to render.  Django
    will automatically search folders called templates inside any of
    your apps directories. Then it builds an HttpResponse for you, based
    on the content of the template.”
    '''
    return render(request, "home.html")


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, "list.html", {"items": items})


def new_list(request: HttpRequest):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{ list_.id }")


def add_item(request: HttpRequest, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{ list_.id }")
