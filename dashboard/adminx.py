import xadmin
from .models import UserProfile,experience,eduction,skills,interests,awards,app,feature

class BaseAdmin(object):
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs

@xadmin.sites.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('chinese_name','street','email','phone')

@xadmin.sites.register(experience)
class experienceAdmin(BaseAdmin):
    list_display = ('name','title','start_time','end_time')

@xadmin.sites.register(eduction)
class eductionAdmin(BaseAdmin):
    list_display = ('school','majer','start_time','end_time')

@xadmin.sites.register(skills)
class skillsAdmin(BaseAdmin):
    list_display = ('skill','program_language',)

@xadmin.sites.register(interests)
class interestsAdmin(BaseAdmin):
    list_display = ('content','status')

@xadmin.sites.register(awards)
class awardsAdmin(BaseAdmin):
    list_display = ('name','status','owner')
@xadmin.sites.register(app)
class appAdmin(BaseAdmin):
    list_display = ('content','owner','created_time')

@xadmin.sites.register(feature)
class featureAdmin(BaseAdmin):
    list_display = ('name','content','owner')