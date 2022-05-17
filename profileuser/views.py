from django.shortcuts import render, redirect
from profileuser.models import *
from django.contrib.auth.decorators import login_required
from .forms import *



@login_required
def profile(request):

    your_profile = Profile.objects.get(user=request.user)


    context = {'profile':your_profile}
    return  render(request,'profiles/profile.html',context)

@login_required
def edit_profile(request):
    instance = Profile.objects.get(user=request.user)
    data = {'real_name': instance.real_name, 'surname': instance.surname,'bio': instance.bio,'main_photo':instance.main_photo}

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=instance , initial=data)
        if profile_form.is_valid():
            print(1)
            profile_form.save()
            return redirect('profile')
        else:
            print(profile_form.errors)
            return redirect('profile_edit')


    profile_form = ProfileForm(instance=request.user,initial=data)
    context = {'profile_form': profile_form}
    return render(request, 'profiles/edit_profile.html', context)