from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('note.html', {'current_date': now})

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
