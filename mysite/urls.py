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
    path('student/',views.showview,name="student"),
    path('',views.Login,name="index"),
    path('get_user_details',views.GetUserDetails,name="get_user_details"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('doLogin',views.doLogin,name="doLogin"),
    path('admin_home',hodviews.showpage,name="admin_home"),
    path('add_staff',hodviews.add_staff,name="add_staff"),
    path('save_staff',hodviews.save_staff,name="save_staff"),
    path('add_students',hodviews.add_students,name="add_students"),
    path('save_student',hodviews.save_student,name="save_student"),
    path('add_course',hodviews.add_course,name="add_course"),
    path('save_course',hodviews.save_course,name="save_course"),
    path('add_subject',hodviews.add_subject,name="add_subject"),
    path('save_subject',hodviews.save_subject,name="save_subject"),
    path('show_manage',hodviews.show_manage,name="show_manage"),
    path('show_student',hodviews.show_student,name="show_student"),
    path('show_cours',hodviews.show_cours,name="show_cours"),
    path('show_subject',hodviews.show_subject,name="show_subject"),
    path('edit_staff/<str:staff_id>',hodviews.edit_staff,name="edit_staff"),
    path('edit_save_staff',hodviews.edit_save_staff,name="edit_save_staff"),
    path('edit_student/<str:student_id>',hodviews.edit_student,name="edit_student"),
    path('edit_student_save',hodviews.edit_student_save,name="edit_student_save"),
    path('edit_cours/<str:cours_id>',hodviews.edit_cours,name="edit_cours"),
    path('edit_cours_save',hodviews.edit_cours_save,name="edit_cours_save"),
    path('edit_subject/<str:subject_id>',hodviews.edit_subject,name="edit_subject"),
    path('edit_subject_save',hodviews.edit_subject_save,name="edit_subject_save"),
    path('admin/', admin.site.urls),
    # Stafff_url
    path('staff_home')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)