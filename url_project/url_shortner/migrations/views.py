from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from url_shortner.models import Url_db
import random, string

# Create your views here.

#View that would process the form 
# Short URL is always prefixed with "http://tinyurl.com/"
def home(request):
    context_dict = {}
    if request.method == "POST":
        l_url = request.POST.get("url", '')
        if not (l_url == ''):
            short_id = Get_Unique_ID()
            l_url = clean_url(l_url)
            s_url = 'http://tinyurl.com/' + short_id
            url_object = Url_db(long_url=l_url, unique_id=short_id, short_url=s_url)
            url_object.save()
            context_dict['orignal_url'] = l_url
            context_dict['short_url'] = s_url
            return render(request, 'url_shortner/home.html', context_dict)
        else:
            context_dict['valid_url'] = 'No URL provided, Please enter valid URL'
            return render(request, 'url_shortner/home.html', context_dict)
    else:
        return render(request, 'url_shortner/home.html', context_dict)

# View to get orignal URL from shortned URL and redirect it to Orignal URL

def redirect_orignal(request):
    context_dict = {}
    if request.method == "POST":
        s_url = request.POST.get("short_url", '')
        start_index = s_url.find('http://tinyurl.com/') + 19
        short_id = s_url[start_index:]
        print short_id
        l_url = Url_db.objects.get(unique_id=short_id)
        print l_url.long_url
        return redirect(l_url.long_url)

# View to clean the URL field. It will attach http:// or https:// if missing
def clean_url(long_url):
    if long_url and not (long_url.startswith('http://') or long_url.startswith('https://')):
        long_url = 'http://' + long_url
    return long_url

# View to generate a 6 digit unique id for the long URL provided
def Get_Unique_ID():
    flag=True
    while flag:
        short_id=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        try:
            Url_db.objects.get(unique_id=short_id)
        except Url_db.DoesNotExist:
            flag = False
    return short_id

def cover_page(request):
    context_dict = {'homepage': "Let's get it on !"}
    return render(request, 'url_shortner/cover_page.html', context_dict)
