from django.contrib import admin
from django.urls import path,include
from task_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task_app.urls')),
    path('members/',include(('django.contrib.auth.urls','members'), namespace='authenticate')),
    path('members/',include('members.urls')),
    path('list_task/',views.list_task,name='list_task'),
]
