from django.urls import path
from . import views #같은 폴더 내에 views.py import함

urlpatterns = [
    # path('', views.index), #~blog/ 뒤에 아무것도 없을때
    # path('<int:pk>/', views.single_post_page),

    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view())
]
