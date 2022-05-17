from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def room(request):


    context = {}
    return render(request,template_name='main_room.html', context=context)