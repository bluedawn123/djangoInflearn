from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse("hello worldsss")
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다. 여기서는 "안녕하세요 pybo에 오신것을 환영합니다."
    #라는 문자열을 브라우저에 출력하기 위해 사용되었다. index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.

#def index(request):
#    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def hello_worlds(request):
    return HttpResponse("hello world!!!!!!!!!!")
    #HttpResponse는 요청 페이지에 대한 응답을 할때 사용하는 장고 클래스이다. 여기서는 "안녕하세요 pybo에 오신것을 환영합니다."
    #라는 문자열을 브라우저에 출력하기 위해 사용되었다. index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
    #request에 대해서는 조금 후에 더 자세히 알아보자.