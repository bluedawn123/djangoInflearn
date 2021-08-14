'''
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



12강
1. 태그들마다 display 속성들이 존재. => html을 구성하는 원리 때문에 중요하다.
-> 4가지 속성이 있다. Blcok Inline Inline-blcok None
Block => 모든 태그에는 부모가 존재. 그 부모의 너비를 모두 가져가면서 block 모양의 형태를 지닌다.
      => 자식들은 아래로 쌓인다.

Inline=> 줄 안의 글씨의 높이 만큼만 가져가는 형식
      => 자식들은 옆으로 쌓인다.


Inline-block => Inline처럼 안쪽으로 쌓이는 블록

None => 아예 존재 xx
vs
Hidden => 보이지만 않을 뿐 존재. (공간 차지)


2. size속성 => 반응형 페이지 때문에 중요
px => 부모의 크기, 레이아웃등과 상관없음.
em => 부모 기타 등등과 상관있음.
   => 부모가 2인데 2배가 커졌으면, 총 4배가 커져서 문제가 된다. (합산 방식)
rem => 제일 종요. root HTML의 변화를 따라간다.
    => 1rem : 16px, 3rem : 48px
% => 바로 부모 위 영향


13강.
css적용 방법 3가지. 1.직접입력(style="..."), 2.별도의 css에서 불러오기. 3.위에서 설정   속싱이 겹칠경우 적용순서는 1 > 3>  2
4가지 속성 실습

14강. model
15강. get, post
16강.
post는 post+body
1. post를 쓰려면 html안에 form을 만들어야 한다. 서버한테 보내는 요청 명세서 느낌. 글, 파일 첨부시 모든 데이터가 post body(form)안에 들어간다.
2. action =" " 에는 요청하려는 url이 필요.
3. form만 있다고 되지 않고 상호작용을 할 수 있는 게 필요하다. input등등..
4. 장고로 post메소드를 사용해 서버에 요청을 보낼때는 csrf토큰이 필요하다. => 보안 기능중 하나.
5. #context=>데이터꾸러미..?

18강.
render 와 redirect 구분
두 함수를 헷갈려 혼동하는 경우가 많습니다. 특히 장고가 익숙하지 않을 때는 둘다 return 뒤에 위치하여 함수를 종료할 시 사용
render 는 템플릿을 불러오고, redirect 는 URL로 이동
URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고 여기서 render 를 할지 다시 redirect 할지 결정


'''
