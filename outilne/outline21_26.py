'''
21. 회원가입
22. 로그인   => login하면 account/profile이라는 에러가 나온다. 기본설정인데 안 정했기 때문

    login, logout view에서 redirect의 경로 찾기
    1. next 없으면 2번으로
    2. login, redirect url로
    3. 2번도 없으면 Default값으로 (account/profile)

#로그인,로그아웃
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),                #as_view()안에 지정 템플릿이 필요하다
    path('logout/', LogoutView.as_view(), name='logout'),


23. 글꼴 적용
24. Read view ( = Detail view)  특정 유저의 정보를 보기
     context_object_name = 'target_user' , target_user

25. UpdateView
   CreateView과 유사.
   mypage에서 수정하는 링크 생성
   path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world2')  #계정 성공 후 재연결..reverser_lazy는 class, reverse는 함수에서 사용
    template_name = 'accountapp/update.html'               #어느 html을 통해서 볼지 설정. create.html이 필요하다

    (username칸)아이디,비번 다 바꿀 수 있는 상태이므로, 아이디는 못 바꾸게 설정해준다. => accountapp.forms.py에서 UserCreationForm을 상속받아 커스터마이즈

26. delete => views.py, urls.py 수정
    header에서 회원가입창 생성


'''