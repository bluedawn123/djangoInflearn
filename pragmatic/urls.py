"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),               #admin접속
    path('accounts/', include('accountapp.urls')), #account접속, accoutnapp내부의 urls.py를 포함해서 하위 디렉토리로 분기.  account => accounts로 변경
    path('profiles/', include('profileapp.urls')),


    ##path('junho/', views.index),  #junho/ URL이 요청되면 views.index를 호출매핑을 urlpatterns에 추가. views.index는 views.py 파일의 index 함수를 의미한다.

    #path("", RedirectView.as_view(url="accounts/hello_world2/", permanent=True))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
