from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from homepage.settings import MEDIA_ROOT
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chinese_name = models.CharField(max_length=128,default='',verbose_name="中文名")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="头像")
    school = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="学校")
    street = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="街道地址")
    email = models.EmailField(default='',verbose_name="电子邮箱")
    phone = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="电话")
    qq = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="qq")
    wechat = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="微信")
    content = models.TextField(verbose_name="自我介绍",default='')
    class Meta:
        verbose_name = verbose_name_plural = "用户信息"
    def __str__(self):
        return self.user.username

    def exp(self,id):
        return experience.objects.filter(status=experience.STATUS_NORMAL).filter(owner=self.user)
    
    def education(self,id):
        return eduction.objects.filter(status=eduction.STATUS_NORMAL).filter(owner=self.user)
    
    def skills(self,id):
        return skills.objects.filter(status=skills.STATUS_NORMAL).filter(owner=self.user)
    
    def interests(self,id):
        return interests.objects.filter(status=interests.STATUS_NORMAL).filter(owner=self.user)

    def awards(self,id):
        return awards.objects.filter(status=awards.STATUS_NORMAL).filter(owner=self.user)
    
    def app(self,id):
        return app.objects.filter(status=app.STATUS_NORMAL).get(owner=self.user)
    """
    def info(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).get(info_catogory=Honor.STATUS_INFO)

    def desc(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).filter(info_catogory=Honor.STATUS_DESC)

    def honor(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).filter(info_catogory=Honor.STATUS_HONOR)"""


class experience(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=50,verbose_name="经历名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    title = models.CharField(max_length=200,verbose_name="子介绍名称")
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    owner = models.ForeignKey(User,verbose_name="经历属主",on_delete=models.CASCADE)
    content = models.TextField(verbose_name="经历介绍")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = "个人经历"
        
class eduction(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    school = models.CharField(max_length=100,verbose_name="学校名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    majer = models.CharField(max_length=100,verbose_name="专业")
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    owner = models.ForeignKey(User,verbose_name="经历属主",on_delete=models.CASCADE)
    gpa = models.FloatField(null=True, blank=True, default=None)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.school+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "教育经历"

class skills(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    skill = models.CharField(max_length=200,verbose_name="个人技能")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    program_language = models.CharField(null=True, blank=True,max_length=50,verbose_name="编程语言")
    skill_explain = models.CharField(null=True, blank=True,max_length=200,verbose_name="技能说明")
    owner = models.ForeignKey(User,verbose_name="技能属主",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.skill+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "技能介绍"

class interests(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    content = models.TextField(verbose_name="兴趣介绍")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="兴趣属主",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.content+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "兴趣介绍"

class awards(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=200,verbose_name="奖励或证书介绍")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="奖励属主",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.name+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "奖励或证书介绍"

class app(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    content = models.CharField(max_length=200,verbose_name="APP介绍")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="App图片")
    android_url = models.FileField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="安卓下载地址")
    ios_url = models.URLField(max_length=300,blank=True,null=True,default='',verbose_name="苹果下载地址")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="app属主",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    
    def features(self,id):
        return feature.objects.filter(status=feature.STATUS_NORMAL).filter(owner=self)

    def __str__(self):
        return self.content+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "App介绍"

class feature(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    ICON_ITEMS = (
        ("icon-screen-smartphone",'icon-screen-smartphone'),
        ("icon-camera",'icon-camera'),
        ("icon-present",'icon-present'),
        ("icon-lock-open",'icon-lock-open'),
    )
    name = models.CharField(max_length=200,verbose_name="特性名称")
    content = models.CharField(max_length=200,verbose_name="特性介绍")
    icon = models.CharField(max_length=200,default=ICON_ITEMS[0][0],choices=ICON_ITEMS,verbose_name="特性图标")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(app,verbose_name="APP特性属主",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = "App特性列表"