from django.urls import path
from accountapp.views import hello_world, hello_worlds, hello_world2

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),    #라우트, 뷰의 함수, 이름설정
    path('hello_worlds/', hello_worlds, name='hello_worlds'),  # 라우트, 뷰함수, 이름설정
    #즉, account/hello_world/ 가 들어오면, view의 hello_world라는 함수로 처리한다. 그 아래도 마찬가지

    path('hello_world2/', hello_world2, name='hello_world2'),




]