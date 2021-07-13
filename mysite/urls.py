"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include 

from mysite import settings
from student_management_app import views,hodviews

urlpatterns = [
    path('student/',views.showview),
    path('',views.Login),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin),
    path('admin_home',hodviews.showpage),
    path('add_staff',hodviews.add_staff),
    path('save_staff',hodviews.save_staff),
    path('add_students',hodviews.add_students),
    path('save_student',hodviews.save_student),
    path('add_course',hodviews.add_course),
    path('save_course',hodviews.save_course),
    path('add_subject',hodviews.add_subject),
    path('save_subject',hodviews.save_subject),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)