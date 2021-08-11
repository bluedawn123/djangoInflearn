# djangoInflearn
11강
1. css파일은 디자인 파일만 따로 분리해 놓은 것이다. html은 뼈대만 남겨두고 디자인적인 css같은 파일들은 css파일 내부로 빼내 따로 관리.
즉, static에 대한 설정이 필요하다.
2. staticfiles디렉토리를 따로 지정해 줄 수 있다. 일단적으론 staticfiles가 app내부의 static 폴더를 찾는데, 임의로 staticfiles디렉
토리를 추가해서 app에 종속되지 않은 static폴더를 따로 만들 수 있다. 
즉, 최상위 (djangoInflearn)폴더에 static폴더를 새로 만들어서 app에 종속되지 않은 staticfiles를 관리할 수 있다.
3. css를 클래스에 적용해 주는 방법 참조 => footer.html파일과 static.base.css를 확인하자

4. static 관련한 파일을 가져오는 과정? 
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'base.css' %}">
=> static폴더의 base.css에서 지정한 .pragmatic_footer_logo {
                                  font-family: 'Lobster', cursive;
                                   } 하기 위해서.

참조로,<h6 class="pragmatic_footer_logo">Pragmatic</h6>에서 pragmatic_footer_logo를 클래스로 지정.(그걸base.css에서 정의)
