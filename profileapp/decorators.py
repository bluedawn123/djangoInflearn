from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])    #urls에서 'update/<int:pk>'의 pk를 받는다.(Profile의 pk를 받아서 profile객체로)
        if not profile.user == request.user:              #
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated