from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.hodviews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))

            elif user.user_type == "2":
                if modulename == "student_management_app.staffViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))

            elif user.user_type == "3":
                if modulename == "student_management_app.studentViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
                     
            else:
                return HttpResponseRedirect(reverse("show_loging "))
        else:
            if request.path == reverse("show_loging") or request.path == ("doLogin"):
                pass 
            else:
                return HttpResponseRedirect(reverse("show_loging"))

