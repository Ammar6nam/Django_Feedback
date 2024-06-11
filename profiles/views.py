from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import profileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# def store_file(file):
#     with open ('temp/image.jpg' ,'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form=profileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form' : form
#         })

#     def post(self, request):
#         submitted_form=profileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             # store_file(request.FILES['image'])
#             profile=UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect('/profiles')
#         return render (request,'create_profile.html',{
#             'form':submitted_form
#         })    

class CreateProfileView(CreateView):
    template_name='profiles/create_profile.html'
    model=UserProfile
    fields='__all__'
    success_url='/profiles'


class ProfileView(ListView):
    model=UserProfile
    template_name='profiles/user_profiles.html'
    context_object_name='profiles'