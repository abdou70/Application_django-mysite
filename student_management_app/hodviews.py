import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import Staffs, Student, CostumUser, Courses, Subject


def showpage(request):
    return render(request,'hod_template/home_content.html')

def add_staff(request):
    return render(request,'hod_template/add_staff_template.html')

def save_staff(request):
    if request.method!="POST":
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
        email = request.POST.get("email")
        password = request.POST.get("password")
        courses_id = request.POST.get("cours_id")

        pic = request.FILES["pic"]
        fs= FileSystemStorage()
        filename=fs.save(pic.name,pic)
        pic_url=fs.url(filename)

        try:
            user=CostumUser.objects.create_user(first_name=nom, last_name=prenom, username=username, email=email, password=password, user_type=3)
            user.student.adresse=adresse
            courses_obj = Courses.objects.get(id=courses_id)
            user.student.coureses_id=courses_obj
            user.student.session_start_year=start_year
            user.student.session_end_year=end_year
            user.student.gender=gender
            user.student.student_pic=pic_url
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

def edit_staff(request,staffs_id):
    staffs=Staffs.objects.get(admin=staffs_id)
    return render(request,'hod_template/edit_staff_template.html',{"staffs":staffs,"id":staffs_id})

def edit_save_staff(request):
    if request.method!="POST":
        return HttpResponse("<h2>La methode n'est pas valide </h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name = request.POST.get("nom")
        last_name = request.POST.get("prenom")
        username = request.POST.get("username")
        email = request.POST.get("email")
        adresse = request.POST.get("adresse")
        try:
            user=CostumUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            user_model=Staffs.objects.get(admin=staff_id)
            user_model.adresse=adresse
            user_model.save()
            messages.success(request, "staff modifie avec success")
            return HttpResponseRedirect('/edit_staff/'+staff_id)
        except:
            messages.error(request, "staff non modifie")
            return HttpResponseRedirect('/edit_staff/'+staff_id)

def edit_student(request,student_id):
    students=Student.objects.get(admin=student_id)
    courses=Courses.objects.all()
    return render(request,'hod_template/edit_student_template.html',{"students":students,"courses":courses,"id":student_id})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>La methode n'est pas valide</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get("nom")
        last_name = request.POST.get("prenom")
        username = request.POST.get("username")
        adresse = request.POST.get("adresse")
        email = request.POST.get("email")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        cours_name = request.POST.get("cours_id")
        gender = request.POST.get("genre")

        if request.FILES.get("pic",False):
            pic = request.FILES["pic"]
            fs = FileSystemStorage()
            filename = fs.save(pic.name, pic)
            pic_url = fs.url(filename)
        else:
            pic_url=None

        try:
            user=CostumUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            user_model=Student.objects.get(admin=student_id)
            user_model.session_start_year=start_year
            user_model.session_end_year=end_year
            user_model.adresse=adresse
            user_model.gender=gender
            courses_obj =Courses.objects.get(id=cours_name)
            user_model.coureses_id =courses_obj
            user_model.student_pic=pic_url
            user_model.save()
            messages.success(request, "student modifie avec success")
            return HttpResponseRedirect('/edit_student/' + student_id)
        except:
            messages.error(request, "staff non modifie")
            return HttpResponseRedirect('/edit_student/' + student_id)

def edit_cours(request,cours_id):
    cours=Courses.objects.get(id=cours_id)
    return render (request,'hod_template/edit_cours_template.html',{"cours":cours,"id":cours_id})

def edit_cours_save(request):
    if request.method!="POST":
        return ("<h2>La methode utilise n'est pas bonne</h2>")
    else:
        cour_id=request.POST.get("cours_id")
        name_cour=request.POST.get("cours")
        try:
            cours=Courses.objects.get(id=cour_id)
            cours.courses_name=name_cour
            cours.save()
            messages.success(request,"cours modifier avec success")
            return HttpResponseRedirect('/edit_cours/' + cour_id)
        except:
            messages.error(request, "Cours non modifie")
            return HttpResponseRedirect('/edit_cours/' + cour_id)

def edit_subject(request,subject_id):
    subject=Subject.objects.get(id=subject_id)
    course = Courses.objects.all()
    staffs=CostumUser.objects.filter(user_type=2)
    return render(request,'hod_template/edit_subject_template.html',{"subject":subject,"course":course,"staffs":staffs,"id":subject_id})

def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>La methode utilise n'est pas valide</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        nom_subject=request.POST.get("subject")
        nom_cour=request.POST.get("cours_id")
        nom_staff=request.POST.get("staff_id")
        try:
            subject=Subject.objects.get(id=subject_id)
            subject.subject_name=nom_subject
            cour_obj = Courses.objects.get(id=nom_cour)
            subject.courses_id = cour_obj
            staff_obj = CostumUser.objects.get(id=nom_staff)
            subject.staffs_id = staff_obj
            subject.save()
            messages.success(request, "sujet modifier avec success")
            return HttpResponseRedirect('/edit_subject/' + subject_id)
        except:
            messages.error(request, "sujet non modifie")
            return HttpResponseRedirect('/edit_subject/' + subject_id)