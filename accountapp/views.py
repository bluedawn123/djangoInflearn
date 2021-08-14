from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import CreateView

from accountapp.models import HelloWorld

#CBV로 만들기.FBV보다 낫다.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world2')  #계정 성공 후 재연결..reverser_lazy는 class, reverse는 함수에서 사용
    template_name = 'accountapp/create.html'            #어느 html을 통해서 볼지 설정. create.html이 필요하다


















'''
def hello_world(request):
    return HttpResponse("hello worldsss")
   
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다. 
    #hello_world 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.
    #view에서 직접 만들어서 되돌려 주는 형식




def hello_world(request):
    return render(request, 'base.html')  #templates의 base.html 반환
                                         #pragmatic.setting.py의 TEMPLATES에서 경로를 설정해줘야한다.

'''
def hello_world(request):
    return render(request, 'accountapp/hello_world.html')    #base.html이면, base.html을 가져오겠지? 우리는 accountapp내부의 정보가 필요하다


def hello_world2(request):
    if request.method == "POST":   #만약 요청받은 매소드가 post일 경우, POST 매소드는 객체 생성시 사용된다.
        ##hello_world_input을 {{ text }}에서 출력하는 것
        temp = request.POST.get('hello_world_input')    #request에서 POST메서드 중, hello_world_input데이터를 가져와 temp변수에 저장
        
        #저장하는 방법
        new_Hello_world = HelloWorld()  #HelloWorld 모델에서 나온 새로운 객체가 new_hello_world에 저장이 된다.
        new_Hello_world.text = temp     #HelloWorld는 text라는 charfield라는 속성값이 있다. new_Hello_world안의 text필드 = temp(입력값)으로 설정
        new_Hello_world.save()          #실제로 db에 저장된다.(우선은 sqlite에)

        #db에 쌓이는 정보list들을 display하는 법
        hello_world_list = HelloWorld.objects.all()   #HelloWorld의 모든 것들을 긁어와 변수에 저장

        #return render(request, 'accountapp/hello_world2.html', context={'text': 'POST METHOD!!!'})  #context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물을 보냄. html에 {{ text }}로 
        #return render(request, 'accountapp/hello_world2.html', context={'hello_world_output': new_hello_world}) #new_hello_world객체를 내보낸다. html에서 hello_world_output 명시 필수
        #return render(request, 'accountapp/hello_world2.html', context={'hello_world_list': hello_world_list})  #받을 것을 그대로 보내준다. 반복하는 문제가 생긴다.
        return HttpResponseRedirect(reverse('accountapp:hello_world2'))  #(account/hello_world2)를 해도 된다.
                                                                         #초기에 설정한 것 이용. accountapp내부의 hello_world2를 재섭속해라



    else:                        #만약 요청받은 매소드가 post가 아닌 경우, get매소드 사용

        #GET에서도 똑같은 행동을 할수 있도록 설정
        hello_world_list = HelloWorld.objects.all()
        #return render(request, 'accountapp/hello_world2.html', context={'text': 'GET METHOD!!!'})  # context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물
        return render(request, 'accountapp/hello_world2.html', context={'hello_world_list': hello_world_list})  # context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물



def hello_worlds(request):
    return HttpResponse("hello world!!!!!!!!!!")
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다.
    #라는 문자열을 브라우저에 출력하기 위해 사용되었다. index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.

#hello_world_input을 {{ text }}에서 출력하는 것

