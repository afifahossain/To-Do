from django.urls import path
from .views import tasklist, taskdetail, taskcreate, taskupdate, taskdelete, userlogin, registerpage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', userlogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', registerpage.as_view(), name='register'),
    path('', tasklist.as_view(), name='tasks'),
    path('task_detail/<int:pk>/', taskdetail.as_view(), name='task_detail'),
    path('task_create/', taskcreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', taskupdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', taskdelete.as_view(), name='task_delete'),

]
