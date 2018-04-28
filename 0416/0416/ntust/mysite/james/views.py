from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Name, Birthday, Gender

# Create your views here.

def index(request):

	names = Name.objects.all()
	return render_to_response('james/menu.html',locals())