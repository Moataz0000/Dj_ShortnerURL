from django.shortcuts import render , redirect, get_object_or_404
import uuid
from .models import Url
from django.http import HttpResponse,Http404

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link'] # get text form the input user form
        uid = str(uuid.uuid4())[:5] # create uuid for ever link to get it and shortner
        new_url = Url(link=link ,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    else:
        return Http404()
    


def go(request, pk):
    url_details = get_object_or_404(Url, uuid=pk)
    return redirect(url_details.link)
    
