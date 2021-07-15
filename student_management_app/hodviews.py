import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.form import AddStudentForm, EditStudentForm
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
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Staff non enregistrer")
            return HttpResponseRedirect(reverse("add_staff"))


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
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request,"cours non ajouter")
            return HttpResponseRedirect(reverse("add_course"))

def add_students(request):
    courses=Courses.objects.all()
    form=AddStudentForm()
    return render(request,'hod_template/add_student_template.html',{"form":form})



def save_student(request):
    if request.method!="POST":
        return HttpResponseRedirect("methode non valide")
    else:
        form=AddStudentForm(request.POST,request.FILES )
        if form.is_valid():
            nom=form.cleaned_data["nom"]
            prenom=form.cleaned_data["prenom"]
            username=form.cleaned_data["username"]
            adresse = form.cleaned_data["adresse"]
            start_year = form.cleaned_data["start_year"]
            end_year = form.cleaned_data["end_year"]
            gender = form.cleaned_data["genre"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            courses_id = form.cleaned_data["cours_id"]

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
                return HttpResponseRedirect(reverse("add_students"))
            except:
                messages.error(request,"student non enregistrer")
                return HttpResponseRedirect(reverse("add_students"))

        else:
            form=AddStudentForm(request.POST)
            return render(request, 'hod_template/add_student_template.html', {"form": form})

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
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request, "subject non ajouter")
            return HttpResponseRedirect(reverse("add_subject"))

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

def edit_staff(request,staff_id):
    staffs=Staffs.objects.get(admin=staff_id)
    return render(request,'hod_template/edit_staff_template.html',{"staffs":staffs,"id":staff_id})

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
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request, "staff non modifie")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))

def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Student.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['nom'].initial=student.admin.first_name
    form.fields['prenom'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['email'].initial=student.admin.email
    form.fields['adresse'].initial=student.adresse
    form.fields['cours_id'].initial=student.coureses_id.id
    form.fields['genre'].initial=student.gender
    form.fields['start_year'].initial=student.session_start_year
    form.fields['end_year'].initial=student.session_end_year
    return render(request,'hod_template/edit_student_template.html',{"form":form,"id":student_id,"username":student.admin.username})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>La methode n'est pas valide</h2>")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_student "))

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["nom"]
            last_name = form.cleaned_data["prenom"]
            username = form.cleaned_data["username"]
            adresse = form.cleaned_data["adresse"]
            email = form.cleaned_data["email"]
            start_year = form.cleaned_data["start_year"]
            end_year = form.cleaned_data["end_year"]
            cours_name = form.cleaned_data["cours_id"]
            gender = form.cleaned_data["genre"]

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
                del request.session['student_id']
                messages.success(request, "student modifie avec success")
                return HttpResponseRedirect(reverse("edit_student" , kwargs={"student_id":student_id}))
            except:
                messages.error(request, "staff non modifie")
                return HttpResponseRedirect(reverse("edit_student",  kwargs={"student_id":student_id}))
        else:
            form=EditStudentForm(request.POST)
            student=Student.objects.get(admin=student_id)
            return render(request,'hod_template/edit_student_template.html',{"form":form,"id":student_id,"username":student.admin.username})

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
            return HttpResponseRedirect(reverse("edit_cours", kwargs={"cour_id":cour_id}))
        except:
            messages.error(request, "Cours non modifie")
            return HttpResponseRedirect(reverse("edit_cours" , kwargs={"cour_id":cour_id}))

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
            return HttpResponseRedirect(reverse("edit_subject/" , kwargs={"subject_id":subject_id}))
        except:
            messages.error(request, "sujet non modifie")
            return HttpResponseRedirect(reverse("edit_subject",  kwargs={"subject_id":subject_id}))