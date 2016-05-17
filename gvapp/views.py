from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html = "<html><body>Good Vampires Home</body></html>"
    return HttpResponse(html)
