from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_account_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

#C
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world2')
    template_name = 'profileapp/create.html'                #profileapp 내부의 create.html 사용

    def form_valid(self, form):
        temp_profile = form.save(commit=False)          #커스텀마이징하려는 내용. 괄호안의 form은 forms.py에서 날라온 데이터이며 (self, form)의 form에 저장된다.
        temp_profile.user = self.request.user            #user라는 데이터가 아직 없다. temp_profile의 user라는 데이터를 self에서 request를 보는 당사자 유저로 정해준다.
        temp_profile.save()

        return super().form_valid(form)       #기존의 함수와 똑같다. 그리고 나머지는 조상(부모클래스)의 원래 그거의 결과를 return해준다.
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
#U
@method_decorator(profile_account_ownership_required, 'get')
@method_decorator(profile_account_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world2')
    template_name = 'profileapp/update.html'                #profileapp 내부의 update.html 사용

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})