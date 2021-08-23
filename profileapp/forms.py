from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']         #models.py에서 설정한 사용할 필드들.
                                                          # user은 서버에서 사용. 추후 없어서 에러가 난다. => views.py, form_valid 로 해결

