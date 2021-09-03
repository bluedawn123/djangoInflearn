from commentapp.views import CommentCreateView

app_name = 'commentapp'
from django.urls import path

urlpatterns =[
    path('create/', CommentCreateView.as_view(), name='create'),

]