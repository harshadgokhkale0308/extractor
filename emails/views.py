from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import HttpResponse
import win32com.client
import os
import re
import pythoncom


# Create your views here.
def output(request):
    pythoncom.CoInitialize()
   
    emails=[]
    return_str=""
    if request.method == 'POST':
        print("here under post")
        files = request.FILES.getlist('file')
        print(files)
        for f1 in request.FILES.getlist('file'):
            
            #  Saving POST'ed file to storage
            file = f1
            file_name = default_storage.save(file.name, file)


        for fl in request.FILES.getlist('file'):
            # file = default_storage.open('1.msg', 'r') 
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")    
            msg = outlook.OpenSharedItem(default_storage.open('1.msg', 'r') )
            message_body = msg.Body
            lst = re.findall('\S+@\S+', str(message_body))
            print("email->" + str(lst))
            emails.append(lst)
        for email in emails:
            return_str += '<br>' + email
            
        return HttpResponse('<h1>'+ return_str + '</h1>')
def index(request):
    return render(request,'emails/emails.html')