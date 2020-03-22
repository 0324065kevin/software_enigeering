from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import Message
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User



def list(request):
    messages = Message.objects.all()
    print(messages)
    return render(request, 'web/message_list.html', locals())

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        print(content)
        message = Message.objects.create(user=request.user, content=content)
        print(request.user)
        message.save()
        messages = Message.objects.all()
        return render(request,'web/message_list.html',locals())
    return render(request, 'web/form.html', locals())

def edit(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        content = request.POST.get('content')
        print(content)
        message.content = content
        message.save()
        messages = Message.objects.all()
        return render(request,'web/message_list.html',locals())
    return render(request, 'web/message_edit.html', locals())

def delete(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()
    messages = Message.objects.all()
    return render(request,'web/message_list.html',locals())
    # return render(request, 'Comment/message_list.html', locals())


