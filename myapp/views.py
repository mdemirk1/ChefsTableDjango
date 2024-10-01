from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# each view func. takes a request object.
# model handels html request and responses.
def index(request):
    content = "<html><body><h1>Welcome to my first django app!</h1></body></html>"
    return HttpResponse(content)   

def menuItems(request, dish):
    items = {
        'pasta' : 'Delicious italian stlye pasta',
        'falafel' : 'Famous plant based falafel balls',
        'cheesecake' : 'Creamy and sugary dessert for the sugar crisis'
    }
    
    description = items[dish] 
    response = HttpResponse(f'<h2>{dish}</h2>' + description)
    
    return response