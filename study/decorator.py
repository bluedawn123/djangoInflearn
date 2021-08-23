from django.contrib.auth.decorators import login_required

1.

def hello_world2(request):
    # 인증과정 만들기
    if request.user.is_authenticated:  # 만약 유저가 인증되었다면,
        if request.method == "POST":  # 만약 요청받은 매소드가 post일 경우, POST 매소드는 객체 생성시 사용된다.
            ##hello_world_input을 {{ text }}에서 출력하는 것
            temp = request.POST.get('hello_world_input')  # request에서 POST메서드 중, hello_world_input데이터를 가져와 temp변수에 저장

            # 저장하는 방법
            new_Hello_world = HelloWorld()  # HelloWorld 모델에서 나온 새로운 객체가 new_hello_world에 저장이 된다.
            new_Hello_world.text = temp  # HelloWorld는 text라는 charfield라는 속성값이 있다. new_Hello_world안의 text필드 = temp(입력값)으로 설정
            new_Hello_world.save()  # 실제로 db에 저장된다.(우선은 sqlite에)

            # db에 쌓이는 정보list들을 display하는 법
            hello_world_list = HelloWorld.objects.all()  # HelloWorld의 모든 것들을 긁어와 변수에 저장

            # return render(request, 'accountapp/hello_world2.html', context={'text': 'POST METHOD!!!'})  #context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물을 보냄. html에 {{ text }}로
            # return render(request, 'accountapp/hello_world2.html', context={'hello_world_output': new_hello_world}) #new_hello_world객체를 내보낸다. html에서 hello_world_output 명시 필수
            # return render(request, 'accountapp/hello_world2.html', context={'hello_world_list': hello_world_list})  #받을 것을 그대로 보내준다. 반복하는 문제가 생긴다.
            return HttpResponseRedirect(reverse('accountapp:hello_world2'))  # (account/hello_world2)를 해도 된다.
            # 초기에 설정한 것 이용. accountapp내부의 hello_world2를 재섭속해라

        else:  # 만약 요청받은 매소드가 post가 아닌 경우, get매소드 사용

            # GET에서도 똑같은 행동을 할수 있도록 설정
            hello_world_list = HelloWorld.objects.all()
            # return render(request, 'accountapp/hello_world2.html', context={'text': 'GET METHOD!!!'})  # context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물
            return render(request, 'accountapp/hello_world2.html', context={
                'hello_world_list': hello_world_list})  # context=>데이터꾸러미..? text라는 이름의 POST METHOD라는 내용물

    else:  # 로그인 안 된 경우 로그인 페이지로 보내버리기
        return HttpResponseRedirect(reverse('accountapp:login'))

1-1.
@login_required
def hello_world2(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_Hello_world = HelloWorld()
        new_Hello_world.text = temp
        new_Hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world2'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world2.html', context={'hello_world_list': hello_world_list})







2.
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'  # 어느 html을 통해서 볼지 설정. create.html이 필요하다
    context_object_name = 'target_user'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

여기서 보면,
if self.request.user.is_authenticated and self.get_object() == self.request.user:
    return super().get(*args, **kwargs)
else:
    return HttpResponseRedirect(reverse('accountapp:login'))

이 반복된다.

2-2.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world2')  #계정 성공 후 재연결..reverser_lazy는 class, reverse는 함수에서 사용
    template_name = 'accountapp/update.html'               #어느 html을 통해서 볼지 설정. create.html이 필요하다
    context_object_name = 'target_user'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'               #어느 html을 통해서 볼지 설정. create.html이 필요하다
    context_object_name = 'target_user'
