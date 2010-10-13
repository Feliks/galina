from django.http import HttpResponse

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
