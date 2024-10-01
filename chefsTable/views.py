from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound('<h1> 404: not found yarram! </h1>')
