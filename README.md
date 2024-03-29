Start a Django project example:

```
django-admin.py startproject superlists
```

To start an app

```
python manage.py startapp lists
```

Django’s main job is to
decide what to do when a user asks for a particular URL on our site.
Django’s workflow goes something like this:


An HTTP request comes in for a particular URL.


Django uses some rules to decide which view function should deal with
the request (this is referred to as resolving the URL).


The view function processes the request and returns an HTTP response.”

Excerpt From
Test-Driven Development with Python
Harry J.W. Percival
This material may be protected by copyright.