from django.shortcuts import render


# Create your views here.
def home_page(request):
    '''
    Instead of building our own HttpResponse, we now use the Django render
    function.  It takes the request as its first parameter (for reasons
    we'll go into later) and the name of the template to render.  Django
    will automatically search folders called templates inside any of
    your apps directories. Then it builds an HttpResponse for you, based
    on the content of the template.”
    '''
    return render(request, "home.html")
