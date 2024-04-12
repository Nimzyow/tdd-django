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

to collect static files in one place to upload to server/cdn

```bash
python manage.py collectstatic
```

to build Django image
```bash
docker build -t superlists .
```

To run Django in container
```bash
docker run -p 8888:8888 --mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 -e DJANGO_SECRET_KEY=sekrit -e DJANGO_ALLOWED_HOST=localhost -it superlists
```