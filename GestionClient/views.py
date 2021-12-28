from django.http import request
from django.shortcuts import render
from .models import ClientModel

def index (request):
    client_form = ClientModel ()

    if request.mothod == "POST": 
       form = client_form (request.POST)
       if form.isvalid ():
           newclient=form.save()
           context = {'client',newclient}
    
    return render(request,'CLTform.html',{'client_form': client_form})