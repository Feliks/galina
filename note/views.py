from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from galina.note.models import Book, Events, Masters, Startstop
import datetime
from django.core.mail import send_mail
from galina.note.forms import ContactForm

def add_master(request):
    return render_to_response('add_master.html')

def add_master_results(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            x = Masters(master=q)
            x.save()
            master = Masters.objects.filter(master__icontains=q)
            return render_to_response('add_master_results.html',
                {'master': master, 'query': q})
    return render_to_response('add_master.html',
        {'errors': errors})

def del_master(request):
    return render_to_response('del_master.html')

def del_master_results(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            x = Masters(master=q)
            x.delete()
            master = Masters.objects.filter(master__icontains=q)
            return render_to_response('del_master_results.html',
                {'master': master, 'query': q})
    return render_to_response('del_master.html',
        {'errors': errors})

def events(request):
    events = Events.objects
    return render_to_response('events.html', {'events': events})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})

def del_master(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            x = Masters(master=q)
            x.delete()
            master = Masters.objects.filter(title__icontains=q)
            return render_to_response('del_master_results.html',
                {'master': master, 'query': q})
    return render_to_response('del_master.html',
        {'errors': errors})
'''
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
'''


def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})


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

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

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

Information About the URL: request.path, request.get_host(), request.get_full_path(), request.is_secure()
'''

# GOOD
def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})

















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
