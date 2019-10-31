from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import DetailView,ListView
from . models import UserProfile,app
# Create your views here.
from django.http import HttpResponse


class UserView(TemplateView):
    model = UserProfile
    template_name = 'dashboard/personalIntro.html'
    def get(self,request,*args,**kwargs):
        user_id = self.kwargs.get('user_id')
        user = UserProfile.objects.get(pk=user_id)
        context = {
            'user': user,
            "exp": user.exp(user.user.id),
            "education": user.education(user.user.id),
            "skills": user.skills(user.user.id),
            "interests": user.interests(user.user.id),
            "awards": user.awards(user.user.id),
        }
        return self.render_to_response(context)

class AppView(TemplateView):
    model = app
    template_name = 'dashboard/appIntro.html'
    def get(self,request,*args,**kwargs):
        user_id = self.kwargs.get('user_id')
        user = UserProfile.objects.get(pk=user_id)
        app = user.app(user.user.id)
        context = {
            'user':user,
            'app':app,
            'features':app.features(app.id)
        }
        return self.render_to_response(context)