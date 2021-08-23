from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')           #1대1 매칭. 프로필과 유저객체를 User에 연결하고,
    #on_delete=models.CASCADE는 연결된 User객체가 없어질때 어떻게 할 것인가를 담당 => 유저가 탈퇴하면 사라짐  #request.user.profile.nickname처럼 바로 접근해서 데이터를 받아올 수 있다.

    image = models.ImageField(upload_to='profile/', null=True)
    #upload_to = 이미지를 받아서 서버내부 어디에 저장 될 것인지   =>  media밑에 profile이라는 경로가 추가돼서 그 아래에 들어간다.

    nickname = models.CharField(max_length=20, unique=True, null=True)      #profile객체중 하나가 유일해야함.(중복불가).
    
    message = models.CharField(max_length=100, null=True)                   #자기소개

