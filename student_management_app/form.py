from django import forms

from student_management_app.models import Courses

class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    nom=forms.CharField(label="Last Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    prenom=forms.CharField(label="First Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=255,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField (label="Password",max_length=255,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    adresse=forms.CharField(label="Adresse",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    cours=Courses.objects.all()
    cours_list=[]
    for cour in cours:
        cour_choisis=(cour.id,cour.courses_name)
        cours_list.append( cour_choisis)

    sex_choisis=(
        ("masculin","masculin"),
        ("Feminin","Feminin")
    )
    cours_id=forms.ChoiceField(label="cours_inscris",choices=cours_list,widget=forms.Select(attrs={"class":"form-control"}))
    genre = forms.ChoiceField(label="sex", choices=sex_choisis,widget=forms.Select(attrs={"class":"form-control"}))
    start_year=forms.DateField(label="Session_start_year",widget=DateInput(attrs={"class":"form-control"}))
    end_year = forms.DateField(label="Session_end_year",widget=DateInput(attrs={"class":"form-control"}))
    pic=forms.FileField(label="Student_pic",widget=forms.FileInput(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
    nom=forms.CharField(label="Last Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    prenom=forms.CharField(label="First Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=255,widget=forms.EmailInput(attrs={"class":"form-control"}))
    adresse=forms.CharField(label="Adresse",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
    cours=Courses.objects.all()
    cours_list=[]
    for cour in cours:
        cour_choisis=(cour.id,cour.courses_name)
        cours_list.append( cour_choisis)

    sex_choisis=(
        ("masculin","masculin"),
        ("Feminin","Feminin")
    )
    cours_id=forms.ChoiceField(label="cours_inscris",choices=cours_list,widget=forms.Select(attrs={"class":"form-control"}))
    genre = forms.ChoiceField(label="sex", choices=sex_choisis,widget=forms.Select(attrs={"class":"form-control"}))
    start_year=forms.DateField(label="Session_start_year")
    end_year = forms.DateField(label="Session_end_year")
    pic=forms.FileField(label="Student_pic",widget=forms.FileInput(attrs={"class":"form-control"}))




