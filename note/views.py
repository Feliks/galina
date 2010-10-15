from django.http import HttpResponse
from django.shortcuts import render_to_response
from galina.note.models import Book
import datetime

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def search_form(request):
    return render_to_response('search_form.html')
'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('note.html', {'current_date': now})

def hello(request):
    return HttpResponse("Hello world")

def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

'''
# BAD!
def current_url_view_bad(request):
    return HttpResponse("Welcome to the page at /current/")

# GOOD
def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

'''
'''
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('note.html', {'current_date': now})
'''
'''
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('note.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''
