from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

'''
def hello_world(request):
    return HttpResponse("hello worldsss")
   
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다. 
    #hello_world 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.
    #view에서 직접 만들어서 되돌려 주는 형식

'''

'''
def hello_world(request):
    return render(request, 'base.html')  #templates의 base.html 반환
                                         #pragmatic.setting.py의 TEMPLATES에서 경로를 설정해줘야한다.

'''
def hello_world(request):
    return render(request, 'accountapp/hello_world.html')    #base.html이면, base.html을 가져오겠지? 우리는 accountapp내부의 정보가 필요하다



def hello_worlds(request):
    return HttpResponse("hello world!!!!!!!!!!")
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다.
    #라는 문자열을 브라우저에 출력하기 위해 사용되었다. index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.

