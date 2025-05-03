from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Nicky\nElmira"
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {"news": [
        "RiffMates now has a new page!",
        "RiffMates has its first page"
    ]}
    return render (request, "news.html", data)
