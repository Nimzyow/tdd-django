from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


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
    if request.method == "POST":
        new_item_text = request.POST["item_text"]
        # objects.create is a shorthand for creating a new item without the 
        # need to call save()
        Item.objects.create(text=new_item_text)
        return redirect("/lists/the-only-list-in-the-world")
    return render(request, "home.html")


def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})


def new_list(request: HttpRequest):
    Item.objects.create(text=request.POST["item_text"])
    return redirect("/lists/the-only-list-in-the-world/")
