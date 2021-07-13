import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import Staffs, Student, CostumUser, Courses, Subject


def showpage(request):
    return render(request,'hod_template/home_content.html')

def add_staff(request):
    return render(request,'hod_template/add_staff_template.html')

def save_staff(request):
    if request.method!= "POST":
        return HttpResponse("La methode n'est pas valide")
    else:
        first_name=request.POST.get("nom")
        last_name=request.POST.get("prenom")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        adresse= request.POST.get("adresse")
        try:
            user=CostumUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,user_type=2)
            user.staffs.adresse=adresse
            user.save()
            messages.success(request,"staff enregistrer avec success")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Staff non enregistrer")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request,'hod_template/add_course_template.html')


def save_course(request):
    if request.method!="POST":
        return HttpResponse("la methode n'est pas valide")
    else:
        nom_course=request.POST.get('cours')
        try:
            course=Courses(courses_name=nom_course)
            course.save()
            messages.success(request,"cours ajouter avec success")
            return HttpResponseRedirect('/add_course')
        except:
            messages.error(request,"cours non ajouter")
            return HttpResponseRedirect('/add_course')

def add_students(request):
    courses=Courses.objects.all()
    return render(request,'hod_template/add_student_template.html',{"courses":courses})



def save_student(request):
    if request.method!="POST":
        return HttpResponseRedirect("methode non valide")
    else:
        nom=request.POST.get("nom")
        prenom=request.POST.get("prenom")
        username=request.POST.get("username")
        adresse = request.POST.get("adresse")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        gender = request.POST.get("genre")
        pic = request.POST.get("pic")
        email = request.POST.get("email")
        password = request.POST.get("password")
        courses_id = request.POST.get("cours_id")
        try:
            user=CostumUser.objects.create_user(first_name=nom, last_name=prenom, username=username, email=email, password=password, user_type=3)
            user.student.adresse=adresse
            courses_obj = Courses.objects.get(id=courses_id)
            user.student.coureses_id=courses_obj
            user.student.session_start_year=start_year
            user.student.session_end_year=end_year
            user.student.gender=gender
            user.student.student_pic=""
            user.save()
            messages.success(request,"student enregistrer avec success")
            return HttpResponseRedirect('/add_students')
        except:
            messages.error(request,"student non enregistrer")
            return HttpResponseRedirect('/add_students')

def add_subject(request):
    courses=Courses.objects.all()
    staffs=CostumUser.objects.filter(user_type=2)
    return render(request,'hod_template/add_subject_template.html',{"staffs":staffs,"courses":courses})

def save_subject(request):
    if request.method!="POST":
        return HttpResponse("methode non valide")
    else:
        nom_subject=request.POST.get("subject")
        nom_cour=request.POST.get("cours_id")
        nom_staff=request.POST.get("staff_id")
        cours_id = Courses.objects.get(id=nom_cour)
        staff_id = CostumUser.objects.get(id=nom_staff)
        try:
            subject = Subject(subject_name=nom_subject,courses_id=cours_id,staffs_id=staff_id)
            subject.save()
            messages.success(request, "subject ajouter avec success")
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request, "subject non ajouter")
            return HttpResponseRedirect('/add_subject ')

def show_manage(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})

def show_student(request):
    students=Student.objects.all()
    return render(request,'hod_template/manage_student_template.html',{"students":students})

def show_cours(request):
    cours=Courses.objects.all()
    return render(request,'hod_template/manage_cours_template.html',{"cours":cours})

def show_subject(request):
    subjects=Subject.objects.all()
    return render(request,'hod_template/manage_subject_template.html',{"subjects":subjects})